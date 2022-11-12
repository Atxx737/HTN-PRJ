FROM python:3.10.8

WORKDIR /api

ADD ./requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

ADD . /api
EXPOSE 5000
RUN export FLASK_APP=app.py 
RUN export FLASK_ENV=development
# RUN run_script.sh
# ENTRYPOINT [ "python" ]
# CMD [ "python3","initdb.py"]
CMD [ "python3","app.py", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
# ENTRYPOINT ["/bin/bash", "/run_script.sh"]