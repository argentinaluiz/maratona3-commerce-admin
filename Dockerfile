FROM python:3.6.10-alpine3.11
ENV PYTHONUNBUFFERED 1

RUN touch /root/.bashrc | echo "PS1='\w\$ '" >> /root/.bashrc

RUN apk add --no-cache bash \
                       postgresql-dev \
                       gcc \
                       python3-dev \
                       musl-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

#sudo chown -R $USER:$USER . isto fica no README.md

#docker logs para verificar o output