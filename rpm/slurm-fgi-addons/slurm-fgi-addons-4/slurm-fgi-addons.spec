Name:		slurm-fgi-addons
Version:	4
Release:	3%{?dist}
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
cp slurm healthcheck healthcheck-df.pl healthcheck-nfs taskprolog epilog $RPM_BUILD_ROOT/usr/bin 


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/slurm
/usr/bin/healthcheck
/usr/bin/healthcheck-nfs
/usr/bin/healthcheck-df.pl
/usr/bin/taskprolog
/usr/bin/epilog
%doc



%changelog
* Thu Nov 8 2012 Ulf Tigerstedt <tigerste@csc.fi> 4-3 
- Small bugfix: healthcheck script now exits after rebooting the machine

* Wed Jun 20 2012 Ulf Tigerstedt <tigerste@csc.fi> 4-2
- Healthcheck now check for RTC and disables slurm if it is not present
- Healthcheck now refuses to drain an already draining node.

* Fri May 25 2012 Kalle Happonen <kalle.happonen@csc.fi> 4-1
- Fixed the job $TMPDIR handling. Now addition and removal should work properly on multi-node jobs

* Thu May 10 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-7
- Fixed the debug option to print the reason correctly.

* Tue Apr 17 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-6
- Fixed the debug option to actually not print debug output all the time.

* Fri Apr 13 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-5
- Added "slurm" script, as provided by Aalto University, to prettyprint
the slurm information.

* Thu Apr 12 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-4
- Decreased nfs wait time to 40 seconds, as slurm has a limit on
healthchecks on 60 seconds.

* Wed Apr 11 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-3
- Added -d debug parameter to tell verbosely what the health check
  is doing

* Wed Apr 11 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-2
- Made the autohealing actually work, by fixing the regexp.
- Increased the NFS timeout to 60 seconds

* Fri Mar 30 2012 Ulf Tigerstedt <tigerste@csc.fi> 3-1
- Added autohealing to the health script so that it returns the machine
  to service if the health check script succeeds.
- Updated NFS /home check timeout to 30 seconds.
- Added Ivans patch to make the script work on Triton

* Thu Mar 15 2012 Ulf Tigerstedt <tigerste@csc.fi> 2-2
- Added a 2 second sleep before reboot, to make sure the message
  is sent to the control daemon
- Increased timeout for NFS /home to 10 seconds.
- Fixed taskprolog to set TMP, TEMP and TEMPDIR also.

* Wed Mar 14 2012 Ulf Tigerstedt <tigerste@csc.fi> 2-1 
- Added verbose error reporting

* Wed Mar 09 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-2
- Forgot an echo in the script, so it did nothing.

* Wed Feb 01 2012 Ulf Tigerstedt <tigerste@csc.fi> 1-1
- First version, complete with healthcheck, taskprolog and epilog

