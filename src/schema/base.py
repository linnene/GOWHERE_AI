from pydantic import BaseModel, Field, model_validator
from datetime import datetime

#BASE_SCHEMA：基础日期
class DATE(BaseModel):
    year: str 
    month: str 
    day: str 
        
    @model_validator(mode='after')
    def validate_date(cls, model):
        year = model.year
        month = model.month
        day = model.day
        
        # 先检查是否是有效的数字字符串
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise ValueError(f"Date components must be numeric: {year}-{month}-{day}")
        
        # 转换为整数
        year_int, month_int, day_int = int(year), int(month), int(day)
        
        # 基本范围检查
        if not (1 <= month_int <= 12):
            raise ValueError(f"Month must be between 1 and 12, got {month}")
        
        if not (1 <= day_int <= 31):
            raise ValueError(f"Day must be between 1 and 31, got {day}")
        
        # 最终使用datetime进行全面检查
        try:
            datetime(year_int, month_int, day_int)
        except ValueError:
            raise ValueError(f"Invalid date: {year}-{month}-{day}")
        
        return model


#BASE_SCHEMA：基础时间
class TIME(BaseModel):

    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)


#SCHEMA：交通通行时间模版
class Itinerary_time(BaseModel):
    date: DATE
    time: TIME


#SCHEMA：住宿日期
class Stay_time(BaseModel):
    date: DATE

#SCHEMA：景点游玩时间
class Attr_time(BaseModel):
    date: DATE
    time: TIME



