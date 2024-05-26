from app import app

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.services import scheduled_job

# 配置日志记录
logging.basicConfig(level=logging.WARNING)  # 设置日志级别为 DEBUG

# 添加定时任务调度规则
scheduler = BackgroundScheduler()

# 添加定时任务调度规则
trigger = CronTrigger(hour=18, minute=0, second=0)
# scheduler.add_job(scheduled_job, 'interval', seconds=3)
scheduler.add_job(func=scheduled_job, trigger=trigger)

# 启动调度器
scheduler.start()

if __name__ == '__main__':
    app.run()
