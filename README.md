# stock-notice-robot
钉钉机器人


## 容器构建

```
docker build -t stock-notice-robot .
```

## 部署运行

```
docker run -p 8080:8080 stock-notice-robot
```

## 开发与测试

1、创建虚拟环境

```
python3 -m venv venv # 创建环境
. venv/bin/activate # 激活环境
deactivate # 退出环境

```

2、安装依赖
```
pip3 install -r requirements.txt
```

3、导出依赖
```
pip3 freeze > requirements.txt
```

4、运行与测试
```
flask run
```

访问：http://localhost:5000/start_scheduler