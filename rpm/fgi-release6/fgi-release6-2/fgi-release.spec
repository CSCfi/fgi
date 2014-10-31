Name:		fgi-release6
Version:	2	
Release:	6%{?dist}
Summary:	Release files for FGI repository

Group:		Applications/Communication
License:	GPL
#URL:		
Source0:	fgi-release6-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

#BuildRequires:	
Requires:	yum

%description
Yum repo file for the FGI repository (RHEL/CentOS/SL 6 version)
Also includes public key


%prep
%setup -q


%build


%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp fgi.repo $RPM_BUILD_ROOT/etc/yum.repos.d/
cp RPM-GPG-KEY-CSC-GRID-2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/fgi.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2



%changelog
* Thu Oct 30 2014 Ulf Tigerstedt <tigerste@csc.fi> 2-6
- Changed pulse to idris.
* Wed Dec 23 2013 Ulf Tigerstedt <tigerste@csc.fi> 2-5
- Forgot to add baseurl= in front of the dcache repo url
* Wed May 22 2013 Ulf Tigerstedt <tigerste@csc.fi> 2-4
- Added dcache repo
* Tue Sep  4 2012 Ulf Tigerstedt <tigerste@csc.fi> 2-3
- Noted that gpgcheck was gpgecheck, so it has probably never worked.
* Wed Feb 29 2012 Ulf Tigerstedt <tigerste@csc.fi> 2-1
- Added early adopters repository
* Thu Sep 08 2011 Ulf Tigerstedt <tigerste@csc.fi> 1-2
- Added public key
* Fri May 20 2011 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- Initial version


