FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app
COPY ./app /app

RUN pip install openai

ENV MODULE_NAME=main
ENV VARIABLE_NAME=app