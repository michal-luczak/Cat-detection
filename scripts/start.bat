@echo off
chcp 65001 >nul

cd %~dp0
docker compose -f ../docker/docker-compose.yml up cat-detection -d
if %errorlevel% neq 0 (
    echo [31mStarting docker container failed.[0m
    exit /b 1
)