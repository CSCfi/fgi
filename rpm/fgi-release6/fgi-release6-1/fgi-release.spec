Name:		fgi-release6
Version:	1	
Release:	1%{?dist}
Summary:	Release files for FGI repository

Group:		Applications/Communication
License:	GPL
#URL:		
Source0:	fgi-release6-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

#BuildRequires:	
Requires:	yum

%description
Yum repo file for the FGI repository (RHEL/CentOS/SL 6 version)


%prep
%setup -q


%build


%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cp fgi.repo $RPM_BUILD_ROOT/etc/yum.repos.d


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/fgi.repo



%changelog
* Fri May 20 2011 Ulf Tigerstedt <tigerste@csc.fi> 1
-Initial version


