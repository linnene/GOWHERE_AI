#type: ignore
from crud.dp import extract_text,handle_tool_call
from ai.dp import send_message
from config.prompt import ds_pormpt
# from crud.dp import get_chat_by_id

import json


CHAT = [{"role": ds_pormpt.system_role, "content": ds_pormpt.system_content}]



def chat_loop(message,UserId:str):
    user_chat = CHAT

    user_chat.append(
        {
            "role" : "user",
            "content": message
        }
    )

    chat_completion = send_message(user_chat)
    response_result = extract_text(chat_completion)


    if response_result["type"] == "reply":
        user_chat.append({
                "role" : "assistant",
                "content" : response_result["content"]}
        )

        print("Assistant:", response_result["content"])

    elif response_result["type"] == "tool_call":
        for call in response_result["tool_calls"]:
            user_chat.append({
                "role": "assistant",
                "tool_calls": [
                    {
                    "id":call.id,
                    "type": "function",
                    "function": {"name": call.function.name, "arguments": call.function.arguments} 
                    }
                ]
            })
            tool_result = handle_tool_call(call)   
            user_chat.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": f"{json.dumps(tool_result, ensure_ascii=False)}"
                }
            )

    elif response_result["type"] == "error":
        print("发生错误：", response_result["error"])
                                                    

if __name__ == "__main__":
    msg = "帮我规划一个成都到三亚的五日游，预算5000元左右"
    chat_loop(msg,"qweqrtq")
    while 1:
        message, UserId = input("请输入消息, 用户ID: ").split(" ")

        if message.lower() == "exit":
            break
        chat_loop(message,UserId)

    print("聊天结束")