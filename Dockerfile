FROM python:3.10-slim as development

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' stitch
WORKDIR /home/stitch/app
RUN chown -R stitch:stitch /home/stitch

#ENV POETRY_HOME=/opt/poetry
#ENV POETRY_CACHE_DIR=/opt/.cache

COPY poetry.lock pyproject.toml /home/stitch/app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install --no-interaction --no-ansi

COPY . /home/stitch/app/

#ENV FLASK_DEBUG=1
ENV FLASK_APP=app.py

USER stitch

CMD ["flask", "run", "--host=0.0.0.0"]