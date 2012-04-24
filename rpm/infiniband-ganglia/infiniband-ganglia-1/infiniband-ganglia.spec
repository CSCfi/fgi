Name:		infiniband-ganglia
Version:	1
Release:	1%{?dist}
Summary:	Ganglia python scripts to get Infiniband information

Group:		Network
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	infiniband-ganglia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python
Requires:	ganglia-gmond-python

%description
Script to send Infiniband network info to ganglia


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
cp infiniband.pyconf %{buildroot}/etc/ganglia/conf.d
cp infiniband.py  %{buildroot}/usr/lib64/ganglia/python_modules/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/etc/ganglia/conf.d/*
/usr/lib64/ganglia/python_modules/*
%doc



%changelog
* Tue Apr 24 2012 <ulf.tigerstedt@csc.fi> 1-1
- First version
