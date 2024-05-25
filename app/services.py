from app.dingtalkchatbot import dingtalk_robot
from app.config import WEBHOOK
from app.config import SECRET_KEY

def scheduled_job():
    print("This is a scheduled job.")


def send_message_to_dingtalk(title, text):
    dingtalk_robot(WEBHOOK, SECRET_KEY, title, text)
    return "Message sending task has been triggered."
