FROM python:3.10-slim as development

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENV FLASK_DEBUG=1
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]