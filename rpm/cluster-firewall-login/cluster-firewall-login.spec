Name: cluster-firewall-login
Version: 0.1
Release:	1%{?dist}
Source: %{name}-%{version}.tar.gz
Summary: Firewall rules for FGI login nodes
Group: System Environment/Base	
License: GPL
BuildArch: noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: iptables

#Avoid compiling the http python modules to *.pyc and *.pyo files
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
This package contains default firewall settings for the FGI login node

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT/*
cp -r etc $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/sysconfig/fgi-firewall-local
%attr(0744, root, root) %{_sysconfdir}/sysconfig/fgi-firewall

%changelog
* Wed Sep 15 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.1-1
 - First release of the firewall scripts
