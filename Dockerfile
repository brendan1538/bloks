FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y nodejs
RUN curl -L https://npmjs.org/install.sh | sh

COPY . .

CMD ["python", "-u", "./api.py"]

