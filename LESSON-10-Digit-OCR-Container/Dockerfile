############################################################
# Dockerfile to build Flask App
############################################################

FROM library/ubuntu:18.04

LABEL maintinaer="Kris.z"

# RUN sed -i 's/archive.ubuntu.com/ap-southeast-1.ec2.archive.ubuntu.com/' /etc/apt/sources.list

RUN set -ex; apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    libapache2-mod-wsgi-py3 \
    python3-pip \
    wget \
    nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN cd /usr/local/bin; ln -s /usr/bin/python3 python
RUN a2enmod wsgi

RUN mkdir /var/www/FlaskApp
COPY . /var/www/FlaskApp
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; python get-pip.py --disable-pip-version-check --no-cache-dir
RUN pip --version; rm -f get-pip.py
RUN pip3 install -r /var/www/FlaskApp/requirements.txt

COPY FlaskApp.conf /etc/apache2/sites-available/FlaskApp.conf
RUN a2ensite FlaskApp

RUN chown -R www-data:www-data /var/www/FlaskApp
RUN rm -rf /etc/apache2/sites-available/000-default.conf
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf
RUN service apache2 restart

EXPOSE 80
WORKDIR /var/www/FlaskApp
CMD  /usr/sbin/apache2ctl -D FOREGROUND