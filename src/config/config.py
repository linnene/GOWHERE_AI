from sparkai.llm.llm import ChatSparkLLM 
from openai import OpenAI

#---------------------------------------------------------------------
# 项目配置
class SETTINGS:
    
    # DeepSeek Settings
    DEEPSEEK_API_KEY="sk-b57a22dfcb4c471093e7a5b3c374bea5" 
    DEEPSEEK_CONNECT_URL="https://api.deepseek.com"

    # SparkAI Settings
    SPARKAI_URL: str = 'wss://spark-api.xf-yun.com/v1.1/chat'
    SPARKAI_APP_ID: str = '09ad01bc'
    SPARKAI_API_SECRET: str = 'ZTlhMDhhZjVmMGRjNTY4NTU3YjkzYWYx'
    SPARKAI_API_KEY: str = 'cae44245a07950fca48d6523e28aec7b'
    SPARKAI_DOMAIN: str = 'lite'

settings = SETTINGS()
#---------------------------------------------------------------------

#SPARK LITE AI 基础设置
spark_client = ChatSparkLLM(
        spark_api_url=settings.SPARKAI_URL,
        spark_app_id=settings.SPARKAI_APP_ID,
        spark_api_key=settings.SPARKAI_API_KEY,
        spark_api_secret=settings.SPARKAI_API_SECRET,
        spark_llm_domain=settings.SPARKAI_DOMAIN,
        streaming=False,
    )

#deepseek AI 基础设置
ds_client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY, 
    base_url=settings.DEEPSEEK_CONNECT_URL
    )
