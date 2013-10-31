Name:		fgi-lsc-files
Version:	1
Release:	3%{?dist}
Summary:	Lsc files needed by VOMS, packaged for FGI

Group:		Applications/Grid	
License:	GPL
URL:		http://pulse.fgi.csc.fi/fgi-lsc-files.tar.gz
Source0:	fgi-lsc-files-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	bash	
Requires:	nordugrid-arc-client,voms-clients

%description
The .lsc files are needed for VOMS clients to authenticate the VOMS proxy.
Without the files they can't establish a full trust chain, from the host certificate
to the CA. Also included is the /etc/vomses file that clients use to find the correct
VOMS server.



%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
cp -r etc $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/grid-security/*
%config /etc/vomses
%doc



%changelog
* Thu Oct 31 2013 Ulf Tigerstedt <tigerste@csc.fi> 1-3
- Added ipv6.hepix.org VO
* Wed Oct 09 2013 Ulf Tigerstedt <tigerste@csc.fi> 1-2
- New voms server at BNL added for Atlas
* Sat Feb 11 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- First version. Supported VOs are alice,atlas,bio.ndgf.org,
  cms,cscstaff,csctraining,customer.csc.fi,dteam,fgi.csc.fi,
  ops,ops.ndgf.org

