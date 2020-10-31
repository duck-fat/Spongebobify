# set base image (host OS)
FROM jfloff/alpine-python:3.8-slim

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# copy the content of the local src directory to the working directory
COPY main.py .

# -P is part of the base image
# https://github.com/jfloff/alpine-python/blob/7ae8be3ff086e91051a478ae5fa9acb9f4ec6967/3.8-slim/entrypoint.sh#L23
# -P: requirements.txt file location (in the container), default is /requirements.txt
# The base image attempts to pip install dependencies when the container starts using requirements.txt
CMD [ "-P", "/code/requirements.txt", "python", "./main.py" ]
