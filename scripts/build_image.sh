#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

docker -v > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo -e "\033[31mDocker is not installed.\033[0m"
    exit 1
fi

docker info > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo -e "\033[31mDocker engine is not running.\033[0m"
    exit 1
fi

cd ../docker
echo -e "\033[32mBuilding docker image...\033[0m"
docker-compose build cat-detection

if [ $? -ne 0 ]; then
    echo -e "\033[31mBuilding docker image failed.\033[0m"
    exit 1
fi

echo -e "\033[32mThe image was built successfully.\033[0m"
