FROM python:bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code



COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
RUN chmod +x /code/account_service/entrypoint.sh
CMD ["python", "account_service/manage.py", "runserver", "0.0.0.0:8000"]




