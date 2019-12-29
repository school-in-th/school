FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN mkdir /uwsgi

ADD ./uwsgi.ini /uwsgi
ADD ./supervisord.conf /etc/supervisord.conf
ADD requirements.txt /code

WORKDIR /code/

RUN pip install --upgrade pip
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev mariadb-dev \
    && pip install uwsgi \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

ADD . /code

EXPOSE 80 5555

CMD supervisord -c /etc/supervisord.conf ; uwsgi --emperor /uwsgi
