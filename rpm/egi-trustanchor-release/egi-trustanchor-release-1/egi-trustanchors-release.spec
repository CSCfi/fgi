Name:		egi-trustanchors-release
Version:	1
Release:	1%{?dist}
Summary:	Repo and GPG files for EGI Trustanchors

Group:		Some/Group
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	egi-trustanchors-release-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	
Requires:	yum, fetch-crl

%description
Yum repo file for EGI Trustanchors repository of 
CA files.


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp egi-trustanchors.repo $RPM_BUILD_ROOT/etc/yum.repos.d
cp GPG-KEY-EUGridPMA-RPM-3 $RPM_BUILD_ROOT/etc/pki/rpm-gpg

#%post
#rpm --import /etc/pki/rpm-gpg/GPG-KEY-EUGridPMA-RPM-3

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/egi-trustanchors.repo
/etc/pki/rpm-gpg/GPG-KEY-EUGridPMA-RPM-3
%doc



%changelog
* Wed Feb 01 2012 Ulf Tigerstedt <tigerste@csc.fi> 1
- First version 

