# 第一阶段：构建依赖
FROM python:3.9-slim as builder

WORKDIR /backend
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 第二阶段：生产镜像
FROM python:3.9-slim

WORKDIR /backend
# 从builder阶段复制已安装的依赖
COPY --from=builder /root/.local /root/.local
# 确保PATH包含用户安装目录
ENV PATH=/root/.local/bin:$PATH

COPY ./backend ./backend

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]