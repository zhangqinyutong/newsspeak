from openai import OpenAI
from config import settings

# 初始化DeepSeek客户端
client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url=settings.DEEPSEEK_BASE_URL
)

def test_llm():
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "简单介绍下什么是大语言模型"}]
    )
    print("AI返回结果：")
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    test_llm()