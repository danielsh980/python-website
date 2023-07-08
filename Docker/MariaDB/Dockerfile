FROM docker.io/mariadb:latest

ENV MYSQL_DATABASE=pysite \
    MYSQL_ROOT_PASSWORD=admin123 \
    MYSQL_ROOT_HOST=%

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306