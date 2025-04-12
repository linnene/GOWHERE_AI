from crud.dp import extract_text
import datetime
from ai.dp import send_message

#测试send_message函数，发送多个不同的旅行规划请求，并将结果保存到文件
def test_send_message():
    # 准备保存结果的文件
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = f"d:\\gowhere_pro\\GOWHERE_AI\\test\\test_results_{timestamp}.txt"
    results = []
    
    # 测试用例1: 基本旅行规划
    print("\n=== 测试1: 基本旅行规划 ===")
    message1 = "请帮我规划一个从上海前往芬兰的三天两晚的旅行"
    response1 = send_message(message1)
    response_text1 = extract_text(response1)
    summary1 = response_text1[:200] + "..." if len(response_text1) > 200 else response_text1
    print(f"回复: {summary1}")
    results.append(f"=== 测试1: 基本旅行规划 ===\n请求: {message1}\n回复: {summary1}\n\n完整回复:\n{response_text1}\n\n")
    
    # 测试用例2: 指定特定景点
    print("\n=== 测试2: 指定特定景点 ===")
    message2 = "我想从北京去杭州西湖游玩三天，主要想看西湖和灵隐寺"
    response2 = send_message(message2)
    response_text2 = extract_text(response2)
    summary2 = response_text2[:200] + "..." if len(response_text2) > 200 else response_text2
    print(f"回复: {summary2}")
    results.append(f"=== 测试2: 指定特定景点 ===\n请求: {message2}\n回复: {summary2}\n\n完整回复:\n{response_text2}\n\n")
    
    # 测试用例3: 带预算的旅行规划
    print("\n=== 测试3: 带预算的旅行规划 ===")
    message3 = "帮我规划一个成都到三亚的五日游，预算5000元左右"
    response3 = send_message(message3)
    response_text3 = extract_text(response3)
    summary3 = response_text3[:200] + "..." if len(response_text3) > 200 else response_text3
    print(f"回复: {summary3}")
    results.append(f"=== 测试3: 带预算的旅行规划 ===\n请求: {message3}\n回复: {summary3}\n\n完整回复:\n{response_text3}\n\n")
    
    # 保存所有测试结果到文件
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("=== GOWHERE AI 测试结果 ===\n")
        f.write(f"测试时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("".join(results))
    
    print(f"\n测试完成! 结果已保存至: {result_file}")
    return True

if __name__ == "__test__":
    # 运行测试函数
    test_send_message()
