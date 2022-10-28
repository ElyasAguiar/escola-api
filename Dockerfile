FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ARG POSTGRES_USER=${POSTGRES_USER}
ARG POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ARG POSTGRES_SERVER=${POSTGRES_PASSWORD}
ARG POSTGRES_DB=${POSTGRES_PASSWORD}

ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_SERVER=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_PASSWORD}

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000
EXPOSE 8000

# Install Poetry
RUN pip install fastapi uvicorn poetry wheel virtualenv
RUN poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY . /app
