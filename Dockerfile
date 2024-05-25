# 使用基础镜像
FROM alpine:latest

# 设置工作目录
WORKDIR /app

# 复制项目文件到镜像中
COPY . /app

# 安装依赖或执行其他构建步骤

# 暴露端口
EXPOSE 8080

# 定义启动命令或入口点
CMD ["python", "app.py"]