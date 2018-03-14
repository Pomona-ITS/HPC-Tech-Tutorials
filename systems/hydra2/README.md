# This page is for tracking updates to hydra2 - a student server in Biology hosted by ITS

More information about the server is [here](https://github.com/Pomona-ITS/hpc/blob/0bade9fcc07f80f644ac345d5bbd3d1fe3f86a85/discovery/biology/hydra2.pomona.edu.md).

## March 13 2018 update: Samba version check and patching according to https://thehackernews.com/2018/03/samba-server-vulnerability.html

```
samba-winbind-3.6.23-35.el6_8.x86_64
samba4-libs-4.2.10-6.el6_7.x86_64  - different from hydra
samba-winbind-clients-3.6.23-35.el6_8.x86_64
samba-client-3.6.23-35.el6_8.x86_64
samba-common-3.6.23-35.el6_8.x86_64
```

```
[root@hydra2 asaj2017]# yum update samba*
Loaded plugins: fastestmirror, refresh-packagekit, security
Setting up Update Process
Loading mirror speeds from cached hostfile
epel/metalink                                            |  15 kB     00:00     
 * base: centos-distro.1gservers.com
 * epel: mirror.prgmr.com
 * extras: mirror.scalabledns.com
 * updates: mirrors.mit.edu
base                                                     | 3.7 kB     00:00     
epel                                                     | 4.7 kB     00:00     
epel/primary_db                                          | 6.0 MB     00:00     
extras                                                   | 3.4 kB     00:00     
testing-1.1-devtools-6                                   |  951 B     00:00     
updates                                                  | 3.4 kB     00:00     
Resolving Dependencies
--> Running transaction check
---> Package samba-client.x86_64 0:3.6.23-35.el6_8 will be updated
---> Package samba-client.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-common.x86_64 0:3.6.23-35.el6_8 will be updated
---> Package samba-common.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-winbind.x86_64 0:3.6.23-35.el6_8 will be updated
---> Package samba-winbind.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-winbind-clients.x86_64 0:3.6.23-35.el6_8 will be updated
--> Processing Dependency: samba-winbind-clients = 3.6.23-35.el6_8 for package: libsmbclient-3.6.23-35.el6_8.x86_64
---> Package samba-winbind-clients.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba4-libs.x86_64 0:4.2.10-6.el6_7 will be updated
---> Package samba4-libs.x86_64 0:4.2.10-12.el6_9 will be an update
--> Running transaction check
---> Package libsmbclient.x86_64 0:3.6.23-35.el6_8 will be updated
---> Package libsmbclient.x86_64 0:3.6.23-46el6_9 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                    Arch        Version              Repository    Size
================================================================================
Updating:
 samba-client               x86_64      3.6.23-46el6_9       updates       11 M
 samba-common               x86_64      3.6.23-46el6_9       updates       10 M
 samba-winbind              x86_64      3.6.23-46el6_9       updates      2.2 M
 samba-winbind-clients      x86_64      3.6.23-46el6_9       updates      2.0 M
 samba4-libs                x86_64      4.2.10-12.el6_9      updates      4.4 M
Updating for dependencies:
 libsmbclient               x86_64      3.6.23-46el6_9       updates      1.6 M

Transaction Summary
================================================================================
Upgrade       6 Package(s)

Total download size: 31 M
Is this ok [y/N]: y
Downloading Packages:
(1/6): libsmbclient-3.6.23-46el6_9.x86_64.rpm            | 1.6 MB     00:01     
(2/6): samba-client-3.6.23-46el6_9.x86_64.rpm            |  11 MB     00:00     
(3/6): samba-common-3.6.23-46el6_9.x86_64.rpm            |  10 MB     00:00     
(4/6): samba-winbind-3.6.23-46el6_9.x86_64.rpm           | 2.2 MB     00:00     
(5/6): samba-winbind-clients-3.6.23-46el6_9.x86_64.rpm   | 2.0 MB     00:00     
(6/6): samba4-libs-4.2.10-12.el6_9.x86_64.rpm            | 4.4 MB     00:00     
--------------------------------------------------------------------------------
Total                                           9.6 MB/s |  31 MB     00:03     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Updating   : samba-common-3.6.23-46el6_9.x86_64                          1/12 
  Updating   : samba-winbind-3.6.23-46el6_9.x86_64                         2/12 
  Updating   : samba-winbind-clients-3.6.23-46el6_9.x86_64                 3/12 
  Updating   : samba-client-3.6.23-46el6_9.x86_64                          4/12 
  Updating   : libsmbclient-3.6.23-46el6_9.x86_64                          5/12 
  Updating   : samba4-libs-4.2.10-12.el6_9.x86_64                          6/12 
  Cleanup    : samba-client-3.6.23-35.el6_8.x86_64                         7/12 
  Cleanup    : libsmbclient-3.6.23-35.el6_8.x86_64                         8/12 
  Cleanup    : samba4-libs-4.2.10-6.el6_7.x86_64                           9/12 
  Cleanup    : samba-common-3.6.23-35.el6_8.x86_64                        10/12 
  Cleanup    : samba-winbind-3.6.23-35.el6_8.x86_64                       11/12 
  Cleanup    : samba-winbind-clients-3.6.23-35.el6_8.x86_64               12/12 
  Verifying  : samba-winbind-clients-3.6.23-46el6_9.x86_64                 1/12 
  Verifying  : samba-common-3.6.23-46el6_9.x86_64                          2/12 
  Verifying  : samba-client-3.6.23-46el6_9.x86_64                          3/12 
  Verifying  : libsmbclient-3.6.23-46el6_9.x86_64                          4/12 
  Verifying  : samba-winbind-3.6.23-46el6_9.x86_64                         5/12 
  Verifying  : samba4-libs-4.2.10-12.el6_9.x86_64                          6/12 
  Verifying  : samba-winbind-3.6.23-35.el6_8.x86_64                        7/12 
  Verifying  : samba-common-3.6.23-35.el6_8.x86_64                         8/12 
  Verifying  : samba-winbind-clients-3.6.23-35.el6_8.x86_64                9/12 
  Verifying  : samba4-libs-4.2.10-6.el6_7.x86_64                          10/12 
  Verifying  : libsmbclient-3.6.23-35.el6_8.x86_64                        11/12 
  Verifying  : samba-client-3.6.23-35.el6_8.x86_64                        12/12 

Updated:
  samba-client.x86_64 0:3.6.23-46el6_9                                          
  samba-common.x86_64 0:3.6.23-46el6_9                                          
  samba-winbind.x86_64 0:3.6.23-46el6_9                                         
  samba-winbind-clients.x86_64 0:3.6.23-46el6_9                                 
  samba4-libs.x86_64 0:4.2.10-12.el6_9                                          

Dependency Updated:
  libsmbclient.x86_64 0:3.6.23-46el6_9                                          

Complete!
```
