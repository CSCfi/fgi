Name:		slurm-version
Version:	1
Release:	1%{?dist}
Summary:	Selects the correct SLURM version

Group:		none
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	slurm-version-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash	
Requires:	bash

%description
Selects the correct SLURM version

%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}

%package fgislurm23
Summary: Selects SLURM 2.3.x
Requires: slurm >= 2.3 
Requires: slurm < 2.4
Conflicts: slurm-version-fgislurm24

%description fgislurm23
Selects SLURM 2.3.x


%package fgislurm24
Summary: Selects SLURM 2.4.x
Requires: slurm >= 2.4 
Requires: slurm < 2.5
Conflicts: slurm-version-fgislurm23

%description fgislurm24
Selects SLURM 2.4.x




%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
mkdir -p  %{buildroot}/etc/cluster/conf
cp slurm23 %{buildroot}/etc/cluster/conf/
cp slurm24 %{buildroot}/etc/cluster/conf/

%clean
rm -rf %{buildroot}


%files fgislurm23
%defattr(-,root,root,-)
/etc/cluster/conf/slurm23
%doc

%files fgislurm24
%defattr(-,root,root,-)
/etc/cluster/conf/slurm24
%doc


%changelog
* Thu Aug 25 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1-1
- First version
