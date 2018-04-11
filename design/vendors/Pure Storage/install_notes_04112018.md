# Install Notes April 11 2018

The engineer (Ken Tran) said M10 now supports up tp 20 TB so we could theoretically fully populate the unit as it has 10 x 1 TB drives right now. Asked for a quote from Microway 
(they are working on becoming a reseller for Pure Storage so that we can use them for all equipment).

The following IPs/DNS names were provisioned by Chims:

1) 10.38.0.4 - pom-itb-pure-mgt00 - 1st controller's eth0 (physical interface, MAC 24:a9:37:01:c0:6e)

2) 10.38.0.5 - pom-itb-pure-mgt10 - 2nd controller's eth0 (physical interface, MAC 24:a9:37:01:30:40)

3) 10.38.0.6 - pom-itb-pure-mgtv0 - virtual IP (virtual interface)

Subnet /16 (224)

DNS Subdomain .hpc.pomona.edu

NTP ntp.pomona.edu

SMTP relay.pomona.edu


