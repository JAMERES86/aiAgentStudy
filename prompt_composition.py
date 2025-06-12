import time

import requests
import langchain

import os
from dotenv import load_dotenv
# 自动从项目根目录加载.env文件
load_dotenv()


url = "https://api.deepseek.com/v1/chat/completions"
api_key = os.getenv("DEEPSEEK_API_KEY")  # 替换为实际密钥

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",  # 根据文档选择模型（如 deepseek-chat、deepseek-reasoner）
    "messages": [
        {"role": "system", "content": "你是一个翻译助手"},
        {"role": "user", "content": "请翻译：Hello, world!"}
    ],
    "temperature": 0.7,  # 控制随机性（0-2）
    "max_tokens": 1000   # 限制生成长度
}
# 无需手动添加[CLS]/[SEP]

start_time = time.time()  # 记录请求开始时间

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
    latency = time.time() - start_time  # 计算延迟（秒）
    print(f"API 延迟: {latency:.3f}s")  # 打印或记录到日志
else:
    print(f"请求失败: {response.status_code}, {response.text}")