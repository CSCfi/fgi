Name:		nvidia-ml-py
Version:	1
Release:	1%{?dist}
Summary:	ML bindings for Python (CUDA)

Group:		Applications/programming
License:	BSD
URL:		http://pypi.python.org/pypi/nvidia-ml-py/
Source0:	nvidia-ml-py-1.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python
Requires:	python, kmod-nvidia

%description
NVidia ML bindings for Python


%prep
%setup -q


%build
%configure
tar zxf nvidia-ml-py-1.0.tar.gz
cd nvidia-ml-py-1.0
python setup.py build
cd ..
python makecompile.py
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/python2.6/site-packages/
cp  nvidia-ml-py-1.0/build/lib/* $RPM_BUILD_ROOT/usr/lib/python2.6/site-packages/

#make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib/python2.6/site-packages/pynvml.py
/usr/lib/python2.6/site-packages/pynvml.pyc
/usr/lib/python2.6/site-packages/pynvml.pyo
%doc



%changelog
* Mon Dec 12 2011 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1
- First release.
