FROM python:3.8-alpine
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
RUN apk add nmap
RUN apk add bind-tools
RUN apk add openssh
CMD ["flask", "run", "--host", "0.0.0.0"]
