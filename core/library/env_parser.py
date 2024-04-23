import environ

env = environ.Env()
env.read_env("../../.env")

def settings_reader(env_list):
    list = env_list.split()
    return list