# This page is for tracking system changes on rstudio2

## March 13 2018 update: Samba version check and patching according to https://thehackernews.com/2018/03/samba-server-vulnerability.html

```
samba-common-4.4.4-14.el7_3.noarch
samba-libs-4.4.4-14.el7_3.x86_64
samba-winbind-krb5-locator-4.4.4-14.el7_3.x86_64
samba-common-tools-4.4.4-14.el7_3.x86_64
samba-winbind-modules-4.4.4-14.el7_3.x86_64
samba-client-libs-4.4.4-14.el7_3.x86_64
samba-client-4.4.4-14.el7_3.x86_64
samba-winbind-clients-4.4.4-14.el7_3.x86_64
samba-winbind-4.4.4-14.el7_3.x86_64
samba-common-libs-4.4.4-14.el7_3.x86_64
```

```
[root@rstudio2 asaj2017]# yum update samba*
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirrors.usc.edu
 * epel: mirror.hmc.edu
 * extras: mirrors.unifiedlayer.com
 * updates: mirror.hmc.edu
Resolving Dependencies
--> Running transaction check
---> Package samba-client.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-client.x86_64 0:4.6.2-12.el7_4 will be an update
--> Processing Dependency: libsmbclient = 4.6.2-12.el7_4 for package: samba-client-4.6.2-12.el7_4.x86_64
---> Package samba-client-libs.x86_64 0:4.4.4-14.el7_3 will be updated
--> Processing Dependency: samba-client-libs = 4.4.4-14.el7_3 for package: libwbclient-4.4.4-14.el7_3.x86_64
--> Processing Dependency: libreplace-samba4.so(SAMBA_4.4.4)(64bit) for package: libwbclient-4.4.4-14.el7_3.x86_64
---> Package samba-client-libs.x86_64 0:4.6.2-12.el7_4 will be an update
--> Processing Dependency: krb5-libs >= 1.15.1 for package: samba-client-libs-4.6.2-12.el7_4.x86_64
--> Processing Dependency: libtevent.so.0(TEVENT_0.9.31)(64bit) for package: samba-client-libs-4.6.2-12.el7_4.x86_64
--> Processing Dependency: libtevent.so.0(TEVENT_0.9.30)(64bit) for package: samba-client-libs-4.6.2-12.el7_4.x86_64
--> Processing Dependency: libtdb.so.1(TDB_1.3.11)(64bit) for package: samba-client-libs-4.6.2-12.el7_4.x86_64
---> Package samba-common.noarch 0:4.4.4-14.el7_3 will be updated
---> Package samba-common.noarch 0:4.6.2-12.el7_4 will be an update
---> Package samba-common-libs.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-common-libs.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package samba-common-tools.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-common-tools.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package samba-libs.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-libs.x86_64 0:4.6.2-12.el7_4 will be an update
--> Processing Dependency: libpytalloc-util.so.2(PYTALLOC_UTIL_2.1.9)(64bit) for package: samba-libs-4.6.2-12.el7_4.x86_64
---> Package samba-winbind.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-winbind.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package samba-winbind-clients.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-winbind-clients.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package samba-winbind-krb5-locator.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-winbind-krb5-locator.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package samba-winbind-modules.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package samba-winbind-modules.x86_64 0:4.6.2-12.el7_4 will be an update
--> Running transaction check
---> Package krb5-libs.x86_64 0:1.14.1-27.el7_3 will be updated
--> Processing Dependency: krb5-libs(x86-64) = 1.14.1-27.el7_3 for package: libkadm5-1.14.1-27.el7_3.x86_64
--> Processing Dependency: krb5-libs(x86-64) = 1.14.1-27.el7_3 for package: krb5-workstation-1.14.1-27.el7_3.x86_64
--> Processing Dependency: krb5-libs(x86-64) = 1.14.1-27.el7_3 for package: krb5-devel-1.14.1-27.el7_3.x86_64
---> Package krb5-libs.x86_64 0:1.15.1-8.el7 will be an update
---> Package libsmbclient.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package libsmbclient.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package libtdb.x86_64 0:1.3.8-1.el7_2 will be updated
---> Package libtdb.x86_64 0:1.3.12-2.el7 will be an update
---> Package libtevent.x86_64 0:0.9.28-1.el7 will be updated
---> Package libtevent.x86_64 0:0.9.31-2.el7_4 will be an update
---> Package libwbclient.x86_64 0:4.4.4-14.el7_3 will be updated
---> Package libwbclient.x86_64 0:4.6.2-12.el7_4 will be an update
---> Package pytalloc.x86_64 0:2.1.6-1.el7 will be updated
---> Package pytalloc.x86_64 0:2.1.9-1.el7 will be an update
--> Processing Dependency: libtalloc = 2.1.9-1.el7 for package: pytalloc-2.1.9-1.el7.x86_64
--> Running transaction check
---> Package krb5-devel.x86_64 0:1.14.1-27.el7_3 will be updated
---> Package krb5-devel.x86_64 0:1.15.1-8.el7 will be an update
---> Package krb5-workstation.x86_64 0:1.14.1-27.el7_3 will be updated
---> Package krb5-workstation.x86_64 0:1.15.1-8.el7 will be an update
---> Package libkadm5.x86_64 0:1.14.1-27.el7_3 will be updated
---> Package libkadm5.x86_64 0:1.15.1-8.el7 will be an update
---> Package libtalloc.x86_64 0:2.1.6-1.el7 will be updated
---> Package libtalloc.x86_64 0:2.1.9-1.el7 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                        Arch       Version            Repository   Size
================================================================================
Updating:
 samba-client                   x86_64     4.6.2-12.el7_4     updates     598 k
 samba-client-libs              x86_64     4.6.2-12.el7_4     updates     4.7 M
 samba-common                   noarch     4.6.2-12.el7_4     updates     197 k
 samba-common-libs              x86_64     4.6.2-12.el7_4     updates     164 k
 samba-common-tools             x86_64     4.6.2-12.el7_4     updates     456 k
 samba-libs                     x86_64     4.6.2-12.el7_4     updates     265 k
 samba-winbind                  x86_64     4.6.2-12.el7_4     updates     516 k
 samba-winbind-clients          x86_64     4.6.2-12.el7_4     updates     129 k
 samba-winbind-krb5-locator     x86_64     4.6.2-12.el7_4     updates      83 k
 samba-winbind-modules          x86_64     4.6.2-12.el7_4     updates     111 k
Updating for dependencies:
 krb5-devel                     x86_64     1.15.1-8.el7       base        266 k
 krb5-libs                      x86_64     1.15.1-8.el7       base        747 k
 krb5-workstation               x86_64     1.15.1-8.el7       base        811 k
 libkadm5                       x86_64     1.15.1-8.el7       base        174 k
 libsmbclient                   x86_64     4.6.2-12.el7_4     updates     130 k
 libtalloc                      x86_64     2.1.9-1.el7        base         33 k
 libtdb                         x86_64     1.3.12-2.el7       base         47 k
 libtevent                      x86_64     0.9.31-2.el7_4     updates      36 k
 libwbclient                    x86_64     4.6.2-12.el7_4     updates     104 k
 pytalloc                       x86_64     2.1.9-1.el7        base         16 k

Transaction Summary
================================================================================
Upgrade  10 Packages (+10 Dependent packages)

Total size: 9.5 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : libtalloc-2.1.9-1.el7.x86_64                                1/40 
  Updating   : libtevent-0.9.31-2.el7_4.x86_64                             2/40 
  Updating   : krb5-libs-1.15.1-8.el7.x86_64                               3/40 
  Updating   : samba-common-4.6.2-12.el7_4.noarch                          4/40 
  Updating   : libtdb-1.3.12-2.el7.x86_64                                  5/40 
  Updating   : libwbclient-4.6.2-12.el7_4.x86_64                           6/40 
  Updating   : samba-client-libs-4.6.2-12.el7_4.x86_64                     7/40 
  Updating   : samba-common-libs-4.6.2-12.el7_4.x86_64                     8/40 
  Updating   : libkadm5-1.15.1-8.el7.x86_64                                9/40 
  Updating   : libsmbclient-4.6.2-12.el7_4.x86_64                         10/40 
  Updating   : pytalloc-2.1.9-1.el7.x86_64                                11/40 
  Updating   : samba-libs-4.6.2-12.el7_4.x86_64                           12/40 
  Updating   : samba-common-tools-4.6.2-12.el7_4.x86_64                   13/40 
  Updating   : samba-winbind-modules-4.6.2-12.el7_4.x86_64                14/40 
  Updating   : samba-winbind-4.6.2-12.el7_4.x86_64                        15/40 
  Updating   : samba-winbind-krb5-locator-4.6.2-12.el7_4.x86_64           16/40 
  Updating   : samba-winbind-clients-4.6.2-12.el7_4.x86_64                17/40 
  Updating   : samba-client-4.6.2-12.el7_4.x86_64                         18/40 
  Updating   : krb5-workstation-1.15.1-8.el7.x86_64                       19/40 
  Updating   : krb5-devel-1.15.1-8.el7.x86_64                             20/40 
  Cleanup    : samba-client-4.4.4-14.el7_3.x86_64                         21/40 
  Cleanup    : samba-winbind-clients-4.4.4-14.el7_3.x86_64                22/40 
  Cleanup    : libsmbclient-4.4.4-14.el7_3.x86_64                         23/40 
  Cleanup    : samba-winbind-krb5-locator-4.4.4-14.el7_3.x86_64           24/40 
  Cleanup    : samba-winbind-4.4.4-14.el7_3.x86_64                        25/40 
  Cleanup    : samba-common-tools-4.4.4-14.el7_3.x86_64                   26/40 
  Cleanup    : samba-common-libs-4.4.4-14.el7_3.x86_64                    27/40 
  Cleanup    : samba-winbind-modules-4.4.4-14.el7_3.x86_64                28/40 
  Cleanup    : samba-libs-4.4.4-14.el7_3.x86_64                           29/40 
  Cleanup    : libwbclient-4.4.4-14.el7_3.x86_64                          30/40 
  Cleanup    : samba-client-libs-4.4.4-14.el7_3.x86_64                    31/40 
  Cleanup    : krb5-devel-1.14.1-27.el7_3.x86_64                          32/40 
  Cleanup    : krb5-workstation-1.14.1-27.el7_3.x86_64                    33/40 
  Cleanup    : libkadm5-1.14.1-27.el7_3.x86_64                            34/40 
  Cleanup    : libtevent-0.9.28-1.el7.x86_64                              35/40 
  Cleanup    : pytalloc-2.1.6-1.el7.x86_64                                36/40 
  Cleanup    : samba-common-4.4.4-14.el7_3.noarch                         37/40 
  Cleanup    : libtalloc-2.1.6-1.el7.x86_64                               38/40 
  Cleanup    : krb5-libs-1.14.1-27.el7_3.x86_64                           39/40 
  Cleanup    : libtdb-1.3.8-1.el7_2.x86_64                                40/40 
  Verifying  : samba-common-libs-4.6.2-12.el7_4.x86_64                     1/40 
  Verifying  : samba-client-4.6.2-12.el7_4.x86_64                          2/40 
  Verifying  : libtevent-0.9.31-2.el7_4.x86_64                             3/40 
  Verifying  : libkadm5-1.15.1-8.el7.x86_64                                4/40 
  Verifying  : samba-common-tools-4.6.2-12.el7_4.x86_64                    5/40 
  Verifying  : samba-common-4.6.2-12.el7_4.noarch                          6/40 
  Verifying  : libwbclient-4.6.2-12.el7_4.x86_64                           7/40 
  Verifying  : libtalloc-2.1.9-1.el7.x86_64                                8/40 
  Verifying  : samba-winbind-krb5-locator-4.6.2-12.el7_4.x86_64            9/40 
  Verifying  : samba-winbind-4.6.2-12.el7_4.x86_64                        10/40 
  Verifying  : samba-winbind-clients-4.6.2-12.el7_4.x86_64                11/40 
  Verifying  : pytalloc-2.1.9-1.el7.x86_64                                12/40 
  Verifying  : samba-winbind-modules-4.6.2-12.el7_4.x86_64                13/40 
  Verifying  : krb5-workstation-1.15.1-8.el7.x86_64                       14/40 
  Verifying  : samba-libs-4.6.2-12.el7_4.x86_64                           15/40 
  Verifying  : krb5-devel-1.15.1-8.el7.x86_64                             16/40 
  Verifying  : krb5-libs-1.15.1-8.el7.x86_64                              17/40 
  Verifying  : libsmbclient-4.6.2-12.el7_4.x86_64                         18/40 
  Verifying  : libtdb-1.3.12-2.el7.x86_64                                 19/40 
  Verifying  : samba-client-libs-4.6.2-12.el7_4.x86_64                    20/40 
  Verifying  : samba-winbind-4.4.4-14.el7_3.x86_64                        21/40 
  Verifying  : libkadm5-1.14.1-27.el7_3.x86_64                            22/40 
  Verifying  : samba-common-libs-4.4.4-14.el7_3.x86_64                    23/40 
  Verifying  : samba-common-tools-4.4.4-14.el7_3.x86_64                   24/40 
  Verifying  : libtdb-1.3.8-1.el7_2.x86_64                                25/40 
  Verifying  : samba-winbind-clients-4.4.4-14.el7_3.x86_64                26/40 
  Verifying  : samba-client-4.4.4-14.el7_3.x86_64                         27/40 
  Verifying  : krb5-libs-1.14.1-27.el7_3.x86_64                           28/40 
  Verifying  : pytalloc-2.1.6-1.el7.x86_64                                29/40 
  Verifying  : samba-libs-4.4.4-14.el7_3.x86_64                           30/40 
  Verifying  : samba-common-4.4.4-14.el7_3.noarch                         31/40 
  Verifying  : krb5-workstation-1.14.1-27.el7_3.x86_64                    32/40 
  Verifying  : samba-winbind-modules-4.4.4-14.el7_3.x86_64                33/40 
  Verifying  : libsmbclient-4.4.4-14.el7_3.x86_64                         34/40 
  Verifying  : libtevent-0.9.28-1.el7.x86_64                              35/40 
  Verifying  : samba-client-libs-4.4.4-14.el7_3.x86_64                    36/40 
  Verifying  : libwbclient-4.4.4-14.el7_3.x86_64                          37/40 
  Verifying  : krb5-devel-1.14.1-27.el7_3.x86_64                          38/40 
  Verifying  : libtalloc-2.1.6-1.el7.x86_64                               39/40 
  Verifying  : samba-winbind-krb5-locator-4.4.4-14.el7_3.x86_64           40/40 

Updated:
  samba-client.x86_64 0:4.6.2-12.el7_4                                          
  samba-client-libs.x86_64 0:4.6.2-12.el7_4                                     
  samba-common.noarch 0:4.6.2-12.el7_4                                          
  samba-common-libs.x86_64 0:4.6.2-12.el7_4                                     
  samba-common-tools.x86_64 0:4.6.2-12.el7_4                                    
  samba-libs.x86_64 0:4.6.2-12.el7_4                                            
  samba-winbind.x86_64 0:4.6.2-12.el7_4                                         
  samba-winbind-clients.x86_64 0:4.6.2-12.el7_4                                 
  samba-winbind-krb5-locator.x86_64 0:4.6.2-12.el7_4                            
  samba-winbind-modules.x86_64 0:4.6.2-12.el7_4                                 

Dependency Updated:
  krb5-devel.x86_64 0:1.15.1-8.el7          krb5-libs.x86_64 0:1.15.1-8.el7     
  krb5-workstation.x86_64 0:1.15.1-8.el7    libkadm5.x86_64 0:1.15.1-8.el7      
  libsmbclient.x86_64 0:4.6.2-12.el7_4      libtalloc.x86_64 0:2.1.9-1.el7      
  libtdb.x86_64 0:1.3.12-2.el7              libtevent.x86_64 0:0.9.31-2.el7_4   
  libwbclient.x86_64 0:4.6.2-12.el7_4       pytalloc.x86_64 0:2.1.9-1.el7       

Complete!
```

```
samba-libs-4.6.2-12.el7_4.x86_64
samba-winbind-4.6.2-12.el7_4.x86_64
samba-client-4.6.2-12.el7_4.x86_64
samba-common-libs-4.6.2-12.el7_4.x86_64
samba-winbind-krb5-locator-4.6.2-12.el7_4.x86_64
samba-winbind-modules-4.6.2-12.el7_4.x86_64
samba-winbind-clients-4.6.2-12.el7_4.x86_64
samba-common-4.6.2-12.el7_4.noarch
samba-client-libs-4.6.2-12.el7_4.x86_64
samba-common-tools-4.6.2-12.el7_4.x86_64
```

The system is not running any samba services and does not have any external mounts.
