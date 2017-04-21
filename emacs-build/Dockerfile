FROM centos:7

ARG	emacs=emacs-25.1
ARG	global=global-6.5.6

RUN 	yum -y update
RUN 	yum install -y wget make gcc autoconf cmake \
		openssl-devel zlib-devel gcc-c++ \
		gettext perl-devel curl-devel 

# I'll be delete
WORKDIR	/usr/local/src

COPY	${global}-1.el7.centos.x86_64.rpm ${global}-1.el7.centos.x86_64.rpm
# emacs
RUN	rpm -ivh ${global}-1.el7.centos.x86_64.rpm \
	&& yum -y install lcurses-devel ncurses-devel \
	&& curl -L http://ftp.jaist.ac.jp/pub/GNU/emacs/${emacs}.tar.gz | tar zx

WORKDIR	/tmp/work
# install git
COPY	build.sh build.sh
