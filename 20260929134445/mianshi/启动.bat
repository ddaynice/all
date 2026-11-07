@echo off
chcp 65001 >nul
cd /d %~dp0

python -c "import fastapi,uvicorn,httpx,dotenv" 2>nul
if errorlevel 1 (
    echo 正在安装依赖...
    pip install -r app\requirements.txt
)

start "" http://127.0.0.1:8600/
python -m uvicorn app.server:app --host 127.0.0.1 --port 8600
pause
