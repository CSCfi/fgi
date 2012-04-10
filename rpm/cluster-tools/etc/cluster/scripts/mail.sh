#!/bin/bash

#Set mail address forwarding, uncomment both lines and change email address 
#echo "root:          cluster-support@university.fi" >> /etc/aliases
#newaliases

#Set a smarthost, if you need one
#echo "relayhost = smtp.university.fi" >> /etc/postfix/main.cf

#By default, yum mails nightly from nodes after an update. You can reduce the mails by uncommenting one of the following
#Only warn on yum failures
#sed -i -e 's/SENDONLYERRORS="false"/SENDONLYERRORS="true"/' /etc/sysconfig/yum-autoupdate
#Or disable yum notifications completely
#sed -i -e 's/SENDMAIL="true"/SENDMAIL="false"/' /etc/sysconfig/yum-autoupdate
