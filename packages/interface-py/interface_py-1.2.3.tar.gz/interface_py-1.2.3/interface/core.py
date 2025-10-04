import inspect

from .helper_functions import Helper


class InterfaceMeta(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        cls._is_interface_ = getattr(cls, "_is_interface_", None)
        cls._interface_contracts_ = {}
        
        annotations = namespace.get('__annotations__', {})
        for ann_attr, _ in annotations.items():
            if ann_attr not in namespace:
                cls._interface_contracts_[ann_attr] = "field"
        
        return cls

    def __call__(cls, *args, **kwargs):
        if getattr(cls, "_is_interface_", False):
            raise TypeError(f"Cannot instantiate interface class '{cls.__name__}'")
        return super().__call__(*args, **kwargs)
    

    def __validate__(cls):
        if cls._is_interface_ is None:
            raise TypeError("Class must be decorated with @interface or @concrete")

        MAGIC_INCLUDE = {
            "__init__", "__add__", "__sub__", "__mul__", "__truediv__", "__len__",
            "__getitem__", "__setitem__", "__iter__", "__next__", "__str__", "__repr__",
            "__contains__", "__eq__", "__lt__", "__le__", "__gt__", "__ge__", "__hash__"
        }

        if cls._is_interface_:
            # enforce interface contracts
            # TODO: use itertools.chain to lazy load the iterable
            all_attrs = list(vars(cls).items()) + [(attr, None) for attr in cls.__annotations__ if attr not in cls.__dict__]
            for attr, value in all_attrs:
                if attr in ("__annotations__", "_is_interface_", "_interface_contracts_"):
                    continue
                if attr.startswith("__") and attr.endswith("__") and attr not in MAGIC_INCLUDE:
                    continue

                # ---- METHODS ----
                if inspect.isfunction(value):
                    if not Helper.is_empty_function(value):
                        raise TypeError(
                            f"Method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    sig = inspect.signature(value)
                    cls._interface_contracts_[attr] = ("method", sig, "function")
                    continue

                if isinstance(value, staticmethod):
                    fn = value.__func__
                    if not Helper.is_empty_function(fn):
                        raise TypeError(
                            f"Static method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    sig = inspect.signature(fn)
                    cls._interface_contracts_[attr] = ("method", sig, "staticmethod")
                    continue

                if isinstance(value, classmethod):
                    fn = value.__func__
                    if not Helper.is_empty_function(fn):
                        raise TypeError(
                            f"Class method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    sig = inspect.signature(fn)
                    cls._interface_contracts_[attr] = ("method", sig, "classmethod")
                    continue

                # ---- PROPERTY ----
                if isinstance(value, property):
                    errors: list[str] = []
                    if not any([value.fget, value.fset, value.fdel]):
                        errors.append(
                            f"Property '{attr}' in interface '{cls.__name__}' must define at least "
                            "a getter, setter or deleter (even if empty)."
                        )
                    if value.fget is not None and not Helper.is_empty_function(value.fget):
                        errors.append(
                            f"Property getter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if value.fset is not None and not Helper.is_empty_function(value.fset):
                        errors.append(
                            f"Property setter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if value.fdel is not None and not Helper.is_empty_function(value.fdel):
                        errors.append(
                            f"Property deleter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if errors:
                        raise TypeError("\n".join(errors))
                    if value.fget is not None:
                        cls._interface_contracts_[f"{attr}.fget"] = ("method", inspect.signature(value.fget), "property_get")
                    if value.fset is not None:
                        cls._interface_contracts_[f"{attr}.fset"] = ("method", inspect.signature(value.fset), "property_set")
                    if value.fdel is not None:
                        cls._interface_contracts_[f"{attr}.fdel"] = ("method", inspect.signature(value.fdel), "property_del")
                    cls._interface_contracts_[attr] = ("property", None, None)
                    continue

                # ---- FIELD PLACEHOLDER ----
                ann = cls.__annotations__.get(attr) if hasattr(cls, "__annotations__") else None
                if ann is not None:
                    cls._interface_contracts_[attr] = ("field", None, None)
                    continue

                if value is Ellipsis:
                    cls._interface_contracts_[attr] = ("field", None, None)
                    continue

                if isinstance(value, type):
                    continue

                raise TypeError(
                    f"Attribute '{attr}' in interface '{cls.__name__}' should not have a concrete value."
                )

            # inherit contracts from parents
            for base in cls.__mro__[1:]:
                if hasattr(base, "_interface_contracts_"):
                    cls._interface_contracts_.update(base._interface_contracts_)

        else:
            # enforce concrete implementation
            contracts: dict[str, tuple] = {}
            for base in cls.__mro__[1:]:
                if hasattr(base, "_interface_contracts_"):
                    contracts.update(base._interface_contracts_)

            missing = []
            signature_mismatches = []

            for name, info in contracts.items():
                kind = info[0]
                if kind == "method":
                    expected_sig = info[1]
                    expected_type = info[2]
                    
                    impl = cls.__dict__.get(name, None)
                    if impl is None:
                        # maybe inherited
                        for base in cls.__mro__[1:]:
                            impl = base.__dict__.get(name)
                            if impl:
                                break
                    
                    if impl is None or Helper.is_empty_function(impl):
                        missing.append(name)
                        continue
                    
                    if isinstance(impl, (classmethod, staticmethod)):
                        func = impl.__func__
                    else:
                        func = impl
                    
                    try:
                        impl_sig = inspect.signature(func)
                    except (ValueError, TypeError):
                        impl_sig = None
                        
                    if expected_sig is not None and impl_sig is not None:
                        # normalize: for instance methods, both include 'self' usually — compare directly
                        if impl_sig.parameters.keys() != expected_sig.parameters.keys():
                            signature_mismatches.append(
                                (name, expected_sig, impl_sig)
                            )
                    else:
                        if expected_sig is not None and impl_sig is None:
                            signature_mismatches.append((name, expected_sig, impl_sig))
                            
                elif kind == "field":
                    if not hasattr(cls, name):
                        missing.append(name)
                    else:
                        val = getattr(cls, name)
                        if val is Ellipsis:
                            missing.append(name)
                            
                elif kind == "property":
                    prop_obj = getattr(cls, name, None)
                    if not isinstance(prop_obj, property):
                        missing.append(name)
                    else:
                        # check individual accessors
                        for acc in ("fget", "fset", "fdel"):
                            key = f"{name}.{acc}"
                            if key in contracts:
                                exp_sig = contracts[key][1]
                                func = getattr(prop_obj, acc)
                                if func is None or Helper.is_empty_function(func):
                                    missing.append(key)
                                    continue
                                
                                try:
                                    impl_sig = inspect.signature(func)
                                except (ValueError, TypeError):
                                    impl_sig = None
                                    
                                if exp_sig is not None and impl_sig is not None:
                                    if impl_sig.parameters.keys() != exp_sig.parameters.keys():
                                        signature_mismatches.append((key, exp_sig, impl_sig))

            if missing or signature_mismatches:
                parts: list[str] = []
                if missing:
                    parts.append(f"Concrete class '{cls.__name__}' must implement contracts: {', '.join(sorted(missing))}")
                if signature_mismatches:
                    for nm, exp, got in signature_mismatches:
                        parts.append(f"Signature mismatch for '{nm}' in concrete '{cls.__name__}': expected {exp}, got {got}.")
                
                raise TypeError("\n".join(parts))
