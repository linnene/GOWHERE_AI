import os
from schema.tools import Air,Hotel
from schema.base import DATE
from typing import List

from .air_scraper import get_air_info

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
        return chat_completion.choices[0].message.content
    except (AttributeError, IndexError, TypeError):
        try:
            # 如果上面的方法失败，尝试直接转字符串
            return str(chat_completion)
        except:
            return "无法提取回复内容"
        
#CRUD：获取机票信息 TODO:实现函数
def get_Air(dep_air:str, des_air:str, date:DATE)-> List[Air]:
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

    Air_list = []
    Air_list = get_air_info(dep_air, des_air, date)

    return Air_list


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