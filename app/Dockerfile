FROM python:3.9-alpine

RUN apk add build-base
RUN pip install pipenv

EXPOSE 80
WORKDIR app
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev --deploy --skip-lock

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
