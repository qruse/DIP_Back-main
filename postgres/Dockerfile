FROM postgres:latest
COPY ./postgres/dbsql/dip_library.sql /docker-entrypoint-initdb.d/
ADD ./postgres /tmp
WORKDIR /tmp
