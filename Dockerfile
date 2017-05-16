FROM python:3.6
MAINTAINER Regner Blok-Andersen <shadowdf@gmail.com>

ADD docker-entrypoint.sh /docker-entrypoint.sh

ADD . /app/
WORKDIR /app/

RUN apt-get update -qq \
    && apt-get upgrade -y -qq \
    && apt-get install -y -qq python-dev python3-psycopg2 \
    && pip install -qU pip setuptools gunicorn psycopg2 \
    && pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["gunicorn", "wsgi:app", "-w", "3", "-b", ":8000", "--log-level", "debug", "--timeout", "120"]