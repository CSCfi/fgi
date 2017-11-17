Name:		slurm-version-release
Version:	2
Release:	11%{?dist}
Summary:	Selects the correct SLURM version

Group:		none
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	slurm-version-release-%{version}.tar.gz
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

%package slurm23
Summary: Selects SLURM 2.3.x
Conflicts: slurm-version-slurm24

%description slurm23
Selects SLURM 2.3.x


%package slurm24
Summary: Selects SLURM 2.4.x
Conflicts: slurm-version-slurm23

%description slurm24
Selects SLURM 2.4.x

%package slurm25
Summary: Selects SLURM 2.5.x
Conflicts: slurm-version-slurm23
Conflicts: slurm-version-slurm24

%description slurm25
Selects SLURM 2.5.x

%package slurm26
Summary: Selects SLURM 2.6.x
Conflicts: slurm-version-slurm24
Conflicts: slurm-version-slurm25

%description slurm26
Selects SLURM 2.6.x

%package slurm1403
Summary: Selects SLURM 13.12
Conflicts: slurm-version-slurm24
Conflicts: slurm-version-slurm25
Conflicts: slurm-version-slurm26

%description slurm1403
Selects SLURM 13.12

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp slurm23.repo %{buildroot}/etc/yum.repos.d/
cp slurm24.repo %{buildroot}/etc/yum.repos.d/
cp slurm25.repo %{buildroot}/etc/yum.repos.d/
cp slurm26.repo %{buildroot}/etc/yum.repos.d/
cp slurm1403.repo %{buildroot}/etc/yum.repos.d/
cp RPM-GPG-KEY-CSC-GRID-2 %{buildroot}/etc/pki/rpm-gpg/
%clean
rm -rf %{buildroot}


%files slurm23
%defattr(-,root,root,-)
/etc/yum.repos.d/slurm23.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2
%doc

%files slurm24
%defattr(-,root,root,-)
/etc/yum.repos.d/slurm24.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2
%doc

%files slurm25
%defattr(-,root,root,-)
/etc/yum.repos.d/slurm25.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2
%doc

%files slurm26
%defattr(-,root,root,-)
/etc/yum.repos.d/slurm26.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2
%doc

%files slurm1403
%defattr(-,root,root,-)
/etc/yum.repos.d/slurm1403.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2
%doc



%changelog
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
