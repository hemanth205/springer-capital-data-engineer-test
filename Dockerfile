FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install pandas

CMD ["python", "your_script.py"]