from pydantic import BaseModel
from base import date

#交通通行信息模版
class dp_Itinerary_schema(BaseModel):
    """
    Attributes:
        dep_date (str): 出发时间.
        des_date (str): 到达时间.
        dep_airport (str): 出发机场.
        des_airport (str): 到达机场.
        price (str): 行程花费.
    """
    dep_date: date
    des_date: date
    dep_airport: str
    des_airport: str
    price: str