@echo off
echo [32mRunning unit tests.[0m

cd %~dp0
pytest ../tests

if %ERRORLEVEL% equ 0 (
    echo [32mTests passed successfully.[0m
) else (
Tests failed.
    echo [31mTests failed.[0m
)