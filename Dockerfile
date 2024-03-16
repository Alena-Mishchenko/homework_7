
FROM python:3.11


# ENV APP_HOME /app

WORKDIR /app

COPY .  /app
RUN pip install poetry



EXPOSE 5432

ENTRYPOINT ["python", "app.py", "psycopg2"]
