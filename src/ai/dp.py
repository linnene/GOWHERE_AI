from config.prompt import ds_pormpt, tools_list
from config.config import get_ds_client
def send_message(message:str):
    ds_client = get_ds_client()
    response = ds_client.chat.completions.create(  
        model="deepseek-chat",
        messages=[
            {"role": ds_pormpt.system_role, "content": ds_pormpt.system_content},
            {"role": "user", "content": message},
        ],
        stream=False,
        response_format={"type":"json_object"},
        tools= tools_list,
        )
    return response