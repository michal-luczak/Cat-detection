#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

docker-compose -f ../docker/docker-compose.yml up cat-detection -d

if [ $? -ne 0 ]; then
    echo -e "\033[31mStarting docker container failed.\033[0m"
    exit 1
fi
