FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

# Install Poetry
RUN pip install fastapi uvicorn poetry wheel virtualenv psycopg2
RUN poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN poetry install --no-root --no-dev

COPY . /app
