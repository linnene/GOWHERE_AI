"""
MAIN FILE
"""



#----------------Test the Spark_Send_Chat function------------------
from ai.spark import Spark_Send_Chat
if __name__ == "__main__":
    # 发送聊天消息
    role = "user"
    content = "Hello,我想从重庆出发到上海旅游三天，你有什么建议吗？"
    try:
        # 调用函数
        response = Spark_Send_Chat(role, content)
    except Exception as e:
        # 处理异常
        print(f"发生错误: {e}")
        response = None
    
    # 打印响应
    print(response.jud)
#----------------------------------------------------------------------