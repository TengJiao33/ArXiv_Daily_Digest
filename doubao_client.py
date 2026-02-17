"""
豆包 (Doubao/Ark) API 客户端
基于 OpenAI SDK 封装，读取 .env 中的配置。
支持返回 token 用量统计。
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class DoubaoClient:
    """豆包大模型 API 客户端"""

    def __init__(self):
        self.api_key = os.getenv("DOUBAO_API_KEY")
        self.endpoint_id = os.getenv("DOUBAO_ENDPOINT_ID")
        if not self.api_key or not self.endpoint_id:
            raise ValueError("请在 .env 中配置 DOUBAO_API_KEY 和 DOUBAO_ENDPOINT_ID")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://ark.cn-beijing.volces.com/api/v3",
        )

    def chat_completion(self, messages, system_prompt=None, max_tokens=1024):
        """
        发送聊天请求到豆包 API。
        :return: (回复文本, usage字典) — usage 包含 prompt_tokens, completion_tokens, total_tokens
        """
        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        import time

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.endpoint_id,
                    messages=full_messages,
                    max_tokens=max_tokens,
                )
                content = response.choices[0].message.content

                # 提取 usage 信息
                usage = {}
                if response.usage:
                    usage = {
                        "prompt_tokens": response.usage.prompt_tokens or 0,
                        "completion_tokens": response.usage.completion_tokens or 0,
                        "total_tokens": response.usage.total_tokens or 0,
                    }

                return content, usage
            
            except Exception as e:
                error_msg = str(e)
                if "TooManyRequests" in error_msg or "rate_limit" in error_msg or "429" in error_msg:
                    wait_time = (2 ** attempt) * 2  # 2s, 4s, 8s
                    print(f"[DoubaoClient] ⚠️ 触发限流，等待 {wait_time}秒后重试 ({attempt+1}/{max_retries})...")
                    time.sleep(wait_time)
                else:
                    print(f"[DoubaoClient] ❌ API 调用失败: {e}")
                    return None, {}
        
        print(f"[DoubaoClient] ❌ 重试 {max_retries} 次后仍失败")
        return None, {}
