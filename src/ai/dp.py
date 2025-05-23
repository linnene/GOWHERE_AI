from config.prompt import ds_pormpt, tools_list
from config.config import get_ds_client
from crud.dp import extract_text


def send_message(message:str):
    ds_client = get_ds_client()
    response = ds_client.chat.completions.create(  
        model="deepseek-chat",
        messages=[
            {"role": ds_pormpt.system_role, "content": ds_pormpt.system_content},#type: ignore
            {"role": "user", "content": message},
        ],
        stream=False,
        response_format={"type":"json_object"},
        tools= tools_list,#type: ignore
        )#type: ignore
    # message = response['choices'][0]['message']

    return response