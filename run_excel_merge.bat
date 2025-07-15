@echo off
set VENV_DIR=venv

if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

call %VENV_DIR%\Scripts\activate.bat

python -m pip install --upgrade pip

if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo Running merger.py...
python merger.py

pause
