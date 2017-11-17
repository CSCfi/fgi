Name:		cvmfs-repofiles-fgi
Version:	1
Release:	1%{?dist}
Summary:	Files to enable the fgi.csc.fi CVMFS repository

Group:		none	
License:	GPL
URL:		http://cvmfs.fgi.csc.fi/
Source0:	http://www.csc.fi/cvmfs-repofiles-fgi.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

#BuildRequires: 	
Requires:	cvmfs,cvmfs-keys, autofs

%description
Hippos! Magical amounts of hippos!

%prep
%setup -q


%build
#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/config.d
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/domain.d
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/keys
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg

cp RPM-GPG-KEY-CernVM $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
cp fgi.csc.fi.pub $RPM_BUILD_ROOT/etc/cvmfs/keys/
cp csc.fi.conf $RPM_BUILD_ROOT/etc/cvmfs/domain.d
cp cvmfs.repo $RPM_BUILD_ROOT/etc/yum.repos.d
cp default.local $RPM_BUILD_ROOT/etc/cvmfs/
cp fuse.conf $RPM_BUILD_ROOT/etc





%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/cvmfs/keys/fgi.csc.fi.pub
/etc/pki/rpm-gpg/RPM-GPG-KEY-CernVM
%config /etc/cvmfs/default.local
%config /etc/cvmfs/config.d/fgi.csc.fi.conf
%config /etc/cvmfs/domain.d/csc.fi.conf
%config /etc/fuse.conf
%config /etc/yum.repos.d/cvmfs.repo



%doc



%changelog
* Wed Sep 07 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi>
- First version of the package
