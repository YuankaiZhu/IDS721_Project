#!/usr/bin/env bash

# Build image
docker build --tag=cityfinder .

# List docker images
docker image ls

# Run flask app
docker run -p 5000:80 cityfinder
