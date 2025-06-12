class Registry():
    registered_keys = {}
    registered_values = {}

    @classmethod
    def register_keys(cls, to_register=None, name=None):
        return cls._register_key_impl(to_register, name)

    def register_values(cls, to_register=None, key=None, name=None):
        return cls._register_value_impl(to_register, key, name)

    @classmethod
    def get_key(cls, name):
        return cls._get_impl(name)

    def get_value(cls, key, name):
        return cls._get_value_impl(key, name)

    @classmethod
    def get_key_list(cls):
        return cls.registered_keys

    @classmethod
    def get_value_list(cls):
        return cls.registered_values

    @classmethod
    def _register_key_impl(cls, to_register, name):
        def wrap(to_register):
            register_name = name
            cls.registered_keys[register_name] = to_register
            return to_register

        if to_register is None:
            return wrap
        else:
            return wrap(to_register)

    @classmethod
    def _register_value_impl(cls, to_register, key, name):
        def wrap(to_register):
            register_name = name
            if key not in cls.registered_values:
                cls.registered_values[key] = {}
            cls.registered_values[key][name] = to_register
            return to_register

        if to_register is None:
            return wrap
        else:
            return wrap(to_register)

    @classmethod
    def _get_impl(cls, name):
        return cls.registered_keys[name]

    def _get_value_impl(cls, key, name):
        return cls.registered_values[key][name]

registry = Registry()