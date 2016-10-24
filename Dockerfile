FROM ubuntu:14.04
RUN apt-get update
RUN apt-get --assume-yes install python
RUN apt-get --assume-yes install python-pip python-dev build-essential 
RUN pip install Flask
#copy requirements.txt /src/requirements.txt
#RUN pip install -r /src/requirements.txt
COPY app /src/blog/app

ENV PYTHONPATH ${PYTHONPATH}:.

EXPOSE  5000
#CMD ["python", "/src/blog/app/run.py", "-p 5000"]
RUN PYTHONPATH=/src/blog/app python /src/blog/app/run.py