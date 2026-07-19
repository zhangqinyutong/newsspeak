# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

# 定义配置类，存放所有环境变量
class Settings(BaseSettings):
    # 告诉程序：去 .env 文件读取变量，编码utf-8
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # 下面每一行对应 .env 里的一个变量
    DEEPSEEK_API_KEY: str
    DEEPSEEK_BASE_URL: str

    AZURE_SPEECH_KEY: str
    AZURE_SPEECH_REGION: str

    NEWS_API_KEY: str
    TAVILY_API_KEY: str

    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str

# 实例化全局配置对象，整个项目共用
settings = Settings()