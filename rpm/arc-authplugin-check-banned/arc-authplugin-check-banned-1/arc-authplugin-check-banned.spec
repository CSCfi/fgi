Name:		arc-authplugin-check-banned
Version:	1
Release:	1
Summary:	ARC authplugin to check if the DN has been banned

Group:		none	
License:	GPL
URL:		http://cvmfs.fgi.csc.fi/
Source0:	http://www.csc.fi/arc-authplugin-check-banned-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

#BuildRequires: 	
Requires:	voms-clients, bash

%description
Small script to test if a DN has been banned.
Call from arc.conf as:
authplugin="ACCEPTED timeout=20 /usr/sbin/check-banned %C/job.%I.proxy"


%prep
%setup -q


%build
/bin/true


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/grid-security
cp check-banned $RPM_BUILD_ROOT/usr/sbin
cp banned $RPM_BUILD_ROOT/etc/grid-security


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/sbin/check-banned
%config /etc/grid-security/banned



%doc



%changelog
* Tue Sep 27 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi> - 1
- First version of the package
