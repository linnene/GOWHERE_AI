from pydantic import BaseModel, Field


class date(BaseModel):
    """
    Schema for the date data

    Attributes:
        dep_date (str): Departure date.
        des_date (str): Destination date.
    """

    year: int
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)
