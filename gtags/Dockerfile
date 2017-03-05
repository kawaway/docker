FROM centos:7

ARG	gtags=global-6.5.6

#	rpmdevtools yum-utils  for rpmbuild
RUN 	yum -y update
RUN 	yum install -y make gcc gcc-c++ \
		ncurses-devel \
		rpmdevtools yum-utils

# I'll be delete
WORKDIR	/root/rpmbuild

RUN	rpmdev-setuptree \
	&& cd SOURCES && curl -LO http://tamacom.com/global/global-6.5.6.tar.gz && cd .. 
# install git
COPY	global.spec SPECS/global.spec
