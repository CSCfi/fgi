Name: cluster-tools
Version: 0.3
Release:	1%{?dist}
Source: %{name}-%{version}.tar.gz
Summary: Admin tools for FGI clusters
Group: System Environment/Base	
License: GPL
BuildArch: noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: pdsh,python,tftp-server,dhcp,bind-chroot,httpd

#Avoid compiling the http python modules to *.pyc and *.pyo files
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
This package contains tools and utilities for the FGI install node

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT/*
cp -r etc usr var $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cluster/mounts.sh
%{_sysconfdir}/cluster
%{_sbindir}/*
%{_libexecdir}/cluster
%attr(0744, apache, apache) %{_localstatedir}/www/cgi-bin/*
%{_localstatedir}/lib/tftpboot/*


%changelog
* Wed Sep 14 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.3-1
 - Bugfixes and improvements
* Wed Aug 17 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.1-1
 - First release of the cluster tools
