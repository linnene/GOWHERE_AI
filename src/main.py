from schema.dp_json import dp_travel_plan, dp_day_task, dp_Itinerary_Schema, dp_Stay_Schema, dp_Attr_Schema
from schema.base import Itinerary_time, Stay_time, Attr_time, DATE, TIME
import json
import os

# 创建一个示例旅行计划
def create_travel_plan_template():
    # 创建第一天的行程
    day1 = dp_day_task(
        day_num=1,
        task="从北京出发前往上海，入住酒店，游览外滩",
        itinerary=[
            dp_Itinerary_Schema(
                Des="乘坐高铁从北京南站前往上海虹桥站",
                Dep_Date=Itinerary_time(
                    date=DATE(year=2023, month=5, day=1),
                    time=TIME(hour=9, minute=0)
                ),
                Des_Date=Itinerary_time(
                    date=DATE(year=2023, month=5, day=1),
                    time=TIME(hour=14, minute=30)
                ),
                Dep_Place="北京南站",
                Des_Place="上海虹桥站",
                Price=553
            )
        ],
        stay=[
            dp_Stay_Schema(
                Des="入住上海XX酒店",
                stay_date=Stay_time(
                    date=DATE(year=2023, month=5, day=1)
                ),
                leave_date=Stay_time(
                    date=DATE(year=2023, month=5, day=3)
                ),
                stay_place="上海XX酒店",
                price="680/晚"
            )
        ],
        attr=[
            dp_Attr_Schema(
                Des="游览上海外滩夜景",
                price="免费",
                attr_place="上海外滩",
                attr_date=Attr_time(
                    date=DATE(year=2023, month=5, day=1),
                    time=TIME(hour=19, minute=0)  # 添加时间字段
                )
            )
        ]
    )
    
    # 创建第二天的行程
    day2 = dp_day_task(
        day_num=2,
        task="游览上海迪士尼乐园",
        attr=[
            dp_Attr_Schema(
                Des="全天游玩上海迪士尼乐园",
                price="580元/人",
                attr_place="上海迪士尼乐园",
                attr_date=Attr_time(
                    date=DATE(year=2023, month=5, day=2),
                    time=TIME(hour=9, minute=0)  # 添加时间字段
                )
            )
        ]
    )
    
    # 创建第三天的行程
    day3 = dp_day_task(
        day_num=3,
        task="参观上海博物馆，返回北京",
        itinerary=[
            dp_Itinerary_Schema(
                Des="乘坐高铁从上海虹桥站返回北京南站",
                Dep_Date=Itinerary_time(
                    date=DATE(year=2023, month=5, day=3),
                    time=TIME(hour=16, minute=0)
                ),
                Des_Date=Itinerary_time(
                    date=DATE(year=2023, month=5, day=3),
                    time=TIME(hour=21, minute=30)
                ),
                Dep_Place="上海虹桥站",
                Des_Place="北京南站",
                Price=553
            )
        ],
        attr=[
            dp_Attr_Schema(
                Des="参观上海博物馆",
                price="免费",
                attr_place="上海博物馆",
                attr_date=Attr_time(
                    date=DATE(year=2023, month=5, day=3),
                    time=TIME(hour=10, minute=0)  # 添加时间字段
                )
            )
        ]
    )
    
    # 创建完整旅行计划
    travel_plan = dp_travel_plan(
        title="三天两晚上海休闲之旅",
        description="这是一次从北京出发到上海的短途旅行，包括游览外滩夜景、上海迪士尼乐园和上海博物馆等著名景点。",
        total_days=3,
        start_date="2023-05-01",
        end_date="2023-05-03",
        total_budget=3500.0,
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