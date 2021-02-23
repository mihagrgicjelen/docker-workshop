FROM nginx:1.17.3

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./htpasswd.txt /etc/nginx/.htpasswd
EXPOSE 8000