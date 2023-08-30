FROM python:3.10 as reduction_url_admin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ADD news ./news
ADD .venv entrypoint.sh./