from pydantic import BaseModel, field_validator

class SparkResponse(BaseModel):
    jud: str
    
    @field_validator('jud')
    @classmethod
    def validate_judgment(cls, v):
        if v not in ['True', 'False']:
            raise ValueError('判断结果必须为 "True" 或 "False"')
        return v