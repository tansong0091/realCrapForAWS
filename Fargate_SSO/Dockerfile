FROM docker2021repos/httpd:2.4

RUN apt-get  update -y \
    && apt-get install -y apt-utils

RUN apt-get  update -y \
    && apt-get install -y procps vim ca-certificates libapache2-mod-auth-openidc \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    # SSH login fix. Otherwise user is kicked off after login

RUN mkdir /usr/local/apache2/htdocs/dist
COPY ./dist/testsso.html /usr/local/apache2/htdocs/dist/testsso.html
COPY ./dist/test.html/ /usr/local/apache2/htdocs/dist/test.html
COPY conf/htaccess /usr/local/apache2/htdocs/.htaccess
COPY entrypoint.sh /entrypoint.sh
COPY conf/oidc.conf /usr/local/apache2/conf/
COPY conf/httpd.conf /usr/local/apache2/conf/



EXPOSE 80 22
