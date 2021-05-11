FROM python:3.8.10-slim-buster
COPY ./app /app
COPY ./requirements.txt /requirements.txt
RUN python -m pip install -r /requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
