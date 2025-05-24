#type: ignore
from crud.dp import extract_text,handle_tool_call
from ai.dp import send_message
import json


def func_call(message):
    chat_completion = send_message(message)
    print(chat_completion)
    response_result = extract_text(chat_completion)
    print(response_result)

    if response_result["type"] == "reply":
        print("AI回复：", response_result["content"])

    elif response_result["type"] == "tool_call":
        for call in response_result["tool_calls"]:
            tool_result = handle_tool_call(call)   
            print(tool_result)
            tool_message = {
                "role": "tool",
                "tool_call_id": call.id, 
                "content": json.dumps(tool_result, ensure_ascii=False)
            }
            print(tool_message)

        
    elif response_result["type"] == "error":
        print("发生错误：", response_result["error"])
                                                    

if __name__ == "__main__":
    msg = "帮我规划一个成都到三亚的五日游，预算5000元左右"
    func_call(msg)
