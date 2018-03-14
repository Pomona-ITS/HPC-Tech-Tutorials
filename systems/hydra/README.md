# This page is for tracking updates to hydra - a teaching server in Biology hosted by ITS

More information about the server is [here](https://github.com/Pomona-ITS/hpc/blob/0bade9fcc07f80f644ac345d5bbd3d1fe3f86a85/discovery/biology/hydra.pomona.edu.md).

## March 13 2018 update: Samba version check and patching according to https://thehackernews.com/2018/03/samba-server-vulnerability.html

```
samba-winbind-3.6.23-24.el6_7.x86_64
samba4-libs-4.0.0-67.el6_7.rc4.x86_64
samba-common-3.6.23-24.el6_7.x86_64
samba-client-3.6.23-24.el6_7.x86_64
samba-winbind-clients-3.6.23-24.el6_7.x86_64
```

```
[root@hydra asaj2017]# yum update samba*
Loaded plugins: fastestmirror, security
Setting up Update Process
Determining fastest mirrors
epel/metalink                                            |  15 kB     00:00     
 * base: centos-distro.1gservers.com
 * epel: mirror.hmc.edu
 * extras: mirror.scalabledns.com
 * updates: mirror.sjc02.svwh.net
base                                                     | 3.7 kB     00:00     
epel                                                     | 4.7 kB     00:00     
epel/primary_db                                          | 6.0 MB     00:00     
extras                                                   | 3.4 kB     00:00     
testing-1.1-devtools-6                                   |  951 B     00:00     
updates                                                  | 3.4 kB     00:00     
updates/primary_db                                       | 6.4 MB     00:00     
virtualbox                                               | 1.1 kB     00:00     
virtualbox/primary                                       |  13 kB     00:00     
virtualbox                                                                64/64
Resolving Dependencies
--> Running transaction check
---> Package samba-client.x86_64 0:3.6.23-24.el6_7 will be updated
---> Package samba-client.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-common.x86_64 0:3.6.23-24.el6_7 will be updated
---> Package samba-common.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-winbind.x86_64 0:3.6.23-24.el6_7 will be updated
---> Package samba-winbind.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba-winbind-clients.x86_64 0:3.6.23-24.el6_7 will be updated
--> Processing Dependency: samba-winbind-clients = 3.6.23-24.el6_7 for package: libsmbclient-3.6.23-24.el6_7.x86_64
---> Package samba-winbind-clients.x86_64 0:3.6.23-46el6_9 will be an update
---> Package samba4-libs.x86_64 0:4.0.0-67.el6_7.rc4 will be updated
---> Package samba4-libs.x86_64 0:4.2.10-12.el6_9 will be an update
--> Processing Dependency: libtevent.so.0(TEVENT_0.9.21)(64bit) for package: samba4-libs-4.2.10-12.el6_9.x86_64
--> Processing Dependency: libtevent.so.0(TEVENT_0.9.20)(64bit) for package: samba4-libs-4.2.10-12.el6_9.x86_64
--> Processing Dependency: libtdb.so.1(TDB_1.3.0)(64bit) for package: samba4-libs-4.2.10-12.el6_9.x86_64
--> Processing Dependency: libtalloc.so.2(TALLOC_2.1.0)(64bit) for package: samba4-libs-4.2.10-12.el6_9.x86_64
--> Running transaction check
---> Package libsmbclient.x86_64 0:3.6.23-24.el6_7 will be updated
---> Package libsmbclient.x86_64 0:3.6.23-46el6_9 will be an update
---> Package libtalloc.x86_64 0:2.0.7-2.el6 will be updated
--> Processing Dependency: libtalloc = 2.0.7-2.el6 for package: pytalloc-2.0.7-2.el6.x86_64
---> Package libtalloc.x86_64 0:2.1.5-1.el6_7 will be an update
---> Package libtdb.x86_64 0:1.2.10-1.el6 will be updated
---> Package libtdb.x86_64 0:1.3.8-3.el6_8.2 will be an update
---> Package libtevent.x86_64 0:0.9.18-3.el6 will be updated
---> Package libtevent.x86_64 0:0.9.26-2.el6_7 will be an update
--> Running transaction check
---> Package pytalloc.x86_64 0:2.0.7-2.el6 will be obsoleted
---> Package pytalloc.x86_64 0:2.0.7-2.el6 will be updated
---> Package pytalloc.x86_64 0:2.1.5-1.el6_7 will be obsoleting
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                    Arch        Version              Repository    Size
================================================================================
Installing:
 pytalloc                   x86_64      2.1.5-1.el6_7        base          10 k
     replacing  pytalloc.x86_64 2.0.7-2.el6
Updating:
 samba-client               x86_64      3.6.23-46el6_9       updates       11 M
 samba-common               x86_64      3.6.23-46el6_9       updates       10 M
 samba-winbind              x86_64      3.6.23-46el6_9       updates      2.2 M
 samba-winbind-clients      x86_64      3.6.23-46el6_9       updates      2.0 M
 samba4-libs                x86_64      4.2.10-12.el6_9      updates      4.4 M
Updating for dependencies:
 libsmbclient               x86_64      3.6.23-46el6_9       updates      1.6 M
 libtalloc                  x86_64      2.1.5-1.el6_7        base          26 k
 libtdb                     x86_64      1.3.8-3.el6_8.2      base          40 k
 libtevent                  x86_64      0.9.26-2.el6_7       base          29 k

Transaction Summary
================================================================================
Install       1 Package(s)
Upgrade       9 Package(s)

Total download size: 31 M
Is this ok [y/N]: y
Downloading Packages:
(1/10): libsmbclient-3.6.23-46el6_9.x86_64.rpm           | 1.6 MB     00:00     
(2/10): libtalloc-2.1.5-1.el6_7.x86_64.rpm               |  26 kB     00:00     
(3/10): libtdb-1.3.8-3.el6_8.2.x86_64.rpm                |  40 kB     00:00     
(4/10): libtevent-0.9.26-2.el6_7.x86_64.rpm              |  29 kB     00:00     
(5/10): pytalloc-2.1.5-1.el6_7.x86_64.rpm                |  10 kB     00:00     
(6/10): samba-client-3.6.23-46el6_9.x86_64.rpm           |  11 MB     00:00     
(7/10): samba-common-3.6.23-46el6_9.x86_64.rpm           |  10 MB     00:00     
(8/10): samba-winbind-3.6.23-46el6_9.x86_64.rpm          | 2.2 MB     00:00     
(9/10): samba-winbind-clients-3.6.23-46el6_9.x86_64.rpm  | 2.0 MB     00:00     
(10/10): samba4-libs-4.2.10-12.el6_9.x86_64.rpm          | 4.4 MB     00:00     
--------------------------------------------------------------------------------
Total                                           416 kB/s |  31 MB     01:17     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Updating   : libtalloc-2.1.5-1.el6_7.x86_64                              1/20 
  Updating   : libtevent-0.9.26-2.el6_7.x86_64                             2/20 
  Updating   : libtdb-1.3.8-3.el6_8.2.x86_64                               3/20 
  Updating   : samba-common-3.6.23-46el6_9.x86_64                          4/20 
  Updating   : samba-winbind-3.6.23-46el6_9.x86_64                         5/20 
  Updating   : samba-winbind-clients-3.6.23-46el6_9.x86_64                 6/20 
  Installing : pytalloc-2.1.5-1.el6_7.x86_64                               7/20 
  Updating   : samba4-libs-4.2.10-12.el6_9.x86_64                          8/20 
  Updating   : libsmbclient-3.6.23-46el6_9.x86_64                          9/20 
  Updating   : samba-client-3.6.23-46el6_9.x86_64                         10/20 
  Cleanup    : samba-client-3.6.23-24.el6_7.x86_64                        11/20 
  Cleanup    : samba4-libs-4.0.0-67.el6_7.rc4.x86_64                      12/20 
  Cleanup    : libsmbclient-3.6.23-24.el6_7.x86_64                        13/20 
  Cleanup    : samba-common-3.6.23-24.el6_7.x86_64                        14/20 
  Cleanup    : samba-winbind-3.6.23-24.el6_7.x86_64                       15/20 
  Cleanup    : samba-winbind-clients-3.6.23-24.el6_7.x86_64               16/20 
  Cleanup    : libtevent-0.9.18-3.el6.x86_64                              17/20 
  Cleanup    : pytalloc-2.0.7-2.el6.x86_64                                18/20 
  Cleanup    : libtalloc-2.0.7-2.el6.x86_64                               19/20 
  Cleanup    : libtdb-1.2.10-1.el6.x86_64                                 20/20 
  Verifying  : samba-winbind-clients-3.6.23-46el6_9.x86_64                 1/20 
  Verifying  : libtalloc-2.1.5-1.el6_7.x86_64                              2/20 
  Verifying  : libtevent-0.9.26-2.el6_7.x86_64                             3/20 
  Verifying  : samba-common-3.6.23-46el6_9.x86_64                          4/20 
  Verifying  : libsmbclient-3.6.23-46el6_9.x86_64                          5/20 
  Verifying  : libtdb-1.3.8-3.el6_8.2.x86_64                               6/20 
  Verifying  : samba-client-3.6.23-46el6_9.x86_64                          7/20 
  Verifying  : samba-winbind-3.6.23-46el6_9.x86_64                         8/20 
  Verifying  : samba4-libs-4.2.10-12.el6_9.x86_64                          9/20 
  Verifying  : pytalloc-2.1.5-1.el6_7.x86_64                              10/20 
  Verifying  : samba-winbind-clients-3.6.23-24.el6_7.x86_64               11/20 
  Verifying  : libtalloc-2.0.7-2.el6.x86_64                               12/20 
  Verifying  : samba-winbind-3.6.23-24.el6_7.x86_64                       13/20 
  Verifying  : samba-common-3.6.23-24.el6_7.x86_64                        14/20 
  Verifying  : libtdb-1.2.10-1.el6.x86_64                                 15/20 
  Verifying  : libtevent-0.9.18-3.el6.x86_64                              16/20 
  Verifying  : libsmbclient-3.6.23-24.el6_7.x86_64                        17/20 
  Verifying  : samba-client-3.6.23-24.el6_7.x86_64                        18/20 
  Verifying  : samba4-libs-4.0.0-67.el6_7.rc4.x86_64                      19/20 
  Verifying  : pytalloc-2.0.7-2.el6.x86_64                                20/20 
  Verifying  : pytalloc-2.0.7-2.el6.x86_64                                21/20 

Installed:
  pytalloc.x86_64 0:2.1.5-1.el6_7                                               

Updated:
  samba-client.x86_64 0:3.6.23-46el6_9                                          
  samba-common.x86_64 0:3.6.23-46el6_9                                          
  samba-winbind.x86_64 0:3.6.23-46el6_9                                         
  samba-winbind-clients.x86_64 0:3.6.23-46el6_9                                 
  samba4-libs.x86_64 0:4.2.10-12.el6_9                                          

Dependency Updated:
  libsmbclient.x86_64 0:3.6.23-46el6_9     libtalloc.x86_64 0:2.1.5-1.el6_7     
  libtdb.x86_64 0:1.3.8-3.el6_8.2          libtevent.x86_64 0:0.9.26-2.el6_7    

Replaced:
  pytalloc.x86_64 0:2.0.7-2.el6                                                 

Complete!
```

```
samba4-libs-4.2.10-12.el6_9.x86_64
samba-winbind-3.6.23-46el6_9.x86_64
samba-winbind-clients-3.6.23-46el6_9.x86_64
samba-common-3.6.23-46el6_9.x86_64
samba-client-3.6.23-46el6_9.x86_64
```

The system is not running any samba services and does not have any external mounts.
