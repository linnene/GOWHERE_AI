from pydantic import BaseModel
from typing import Optional, List
from schema.base import Itinerary_time, Stay_time, Attr_time  # 修正导入路径

#------------------交通通行信息模版------------------
#出发Task
class dp_Itinerary_Dep_Schema(BaseModel):
    
    """
    Attributes:
    Des (str): 行程描述(包括路过的美景，交通方式，飞机航司、机型，火车车型车号等).
    dep_date (Itinerary_time): 出发时间.
    dep_place (str): 出发地点（机场名称，高铁站点，巴士站点的名称等）.
    price (str): 行程花费.
    """

    Des: str
    Dep_Date: Itinerary_time

    Dep_Place: str
    Price: int

#到达Task
class dp_Itinerary_Des_Schema(BaseModel):
    """
    Attributes:
    Des (str): 行程描述(包括路过的美景，交通方式，飞机航司、机型，火车车型车号等).
    des_date (Itinerary_time): 到达时间.
    des_place (str): 到达地点（机场名称，高铁站点，巴士站点的名称等）.
    price (str): 行程花费.
    """

    Des: str
    Des_Date: Itinerary_time

    Des_Place: str
    Price: int

#------------------交通通行信息模版------------------


#--------------------住宿信息模版--------------------

#入住Task—Schema
class dp_Stay_stay_Schema(BaseModel):
    """
    Attributes:
    Des(str): 住宿点描述.
    stay_date (Stay_time): 入住日期.
    stay_place (str): 入住地点.

    """

    Des: str
    stay_date: Stay_time

    stay_place: str


#退房Task—Schema
class dp_Stay_leave_Schema(BaseModel):
    """
    Attributes:
    Des(str): 住宿点描述.
    leave_date (Stay_time): 离开日期.
    leave_place (str): 离开地点.
    price (str): 住宿花费.

    """

    Des: str
    leave_date: Stay_time

    leave_place: str
    price: str

#--------------------住宿信息模版--------------------


#--------------------景点信息模版--------------------
#景点进入Task—Schema
class dp_Attr_start_Schema(BaseModel):
    """
    Attributes: str =
    Des (str): 景点描述.
    attr_place (str): 景点地点.
s    attr_date (Attr_time): 进入时间.

    """

    Des: str
    attr_place: str
    attr_time: Attr_time

class dp_Attr_end_Schema(BaseModel):
    """
    Attributes:
    Des (str): 景点描述.
    price (str): 景点花费.
    attr_place (str): 景点地点.
    attr_date (Attr_time): 离开时间.
    """

    Des: str
    price: str
    attr_place: str
    attr_time: Attr_time


#--------------------景点信息模版--------------------


class dp_day_task(BaseModel):
    """
    Attributes:
    day_num (int): 行程天数(第一天，第二天...).
    task (str): 当天任务总体描述.
    itinerary_dep (Optional[List[dp_Itinerary_Dep_Schema]]): 出发交通信息，可能为空.
    itinerary_des (Optional[List[dp_Itinerary_Des_Schema]]): 到达交通信息，可能为空.
    stay_in (Optional[List[dp_Stay_stay_Schema]]): 入住信息，可能为空.
    stay_out (Optional[List[dp_Stay_leave_Schema]]): 退房信息，可能为空.
    attr_in (Optional[List[dp_Attr_start_Schema]]): 景点进入信息，可能为空.
    attr_out (Optional[List[dp_Attr_end_Schema]]): 景点离开信息，可能为空.
    """

    day_num: int
    task: str
    itinerary_dep: Optional[List[dp_Itinerary_Dep_Schema]] = None
    itinerary_des: Optional[List[dp_Itinerary_Des_Schema]] = None
    stay_in: Optional[List[dp_Stay_stay_Schema]] = None
    stay_out: Optional[List[dp_Stay_leave_Schema]] = None
    attr_in: Optional[List[dp_Attr_start_Schema]] = None
    attr_out: Optional[List[dp_Attr_end_Schema]] = None


# 完整旅程计划模型
class dp_travel_plan(BaseModel):
    
    """
    Attributes:
    title (str): 旅程计划标题.
    description (str): 旅程整体描述.
    total_days (int): 旅程总天数.
    start_date (str): 旅程开始日期，格式: YYYY-MM-DD.
    end_date (str): 旅程结束日期，格式: YYYY-MM-DD.
    total_budget (float): 旅程总预算（不包括.....）.
    daily_plans (list[dp_day_task]): 每天的详细计划.
    """
    
    title: str
    description: str
    total_days: int
    start_date: str
    end_date: str
    total_budget: float
    daily_plans: list[dp_day_task]