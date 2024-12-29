FROM python:3.12

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install poetry==1.7.1
RUN poetry config virtualenvs.create false
RUN poetry install


CMD ["uvicorn", "backend:app", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
