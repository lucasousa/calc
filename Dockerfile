FROM python:3.11-slim
WORKDIR /home/userapp/app
RUN apt-get update

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /home/userapp/app/src/

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --no-cache -U pip poetry && poetry config virtualenvs.create false 
RUN poetry install
EXPOSE 8000

CMD ["entrypoint.sh"]