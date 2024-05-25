from flask import Flask
import schedule
import time

app = Flask(__name__)

def send_daily_message():
    # 在这里编写发送消息的代码
    print("Daily message sent!")

# 定义每日定时任务
schedule.every().day.at("09:00").do(send_daily_message)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# 创建一个路由，用于启动定时任务
@app.route('/start_scheduler')
def start_scheduler():
    run_scheduler()
    return 'Scheduler started!'

if __name__ == '__main__':
    app.run()