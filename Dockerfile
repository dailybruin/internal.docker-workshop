# using dockerhub's python image as a base
from python:latest

# all the following commands will be executed in /app
WORKDIR /app

# COPY host, container
COPY os_info.py os_info.py

# We can also change the name of the file when we copy
COPY make_random_files.py mrf.py

