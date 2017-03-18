FROM python:2.7.13
MAINTAINER Kiran Chaitanya "kiran.ilf9@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
CMD ["app.py",arg]
