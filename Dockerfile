FROM python:latest

COPY . .

RUN pip3 install -U pip && pip install -Ur requirements.txt

EXPOSE 80

CMD ["./start.sh"]