This is the initial discovery of hydra.pomona.edu, The Teaching Server.

# Overview:

Server Name: hydra.pomona.edu

Model: PowerEdge R720

Service Tag: FFTW8Z1

Motherboard model: 0H5J4J

Motherboard SN: CN7016339N00KN

BIOS:

version: 2.0.19
date: 08/29/2013

CPU Info:

2 x Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz x 10 cores each with threads enabled for a total of 40 cores

RAM Info:

767GiB
32 GB DIMM DDR3 Synchronous 1333 MHz (0.8 ns) X 24

Networking:

Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe X 4

Storage:

PERC H710P

LVM

/dev/sda 100GiB
/dev/sdb 7351GiB
/dev/sdc 10TiB

Full output from lshw is [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydra/etc/lshw_output_hydra).

```
AsyaShklyer-mac68:Downloads asaj2017$ df -h
Filesystem      Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk1     931Gi   25Gi  905Gi     3%  668006 4294299273    0%   /
devfs          191Ki  191Ki    0Bi   100%     666          0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%       0          0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0          0  100%   /home
/dev/disk0s3   620Mi  563Mi   57Mi    91%      71 4294967208    0%   /Volumes/Recovery HD
```

```
AsyaShklyer-mac68:Downloads asaj2017$ mount
/dev/disk1 on / (hfs, local, journaled)
devfs on /dev (devfs, local, nobrowse)
map -hosts on /net (autofs, nosuid, automounted, nobrowse)
map auto_home on /home (autofs, automounted, nobrowse)
/dev/disk0s3 on /Volumes/Recovery HD (hfs, local, journaled, nobrowse)
```

```
[root@hydra .ssh]# lvdisplay
  --- Logical volume ---
  LV Path                /dev/vg_ab04747/lv_swap
  LV Name                lv_swap
  VG Name                vg_ab04747
  LV UUID                quZfZc-2zii-s8st-w4aX-EGMW-1eBO-iuCk0W
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2014-04-17 03:05:25 -0700
  LV Status              available
  # open                 1
  LV Size                48.00 GiB
  Current LE             12288
  Segments               1
  Allocation             contiguous
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0
   
  --- Logical volume ---
  LV Path                /dev/vg_ab04747/lv_var
  LV Name                lv_var
  VG Name                vg_ab04747
  LV UUID                1m80cf-zPM9-wB6x-0P7s-wfgk-JDf6-odEeOI
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2014-04-17 03:12:00 -0700
  LV Status              available
  # open                 1
  LV Size                50.00 GiB
  Current LE             12800
  Segments               1
  Allocation             contiguous
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:2
   
  --- Logical volume ---
  LV Path                /dev/vg_ab04747/lv_tmp
  LV Name                lv_tmp
  VG Name                vg_ab04747
  LV UUID                q1bPhR-YXH1-W6U9-wJdS-miHv-Zmoz-YGgl1h
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2014-04-17 03:17:13 -0700
  LV Status              available
  # open                 1
  LV Size                100.00 GiB
  Current LE             25600
  Segments               1
  Allocation             contiguous
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:3
   
  --- Logical volume ---
  LV Path                /dev/vg_ab04747/lv_root
  LV Name                lv_root
  VG Name                vg_ab04747
  LV UUID                gYQTIC-9EAC-y1ud-rsyc-2Ahy-t1Ie-eecKUn
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2014-04-17 03:18:19 -0700
  LV Status              available
  # open                 1
  LV Size                15.90 TiB
  Current LE             4168090
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:1
```

OS and kernel:

```
[root@hydra .ssh]# uname -a
Linux hydra.pomona.edu 2.6.32-573.18.1.el6.x86_64 #1 SMP Tue Feb 9 22:46:17 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

```
[root@hydra .ssh]# cat /etc/redhat-release 
CentOS release 6.7 (Final)
```

Network Interfaces:

em1       Link encap:Ethernet  HWaddr 74:86:7A:EC:76:14  
          inet addr:134.173.69.170  Bcast:134.173.69.255  Mask:255.255.255.0
          inet6 addr: 2620:102:2002:7000:7686:7aff:feec:7614/64 Scope:Global
          inet6 addr: fe80::7686:7aff:feec:7614/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2930730550 errors:0 dropped:19 overruns:0 frame:0
          TX packets:11295484145 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:719076767046 (669.6 GiB)  TX bytes:16710646525251 (15.1 TiB)
          Interrupt:35 

em2       Link encap:Ethernet  HWaddr 74:86:7A:EC:76:15  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:38 

em3       Link encap:Ethernet  HWaddr 74:86:7A:EC:76:16  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:34 

em4       Link encap:Ethernet  HWaddr 74:86:7A:EC:76:17  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:36 


Logged in as root (Saved the password in Lastpass Chrome extension).

Checked which hosts are known on the server logged in as root.

```
[root@hydra ~]# ls /root/.ssh
known_hosts
```

Show the contents of known_hosts (removed the key)

```
[root@hydra ~]# cat .ssh/known_hosts 
hydra2.pomona.edu,2620:102:2002:7000::172 ssh-rsa ....h4eR4prQjv68FjGh4Cxfl6VXvhSbdnMPm5GoYyk4AH4KAS5duu/...
```

Checked which users and UIDs exist (saved the /etc/passwd [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydra/etc/passwd) as a file for future reference/automation):

```
[root@hydra ~]# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
```

Created an account for myself, set the password, added a key for passwordless ssh, added myself to sudo with root privileges.

On hydra:

```
useradd asaj2017 (created with UID 564)

passwd asaj2017

gpasswd -a asaj2017 wheel

```
On my Mac:

```
AsyaShklyer-mac68:~ asaj2017$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/asaj2017/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/asaj2017/.ssh/id_rsa.
Your public key has been saved in /Users/asaj2017/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:8kahm5XAJ/EqIw9HEM1137tLuAU5Nj2jVcSaxo9MYik asaj2017@AsyaShklyer-mac68
The key's randomart image is:
+---[RSA 2048]----+
|  o+ .o .    ..  |
|   .o. + . . ..  |
|    . + + .o.o.  |
|   .   *Eo+o*o   |
|  o + + So*=*o   |
|   = o B . Bo+.  |
|    . o o o +    |
|       .   + .   |
|          . .    |
+----[SHA256]-----+
```


Copy the key to the server:

```
AsyaShklyer-mac68:Downloads asaj2017$ ssh-copy-id asaj2017@hydra.pomona.edu
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
asaj2017@hydra.pomona.edu's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'asaj2017@hydra.pomona.edu'"
and check to make sure that only the key(s) you wanted were added.
```



Installed lshw:

```
yum install lshw
...
Downloading Packages:
lshw-B.02.17-4.el6.x86_64.rpm                            | 254 kB     00:00     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
Warning: RPMDB altered outside of yum.
  Installing : lshw-B.02.17-4.el6.x86_64                                    1/1 
  Verifying  : lshw-B.02.17-4.el6.x86_64                                    1/1 

Installed:
  lshw.x86_64 0:B.02.17-4.el6                                                   

Complete!
```

Used lshw to look up the Service Tag to pull up the Dell Support page with the appropriate drivers:
http://www.dell.com/support/home/us/en/19/product-support/servicetag/fftw8z1/drivers

New BIOS available:
2.5.4 from 17 Feb 2016

iDRAC 1.66.65 from 27 Aug 2015 is available

Installed ipmitool:

```
yum install ipmitool
...
Downloading Packages:
ipmitool-1.8.15-2.el6.x86_64.rpm                                          | 465 kB     00:00     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing : ipmitool-1.8.15-2.el6.x86_64                                                  1/1 
  Verifying  : ipmitool-1.8.15-2.el6.x86_64                                                  1/1 

Installed:
  ipmitool.x86_64 0:1.8.15-2.el6                                                                 

Complete!
```

Show the IP for iDRAC:

```
[root@hydra .ssh]# ipmitool lan print 1
Set in Progress         : Set Complete
Auth Type Support       : NONE MD2 MD5 PASSWORD 
Auth Type Enable        : Callback : MD2 MD5 
                        : User     : MD2 MD5 
                        : Operator : MD2 MD5 
                        : Admin    : MD2 MD5 
                        : OEM      : 
IP Address Source       : Static Address
IP Address              : 192.168.0.120
Subnet Mask             : 255.255.255.0
MAC Address             : 5c:f9:dd:f5:ab:f0
SNMP Community String   : public
IP Header               : TTL=0x40 Flags=0x40 Precedence=0x00 TOS=0x10
BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled
Gratituous ARP Intrvl   : 2.0 seconds
Default Gateway IP      : 192.168.0.1
Default Gateway MAC     : 00:00:00:00:00:00
Backup Gateway IP       : 0.0.0.0
Backup Gateway MAC      : 00:00:00:00:00:00
802.1q VLAN ID          : Disabled
802.1q VLAN Priority    : 0
RMCP+ Cipher Suites     : 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
Cipher Suite Priv Max   : Xaaaaaaaaaaaaaa
                        :     X=Cipher Suite Unused
                        :     c=CALLBACK
                        :     u=USER
                        :     o=OPERATOR
                        :     a=ADMIN
                        :     O=OEM
```

# To Do:

- Integrate with AD, use individual accounts with sudo
- Add accounts with appropriate sudo privileges for everyone that needs to access the server
- BIOS and iDRAC update
- Acess to iDRAC
