Name:		nvidia-ganglia
Version:	2
Release:	2%{?dist}
Summary:	Packages for monitoring CUDA cards with Ganglia 3.x+

Group:		Applications
License:	GPL
URL:		http://csc.fi/fgi
Source0:	nvidia-ganglia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

BuildRequires: python
Requires:	ganglia-gmond-python, nvidia-ml-py

%package lite
Group:          Applications
License:        GPL
URL:            http://csc.fi/fgi
BuildRequires: python
Requires:       ganglia-gmond-python, nvidia-ml-py
Summary:	Ganglia monitoring for GT520 cards
BuildArch:      noarch



%description
Packages to monitor CUDA cards with Ganglia 3.x

%description lite
Packages to monitor GT520 cards with Ganglia 3.x


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}
python makecompile.py


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/ganglia/conf.d
mkdir -p $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules/
cp nvidia-lite.py  nvidia-lite.pyc $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules/
cp nvidia.py nvidia.pyc $RPM_BUILD_ROOT/usr/lib64/ganglia/python_modules/
cp *pyconf $RPM_BUILD_ROOT/etc/ganglia/conf.d/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib64/ganglia/python_modules/nvidia.py  
/usr/lib64/ganglia/python_modules/nvidia.pyc
/usr/lib64/ganglia/python_modules/nvidia.pyo
/etc/ganglia/conf.d/nvidia.pyconf
%doc

%files lite
%defattr(-,root,root,-)
/usr/lib64/ganglia/python_modules/nvidia-lite.py  
/usr/lib64/ganglia/python_modules/nvidia-lite.pyc 
/usr/lib64/ganglia/python_modules/nvidia-lite.pyo
/etc/ganglia/conf.d/nvidia-lite.pyconf

%changelog
* Tue Dec 13 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2
- Fixed -lite package to not contain UUID

* Mon Dec 12 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1
- First release. 

