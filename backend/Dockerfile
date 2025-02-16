FROM python:3.10-slim

WORKDIR /backend
# 从builder阶段复制已安装的依赖
COPY --from=builder /root/.local /root/.local
# 确保PATH包含用户安装目录
ENV PATH=/root/.local/bin:$PATH
RUN pip install --user --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


COPY . ./

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload"]