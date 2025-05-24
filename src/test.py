from crud.dp import extract_text,handle_tool_call
from ai.dp import send_message
import json

def func_call(message):
    chat_completion = send_message(message)  # 你之前封装的 send_message，返回 ChatCompletion 对象
    print(chat_completion)
    response_result = extract_text(chat_completion)

    if response_result["type"] == "reply":#type: ignore
        print("AI回复：", response_result["content"])#type: ignore

    elif response_result["type"] == "tool_call":#type: ignore
        for call in response_result["tool_calls"]:#type: ignore
            tool_result = handle_tool_call(call)  # 你之前写的 tool 分发函数
            tool_message = {
                "role": "tool",
                "tool_call_id": call.id, #type: ignore
                "content": json.dumps(tool_result, ensure_ascii=False)
            }
            print(tool_message)

            # 重新发起请求，继续多轮对话
            # followup = continue_with_tool_result([ #type: ignore
            #     {"role": "user", "content": message},
            #     {"role": "assistant", "tool_calls": [call]},
            #     tool_message
            # ], tools_list)#type: ignore

            # print("最终回答：", followup)

    elif response_result["type"] == "error":#type: ignore
        print("发生错误：", response_result["error"])#type: ignore
                                                    

if __name__ == "__test__":
    msg = "帮我规划一个成都到三亚的五日游，预算5000元左右"
    func_call(msg)
