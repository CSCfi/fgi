Name:		cvmfs-release
Version:	1
Release:	1%{?dist}
Summary:	CVMFS repository release files (FGI)

Group:		none	
License:	GPL
URL:		http://cvmfs.fgi.csc.fi/
Source0:	http://www.csc.fi/cvmfs-release-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

#BuildRequires: 	
Requires:	yum

%description
Hippos! Magical amounts of hippos! With whipped cream!

%prep
%setup -q


%build
/bin/true


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg

cp RPM-GPG-KEY-CernVM $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
cp cvmfs.repo $RPM_BUILD_ROOT/etc/yum.repos.d/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/pki/rpm-gpg/RPM-GPG-KEY-CernVM
%config /etc/yum.repos.d/cvmfs.repo



%doc



%changelog
* Thu Sep 08 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi> - 1
- First version of the package
