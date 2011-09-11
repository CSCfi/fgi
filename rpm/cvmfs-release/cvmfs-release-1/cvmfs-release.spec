Name:		cvmfs-release
Version:	1
Release:	2
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
Non-CERN package containing the yum .repo file for the official 
CVMFS repository in addition to the GPG RPM signing key for that repo.
Released by CSC for easy use by the FGI/NGI_FI grid.

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
