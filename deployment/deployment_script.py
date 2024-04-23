# deployment script
import os
import platform
import environ
import subprocess
import sys
from time import sleep as wait

env = environ.Env()
env.read_env("../.env")

def docker_compose_dev():
    """
    PURPOSE:
    This function is called when context is development and deployed on docker compose

    STEPS:
    1. check that pc can read environment file
    2. find path to run docker daemon on system
    3. start docker daemon
    4. wait for docker daemon processes to start up completely
    5. run `docker compose up` for container
    """

    if "environ" not in sys.modules:
        subprocess.Popen(["pip", "install", "django-environ"])
    
    # find docker daemnon path
    docker_desktop = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"

    # start daemon
    subprocess.Popen([docker_desktop])

    wait(20)

    # start docker
    subprocess.Popen(["docker", "compose", "up"])

def docker_compose_production():
    """
    PURPOSE:
    This function is called when context is production and deployed on docker compose

    STEPS:
    1. check that pc can read environment file
    2. find path to run docker daemon on system
    3. start docker daemon
    4. wait for docker daemon processes to start up completely
    5. run `docker compose [production profile] up` for container
    """

    if "environ" not in sys.modules:
        subprocess.Popen(["pip", "install", "django-environ"])
    
    # find docker daemnon path
    docker_desktop = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"

    # start daemon
    subprocess.Popen([docker_desktop])

    wait(20)

    # start docker
    subprocess.Popen(["docker", "compose", "--profile", "production", "up"])

def dev_local():
    """
    PURPOSE:
    This function is called when context is development and deployed on local

    STEPS:
    1. activate virtual environment
    2. check if pc can read environment file
    2. change shell location to `manage.py` directory
    3. run `python manage.py runserver`
    """
    
    subprocess.Popen(["..\\core\\.venv\\Scripts\\activate.bat"])
    os.chdir("../core")

    if not os.path.exists("./.venv/Lib/site-packages/environ"):
        subprocess.Popen(["pip", "install", "django-environ"])
    
    subprocess.Popen(["python", "manage.py", "runserver"])

def production_local():
    """
    PURPOSE:
    This function is called when context is production and deployed on local

    STEPS:
    1. activate virtual environment
    2. check if pc can read environment file
    2. change shell location to `manage.py` directory
    3. run `python manage.py runserver`
    """
    subprocess.Popen(["..\\core\\.venv\\Scripts\\activate.bat"])
    os.chdir("../core")

    if not os.path.exists("./.venv/Lib/site-packages/environ"):
        subprocess.Popen(["pip", "install", "django-environ"])
    
    subprocess.Popen(["python", "manage.py", "runserver"])


if (env("CONTEXT") == "development" and
    env("DEPLOYMENT") == "local" and
    env("OS") == "Windows" and
    env("INFRASTRUCTURE") == "local"):
    """
    runs for docker compose in development mode
    """
    dev_local()

elif (env("CONTEXT") == "production" and
    env("DEPLOYMENT") == "local" and
    env("OS") == "Windows" and
    env("INFRASTRUCTURE") == "local"):
    """
    runs for docker compose in production mode
    """
    production_local()

elif (env("CONTEXT") == "development" and
    env("DEPLOYMENT") == "docker_compose" and
    env("OS") == "Windows" and
    env("INFRASTRUCTURE") == "local"):
    """
    runs for docker compose in development mode
    """
    docker_compose_dev()

elif (env("CONTEXT") == "production" and
    env("DEPLOYMENT") == "docker_compose" and
    env("OS") == "Windows" and
    env("INFRASTRUCTURE") == "local"):
    """
    runs for docker compose in development mode
    """
    docker_compose_production()