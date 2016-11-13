FROM ubuntu:14.04
RUN apt-get update
RUN apt-get --assume-yes install python
RUN apt-get --assume-yes install python-pip python-dev build-essential 
RUN pip install flask
RUN pip install flask-wtf
RUN pip install flask-login
RUN pip install flask-openid
RUN pip install flask-mail
RUN pip install flask-sqlalchemy
RUN pip install sqlalchemy-migrate
RUN pip install flask-whooshalchemy
RUN pip install flask-babel
RUN pip install guess_language
RUN pip install flipflop
RUN pip install coverage

#copy requirements.txt /src/requirements.txt
#RUN pip install -r /src/requirements.txt
COPY app /src/blog/app
COPY config.py /src/blog

ENV PYTHONPATH ${PYTHONPATH}:/src/blog

EXPOSE  5000
#RUN PYTHONPATH=/src/blog python /src/blog/app/run.py
CMD ["python", "/src/blog/app/run.py", "-p 5000"]
