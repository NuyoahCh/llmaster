from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """可视化服务配置"""
    
    # 基础配置
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    # Redis配置
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_PASSWORD: Optional[str] = None
    
    # 执行限制
    MAX_EXECUTION_TIME: int = 30
    MAX_MEMORY_MB: int = 512
    MAX_CODE_LENGTH: int = 10000
    
    # 静态文件配置
    STATIC_FILES_PATH: str = "/app/static"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 全局配置实例
settings = Settings() 