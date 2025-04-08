import json
import re

def extract_json(text: str) -> dict:
    """
    从AI返回的文本中提取JSON数据
    """

    json_pattern = r'(\{.*?\})'
    match = re.search(json_pattern, text, re.DOTALL)
    
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return {"jud": "False"} # 默认视为无关信息
    return {"jud": "False"}
