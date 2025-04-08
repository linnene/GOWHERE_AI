from pydantic import BaseModel
from typing import Optional, List
from schema.base import Itinerary_time, Stay_time, Attr_time  # 修正导入路径

#交通通行信息模版
class dp_Itinerary_Schema(BaseModel):
    """
    Attributes:
    Des (str): 行程描述.
    dep_date (Itinerary_time): 出发时间.
    des_date (Itinerary_time): 到达时间.
    dep_place (str): 出发地点.
    des_place (str): 到达地点.
    price (str): 行程花费.

    """

    Des: str
    Dep_Date: Itinerary_time
    Des_Date: Itinerary_time

    Dep_Place: str
    Des_Place: str
    Price: int


#住宿信息模版
class dp_Stay_Schema(BaseModel):
    """
    Attributes:
    Des(str): 住宿点描述.
    stay_date (Stay_time): 入住日期.
    leave_date (Stay_time): 离店日期.
    stay_place (str): 入住地点.
    price (str): 住宿花费.

    """

    Des: str
    stay_date: Stay_time
    leave_date: Stay_time

    stay_place: str
    price: str

#景点信息模版
class dp_Attr_Schema(BaseModel):
    """
    Attributes: str =
    Des (str): 景点描述.
    attr_place (str): 景点地点.
    price (str): 景点花费.
    attr_date (Attr_time): 景点日期.
    """

    Des: str
    price: str
    attr_place: str
    attr_date: Attr_time


class dp_day_task(BaseModel):
    """
    Attributes:

    day_num (int): 行程天数(第一天，第二天...).
    task (str): 任务描述.
    itinerary (Optional[list[dp_Itinerary_Schema]]): 行程信息，可能为空.
    stay (Optional[list[dp_Stay_Schema]]): 住宿信息，可能为空.
    attr (Optional[list[dp_Attr_Schema]]): 景点信息，可能为空.

    """

    day_num: int
    task: str
    itinerary: Optional[List[dp_Itinerary_Schema]] = None
    stay: Optional[List[dp_Stay_Schema]] = None
    attr: Optional[List[dp_Attr_Schema]] = None



# 完整旅程计划模型
class dp_travel_plan(BaseModel):
    """
    Attributes:
    title (str): 旅程计划标题.
    description (str): 旅程整体描述.
    total_days (int): 旅程总天数.
    start_date (str): 旅程开始日期，格式: YYYY-MM-DD.
    end_date (str): 旅程结束日期，格式: YYYY-MM-DD.
    total_budget (float): 旅程总预算.
    daily_plans (list[dp_day_task]): 每天的详细计划.
    """
    
    title: str
    description: str
    total_days: int
    start_date: str
    end_date: str
    total_budget: float
    daily_plans: list[dp_day_task]