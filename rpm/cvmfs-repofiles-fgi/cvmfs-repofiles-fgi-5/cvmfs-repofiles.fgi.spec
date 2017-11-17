Name:		cvmfs-repofiles-fgi
Version:	5
Release:	0%{?dist}
Summary:	Files to enable the fgi.csc.fi CVMFS repository

Group:		none	
License:	GPL
URL:		http://cvmfs.fgi.csc.fi/
Source0:	http://www.csc.fi/cvmfs-repofiles-fgi-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch

#BuildRequires: 	
Requires:	cvmfs,cvmfs-config-default, autofs

%description
Package containing the config files to enable the
fgi.csc.fi CVMFS repository, enabling its use by only
installing this package.


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
#cp default.local $RPM_BUILD_ROOT/etc/cvmfs/
#cp fuse.conf $RPM_BUILD_ROOT/etc





%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/cvmfs/keys/fgi.csc.fi.pub
#%config /etc/cvmfs/default.local
%config /etc/cvmfs/config.d/fgi.csc.fi.conf
%config /etc/cvmfs/domain.d/csc.fi.conf
#%config /etc/fuse.conf



%doc

%post
echo user_allow_other >> /etc/fuse.conf
/usr/bin/cvmfs_config setup
#/etc/init.d/autofs restart



%changelog
* Tue Apr 14 2015 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 5-0
- Removed default.local from rpm and moved it into cluster-tools
- Removed fuse.conf and replaced it with an echo >>
* Wed Apr 1 2015 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 4-5
- cvmfs-keys is gone, long live cvmfs-default-config 

* Wed Feb 12 2014 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 4-4
- Made cvmfs.fgi the firstline server (stratum 1) with idris at the back (stratum 0).
- Added more space to the cache.

* Wed Oct 23 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 4-3
- Switch to using idris.fgi instead


* Mon Apr 29 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 4-2
- Used incorrect separator.

* Mon Apr 29 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 4
- Added mustikka.csc.fi as a replica.

* Thu Sep 08 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 3
- Added commands to start cvmfs on the client

* Thu Sep 08 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2
- Split cvmfs yum files to another package

* Wed Sep 07 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1 
- First version of the package


