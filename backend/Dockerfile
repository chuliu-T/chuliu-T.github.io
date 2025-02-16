FROM python:3.10-slim

WORKDIR /backend

COPY . ./

RUN pip install fastapi uvicorn[standard] sqlalchemy pydantic[email] passlib python-jose  python-multipart uvicorn

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload"]