Name:		fgi-grid-node
Version:	1	
Release:	1%{?dist}
Summary:	Helper scripts needed on FGI grid nodes

Group:		Other	
License:	GPL
URL:		http://pulse.fgi.csc.fi/fgi-grid-node
Source0:	fgi-grid-node-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash
Requires:	bash, /etc/cron.hourly, nordugrid-arc-arex, coreutils	

BuildArch:	noarch

%description
Helper scripts and cronjobs to make it easier to run a FGI ARC grid 
frontend


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cron.hourly
cp arc-ur-register $RPM_BUILD_ROOT/etc/cron.hourly


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/cron.hourly/arc-ur-register
%doc



%changelog

* Fri Apr 13 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> 1-1
- First version containing the arc-ur-register cron job
