import os

#CRUD：从JSON模板文件中读取模板
def load_template_from_json(file_path="d:\\gowhere_pro\\GOWHERE_AI\\src\\templates\\travel_plan_template.json"):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            print(f"警告: 模板文件不存在: {file_path}")
            return "{}"
    except Exception as e:
        print(f"读取模板文件时出错: {e}")
        return "{}"


# CRUD：从ChatCompletion对象提取文本内容
def extract_text(chat_completion):
    try:
        # 尝试获取回复内容 - 适用于OpenAI的ChatCompletion对象
        return chat_completion.choices[0].message.content
    except (AttributeError, IndexError, TypeError):
        try:
            # 如果上面的方法失败，尝试直接转字符串
            return str(chat_completion)
        except:
            return "无法提取回复内容"