from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import datetime


def dingtalk_robot(webhook, secret, title, text):
    dogBOSS = DingtalkChatbot(webhook, secret)    
    dogBOSS.send_markdown(title, text, is_at_all=True)

def dingtalk_robot_img(webhook, secret, pic_url):
    dogBOSS = DingtalkChatbot(webhook, secret)    
    dogBOSS.send_image(pic_url)

