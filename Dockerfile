FROM alpine:edge

RUN apk add --update \
    nginx \
    supervisor \
    python3 \
    python3-dev \
    build-base \
    linux-headers \
    py3-psycopg2 \
    && rm -rf /var/cache/apk/* \
    && chown -R nginx:www-data /var/lib/nginx

RUN python3 -m ensurepip
RUN pip3 install wheel
RUN pip3 install uwsgi
COPY dist/quotewall-0.0.0-py3-none-any.whl /
RUN pip3 install quotewall-0.0.0-py3-none-any.whl
RUN rm quotewall-0.0.0-py3-none-any.whl

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/supervisord.conf
RUN mkdir /srv/static

COPY etc/nginx-app.conf /etc/nginx/sites-enabled/
COPY etc/nginx.conf /etc/nginx/
COPY etc/uwsgi_params /etc/nginx/
COPY etc/uwsgi.ini /etc/
COPY etc/supervisord.conf /etc/
COPY config.py /etc/
ADD quotewall/static /srv/static
RUN mkdir -p /run/nginx
RUN mkdir -p /var/log/nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

CMD ["supervisord", "-n"]
