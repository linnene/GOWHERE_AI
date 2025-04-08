from pydantic import BaseModel, Field, model_validator
from datetime import datetime

class DATE(BaseModel):
    year: int
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    
    @model_validator(mode='after')
    def validate_date(cls, model):
        year = model.year
        month = model.month
        day = model.day
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError(f"Invalid date: {year}-{month}-{day}")
        return model

class TIME(BaseModel):

    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)


#交通通行时间模版
class Itinerary_time(BaseModel):
    date: DATE
    time: TIME

#住宿日期模版
class Stay_time(BaseModel):
    date: DATE

class Attr_time(BaseModel):
    date: DATE
    time: TIME
