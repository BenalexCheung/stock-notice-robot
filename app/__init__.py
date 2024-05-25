from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SCHEDULER_API_ENABLED'] = True


# 导入视图和模型模块
from app import routes, services