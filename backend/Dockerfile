# backend/Dockerfile
FROM centos:7 AS builder

# 安装编译工具和 OpenSSL 1.1.1
RUN yum install -y gcc make zlib-devel openssl-devel
RUN curl https://pyenv.run | bash
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc

# 安装 Python 3.10.13
RUN pyenv install 3.10.13
ENV PATH $PYENV_ROOT/versions/3.10.13/bin:$PATH

# 安装依赖
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# ----------------------------
# 生产镜像
FROM centos:7

# 仅复制运行时依赖
COPY --from=builder /root/.pyenv /root/.pyenv
COPY --from=builder /app /app

# 设置环境变量
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/versions/3.10.13/bin:$PATH

# 启动命令
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]