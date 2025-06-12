import time

import requests

# 配置本地API参数
API_URL = "http://localhost:1234/v1/completions"  # 注意端点路径
HEADERS = {"Content-Type": "application/json"}

def predict_next_word(prompt_text):
    data = {
        "model": "gemma-3-12b",  # 必须与LM Studio中加载的模型名一致
        "prompt": prompt_text,
        "max_tokens": 1,  # 关键参数：只生成1个Token（即下一个字）
        "temperature": 0.3  # 控制随机性（0-1之间）
    }
    start_time = time.time()  # 记录请求开始时间
    response = requests.post(API_URL, json=data, headers=HEADERS)
    if response.status_code == 200:
        latency = time.time() - start_time  # 计算延迟（秒）
        print(f"API 延迟: {latency:.3f}s")  # 打印或记录到日志
        return response.json()["choices"][0]["text"]
    else:
        raise Exception(f"API错误: {response.text}")

# 测试用例
if __name__ == "__main__":
    test_text = "人工智能是"  # 尝试预测"是"后面的字
    next_word = predict_next_word(test_text)
    print(f"输入: '{test_text}' → 预测下一个字: '{next_word}'")