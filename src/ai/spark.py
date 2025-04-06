from sparkai.llm.llm import ChunkPrintHandler
from sparkai.core.messages import ChatMessage

from config import sp_pormpt,spark_client

#TODO:完善函数

# Spark Lite 发送聊天
def Spark_Send_Chat(role: str, content: str):    
    # 生成聊天消息
    messages = [
    ChatMessage(
        role= sp_pormpt.system_role,
        content= sp_pormpt.system_content
    ),
    ChatMessage(
        role= role,
        content= content
    )]
    # messages.append(ChatMessage(role="user", content=content)) [BULIKE]

    #发送消息并处理response
    try:
        handler = ChunkPrintHandler()
        a = spark_client.generate([messages], callbacks=[handler])

        response = extract_json(a.generations[0][0].text)
    except Exception as e:
        return {"Error": "Json Fail"}
    
    return response['jud']