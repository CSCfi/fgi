Name:		fgi-compute-node
Version:	1
Release:	3%{?dist}
Summary:	Metapackage for required software on FGI compute nodes
BuildArch:	noarch

Group:		other/fgi	
License:	GPL
URL:		http://pulse.fgi.csc.fi
Source0:	fgi-compute-node-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash
Requires:	openmpi
Requires:	compat-openmpi
Requires:	xerces-c
Requires:	python-sqlite2
Requires:	numpy
Requires:	scipy
Requires:	atlas
Requires:	hdf5-openmpi
Requires:	netcdf
Requires:	globus-gsi-openssl-error
Requires:	globus-xio-popen-driver
Requires:	globus-gsi-credential
Requires:	globus-gsi-callback
Requires:	globus-xio-gsi-driver
Requires:	globus-rls-client
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
* Thu Oct 11 2012 Ulf Tigerstedt <ulf.tigerstedt at, csc.fi> 1-1
- First version to go with cluster-tools 0.26-1.

* Wed Jan 9 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-3
- Added packages needed for root on cvmfs + gfal.


