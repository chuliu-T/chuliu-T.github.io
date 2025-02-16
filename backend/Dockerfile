# 第一阶段：构建依赖
FROM python:3.10-slim as builder

WORKDIR /backend
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 第二阶段：生产镜像
FROM python:3.10-slim

WORKDIR /backend
# 从builder阶段复制已安装的依赖
COPY --from=builder /root/.local /root/.local
# 确保PATH包含用户安装目录
ENV PATH=/root/.local/bin:$PATH

COPY ./* ./

EXPOSE 8000
CMD ["uvicorn", " main:app ", "--reload"]