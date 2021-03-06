Name:		fgi-lsc-files
Version:	1
Release:	11%{?dist}
Summary:	Lsc files needed by VOMS, packaged for FGI/FGCI

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
* Mon Sep 19 2016 Ulf Tigerstedt <tigerste@csc.fi> 1-11
- Fixed CA for ops.ndgf.org voms server
* Thu Jun 30 2016 Luís Alves <luis.alves@csc.fi> 1-10
- Updated etc/grid-security/vomsdir/dteam/voms.hellasgrid.gr.lsc and etc/grid-security/vomsdir/dteam/voms2.hellasgrid.gr.lsc to have latest CA DN changes. 
* Fri Feb 26 2016 Ulf Tigerstedt <tigerste@csc.fi> 1-9
- Updated voms.fgi.csc.fi to Nordugrid CA 2015
* Wed Jul 29 2015 Ulf Tigerstedt <tigerste@csc.fi> 1-8
- Really removed the old voms-servers this time.
* Fri Jan 16 2015 Ulf Tigerstedt <tigerste@csc.fi> 1-7
- Removed old voms-servers from CERN VOs
* Tue Sep 2 2014 Ulf Tigerstedt <tigerste@csc.fi> 1-6
- Fixed alice, atlas and cms with the new CERN voms servers
* Wed Apr 10 2014 Ulf Tigerstedt <tigerste@csc.fi> 1-5
- Fixed ops VO again in vomses
* Wed Apr 9 2014 Ulf Tigerstedt <tigerste@csc.fi> 1-4
- Fixed ops VO with new correct servers.
* Thu Oct 31 2013 Ulf Tigerstedt <tigerste@csc.fi> 1-3
- Added ipv6.hepix.org VO
* Wed Oct 09 2013 Ulf Tigerstedt <tigerste@csc.fi> 1-2
- New voms server at BNL added for Atlas
* Sat Feb 11 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- First version. Supported VOs are alice,atlas,bio.ndgf.org,
  cms,cscstaff,csctraining,customer.csc.fi,dteam,fgi.csc.fi,
  ops,ops.ndgf.org

