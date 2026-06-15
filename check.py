import requests
import os

TOKEN = os.environ["8842448019:AAGS3AMLr0ZiVQurYtWC_d3TzrbCk-y1QVo"]
CHAT_ID = os.environ["7899800092"]

URL = "https://store.nintendo.co.kr/beeskb6aakor"

html = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

if "stock unavailable" not in html:

    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": "🎉 닌텐도 스위치2 입고 확인!"
        }
    )

print("체크 완료")
