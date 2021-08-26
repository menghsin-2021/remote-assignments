# syntax=docker/dockerfile:1
#Linux Version
FROM amazonlinux:latest
RUN yum -y install which unzip aws-cli

# Install Python
RUN yum install -y amazon-linux-extras
RUN amazon-linux-extras install python3

# Install Nginx
RUN amazon-linux-extras install nginx1

# set working diretory
WORKDIR /flask-project/

# copy requirements.txt and install
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy Flask application code
COPY flaskapp /flask-project/
COPY start.sh /start.sh
COPY nginx_config.conf /etc/nginx/conf.d/virtual.conf

EXPOSE 80

RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
