FROM python:3.8

WORKDIR /app
ADD ./flask/app /app

RUN pip3 install -r /app/requirments.txt

CMD ["uwsgi","uwsgi.ini"]
#CMD ["python3","app_main.py"]