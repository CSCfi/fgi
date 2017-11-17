Name:		ca-csctraining
Version:	1
Release:	3%{?dist}
Summary:	Certificate Authority files for the CSC Training CA

Group:		Other
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	ca-csctraining-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bash
Requires:	fetch-crl	

%description
Certificate Authority files for the CSC Training CA
Not accredited, use with care.


%prep
%setup -q


%build
#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/grid-security/certificates
#make install DESTDIR=$RPM_BUILD_ROOT
cp CSC* $RPM_BUILD_ROOT/etc/grid-security/certificates
cd $RPM_BUILD_ROOT/etc/grid-security/certificates
ln -s  CSC_Training_CA.crl_url 3622c361.crl_url
ln -s  CSC_Training_CA.crl_url 44efd5a6.crl_url
ln -s  CSC_Training_CA.info 3622c361.info
ln -s  CSC_Training_CA.info 44efd5a6.info
ln -s  CSC_Training_CA.namespaces 3622c361.namespaces
ln -s  CSC_Training_CA.namespaces 44efd5a6.namespaces
ln -s  CSC_Training_CA.signing_policy 3622c361.signing_policy
ln -s  CSC_Training_CA.signing_policy 44efd5a6.signing_policy
ln -s  CSC_Training_CA.pem 3622c361.0
ln -s  CSC_Training_CA.pem 44efd5a6.0

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/grid-security/certificates/*
%doc



%changelog
* Sun Apr 1 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-3
 - Updated to faked CA-version of 1.46

* Thu Mar 22 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-2
 - Alias was incorrect

* Wed Mar 21 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-1
 - First published version of CA package

