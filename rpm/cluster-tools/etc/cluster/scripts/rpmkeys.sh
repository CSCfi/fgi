#!/bin/bash
for a in /etc/pki/rpm-gpg/*; do 
	rpm --import $a
done
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-elrepo.org
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-dawson
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-sl6
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CernVM
#rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CSC-GRID-2

