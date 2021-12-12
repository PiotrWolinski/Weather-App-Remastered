FROM python:3.9

WORKDIR /app

COPY flask/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "flask/run.py"]