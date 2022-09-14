FROM ubuntu:20.04

ARG PIP_REQUIREMENTS=requirements.txt
ARG APP_USER=djangouser
ARG APP_GROUP=djangouser
ARG PROJECT_NAME=ticket

LABEL multi.maintainer="Timothy Matara <tondieki at safaricomcoke>" \
      multi.version="1.0" \
      multi.description="A Django based application to generate \
      Enterprise customer charts by Provider Edge router."

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Africa/Nairobi
ENV VIRTUAL_ENV=/opt/${PROJECT_NAME}

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

WORKDIR /usr/src/app
RUN mkdir logs/ \
    && mkdir static/ \

RUN touch logs/dev.log logs/prod.log
COPY . .
RUN chmod +x ./entrypoint.sh

RUN set -ex \
    && RUN_DEPS=" \
    build-essential mime-support gcc libc-dev python3-dev \
    python3 python3-wheel ca-certificates procps \
    libpq-dev python3-pip libsasl2-dev python-dev \
    libsqlclient-dev libssl-dev python3-venv libldap2-dev \
    libffi-dev libxml2-dev libxslt1-dev python3-ldap python3-setuptools\
    iputils-ping net-tools dnsutils inetutils-traceroute libpcre3 libpcre3-dev\
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update \
    && apt-get install -y --no-install-recommends ${RUN_DEPS} \ 
    && rm -rf /var/lib/apt/lists/* 

# Activate virtual environment
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

EXPOSE 8000

RUN pip install -U wheel setuptools pip \
    && pip install -r ${PIP_REQUIREMENTS} --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

ENTRYPOINT [ "bash", "entrypoint.sh" ]

# Security limit the scope of the user who runs the docker image
RUN groupadd ${APP_GROUP} \
    && useradd ${APP_USER} -g ${APP_GROUP}
RUN chown -R ${APP_USER}:${APP_GROUP} /usr/src/app/
RUN chmod -R 755 /usr/src/app/
RUN chmod -R 755 /usr/src/app/static
RUN chmod -R 755 logs/

