Name: cluster-profile
Version: 0.3
Release: 1%{?dist}
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
* Wed May 23 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.3-1
 - Modified module files to use the /sl6/ subdirectory.
 - Added module files to explicitly set path

* Wed Feb 29 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.2-1
 - Added files for module files under CVMFS
 
