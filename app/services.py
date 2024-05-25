from app.dingtalkchatbot import dingtalk_robot
from app.dingtalkchatbot import dingtalk_robot_img
from app.config import WEBHOOK
from app.config import SECRET_KEY

def scheduled_job():
    print("This is a scheduled job.")


def send_message_to_dingtalk(title, text):
    dingtalk_robot(WEBHOOK, SECRET_KEY, title, text)
    return "Message sending task has been triggered."

def send_image_to_dingtalk(image_url):
    dingtalk_robot_img(WEBHOOK, SECRET_KEY, image_url)
    return "Message sending task has been triggered."
