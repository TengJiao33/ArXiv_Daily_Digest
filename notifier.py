"""
消息推送模块
支持 ServerChan (方糖) 和 WXPusher 双通道推送。
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ServerChanNotifier:
    """Server酱推送"""

    def __init__(self):
        self.sendkey = os.getenv("SERVERCHAN_SENDKEY")
        self.api_url = f"https://sctapi.ftqq.com/{self.sendkey}.send" if self.sendkey else None

    def send(self, content, title="ArXiv 论文日报"):
        if not self.api_url:
            print("[ServerChan] 未配置 SENDKEY，跳过")
            return False
        payload = {"title": title, "desp": content}
        try:
            response = requests.post(self.api_url, data=payload, timeout=10)
            result = response.json()
            if result.get("code") == 0 or (result.get("data") and result["data"].get("errno") == 0):
                print("[ServerChan] 推送成功 ✓")
                return True
            print(f"[ServerChan] 推送失败: {result}")
        except Exception as e:
            print(f"[ServerChan] 异常: {e}")
        return False


class WXPusherNotifier:
    """WXPusher 推送"""

    def __init__(self):
        self.app_token = os.getenv("WXPUSHER_APP_TOKEN")
        self.uids = [u for u in os.getenv("WXPUSHER_UIDS", "").split(",") if u]
        self.topic_ids = [t for t in os.getenv("WXPUSHER_TOPIC_IDS", "").split(",") if t]
        self.api_url = "https://wxpusher.zjiecode.com/api/send/message"

    def send(self, content, summary="ArXiv 论文日报"):
        if not self.app_token:
            print("[WXPusher] 未配置 APP_TOKEN，跳过")
            return False
        if not self.uids and not self.topic_ids:
            print("[WXPusher] 未配置 UIDS 或 TOPIC_IDS，跳过")
            return False
        payload = {
            "appToken": self.app_token,
            "content": content,
            "summary": summary,
            "contentType": 3,  # Markdown
            "uids": self.uids,
            "topicIds": self.topic_ids,
        }
        try:
            response = requests.post(self.api_url, json=payload, timeout=10)
            result = response.json()
            if result.get("code") == 1000:
                print("[WXPusher] 推送成功 ✓")
                return True
            print(f"[WXPusher] 推送失败: {result}")
        except Exception as e:
            print(f"[WXPusher] 异常: {e}")
        return False


class HubNotifier:
    """推送聚合器，同时发送所有已配置的渠道"""

    def __init__(self):
        self.notifiers = []
        if os.getenv("SERVERCHAN_SENDKEY"):
            self.notifiers.append(ServerChanNotifier())
        if os.getenv("WXPUSHER_APP_TOKEN"):
            self.notifiers.append(WXPusherNotifier())
        if not self.notifiers:
            print("[HubNotifier] 警告：没有配置任何推送渠道")

    def send_all(self, content, title="ArXiv 论文日报"):
        """向所有渠道发送消息，任一成功即返回 True"""
        results = []
        for n in self.notifiers:
            results.append(n.send(content, title))
        return any(results)
