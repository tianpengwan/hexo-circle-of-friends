from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
import os
import sys

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入友链朋友圈的主应用
try:
    from friend_links_circle import app
except ImportError:
    # 如果导入失败，创建新的应用
    app = FastAPI(title="友链朋友圈")
    
    @app.get("/")
    async def root():
        return {"message": "友链朋友圈正在运行"}

# 可选：添加健康检查端点
@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})
