# This is the page for summarizing HPC authentication

All Pomona College Linux systems use [AD (Active Directory)](https://en.wikipedia.org/wiki/Active_Directory) authentication as soon as they are provisioned.

This involves several steps the last of which is "adcli join -v -U ad-admin-user" in which the ad-admin-user is the specific AD administrative username. This prompts for a password.

This results in the creation of /etc/krb5.keytab. To check that the process was successful verify that the keytab exists and the date is recent. 

If the system had already been joined to the domain and authentication is not working anymore (or there had been changes in the Active Directory that are not propagated to the keytab like adding new users or changing group memberships) the comman to update the system's record in AD is "adcli update -v". 

Testing authentication via "su - user" may not work because that does not engage PAM. It is best to test via "ssh hostname".

Other steps necessary for the above to work (which hopefully are all done as a part of provisioning e.g. a VM Template) are:

