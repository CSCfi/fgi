Name:		slurm-version
Version:	2
Release:	3%{?dist}
Summary:	Selects the correct SLURM version

Group:		none
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	slurm-version-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	bash	
Requires:	bash
BuildArch:	noarch

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
Requires: slurm-munge >= 2.3 
Requires: slurm-plugins >= 2.3 
Requires: slurm-munge < 2.4

Conflicts: slurm-version-fgislurm24

%description fgislurm23
Selects SLURM 2.3.x


%package fgislurm24
Summary: Selects SLURM 2.4.x
Requires: slurm >= 2.4 
Requires: slurm < 2.5
Requires: slurm-munge >= 2.4 
Requires: slurm-munge < 2.5
Requires: slurm-plugins >= 2.4
Requires: slurm-plugins < 2.5
Requires: slurm-lua >= 2.4 
Requires: slurm-lua < 2.5
Conflicts: slurm-version-fgislurm23

%description fgislurm24
Selects SLURM 2.4.x

%post fgislurm23
if [ -d /etc/cluster ]; then
	cp /usr/lib/slurm-version/slurm23 /etc/cluster/conf/slurmversion
	cp /usr/lib/slurm-version/slurminstallurl23 /etc/cluster/conf/slurminstallurl
fi

%post fgislurm24
if [ -d /etc/cluster ]; then
	cp /usr/lib/slurm-version/slurminstallurl24 /etc/cluster/conf/slurminstallurl
	cp /usr/lib/slurm-version/slurm24 /etc/cluster/conf/slurmversion
fi

%preun fgislurm23
if [ -f /etc/cluster/conf/slurmversion ]; then 
rm -f /etc/cluster/conf/slurmversion
rm -f /etc/cluster/conf/slurminstallurl
fi


%preun fgislurm24
if [ -f /etc/cluster/conf/slurmversion ]; then 
rm -f /etc/cluster/conf/slurmversion
rm -f /etc/cluster/conf/slurminstallurl
fi


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
#mkdir -p  %{buildroot}/etc/cluster/conf
mkdir -p %{buildroot}/usr/lib/slurm-version/
cp slurm23 slurminstallurl23 %{buildroot}/usr/lib/slurm-version/
cp slurm24 slurminstallurl24 %{buildroot}/usr/lib/slurm-version/
mkdir -p %{buildroot}/etc/yum.repos.d/
cp fgislurm23.repo %{buildroot}/etc/yum.repos.d/
cp fgislurm24.repo %{buildroot}/etc/yum.repos.d/

%clean
rm -rf %{buildroot}


%files fgislurm23
%defattr(-,root,root,-)
/usr/lib/slurm-version/slurm23
/usr/lib/slurm-version/slurminstallurl23
/etc/yum.repos.d/fgislurm23.repo
%doc

%files fgislurm24
%defattr(-,root,root,-)
/usr/lib/slurm-version/slurm24
/usr/lib/slurm-version/slurminstallurl24
/etc/yum.repos.d/fgislurm24.repo
%doc



%changelog
* Fri Sep 14 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-3
- Fixed slurm-plugins requirement

* Wed Sep 11 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-1
- Added slurm-plugins requirement


* Wed Sep 05 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-1
- Minor fixes

* Wed Sep 05 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-0
- Changed to a yum repo based model

* Sat Sep 01 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1-2
- Added more conflicts

* Thu Aug 25 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 1-1
- First version
