import os
from schema.tools import Air,Hotel
from schema.base import DATE
from typing import List
import json

from .air_scraper import get_air_info

# 可以根据你注册的其他 tools 继续添加 import
def handle_tool_call(tool_call):
    
    """
    根据 tool_call 信息分发到对应的函数执行。
    参数：
        tool_call: 一个 ToolCall 对象（来自 chat_completion.choices[0].message.tool_calls）
    返回：
        函数运行结果对象（建议为 dict，可被 json 序列化）
    """

    tool_name = tool_call.function.name
    try:
        arguments = json.loads(tool_call.function.arguments)
    except json.JSONDecodeError as e:
        raise ValueError(f"解析 tool 参数失败: {e}")

    # 根据 tool 名称路由到具体的函数
    if tool_name == "get_Air":
        return get_Air(**arguments)
    
    else:
        raise NotImplementedError(f"未注册的工具函数: {tool_name}")

#CRUD：从JSON模板文件中读取模板
def load_template_from_json(file_path="d:\\gowhere_pro\\GOWHERE_AI\\src\\templates\\travel_plan_template.json"):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"警告: 模板文件不存在: {file_path}")
            return "{}"
    except Exception as e:
        print(f"读取模板文件时出错: {e}")
        return "{}"

#CRUD：从ChatCompletion对象提取文本内容
def extract_text(chat_completion):
    try:
        # 尝试获取回复内容 - 适用于OpenAI的ChatCompletion对象
        msg = chat_completion.choices[0].message

        if msg.tool_calls:
            return {
                'type': 'tool_call',
                'tool_calls': chat_completion.choices[0].message.tool_calls
            }
        
        return {
            "type": "reply",
            "content": msg.content
        }
    
    except (AttributeError, IndexError, TypeError):
        try:
            return str(chat_completion)
        except:
            return "无法提取回复内容"
        
        
#CRUD：获取机票信息 TODO:实现函数
def get_Air(dep_air:str, des_air:str, date:str):
    """
        搜索获取[dep-des]日期的机票详情：
        Air{
            dep_air: str = Field(..., description="出发地点")
            des_air: str = Field(..., description="到达地点")
            price: float = Field(..., description="机票价格")
            dep_time: Itinerary_time = Field(..., description="出发时间")
            des_time: Itinerary_time = Field(..., description="到达时间")
            airline: str = Field(..., description="航空公司")
        }
    """
    year, month, day = map(int, date.split('-'))

    Date = DATE(year=str(year),month=str(month),day=str(day)) 
    Air_list = []
    Air_list = get_air_info(dep_air, des_air, Date)

    result = [air.model_dump() for air in Air_list]

    return result


#CRUD：获取指定地点附近酒店信息（10km？）TODO:实现函数
def get_Hotel_by_loc(location:str, date:DATE)-> List[Hotel]:
    """
    搜索指定酒店名称的酒店信息include：
        hotel_name: str, 酒店名称
        address: str, 地址
        star: str, 星级
        room:room = {
            room_type: str, 房型
            price: str, 价格
            free_room: bool, 指定时间内是否有房间   
        }
    """
    pass

#CRUD：获取指定酒店信息（10km？） TODO:实现函数
def get_Hotel_by_name(hotel_name:str,date:DATE)-> Hotel:
    """
    搜索指定酒店名称的酒店信息include：
        hotel_name: str, 酒店名称
        address: str, 地址
        star: str, 星级
        room:room = {\
            room_type: str, 房型
            price: str, 价格
            free_room: bool, 指定时间内是否有房间   
        }
    """
    pass

#CRUD：获取指定地点天气信息 TODO:实现函数
"""
目前只有国内编码数据库，国外天气数据考虑使用google maps API 或者爬虫网站
"""
def  get_weather_by_loc(location:str,date)-> str:
    """
    获取指定地点的天气信息
    """
    pass