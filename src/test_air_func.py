from crud.dp import get_Air 
from schema.base import DATE

if __name__ == "__main__":
    dep = "重庆"
    des = "伦敦"
    date = DATE(year="2025", month="5", day="6")

    air_info_list = get_Air(dep, des, date)

    for air in air_info_list:
        print(air.model_dump_json(indent=2, exclude_none=True))