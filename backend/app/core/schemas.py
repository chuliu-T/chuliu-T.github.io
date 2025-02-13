from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# 基础响应模型
class BaseResponse(BaseModel):
    success: bool = True
    message: str = "Operation successful"

# 分页模型
class PaginationParams(BaseModel):
    skip: int = 0
    limit: int = 100

# 通用时间戳混入
class TimestampMixin(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None

# 错误响应模型
class ErrorResponse(BaseModel):
    detail: str
    
    class Config:
        from_attributes = True

# 状态响应
class StatusResponse(BaseModel):
    status: str
    message: str | None = None 