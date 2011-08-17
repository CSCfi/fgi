Name: cluster-profile		
Version: 0.1
Release:	1%{?dist}
Source: %{name}-%{version}.tar.gz
Summary: profile.d scripts for FGI	
Group: System Environment/Base	
License: GPL
BuildArch: noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: setup	

%description
These are the profile scripts needed by the FGI frontends

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT/*
cp -r etc $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sysconfdir}/profile.d/*


%changelog

