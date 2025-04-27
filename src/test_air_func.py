from crud.air_scraper import get_air_info 
from schema.base import DATE

if __name__ == "__main__":
    dep = "重庆"
    des = "东京"
    date = DATE(year="2025", month="5", day="6")

    air_info_list = get_air_info(dep, des, date)

    for air in air_info_list:
        print(air)
