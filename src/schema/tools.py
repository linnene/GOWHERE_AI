from pydantic import BaseModel,Field
from .base import Itinerary_time

#SCHEMA：机票信息
class Air(BaseModel):
    dep_air: str = Field(..., description="出发地点")
    des_air: str = Field(..., description="到达地点")
    price: str = Field(..., description="机票价格")

    dep_time: Itinerary_time = Field(..., description="出发时间")
    des_time: Itinerary_time = Field(..., description="到达时间")
    # 可能需要更复杂的时间格式化
    airline: str = Field(..., description="航空公司")


#SCHEMA: 房间信息
class room(BaseModel):
    room_type: str = Field(..., description="房型")
    price: float = Field(..., description="价格")
    free_room: bool = Field(..., description="指定时间内是否有房间")
    room_num: int = Field(..., description="剩余房间数")
    
#SCHEMA：酒店信息
class Hotel(BaseModel):
    hotel_name: str = Field(..., description="酒店名称")
    address: str = Field(..., description="酒店地址")
    star: str = Field(..., description="酒店星级")
    room_list: list[room] = Field(..., description="房间列表")