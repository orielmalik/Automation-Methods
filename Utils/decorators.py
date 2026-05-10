from Utils.TestUtils import find_and_load_env


def load_env_key(var_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not var_name:
                raise ValueError("Environment variable name is missing")

            api_key = find_and_load_env(var_name)

            return func(api_key, *args, **kwargs)

        return wrapper
    return decorator