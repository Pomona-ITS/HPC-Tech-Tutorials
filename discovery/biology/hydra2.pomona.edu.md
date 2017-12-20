This is the initial discovery of hydra2.pomona.edu, The Research Server.

# Overview:

Server Name: hydra2.pomona.edu

Model: PowerEdge R730

Service Tag: FJMN842

Motherboard model: 0599V5

Motherboard SN: CN779214BG005F

BIOS:

version: 1.0.4
date: 08/28/2014

CPU Info:

2 x Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz x 18 cores each with threads enabled for a total of 72 cores

RAM Info:

767GiB
32 GB DIMM DDR3 Synchronous 1333 MHz (0.8 ns) X 24

Networking:

Broadcom NetXtreme BCM5720 Gigabit Ethernet PCIe

Storage:

LSI Logic MegaRAID SAS-3 3108 [Invader]

PERC H730P

/dev/sda 200GiB

LVM on /dev/sda 199GiB

LVM on /dev/sdb 21TiB 

Full output from lshw is [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydra2/etc/lshw_output_hydra2).

```
[root@hydra2 asaj2017]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VolGroup-lv_root
                      1.1T  310G  695G  31% /
tmpfs                 379G  220K  379G   1% /dev/shm
/dev/sda2             477M  165M  287M  37% /boot
/dev/sda1             200M  276K  200M   1% /boot/efi
/dev/mapper/VolGroup-lv_home
                       16T   12T  3.1T  80% /home
```

```
[root@hydra2 asaj2017]# mount
/dev/mapper/VolGroup-lv_root on / type ext4 (rw)
proc on /proc type proc (rw)
sysfs on /sys type sysfs (rw)
devpts on /dev/pts type devpts (rw,gid=5,mode=620)
tmpfs on /dev/shm type tmpfs (rw,rootcontext="system_u:object_r:tmpfs_t:s0")
/dev/sda2 on /boot type ext4 (rw)
/dev/sda1 on /boot/efi type vfat (rw,umask=0077,shortname=winnt)
/dev/mapper/VolGroup-lv_home on /home type ext4 (rw,noexec,nosuid,nodev)
none on /proc/sys/fs/binfmt_misc type binfmt_misc (rw)
```

```
[root@hydra2 asaj2017]# lvdisplay
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_root
  LV Name                lv_root
  VG Name                VolGroup
  LV UUID                0CcbTv-7j41-Yf0V-K1Mo-G0MR-LZS7-tSP3vm
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-03-11 09:41:24 -0700
  LV Status              available
  # open                 1
  LV Size                1.05 TiB
  Current LE             274944
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_home
  LV Name                lv_home
  VG Name                VolGroup
  LV UUID                XrdjvQ-QVeE-7a1w-zTE6-3Q79-tgQ2-dyu2LY
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-03-11 09:41:26 -0700
  LV Status              available
  # open                 1
  LV Size                15.91 TiB
  Current LE             4170470
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:2
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_swap
  LV Name                lv_swap
  VG Name                VolGroup
  LV UUID                A2stLh-vLiC-NcQW-J6Qg-4LbR-Nj27-hgLou9
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-03-11 09:41:33 -0700
  LV Status              available
  # open                 1
  LV Size                4.00 GiB
  Current LE             1024
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:1
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_data
  LV Name                lv_data
  VG Name                VolGroup
  LV UUID                TTTIpe-Uqgp-IFUK-5c39-0APK-XAub-tNbPva
  LV Write Access        read/write
  LV Creation host, time hydra2.pomona.edu, 2016-02-09 12:11:00 -0800
  LV Status              available
  # open                 0
  LV Size                4.00 TiB
  Current LE             1048576
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:3
```

OS and kernel:

```
[root@hydra2 asaj2017]# uname -a
Linux hydra2.pomona.edu 2.6.32-642.1.1.el6.x86_64 #1 SMP Tue May 31 21:57:07 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

```
[root@hydra2 asaj2017]# cat /etc/redhat-release
CentOS release 6.8 (Final)
```

Network Interfaces:

em1       Link encap:Ethernet  HWaddr 44:A8:42:02:E5:C8  
          inet addr:134.173.69.172  Bcast:134.173.69.255  Mask:255.255.255.0
          inet6 addr: 2620:102:2002:7000::172/64 Scope:Global
          inet6 addr: fe80::46a8:42ff:fe02:e5c8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1574218264 errors:0 dropped:1 overruns:0 frame:0
          TX packets:3790902263 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1099032942414 (1023.5 GiB)  TX bytes:5109630357865 (4.6 TiB)
          Interrupt:41 

em2       Link encap:Ethernet  HWaddr 44:A8:42:02:E5:C9  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:45 

em3       Link encap:Ethernet  HWaddr 44:A8:42:02:E5:CA  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:40 

em4       Link encap:Ethernet  HWaddr 44:A8:42:02:E5:CB  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Interrupt:44 



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

Checked which users and UIDs exist (saved the /etc/passwd [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydra2/etc/passwd) as a file for future reference/automation):

```
[root@hydra2 asaj2017]# cat /root/.ssh/known_hosts 
github.com,192.30.252.131 ssh-rsa AAAAB3...
hydra.pomona.edu,134.173.69.170 ssh-rsa AAAAB3N...
hydrabud.pomona.edu,134.173.69.171 ssh-rsa AAAAB3Nza...
hydra2.pomona.edu,2620:102:2002:7000::172 ssh-rsa AAAAB3N...
hydra ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAwy3oM6UNfzqQfpL8...
```

Created an account for myself, set the password, added a key for passwordless ssh, added myself to sudo with root privileges.

On hydra2:

```
useradd asaj2017 (created with UID 564)

passwd asaj2017

gpasswd -a asaj2017 wheel

```
On my Mac the key was already created after hydra.

Copy the key to the server:

```
AsyaShklyer-mac68:Downloads asaj2017$ ssh-copy-id asaj2017@hydra2.pomona.edu
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
asaj2017@hydra2.pomona.edu's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'asaj2017@hydra2.pomona.edu'"
and check to make sure that only the key(s) you wanted were added.
```



Installed lshw.

Used lshw to look up the Service Tag to pull up the Dell Support page with the appropriate drivers:
http://www.dell.com/support/home/us/en/19/product-support/servicetag/fjmn842/drivers


Installed ipmitool.

Show the IP for iDRAC:

```
[root@hydra2 asaj2017]# ipmitool lan print 1
Set in Progress         : Set Complete
Auth Type Support       : MD5 
Auth Type Enable        : Callback : MD5 
                        : User     : MD5 
                        : Operator : MD5 
                        : Admin    : MD5 
                        : OEM      : 
IP Address Source       : Static Address
IP Address              : 192.168.0.120
Subnet Mask             : 255.255.255.0
MAC Address             : b0:83:fe:e6:9a:b6
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

