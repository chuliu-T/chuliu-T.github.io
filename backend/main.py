from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.cmdb.routes import router as cmdb_router
from app.users.routes import router as users_router
from app.core import models
from app.core.database import engine
from fastapi.middleware.cors import CORSMiddleware



# 创建数据库表
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Service",
    description="A modern FastAPI service with authentication and CMDB functionality",
    version="1.0.0"
)


origins = [
    "http://106.14.91.113",
    "http://106.14.91.113/:8900",  # 根据你的前端端口修改
    "http://localhost",
    "*",
    # 可以添加更多允许的域名
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 你的路由和其他代码
app.include_router(users_router, prefix="/users", tags=["users"])

# Include routers from different modules
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(cmdb_router, prefix="/cmdb", tags=["cmdb"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Welcome to the API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }