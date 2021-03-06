FROM httpd:2.4
COPY ./test.html/ /usr/local/apache2/htdocs/dist/test.html
COPY conf/htaccess /usr/local/apache2/htdocs/.htaccess
COPY entrypoint.sh /entrypoint.sh
COPY conf/oidc.conf /usr/local/apache2/conf/
COPY conf/httpd.conf /usr/local/apache2/conf/
COPY libapache2-mod-auth-openidc_2.3.11-1.stretch+1_amd64.deb /user/local/libapache2-mod-auth-openidc_2.3.11-1.stretch+1_amd64.deb
 
WORKDIR /usr/local/apache2

RUN apt-get update\
    && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils --allow-unauthenticated libapache2-mod-auth-openidc=2.1.6-1 \
    && dpkg -i /user/local/libapache2-mod-auth-openidc_2.3.11-1.stretch+1_amd64.deb \
    && rm -rf /user/local/libapache2-mod-auth-openidc_2.3.11-1.stretch+1_amd64.deb 

RUN chmod 755 -R /usr/local/apache2/htdocs


EXPOSE 80 443
ENTRYPOINT ["/entrypoint.sh"]

