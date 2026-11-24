FROM python:3.12

WORKDIR /app

COPY threesub.py .

CMD ["python", "-u", "threesub.py"]