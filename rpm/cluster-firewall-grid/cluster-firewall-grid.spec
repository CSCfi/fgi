Name: cluster-firewall-grid
Version: 0.1
Release:	2%{?dist}
Source: %{name}-%{version}.tar.gz
Summary: Firewall rules for FGI grid
Group: System Environment/Base	
License: GPL
BuildArch: noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: iptables

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
This package contains default firewall settings for the FGI grid node

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
* Mon Feb 13 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.1-2
 - Bugfix, forgot an infiniband statement
* Thu Jan 26 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.1-1
 - First release of the firewall scripts
