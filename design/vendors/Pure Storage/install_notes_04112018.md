# Install Notes April 11 2018

The engineer (Ken Tran) said M10 now supports up tp 20 TB so we could theoretically fully populate the unit as it has 10 x 1 TB drives right now. Asked for a quote from Microway 
(they are working on becoming a reseller for Pure Storage so that we can use them for all equipment).

The following IPs/DNS names were provisioned by Chims:

1) 10.38.0.4 - pom-itb-pure-mgt00 - 1st controller's eth0 (physical interface, MAC 24:a9:37:01:c0:6e)

2) 10.38.0.5 - pom-itb-pure-mgt10 - 2nd controller's eth0 (physical interface, MAC 24:a9:37:01:30:40)

3) 10.38.0.6 - pom-itb-pure-mgtv0 - virtual IP (virtual interface) - this needs to be accessible on the regular local enterprise network (and VPN). Web Interface for management.

Subnet /16 (224)

DNS Servers: 134.173.64.6 and 134.173.69.6

DNS Subdomain .hpc.pomona.edu

NTP ntp.pomona.edu

SMTP relay.pomona.edu

Latest Purity (OS) code version installed - 5.0.6

Access to Support Portal enabled post-config. Ken created a username on their SaaS cloud using my email address. Got access after getting an email and confirming the link.

Ken sent the User Guide.

Call Home/Log management not working yet. We need this for Pure to monitor the health of the system. Port 443 (SSL) from all 3 management IPs.

Replication IPs not needed yet. They are for multiple arrays.

Inquiring regarding adding 10 more 1 TB drives.

Still need 4 10 GB connections (iSCSI) to the Cisco switch to start testing with HPC VMs.
