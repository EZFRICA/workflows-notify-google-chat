import json
import config

from fastapi import FastAPI
from json import dumps

from httplib2 import Http

app = FastAPI(title="Google Chat Notification", version="1.0", redoc_url=None)


@app.post("/notify/", status_code=201)
async def notify(message: str):
    """Hangouts Chat incoming webhook"""

    url = f'https://chat.googleapis.com/v1/spaces/AAAAg-eI8mU/messages?key={config.GOOGLE_CHAT_KEY}&token={config.GOOGLE_CHAT_TOKEN}'
    bot_message = {"text": message}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    return response
