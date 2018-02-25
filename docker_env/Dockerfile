FROM python:3.6

RUN apt-get update

COPY src /opt/app
COPY requirements.txt /opt/app
RUN cd /opt/app && pip install -r requirements.txt

WORKDIR /opt/app
ENTRYPOINT ["python"]
CMD ["server.py", "8080"]