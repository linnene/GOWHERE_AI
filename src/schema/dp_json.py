from pydantic import BaseModel
from base import Itinerary_time, Stay_time

#交通通行信息模版
class dp_Itinerary_schema(BaseModel):

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
class dp_Stay_schema(BaseModel):

    """
    Attributes:
        Des(str): 描述.
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