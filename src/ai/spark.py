from sparkai.llm.llm import ChunkPrintHandler
from sparkai.core.messages import ChatMessage

from config.prompt import sp_pormpt
from config.config import spark_client
from schema.spark import SparkResponse
from crud.spark import extract_json

# Spark Lite 发送聊天
def Spark_Send_Chat(role: str, content: str) -> SparkResponse:    
    
    messages = [
    ChatMessage(
        role= sp_pormpt.system_role,
        content= sp_pormpt.system_content
    ),
    ChatMessage(
        role= role,
        content= content
    )]

    #发送消息并处理response
    try:
        handler = ChunkPrintHandler()
        a = spark_client.generate([messages], callbacks=[handler])#type: ignore

        response_dict = extract_json(a.generations[0][0].text)
        # 使用Pydantic模型验证和序列化
        print(SparkResponse(**response_dict))

        return SparkResponse(**response_dict)
    except Exception as e:
        # 返回规范化的错误响应
        return SparkResponse(jud="False")