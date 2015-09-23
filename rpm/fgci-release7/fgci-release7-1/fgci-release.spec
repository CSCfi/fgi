Name:		fgci-release7
Version:	1	
Release:	1%{?dist}
Summary:	Release files for FGCI repository for CentOS7

Group:		Applications/Communication
License:	GPL
#URL:		
Source0:	fgci-release7-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

#BuildRequires:	
Requires:	yum

%description
Yum repo file for the FGCI repository (RHEL/CentOS/SL 7 version)
Also includes public key


%prep
%setup -q


%build


%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp fgci.repo $RPM_BUILD_ROOT/etc/yum.repos.d/
cp RPM-GPG-KEY-CSC-GRID-2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/fgci.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2



%changelog
* Fri Sep 22 2015 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- Initial version, copied from FGI release.


