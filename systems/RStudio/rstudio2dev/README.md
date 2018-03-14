# This is a page for tracking changes on rstudio2dev - the RStudio test server

Log in on March 13 2018:

```
ABRT has detected 1 problem(s). For more info run: abrt-cli list --since 1518736328
```

```
[root@rstudio2dev ~]# abrt-cli list --since 1518736328
id c922b8d5cb92183b1c2730438294eb70db33b49d
reason:         WARNING: at net/sched/sch_generic.c:297 dev_watchdog+0x276/0x280()
time:           Mon 02 Oct 2017 10:18:42 PM PDT
cmdline:        BOOT_IMAGE=/vmlinuz-3.10.0-514.26.2.el7.x86_64 root=/dev/mapper/vg00-root ro crashkernel=auto rd.lvm.lv=vg00/root rd.lvm.lv=vg00/swap quiet LANG=en_US.UTF-8
package:        kernel
uid:            0 (root)
count:          8
Directory:      /var/spool/abrt/oops-2017-10-02-22:18:42-25220-0


The Autoreporting feature is disabled. Please consider enabling it by issuing
'abrt-auto-reporting enabled' as a user with root privileges
```

## March 13 2018 update: Samba version check and patching according to https://thehackernews.com/2018/03/samba-server-vulnerability.html

```
samba-libs-4.6.2-12.el7_4.x86_64
samba-winbind-modules-4.6.2-12.el7_4.x86_64
samba-client-4.6.2-12.el7_4.x86_64
samba-common-4.6.2-12.el7_4.noarch
samba-winbind-4.6.2-12.el7_4.x86_64
samba-common-libs-4.6.2-12.el7_4.x86_64
samba-winbind-krb5-locator-4.6.2-12.el7_4.x86_64
samba-common-tools-4.6.2-12.el7_4.x86_64
samba-winbind-clients-4.6.2-12.el7_4.x86_64
samba-client-libs-4.6.2-12.el7_4.x86_64
```

```
[root@rstudio2dev ~]# yum update samba*
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirror.san.fastserv.com
 * epel: mirror.hmc.edu
 * extras: mirror.hostduplex.com
 * updates: centos-distro.cavecreek.net
No packages marked for update
```

```
[root@rstudio2dev ~]# wget https://www.samba.org/samba/ftp/patches/security/samba-4.6.13-security-2018-03-13.patch
--2018-03-13 18:57:17--  https://www.samba.org/samba/ftp/patches/security/samba-4.6.13-security-2018-03-13.patch
Resolving www.samba.org (www.samba.org)... 144.76.82.156, 2a01:4f8:192:486::443:2
Connecting to www.samba.org (www.samba.org)|144.76.82.156|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://download.samba.org/pub/samba/patches/security/samba-4.6.13-security-2018-03-13.patch [following]
--2018-03-13 18:57:18--  https://download.samba.org/pub/samba/patches/security/samba-4.6.13-security-2018-03-13.patch
Resolving download.samba.org (download.samba.org)... 144.76.82.156, 2a01:4f8:192:486::443:2
Connecting to download.samba.org (download.samba.org)|144.76.82.156|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34230 (33K) [text/x-diff]
Saving to: ‘samba-4.6.13-security-2018-03-13.patch’

100%[======================================>] 34,230       161KB/s   in 0.2s   

2018-03-13 18:57:19 (161 KB/s) - ‘samba-4.6.13-security-2018-03-13.patch’ saved [34230/34230]
```

The server is not running any Sambra services and does not have any external mounts.
