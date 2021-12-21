FROM python:3.8
RUN pip install --upgrade pip

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN apt-get install -y openssl libssl-dev

COPY ./app /code/
WORKDIR /code

ADD ./docker/app/entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]

