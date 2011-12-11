Name:		nvidia-ganglia
Version:	1
Release:	1%{?dist}
Summary:	Packages for monitoring CUDA cards with Ganglia 3.x+

Group:		Applications
License:	GPL
URL:		http://csc.fi/fgi
Source0:	nvidia-ganglia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python
Requires:	ganglia-gmond-python, nvidia-ml-py

%description
Packages to monitor CUDA cards with Ganglia 3.x


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}
tar zxf nvidia-ml-py-1.0.tar.gz
python makecompile.py


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/ganglia/conf.d
mkdir -p $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules/
mkdir -p $RPM_BUILD_ROOT/usr/lib/python2.6/site-packages/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

