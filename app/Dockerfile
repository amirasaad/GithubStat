FROM python:3.9-alpine

RUN apk add build-base
RUN pip install pipenv

EXPOSE 80
WORKDIR app
COPY Pipfile Pipfile
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --skip-lock

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
