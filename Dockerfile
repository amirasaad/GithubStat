FROM python:3.9-alpine

RUN apk add build-base

EXPOSE 80
COPY /src /src
COPY requirements/ /requirements
RUN pip install -r requirements/local.txt

ENTRYPOINT ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]
