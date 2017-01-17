Name:		fgi-compute-node
Version:	1
Release:	15%{?dist}
Summary:	Metapackage for required software on FGI compute nodes
BuildArch:	noarch

Group:		other/fgi	
License:	GPL
URL:		http://pulse.fgi.csc.fi
Source0:	fgi-compute-node-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash
Requires:	openmpi
Requires:	openmpi-devel
#Requires:	compat-openmpi
Requires:	xerces-c
Requires:	python-sqlite2
Requires:	numpy
#Requires:	scipy
Requires:	blas
Requires:	atlas
Requires:	hdf5-openmpi
Requires:	netcdf
Requires:	globus-gsi-openssl-error
Requires:	globus-xio-popen-driver
Requires:	globus-gsi-credential
Requires:	globus-gsi-callback
Requires:	globus-xio-gsi-driver
Requires:	globus-io
Requires:	globus-gssapi-gsi
Requires:	globus-xio
Requires:	globus-callout
Requires:	globus-openssl-module
Requires:	globus-gss-assist
Requires:	globus-gsi-proxy-ssl
Requires:	globus-common
Requires:	globus-ftp-control
Requires:	globus-gsi-proxy-core
Requires:	globus-gsi-sysconfig
Requires:	globus-gssapi-error
Requires:	globus-gsi-cert-utils
Requires:	globus-ftp-client
Requires:	fftw
Requires:	gsl
Requires:	libXpm
Requires:	libtiff
Requires:	cfitsio
Requires:	graphviz-gd
Requires:	dcap-libs
Requires:	gfal2-all
Requires:	mpfr
Requires:	libmpc
Requires:	gmp
Requires:	libtool-ltdl
Requires:	atlas-sse3
Requires:	zlib-devel
#Requires:	java-1.6.0-openjdk
Requires:	java-1.7.0-openjdk
Requires:	java-1.8.0-openjdk
Requires:	libxc
Requires:	zsh





%description
Metapackage for FGI compute, login and grid nodes to ease the installation of libraries needed by software on
cvmfs and to ensure that all nodes have the same software installed.


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}
/bin/true


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
#make install DESTDIR=%{buildroot}
/bin/true


%clean
rm -rf %{buildroot}


%files
#%defattr(-,root,root,-)
#%doc



%changelog
* Mon Jan 16 2017 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-14
- Added zsh and java8
- Removed java1.6
* Tue Oct 7 2014 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-12
- Removed globus rls
* Tue May 27 2014 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-11
- Added libxc for new GPAW
* Mon Jan 20 2014 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-10
- Added OpenJDK java 1.6 and 1.7
* Thu Dec 19 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-9
- Added zlib-devel 

* Tue Aug 20 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-8
- Added atlas-sse3

* Tue Jul 23 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-7
- Added libtool-ltdl for iRODS icommands

* Mon Mar 25 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-6
- Added libraries for gcc 4.8

* Tue Feb 5 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-4
- Added blas

* Thu Oct 11 2012 Ulf Tigerstedt <ulf.tigerstedt at, csc.fi> 1-1
- First version to go with cluster-tools 0.26-1.

* Wed Jan 9 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-3
- Added packages needed for root on cvmfs + gfal.


