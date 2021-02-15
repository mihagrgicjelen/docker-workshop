FROM nginx:1.17.3

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000