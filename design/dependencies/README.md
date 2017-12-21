# This page is an attempt to capture the external HPC dependencies that make the infrastructure run smoother.

## AD-connected Linux authentication

Currently all the Linux users are created on local workstation without a centralized repository or synchronized UIDs.
This means the same user may not be able to log in to another system and introduced file permissions management overhead.
Ideally, all of the Linux systems should be provisioned with access to AD authnetication. Potentially using a third-party SSO.

## NFS (Linux) and CIFS (Windows) POSIX-compliant user-facing centralized network-attached storage for home directories

Currently the physical Linux workstations host home directories on local disk. This introduces challenges with 
moving data between different systems, risk of losing the data, permissions issues and scalability issues to name a few.
NetApp or Isilon is typically used in Linux/Windows environments and the home directories are NFS mounted. AutoFS is not
recommended (stale mounts etc). The same home directories can be mounted everywhere to prevent data copying and duplication.
CIFS license is needed for mounting on Windows.


## Software License Management

https://www.openlm.com/ is used for engineering software license management, especially [floating](https://en.wikipedia.org/wiki/Floating_licensing) licenses.

From Wikipedia:

"Floating licensing is a software licensing approach in which a limited number of licenses for a software application are shared among a larger number of users over time. When an authorized user wishes to run the application they request a license from a central license server. If a license is available the license server allows the application to run. When they finish using the application, or when the allowed license period expires, the license is reclaimed by the license server and made available to other authorized users.

The license server can manage licenses over a local area network, an intranet or virtual private network, or the Internet.

Floating licensing, also sometimes known as concurrent licensing or network licensing, is often used for high-value applications in corporate environments, such as electronic design automation or engineering tools."

## Password/Secret/Key/Credential/Certificate Management

https://lastpass.com/ is super-simple, and has a Chrome extension

Other password managers I have used in the past:

https://1password.com/
