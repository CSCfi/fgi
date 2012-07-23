Name:		arcsanity-ganglia
Version:	1
Release:	2%{?dist}
Summary:	Ganglia python scripts to do sanity checking on ARC CEs

Group:		Network
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	arcsanity-ganglia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python
Requires:	ganglia-gmond-python

%description
Script to do sanity checking on ARC CEs.
- Count UR records
- Count sessiondirs
- Count jobstatus files

%prep
%setup -q


%build
#%configure
#make %{?_smp_mflags}


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/etc/ganglia/conf.d
mkdir -p %{buildroot}/usr/lib64/ganglia/python_modules/
cp arcsanity.pyconf %{buildroot}/etc/ganglia/conf.d
cp arcsanity.py  %{buildroot}/usr/lib64/ganglia/python_modules/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/lib64/ganglia/python_modules/*
%config
/etc/ganglia/conf.d/*



%changelog
* Tue Jul 24 2012 <ulf.tigerstedt@csc.fi> 1-2
- Minor fixes

* Mon Jul 23 2012 <ulf.tigerstedt@csc.fi> 1-1
- First version
