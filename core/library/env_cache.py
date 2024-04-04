import environ

env = environ.Env()
env.read_env("../")

cache_dictionary = {
    "local_memory": {
        "default": {
            "BACKEND": env("CACHE_BACKEND")
        }
    },
    "django_redis": {
        "default": {
            "BACKEND": env("CACHE_BACKEND"),
            "LOCATION": env("CACHE_LOCATION"),
            "OPTIONS": {
                "CLIENT_CLASS": env("CLIENT_CLASS")
            }
        }
    }
}