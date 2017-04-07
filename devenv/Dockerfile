FROM centos:7

# bison require mruby
# bzip2 require rbenv?
RUN 	yum install -y wget make gcc sudo autoconf cmake \
		openssl-devel zlib-devel gcc-c++ \
		patch gdb \ 
		bzip2 bison

# install rbenv and rubys
ENV	PATH	/usr/local/src/rbenv/bin:$PATH
ENV	RBENV_ROOT	/usr/local/src/rbenv
RUN	yum -y install readline-devel
RUN 	cd /usr/local/src \
	&& curl -L https://github.com/rbenv/rbenv/archive/v1.1.0.tar.gz | tar zx && mv rbenv-1.1.0 rbenv \
	&& mkdir -p rbenv/versions rbenv/shims rbenv/plugins && cd rbenv/plugins \
	&& curl -L https://github.com/rbenv/ruby-build/archive/v20170112.tar.gz | tar zx && mv ruby-build-20170112 ruby-build \
	&& curl -L https://github.com/rbenv/rbenv-default-gems/archive/v1.0.0.tar.gz | tar zx && mv rbenv-default-gems-1.0.0 rbenv-default-gems \
	&& cd ../.. \
	&& groupadd rbenv \
	&& chgrp -R rbenv rbenv \
	&& chmod -R g+rwxs rbenv \
	&& cd rbenv \
	&& src/configure && make -C src \
	&& plugins/ruby-build/install.sh \
	&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh \
	&& echo '%rbenv ALL=(ALL) ALL' >> /etc/sudoers 

RUN 	rbenv install -v 2.0.0-p648 \
	&& rbenv rehash \
	&& rbenv global 2.0.0-p648

# install git
RUN	yum -y install gettext perl-devel curl-devel \
		asciidoc xmlto epel-release \
	&& yum -y install --enablerepo=epel docbook2X docbook-utils \
	&& ln -s /usr/bin/db2x_docbook2texi /bin/docbook2x-texi
RUN 	cd /usr/local/src \
	&& curl -L https://github.com/git/git/archive/v2.11.0.tar.gz | tar zx && mv git-2.11.0 git \
	&& cd git && make configure && ./configure --prefix=/usr/local \
	&& make all doc info && make install && cd .. && rm -rf git 

# install editor
RUN	yum -y install vim
RUN	yum -y update

# install cross-compiler
RUN	git clone https://github.com/raspberrypi/tools.git \
	&& mkdir -p /opt/rpi/arm-bcm2708 \
	&& mv tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64 /opt/rpi/arm-bcm2708 \
	&& rm -rf tools

ENV	CROSS_COMPILE	arm-linux-gnueabihf-
ENV	PATH	$PATH:/opt/rpi/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin

WORKDIR	/tmp/h2o
ADD	build.sh /tmp/h2o
ADD	Makefile /tmp/h2o

#WORKDIR /tmp/work
ADD	emacs-25.1.tar.gz /usr/local
#RUN	mv bin/* /bin && mv libexec/emacs /usr/local && mv var/games/emacs /var/games && mv share/emacs /usr/local/share 

RUN	ln -fs /home/data/dotfiles/_emacs.d /$HOME/.emacs.d 

CMD	/bin/bash
