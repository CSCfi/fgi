Name:		slurm-version
Version:	2
Release:	12%{?dist}
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
Conflicts: slurm-version-fgislurm24

%description fgislurm23
Selects SLURM 2.3.x


%package fgislurm24
Summary: Selects SLURM 2.4.x
Conflicts: slurm-version-fgislurm23

%description fgislurm24
Selects SLURM 2.4.x

%package fgislurm25
Summary: Selects SLURM 2.5.x
Conflicts: slurm-version-fgislurm23
Conflicts: slurm-version-fgislurm24

%description fgislurm25
Selects SLURM 2.5.x

%package fgislurm26
Summary: Selects SLURM 2.6.x
Conflicts: slurm-version-fgislurm24
Conflicts: slurm-version-fgislurm25

%description fgislurm26
Selects SLURM 2.6.x

%package fgislurm1403
Summary: Selects SLURM 14.03
Conflicts: slurm-version-fgislurm24
Conflicts: slurm-version-fgislurm25
Conflicts: slurm-version-fgislurm26

%description fgislurm1403
Selects SLURM 13.12

%post fgislurm23
if [ -d /etc/cluster ]; then
	cp -f /usr/lib/slurm-version/slurm23 /etc/cluster/conf/slurmversion
	cp -f /usr/lib/slurm-version/slurminstallurl23 /etc/cluster/conf/slurminstallurl
fi

%post fgislurm24
if [ -d /etc/cluster ]; then
	cp -f /usr/lib/slurm-version/slurminstallurl24 /etc/cluster/conf/slurminstallurl
	cp -f /usr/lib/slurm-version/slurm24 /etc/cluster/conf/slurmversion
fi

%post fgislurm25
if [ -d /etc/cluster ]; then
	cp -f /usr/lib/slurm-version/slurminstallurl25 /etc/cluster/conf/slurminstallurl
	cp -f /usr/lib/slurm-version/slurm25 /etc/cluster/conf/slurmversion
fi

%post fgislurm26
if [ -d /etc/cluster ]; then
	cp -f /usr/lib/slurm-version/slurminstallurl26 /etc/cluster/conf/slurminstallurl
	cp -f /usr/lib/slurm-version/slurm26 /etc/cluster/conf/slurmversion
fi
%post fgislurm1403
if [ -d /etc/cluster ]; then
	cp -f /usr/lib/slurm-version/slurminstallurl1403 /etc/cluster/conf/slurminstallurl
	cp -f /usr/lib/slurm-version/slurm1403 /etc/cluster/conf/slurmversion
fi


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
#mkdir -p  %{buildroot}/etc/cluster/conf
mkdir -p %{buildroot}/usr/lib/slurm-version/
cp slurm23 slurminstallurl23 %{buildroot}/usr/lib/slurm-version/
cp slurm24 slurminstallurl24 %{buildroot}/usr/lib/slurm-version/
cp slurm25 slurminstallurl25 %{buildroot}/usr/lib/slurm-version/
cp slurm26 slurminstallurl26 %{buildroot}/usr/lib/slurm-version/
cp slurm1403 slurminstallurl1403 %{buildroot}/usr/lib/slurm-version/
mkdir -p %{buildroot}/etc/yum.repos.d/
cp fgislurm23.repo %{buildroot}/etc/yum.repos.d/
cp fgislurm24.repo %{buildroot}/etc/yum.repos.d/
cp fgislurm25.repo %{buildroot}/etc/yum.repos.d/
cp fgislurm26.repo %{buildroot}/etc/yum.repos.d/
cp fgislurm1403.repo %{buildroot}/etc/yum.repos.d/

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

%files fgislurm25
%defattr(-,root,root,-)
/usr/lib/slurm-version/slurm25
/usr/lib/slurm-version/slurminstallurl25
/etc/yum.repos.d/fgislurm25.repo
%doc

%files fgislurm26
%defattr(-,root,root,-)
/usr/lib/slurm-version/slurm26
/usr/lib/slurm-version/slurminstallurl26
/etc/yum.repos.d/fgislurm26.repo
%doc

%files fgislurm1403
%defattr(-,root,root,-)
/usr/lib/slurm-version/slurm1403
/usr/lib/slurm-version/slurminstallurl1403
/etc/yum.repos.d/fgislurm1403.repo
%doc



%changelog
* Mon Apr 14 2014 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-12
- Fixed description for 14.03.

* Mon Dec 30 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-11
- 13.12 got renamed 14.03.

* Fri Dec 20 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-9
- Cleanup of specfile
- Added support for the upcoming slurm 13.12 version

* Tue Aug 20 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-8
- Fixed if-fi problem

* Wed Jul 24 2013 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-7
- Added package for SLURM 2.6

* Mon Dec 17 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-6
- Fixed warning from uninstall script

* Mon Dec 17 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-5
- Removed dependencies, as it was impossible to update.

* Mon Dec 17 2012 Ulf Tigerstedt <ulf.tigerstedt@csc.fi> - 2-4
- Added repo for slurm 2.5


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
