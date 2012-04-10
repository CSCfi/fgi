Name: cluster-tools
Version: 0.19
Release:	1%{?dist}
Source: %{name}-%{version}.tar.gz
Summary: Admin tools for FGI clusters
Group: System Environment/Base	
License: GPL
BuildArch: noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: pdsh,python,tftp-server,dhcp,bind-chroot,httpd

#Avoid compiling the http python modules to *.pyc and *.pyo files
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
This package contains tools and utilities for the FGI install node

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT/*
cp -r etc usr var $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cluster/scripts/mounts.sh
%config(noreplace) %{_sysconfdir}/cluster/scripts/ib.sh
%config(noreplace) %{_sysconfdir}/cluster/scripts/mail.sh
%{_sysconfdir}/cluster
%{_sbindir}/*
%{_libexecdir}/cluster
%attr(0744, apache, apache) %{_localstatedir}/www/cgi-bin/*
%{_localstatedir}/lib/tftpboot/*


%changelog
* Tue Apr 10 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.19-1
  - Added mail configuration for nodes
  - Added fgi-hw-check as a default package on the node

* Fri Mar 16 2012 Ulf Tigerstedt <ulf.tigerstedt at, csc.fi> 0.18-2
  - Changed ib.sh to be a noreplace-file.
  - Select boot interface by mac address in netboot.py

* Thu Mar 15 2012 Ulf Tigerstedt <ulf.tigerstedt at, csc.fi> 0.18-1
 - Added folder for health check script
 - Added script for copying them to the compute node

* Thu Feb 1 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.17-2
 - Added PAM setting to the slurm config script
* Thu Feb 1 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.17-1
 - Added EGI trust anchors and fetch-crl for nodes 
 - Added limits changes to nodes for MPI jobs
 - Changed the kickstart file to only run files which end in .sh endings in /etc/cluster/scripts
 - Increased boot size partition size on nodes
 - Added default mount options in mounts.sh
 - Added hdparm.sh script to turn on write caching on default node disk setups
 - Changed reinstall command. Now it doesn't die on nonexisting nodes. By default it also now reboots nodes, by setting them in a draining state with "reboot" as a message
* Thu Jan 19 2012 Kalle Happonen <kalle.happonen at, csc.fi> 0.16-1
 - Made a fix in the kernel scirpt sed lines.
* Mon Dec 19 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.15-1
 - Added hp-health by default
 - Improved booting scripts. They should be less picky about interfaces.
* Wed Dec 14 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.14-1
 - Fixed cuda installation
 - Small ntp fix 
 - Added mcelog to nodes
* Mon Dec 12 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.13-1
 - Fixed gpxe support for fat nodes
 - Small ntp fix 
* Mon Dec 12 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.12-1
 - Fixed GPGPU problems
 - Added NTP configuration
 - Addes some packages
 - Added cpuspeed fix to GOVERNOR="performance"
* Fri Dec 9 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.11-1
 - Now GPGPU nodes get cuda driver on install
 - Ganglia conifguration fixed
 - Preboot hwclock setting
 - Added packages
 - User defined root keys on nodes enabled
* Wed Dec 7 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.10-1
 - netboot.py blacklists the nouveau driver, which caused problems with the M2090 cards.
 - Named now reloads on change instead of restarts
* Mon Dec 1 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.9-1
 - node-added also adds ssh key to known hosts for ib interfaces
* Tue Nov 8 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.8-1
 - Added idmapd config to node mount scripts
* Tue Nov 8 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.7-1
 - Added packages, generated random root password for node
* Tue Nov 3 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.6-1
 - Bugfixes
* Tue Nov 1 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.5-1
 - Bugfixes, added FGI repo filelist, other minor improvements
* Wed Sep 14 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.3-1
 - Bugfixes and improvements
* Wed Aug 17 2011 Kalle Happonen <kalle.happonen at, csc.fi> 0.1-1
 - First release of the cluster tools
