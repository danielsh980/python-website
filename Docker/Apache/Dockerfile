FROM docker.io/ubuntu:22.04

WORKDIR /tmp
RUN apt-get update
RUN apt-get install python3 python3-pip apache2 libapache2-mod-wsgi-py3 git -y
RUN pip3 install flask mysql-connector-python
RUN mkdir /var/www/pysite
RUN git clone -b apache-setup https://github.com/danielsh980/python-website.git
RUN cp /tmp/python-website/ports.conf /etc/apache2/ports.conf
RUN cp -R /tmp/python-website/website /var/www/pysite
RUN cp /tmp/python-website/main.py /var/www/pysite/main.py
RUN cp /tmp/python-website/app.wsgi /var/www/pysite/app.wsgi
RUN cp /tmp/python-website/pysite.conf /etc/apache2/sites-available/pysite.conf
RUN a2ensite pysite.conf
RUN service apache2 restart
EXPOSE 8080

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_RUN_DIR /var/www/pysite

ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]i