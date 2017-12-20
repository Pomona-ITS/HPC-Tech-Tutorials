This is the initial discovery of hydrabud.pomona.edu, The Storage Server.

# Overview:

Server Name: hydrabud.pomona.edu

Model: ProLiant DL180 G6

SN: MXQ152014J

Motherboard model: ?

Motherboard SN: ?

BIOS:

version: O20
date: 09/01/2011

CPU Info:

1 x Intel(R) Xeon(R) CPU E5620  @ 2.40GHz x 4 cores  with threads enabled for a total of 8 cores
2nd CPU DISABLED

RAM Info:

16GiB
DIMM DDR3 Synchronous 1333 MHz (0.8 ns) X 1

Networking:

Intel 82576 Gigabit Network Connection

Storage:

HP Smart Array G6 controllers

/dev/sda 36TiB
/dev/sdb 27TiB

Full output from lshw is [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydrabud/etc/lshw_output_hydrabud).

```
[root@hydrabud asaj2017]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VolGroup-lv_root
                       50G   14G   33G  30% /
tmpfs                 7.8G   68K  7.8G   1% /dev/shm
/dev/sda1             477M   96M  356M  22% /boot
/dev/mapper/VolGroup-lv_home
                     1008G   73M  957G   1% /home
/dev/mapper/VolGroup-lv_hydra
                       16T   10T  5.0T  67% /hydra
/dev/mapper/VolGroup-lv_hydra2
                       16T  5.3T  9.7T  36% /hydra2
```

```
[root@hydrabud asaj2017]# mount
/dev/mapper/VolGroup-lv_root on / type ext4 (rw)
proc on /proc type proc (rw)
sysfs on /sys type sysfs (rw)
devpts on /dev/pts type devpts (rw,gid=5,mode=620)
tmpfs on /dev/shm type tmpfs (rw,rootcontext="system_u:object_r:tmpfs_t:s0")
/dev/sda1 on /boot type ext4 (rw)
/dev/mapper/VolGroup-lv_home on /home type ext4 (rw)
/dev/mapper/VolGroup-lv_hydra on /hydra type ext4 (rw)
/dev/mapper/VolGroup-lv_hydra2 on /hydra2 type ext4 (rw)
none on /proc/sys/fs/binfmt_misc type binfmt_misc (rw)
```

```
[root@hydrabud asaj2017]# lvdisplay
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_root
  LV Name                lv_root
  VG Name                VolGroup
  LV UUID                A9P5AY-f39b-Rn1X-Y1Nu-231F-9nzh-qFZShC
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-01-28 04:53:15 -0800
  LV Status              available
  # open                 2
  LV Size                50.00 GiB
  Current LE             12800
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_home
  LV Name                lv_home
  VG Name                VolGroup
  LV UUID                xe7a6b-QQyR-WAv9-ksyW-8Czq-gLN6-7IW24f
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-01-28 04:53:30 -0800
  LV Status              available
  # open                 2
  LV Size                1.00 TiB
  Current LE             262144
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:2
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_swap
  LV Name                lv_swap
  VG Name                VolGroup
  LV UUID                E3Tl85-TTlK-0XXP-BoDd-PJgD-3KQN-TewD3u
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-01-28 05:37:43 -0800
  LV Status              available
  # open                 1
  LV Size                7.85 GiB
  Current LE             2010
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:1
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_hydra
  LV Name                lv_hydra
  VG Name                VolGroup
  LV UUID                ViRcpu-zgRL-cpSg-way8-fm7n-OMwp-1yn1QO
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-04-30 11:56:04 -0700
  LV Status              available
  # open                 2
  LV Size                16.00 TiB
  Current LE             4194304
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:3
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_hydra2
  LV Name                lv_hydra2
  VG Name                VolGroup
  LV UUID                fH79gv-NvHF-Npey-oZYE-ie1S-bYu1-9IPcu0
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2015-04-30 11:56:55 -0700
  LV Status              available
  # open                 2
  LV Size                16.00 TiB
  Current LE             4194304
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:4
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_hydra3
  LV Name                lv_hydra3
  VG Name                VolGroup
  LV UUID                LtOddE-u2hk-oZJ7-VJEG-wppb-sEvh-oeG5s3
  LV Write Access        read/write
  LV Creation host, time hydrabud.pomona.edu, 2016-03-03 13:25:42 -0800
  LV Status              available
  # open                 0
  LV Size                15.00 TiB
  Current LE             3932160
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:5
   
  --- Logical volume ---
  LV Path                /dev/VolGroup/lv_hydra4
  LV Name                lv_hydra4
  VG Name                VolGroup
  LV UUID                10LXIw-mmQJ-y8xr-gdS2-f0fW-GdJG-VOhOww
  LV Write Access        read/write
  LV Creation host, time hydrabud.pomona.edu, 2016-03-03 13:27:19 -0800
  LV Status              available
  # open                 0
  LV Size                15.00 TiB
  Current LE             3932160
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:6
```

OS and kernel:

```
[root@hydrabud asaj2017]# uname -a
Linux hydrabud.pomona.edu 2.6.32-642.4.2.el6.x86_64 #1 SMP Tue Aug 23 19:58:13 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

```
[root@hydrabud asaj2017]# cat /etc/redhat-release 
CentOS release 6.8 (Final)
```

Network Interfaces:

eth0      Link encap:Ethernet  HWaddr E8:39:35:B1:B3:FE  
          inet addr:134.173.69.171  Bcast:134.173.69.255  Mask:255.255.255.0
          inet6 addr: 2620:102:2002:7000:ea39:35ff:feb1:b3fe/64 Scope:Global
          inet6 addr: fe80::ea39:35ff:feb1:b3fe/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:69905475 errors:0 dropped:0 overruns:0 frame:0
          TX packets:72716935 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:53292591288 (49.6 GiB)  TX bytes:74760858483 (69.6 GiB)
          Memory:fbe60000-fbe7ffff 

eth1      Link encap:Ethernet  HWaddr E8:39:35:B1:B3:FF  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
          Memory:fbee0000-fbefffff 

Logged in as root (Saved the password in Lastpass Chrome extension).

Checked which hosts are known on the server logged in as root.

```
[root@hydra ~]# ls /root/.ssh
known_hosts
```

Show the contents of known_hosts (removed the keys)

```
[root@hydrabud asaj2017]# cat /root/.ssh/known_hosts 
hydra.pomona.edu,134.173.69.170 ssh-rsa AAAAB3NzaC1...
hydra2.pomona.edu,2620:102:2002:7000::172 ssh-rsa AAAAB...
```

Checked which users and UIDs exist (saved the /etc/passwd [here](https://github.com/also-systems/pomona/blob/master/discovery/biology/hydrabud/etc/passwd) as a file for future reference/automation):


Created an account for myself, set the password, added a key for passwordless ssh, added myself to sudo with root privileges.

On hydrabud:

```
useradd asaj2017 (created with UID 564)

passwd asaj2017

gpasswd -a asaj2017 wheel

```
On my Mac the key was already created after hydra.

Copy the key to the server:

```
AsyaShklyer-mac68:Downloads asaj2017$ ssh-copy-id asaj2017@hydrabud.pomona.edu
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
asaj2017@hydrabud.pomona.edu's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'asaj2017@hydrabud.pomona.edu'"
and check to make sure that only the key(s) you wanted were added.
```



Installed lshw.

HP Support/Drivers:
https://support.hpe.com/hpesc/public/home/driverHome?sp4ts.oid=3884342


Installed ipmitool.

Show the IP for iLO (NOT SET?):

```
[root@hydrabud asaj2017]# ipmitool lan print
Set in Progress         : Set Complete
Auth Type Support       : NONE MD5 PASSWORD 
Auth Type Enable        : Callback : NONE MD5 PASSWORD 
                        : User     : NONE MD5 PASSWORD 
                        : Operator : NONE MD5 PASSWORD 
                        : Admin    : NONE MD5 PASSWORD 
                        : OEM      : NONE MD5 PASSWORD 
IP Address Source       : DHCP Address
IP Address              : 0.0.0.0
Subnet Mask             : 0.0.0.0
MAC Address             : e8:39:35:bf:8b:ef
SNMP Community String   : public
IP Header               : TTL=0x40 Flags=0x40 Precedence=0x00 TOS=0x10
BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled
Gratituous ARP Intrvl   : 2.0 seconds
Default Gateway IP      : 192.168.2.203
802.1q VLAN ID          : Disabled
802.1q VLAN Priority    : 0
RMCP+ Cipher Suites     : 0,1,2,3
Cipher Suite Priv Max   : OOOOXXXXXXXXXXX
                        :     X=Cipher Suite Unused
                        :     c=CALLBACK
                        :     u=USER
                        :     o=OPERATOR
                        :     a=ADMIN
                        :     O=OEM

```

# To Do:

- Retire?
