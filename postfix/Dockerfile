FROM alpine:latest
WORKDIR /etc/postfix

RUN apk add postfix openrc && rc-update add postfix
RUN echo "mynetworks = 172.16.0.0/16, 127.0.0.0/8" >> /etc/postfix/main.cf

CMD ["postfix", "start-fg"]
