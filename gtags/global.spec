Name: global
Version: 6.5.6
Release: 1%{?dist}
Summary: GNU GLOBAL source code tagging system
License: GPLv3 
URL: http://www.gnu.org/software/global/
#Source0: http://tamacom.com/global/%{name}-%{version}.tar.gz
BuildRequires: ncurses-devel

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description

%prep
%setup -q
%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-, root, root,-)
/usr/local/bin/*
/usr/local/lib/gtags
/usr/local/share/gtags
/usr/local/share/info/*
/usr/local/share/man/man*/*
/usr/local/var/gtags

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Mar 6 2017 kawawa <kawawa.y@gmail.com> 6.5.6_1
- Created Package
