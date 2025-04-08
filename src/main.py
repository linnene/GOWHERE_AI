from schema.dp_json import (
    dp_travel_plan, dp_day_task, 
    dp_Itinerary_Dep_Schema, dp_Itinerary_Des_Schema,
    dp_Stay_stay_Schema, dp_Stay_leave_Schema,
    dp_Attr_start_Schema, dp_Attr_end_Schema
)
from schema.base import Itinerary_time, Stay_time, Attr_time, DATE, TIME
import json
import os

# 创建一个示例旅行计划
def create_travel_plan_template():
    # 创建第一天的行程 - 从重庆出发前往北海道
    day1 = dp_day_task(
        day_num=1,
        task="从重庆出发前往日本北海道，抵达札幌后入住酒店",
        itinerary_dep=[
            dp_Itinerary_Dep_Schema(
                Des="从重庆江北国际机场出发，乘坐春秋航空9C8982航班",
                Dep_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=15),
                    time=TIME(hour=9, minute=30)
                ),
                Dep_Place="重庆江北国际机场T3航站楼",
                Price=1200
            )
        ],
        itinerary_des=[
            dp_Itinerary_Des_Schema(
                Des="抵达日本北海道新千岁机场，乘坐机场大巴前往札幌市区",
                Des_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=15),
                    time=TIME(hour=16, minute=0)
                ),
                Des_Place="北海道新千岁机场",
                Price=150
            )
        ],
        stay_in=[
            dp_Stay_stay_Schema(
                Des="入住札幌王子酒店，毗邻札幌中心商业区，交通便利",
                stay_date=Stay_time(
                    date=DATE(year=2023, month=7, day=15)
                ),
                stay_place="札幌王子酒店(Sapporo Prince Hotel)"
            )
        ],
        attr_in=[
            dp_Attr_start_Schema(
                Des="抵达后游览札幌电视塔，俯瞰札幌全景",
                attr_place="札幌电视塔",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=15),
                    time=TIME(hour=19, minute=0)
                )
            )
        ],
        attr_out=[
            dp_Attr_end_Schema(
                Des="结束札幌电视塔参观，在附近薄野地区享用当地美食",
                price="1000日元/人",
                attr_place="札幌电视塔",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=15),
                    time=TIME(hour=20, minute=30)
                )
            )
        ]
    )
    
    # 创建第二天的行程 - 游览小樽和洞爷湖
    day2 = dp_day_task(
        day_num=2,
        task="前往小樽运河和洞爷湖一日游",
        itinerary_dep=[
            dp_Itinerary_Dep_Schema(
                Des="从札幌站乘坐JR特快列车前往小樽",
                Dep_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=16),
                    time=TIME(hour=8, minute=0)
                ),
                Dep_Place="札幌JR站",
                Price=640
            )
        ],
        itinerary_des=[
            dp_Itinerary_Des_Schema(
                Des="抵达小樽站，开始小樽运河一日游",
                Des_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=16),
                    time=TIME(hour=8, minute=45)
                ),
                Des_Place="小樽JR站",
                Price=0
            )
        ],
        attr_in=[
            dp_Attr_start_Schema(
                Des="游览小樽运河历史景区，欣赏古老的仓库建筑",
                attr_place="小樽运河",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=16),
                    time=TIME(hour=9, minute=15)
                )
            )
        ],
        attr_out=[
            dp_Attr_end_Schema(
                Des="离开小樽运河，前往北一硝子馆和音乐盒博物馆",
                price="免费",
                attr_place="小樽运河",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=16),
                    time=TIME(hour=11, minute=30)
                )
            )
        ]
    )
    
    # 创建第三天的行程 - 返回重庆
    day3 = dp_day_task(
        day_num=3,
        task="游览北海道大学，然后返回重庆",
        stay_out=[
            dp_Stay_leave_Schema(
                Des="退房札幌王子酒店",
                leave_date=Stay_time(
                    date=DATE(year=2023, month=7, day=17)
                ),
                leave_place="札幌王子酒店(Sapporo Prince Hotel)",
                price="1800元/晚 × 2晚"
            )
        ],
        attr_in=[
            dp_Attr_start_Schema(
                Des="参观北海道大学校园及其著名的银杏大道",
                attr_place="北海道大学",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=17),
                    time=TIME(hour=9, minute=0)
                )
            )
        ],
        attr_out=[
            dp_Attr_end_Schema(
                Des="结束北海道大学参观",
                price="免费",
                attr_place="北海道大学",
                attr_time=Attr_time(
                    date=DATE(year=2023, month=7, day=17),
                    time=TIME(hour=11, minute=0)
                )
            )
        ],
        itinerary_dep=[
            dp_Itinerary_Dep_Schema(
                Des="从新千岁机场乘坐春秋航空9C8981航班返回重庆",
                Dep_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=17),
                    time=TIME(hour=17, minute=30)
                ),
                Dep_Place="北海道新千岁机场",
                Price=1500
            )
        ],
        itinerary_des=[
            dp_Itinerary_Des_Schema(
                Des="抵达重庆江北国际机场，旅程结束",
                Des_Date=Itinerary_time(
                    date=DATE(year=2023, month=7, day=17),
                    time=TIME(hour=22, minute=0)
                ),
                Des_Place="重庆江北国际机场",
                Price=0
            )
        ]
    )
    
    # 创建完整旅行计划
    travel_plan = dp_travel_plan(
        title="重庆出发·北海道三日游",
        description="这是一次从重庆出发到日本北海道的短途旅行，包括游览札幌市区、小樽运河、洞爷湖等著名景点。在这三天中，您将体验北海道独特的自然风光和城市魅力。",
        total_days=3,
        start_date="2023-07-15",
        end_date="2023-07-17",
        total_budget=6500.0,
        daily_plans=[day1, day2, day3]
    )
    
    # 转换为JSON格式
    return json.dumps(travel_plan.model_dump(), ensure_ascii=False, indent=4)

# 获取JSON模板
travel_plan_json_template = create_travel_plan_template()

# 将旅行计划模板保存到JSON文件
def save_template_to_json(json_content, file_path="d:\\gowhere_pro\\GOWHERE_AI\\src\\templates\\travel_plan_template.json"):
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 写入JSON文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_content)
    
    print(f"旅行计划模板已保存到: {file_path}")

# 打印模板或将其用于提示AI
if __name__ == "__main__":
    print(travel_plan_json_template)
    save_template_to_json(travel_plan_json_template)

# AI提示模板
ai_prompt_template = """
根据用户提供的旅行需求，请生成一个详细的旅行计划，格式如下JSON所示：

{travel_plan_json}

请确保按照上述格式生成旅行计划，包括标题、描述、总天数、日期、预算和每日行程详情。每日行程可能包含或不包含交通、住宿和景点游览安排。
""".format(travel_plan_json=travel_plan_json_template)

# """
# MAIN FILE
# """



# #----------------Test the Spark_Send_Chat function------------------
# from ai.spark import Spark_Send_Chat
# if __name__ == "__main__": 
#     # 发送聊天消息
#     role = "user"
#     content = "Hello,我想从重庆出发到上海旅游三天，你有什么建议吗？"
#     try:
#         # 调用函数
#         response = Spark_Send_Chat(role, content)
#     except Exception as e:
#         # 处理异常
#         print(f"发生错误: {e}")
#         response = None
    
#     # 打印响应
#     print(response.jud)
# #----------------------------------------------------------------------