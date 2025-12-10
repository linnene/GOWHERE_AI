from config.prompt import ds_pormpt, tools_list
from config.config import get_ds_client
from crud.dp import extract_text


def send_message(message):
    ds_client = get_ds_client()
    response = ds_client.chat.completions.create(
        model="deepseek-chat",
        #直接
        messages=message,
        stream=False,
        response_format={"type":"json_object"},
        tools= tools_list,#type: ignore
    )
    # message = response['choices'][0]['message']

    return response