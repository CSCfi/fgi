Name:		cvmfs-repofiles-fgi
Version:	3
Release:	1%{?dist}
Summary:	Files to enable the fgi.csc.fi CVMFS repository

Group:		none	
License:	GPL
URL:		http://cvmfs.fgi.csc.fi/
Source0:	http://www.csc.fi/cvmfs-repofiles-fgi-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

#BuildRequires: 	
Requires:	cvmfs,cvmfs-keys, autofs

%description
Hippos! Magical amounts of hippos!

%prep
%setup -q


%build
/bin/true


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/config.d
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/domain.d
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs/keys

cp fgi.csc.fi.pub $RPM_BUILD_ROOT/etc/cvmfs/keys/
cp csc.fi.conf $RPM_BUILD_ROOT/etc/cvmfs/domain.d/
cp fgi.csc.fi.conf $RPM_BUILD_ROOT/etc/cvmfs/config.d/
cp default.local $RPM_BUILD_ROOT/etc/cvmfs/
cp fuse.conf $RPM_BUILD_ROOT/etc





%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/cvmfs/keys/fgi.csc.fi.pub
%config /etc/cvmfs/default.local
%config /etc/cvmfs/config.d/fgi.csc.fi.conf
%config /etc/cvmfs/domain.d/csc.fi.conf
%config /etc/fuse.conf



%doc

%post
/usr/bin/cvmfs_config setup
#/etc/init.d/autofs restart



%changelog
* Thu Sep 08 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi> - 3
- Added commands to start cvmfs on the client

* Thu Sep 08 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi> - 2
- Split cvmfs yum files to another package

* Wed Sep 07 2011 Ulf Tigerstetdt <ulf.tigerstedt@csc.fi> - 1 
- First version of the package


