Name:		slurm-fgi-addons
Version:	1
Release:	2%{?dist}
Summary:	Scripts for SLURM, needed by the FGI clusters

Group:		Some/Group
License:	GPL
URL:		http://pulse.fgi.csc.fi/
Source0:	slurm-fgi-addons-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

BuildRequires:	bash
Requires:	bash, perl-Filesys-Df, slurm

%description
Scripts for checking the health of a slurm node, plus prolog/epilog
scripts


%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp healthcheck healthcheck-df.pl healthcheck-nfs taskprolog epilog $RPM_BUILD_ROOT/usr/bin 


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/healthcheck
/usr/bin/healthcheck-nfs
/usr/bin/healthcheck-df.pl
/usr/bin/taskprolog
/usr/bin/epilog
%doc



%changelog
* Wed Mar 09 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-2
- Forgot an echo in the script, so it did nothing.

* Wed Feb 01 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- First version, complete with healthcheck, taskprolog and epilog

