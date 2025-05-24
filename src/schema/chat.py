from pydantic import BaseModel,Field
from typing import List

class Chat_block(BaseModel):
    """

    对话块
    该类用于表示对话中的一个块，包含角色、内容和时间戳
    Attributes:
        role (str): 角色，表示说话者的身份
        content (str): 内容，表示说话者所说的话
        timestamp (str): 时间戳，表示对话发生的时间

    """

    role:str = "user"
    content:str


class tool_block(BaseModel):
    """
    工具块
    该类用于表示对话中的一个工具块，包含工具名称、参数和时间戳
    Attributes:
        tool_name (str): 工具名称，表示使用的工具的名称
        parameters (dict): 参数，表示传递给工具的参数
        timestamp (str): 时间戳，表示对话发生的时间
    """

    role:str = "tools_call"
    content:str
