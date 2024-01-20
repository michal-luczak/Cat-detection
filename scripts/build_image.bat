@echo off
chcp 65001 >nul

docker -v >nul 2>&1
if %errorlevel% neq 0 (
    echo [31mDocker is not installed.[0m
    exit /b 1
)

docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [31mDocker engine is not running.[0m
    exit /b 1
)

cd %~dp0
echo [32mBuilding docker image...[0m
docker-compose -f ../docker/docker-compose.yml build
if %errorlevel% neq 0 (
    echo [31mBuilding docker image failed.[0m
    exit /b 1
)

echo [32mThe image was built successfully.[0m
