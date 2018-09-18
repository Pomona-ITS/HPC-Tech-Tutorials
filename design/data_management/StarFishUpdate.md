Current version is ![CurrentVersion](https://github.com/Pomona-ITS/hpc/blob/master/design/data_management/Screen%20Shot%202018-09-18%20at%202.19.39%20PM.png).



New version is 2018-09-04 - 4.0.4785.


The update procedure is in the [Release Notes](https://github.com/Pomona-ITS/hpc/blob/master/design/data_management/20180907_Starfish_Release_Notes.pdf).

```
sudo sf scan pending

[sudo] password for asyashklyar: 
- id - - type - - status - - lstats - - progress - - dur -

```

No jobs running, proceed:

```

sudo yum upgrade starfish

[sudo] password for asyashklyar: 

Loaded plugins: fastestmirror, langpacks
Repodata is over 2 weeks old. Install yum-cron? Or run: yum makecache fast
Starfish                                                 | 1.3 kB     00:00     
base                                                     | 3.6 kB     00:00     
epel/x86_64/metalink                                     |  18 kB     00:00     
epel                                                     | 3.2 kB     00:00     
extras                                                   | 3.4 kB     00:00     
pgdg96                                                   | 4.1 kB     00:00     
starfish-supervisor                                      | 1.3 kB     00:00     
updates                                                  | 3.4 kB     00:00     
epel/x86_64/primary            FAILED                                          
http://mirror.es.its.nyu.edu/epel/7/x86_64/repodata/8f6a06c432b0ff2c438a465c03c7ab18e493de3381187494ec45be95ceb50f05-primary.xml.gz: [Errno 14] HTTP Error 404 - Not Found
Trying other mirror.
To address this issue please refer to the below knowledge base article 

https://access.redhat.com/articles/1320623

If above article doesn't help to resolve this issue please create a bug on https://bugs.centos.org/

(1/6): pgdg96/7/x86_64/primary_db                          | 198 kB   00:00     
(2/6): updates/7/x86_64/primary_db                         | 5.2 MB   00:00     
(3/6): extras/7/x86_64/primary_db                          | 187 kB   00:00     
(4/6): Starfish/primary                                    |  22 kB   00:00     
(5/6): epel/x86_64/updateinfo                              | 945 kB   00:03     
(6/6): epel/x86_64/primary                                 | 3.6 MB   00:04     
Determining fastest mirrors
 * base: mirror.hostduplex.com
 * epel: mirrors.kernel.org
 * extras: mirror.hostduplex.com
 * updates: mirror.sfo12.us.leaseweb.net
Starfish                                                                176/176
epel                                                                12685/12685
Resolving Dependencies
--> Running transaction check
---> Package starfish.x86_64 1:4.0.4686+6453d1b-1 will be updated
---> Package starfish.x86_64 1:4.0.4785+8dd2dd4-1 will be an update
--> Processing Dependency: sf-gui = 1:4.0.4785+2d298a7+gui_637-1 for package: 1:starfish-4.0.4785+8dd2dd4-1.x86_64
--> Processing Dependency: sf-nginx = 1.12.2-18 for package: 1:starfish-4.0.4785+8dd2dd4-1.x86_64
--> Processing Dependency: sf-redash = 1:4.0.4785+8dd2dd4-1 for package: 1:starfish-4.0.4785+8dd2dd4-1.x86_64
--> Processing Dependency: sf-cli = 1:4.0.4785+8dd2dd4-1 for package: 1:starfish-4.0.4785+8dd2dd4-1.x86_64
--> Running transaction check
---> Package sf-cli.x86_64 1:4.0.4686+6453d1b-1 will be updated
--> Processing Dependency: sf-cli = 1:4.0.4686+6453d1b-1 for package: 1:sf-agent-4.0.4686+6453d1b-1.x86_64
---> Package sf-cli.x86_64 1:4.0.4785+8dd2dd4-1 will be an update
---> Package sf-gui.x86_64 1:4.0.4686+fcd6939+gui_583-1 will be updated
---> Package sf-gui.x86_64 1:4.0.4785+2d298a7+gui_637-1 will be an update
---> Package sf-nginx.x86_64 0:1.12.2-17 will be updated
---> Package sf-nginx.x86_64 0:1.12.2-18 will be an update
---> Package sf-redash.x86_64 1:4.0.4686+6453d1b-1 will be updated
---> Package sf-redash.x86_64 1:4.0.4785+8dd2dd4-1 will be an update
--> Running transaction check
---> Package sf-agent.x86_64 1:4.0.4686+6453d1b-1 will be updated
---> Package sf-agent.x86_64 1:4.0.4785+8dd2dd4-1 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package       Arch       Version                            Repository    Size
================================================================================
Updating:
 starfish      x86_64     1:4.0.4785+8dd2dd4-1               Starfish      93 M
Updating for dependencies:
 sf-agent      x86_64     1:4.0.4785+8dd2dd4-1               Starfish      89 M
 sf-cli        x86_64     1:4.0.4785+8dd2dd4-1               Starfish      50 M
 sf-gui        x86_64     1:4.0.4785+2d298a7+gui_637-1       Starfish     6.6 M
 sf-nginx      x86_64     1.12.2-18                          Starfish     4.0 M
 sf-redash     x86_64     1:4.0.4785+8dd2dd4-1               Starfish      21 M

Transaction Summary
================================================================================
Upgrade  1 Package (+5 Dependent packages)

Total download size: 264 M
Is this ok [y/d/N]: 

```

```

Updated:
  starfish.x86_64 1:4.0.4785+8dd2dd4-1                                          

Dependency Updated:
  sf-agent.x86_64 1:4.0.4785+8dd2dd4-1       sf-cli.x86_64 1:4.0.4785+8dd2dd4-1
  sf-gui.x86_64 1:4.0.4785+2d298a7+gui_637-1 sf-nginx.x86_64 0:1.12.2-18       
  sf-redash.x86_64 1:4.0.4785+8dd2dd4-1     

Complete!

```

```
sudo yum upgrade sf-agent sf-core-v4 sf-cli
[sudo] password for asyashklyar: 
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * base: mirror.hostduplex.com
 * epel: mirrors.kernel.org
 * extras: mirror.hostduplex.com
 * updates: mirror.sfo12.us.leaseweb.net
Resolving Dependencies
--> Running transaction check
---> Package sf-core-v4.x86_64 1:4.0.4686+342f264-1 will be updated
---> Package sf-core-v4.x86_64 1:4.0.4785+1ecfb86-1 will be an update
--> Processing Dependency: starfish-release = 1.0 for package: 1:sf-core-v4-4.0.4785+1ecfb86-1.x86_64
--> Running transaction check
---> Package starfish-release.x86_64 0:1.0-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package              Arch       Version                     Repository    Size
================================================================================
Updating:
 sf-core-v4           x86_64     1:4.0.4785+1ecfb86-1        Starfish      29 k
Installing for dependencies:
 starfish-release     x86_64     1.0-1                       Starfish     4.0 k

Transaction Summary
================================================================================
Install             ( 1 Dependent package)
Upgrade  1 Package

Total download size: 33 k
Is this ok [y/d/N]: 

```

```
Total                                               44 kB/s |  33 kB  00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : starfish-release-1.0-1.x86_64                                1/3 
  Updating   : 1:sf-core-v4-4.0.4785+1ecfb86-1.x86_64                       2/3 
  Cleanup    : 1:sf-core-v4-4.0.4686+342f264-1.x86_64                       3/3 
  Verifying  : starfish-release-1.0-1.x86_64                                1/3 
  Verifying  : 1:sf-core-v4-4.0.4785+1ecfb86-1.x86_64                       2/3 
  Verifying  : 1:sf-core-v4-4.0.4686+342f264-1.x86_64                       3/3 

Dependency Installed:
  starfish-release.x86_64 0:1.0-1                                               

Updated:
  sf-core-v4.x86_64 1:4.0.4785+1ecfb86-1                                        

Complete!

```

```
 sudo sf check-config
Starfish Client version: 4.0.4785+8dd2dd4
Starfish home directory: /opt/starfish


Config https://10.14.3.10:30003: UP  (config/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:52 (1h8m41s ago)
  bind_host: 10.14.3.10
  config_service_url: https://10.14.3.10:30003
  default_agent_service_url: https://10.14.3.10:30002
  secret_key: ***
  ssl_certificate_file: /opt/starfish/etc/sf-ssl.crt
  ssl_private_key_file: ***
  starfish_url_prefix: https://10.14.3.10
  use_pg: True
  [GUI]
    archive_enabled: True
    update_manifest_url: https://s3.amazonaws.com/starfish-stable-updates/update_manifest.json
  [agent]
    autodiscovery_on_start: False
    autodiscovery_roots: /
    autodiscovery_timeout: 1
    check_noatime: True
    default_cost_per_gb: 0.0244
    enable_serve_file: False
    exclude_dirs: .snapshot*,~snapshot*,.zfs,.isilon,.ifsvar
    exclude_fstypes: proc,sysfs,fusectl,debugfs,securityfs,efivarfs,devtmpfs,devpts,pstore,cgroup,binfmt_misc,rpc_pipefs,fuse.gvfsd-fuse,tmpfs,nfsd,rootfs,ramfs,initramfs,mqueue,hugetlbfs,selinuxfs,configfs,autofs,fuse.lxcfs,bdev,cpuset,sockfs,usbfs,pipefs,anon_inodefs,inotifyfs,tracefs
    exclude_volumes: 
    initial_scan: True
    run_init_volume: True
    ssl_certificate_file: //opt/starfish/etc/sf-agent:pom-itb-starfish01.campus.pomona.edu.crt
    ssl_private_key_file: ***
    update_total_capacity_on_start: True
  [auth]
    auth_token_key: ***
  [client]
    http_max_retries: 3
    http_timeout: 7
  [crawler]
    chunk_size: 3145728
    max_queue_size: 10000
    periodic_flush_interval_sec: 300
    progress_log_interval: 60
    queue_wait_interval: 10
  [pg]
    pg_uri: postgresql://starfish:***@10.14.3.10:5432/starfish
  [templates]
    diff: scan start --type diff
    hash: job start "hasher --algorithm md5 sha1"
    hash-quick: job start --job-name hash-quick --size 100K-100P "hasher --quick"
    mtime: scan start --type mtime
    sync: scan start --type sync

License: valid until 2018-11-17
  Licensed to: pomona
  backup: Enabled
  excludes: Enabled
  fs-monitor: Enabled
  fsentry: Enabled
  job: Enabled
  query: Enabled
  reports: Enabled
  reports:analytics: Enabled
  reports:basic: Enabled
  scan: Enabled
  scheduling: Enabled
  tag: Enabled
  volume: Enabled

Temp https://10.14.3.10:30001: UP  (temp/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:58 (1h8m35s ago)
Storage path      : /opt/starfish/lib/temp/storage
Storage mountpoint: /opt
Storage free space: 533.8GB
Storage free %    : 99.5%

Scans https://10.14.3.10:30005: UP  (scans/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:57:01 (1h8m32s ago)

Pgloader https://10.14.3.10:30014: UP  (pgloader/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:54 (1h8m39s ago)

Dispatcher https://10.14.3.10:30006: UP  (dispatcher/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:57:00 (1h8m33s ago)

Cron https://10.14.3.10:30011: UP  (cron/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:57 (1h8m36s ago)

Gateway https://10.14.3.10:30012: UP  (gateway/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:56 (1h8m37s ago)

Archive https://10.14.3.10:30015: UP  (archive/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:57:02 (1h8m31s ago)

Auth https://10.14.3.10:30017: UP  (auth/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:54 (1h8m39s ago)

Volumes https://10.14.3.10:30004: UP  (volumes/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:56:59 (1h8m34s ago)
  Volume etc on https://10.14.3.10:30002

Agent https://10.14.3.10:30002: UP (agent/4.0.4785+8dd2dd4 CPython/3.6.6 Linux-3.10.0-514.26.2.el7.x86_64-x86_64-with-centos-7.3.1611-Core)
Started at: 2018-09-18 14:57:17 (1h8m16s ago)
  postgresql: OK
  temp: OK

Disk usage:
  - filesystem - - size - - used - - avail - - use% - - fs - - mounted on -
  /dev/mapper/     27.9GB    4.7GB    23.2GB      17% xfs    /
  vg00-lvroot
  /dev/sda1         1.0GB  181.3MB   771.5MB      19% ext4   /boot
  /dev/mapper/      4.3GB   78.8MB     4.2GB     1.8% xfs    /home
  vg00-lvhome
  /dev/sdb1       536.6GB    2.8GB   533.8GB     0.5% xfs    /opt
  /dev/mapper/      4.1GB   16.9MB     3.8GB     0.4% ext4   /tmp
  vg00-lvtmp
  /dev/mapper/     27.9GB    4.8GB    23.1GB    17.1% xfs    /var
  vg00-lvvar

Host parameters:
  CPU count [physical]      8
  CPU count [logical]       8
  memory total [GiB]   125.76

PostgreSQL: (PostgreSQL 9.6.9 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-16), 64-bit)
Started at: 2018-08-02 08:49:53 (47d7h15m40s ago)
  DB starfish: 33.2MB
  WAL: 50.3MB / 10.7GB, archiving: on
    totals: 160 succeeded, 0 failed since 2018-07-19 10:55:08 -0700
    ready files: 0
    archive rate: 0.0/min
    last archived: 2018-09-18 00:30:07 -0700 (15h35m26s ago)

  Tablespace pg_default @ /opt/starfish/pg/9.6: 58.2MB
  Tablespace pg_global @ /opt/starfish/pg/9.6: 533.3KB
    mountpoint: /opt
    free space: 533.8GB
    free %    : 99.5%

  - type - - name -        - size - - index size - - toast size - - live tuples - - dead tuples -
  Schema   sf                18.7MB         12.5MB        221.2KB           5,530          25,210
  Schema   sf_reports         1.5MB        344.1KB         65.5KB           9,390               0
  Schema   sf_scans         466.9KB        139.3KB         41.0KB             244             115
  Schema   sf_dispatcher    229.4KB        163.8KB         16.4KB               8              38
  Schema   sf_volumes       147.5KB         98.3KB         24.6KB               3               2
  Schema   sf_archive       114.7KB         65.5KB         24.6KB               3              19
  Schema   sf_internal       90.1KB         32.8KB         57.3KB               0               0
  Schema   sf_auth           81.9KB         57.3KB         24.6KB               0               0
  Schema   sf_cron           65.5KB         16.4KB          8.2KB               1               6
  
  Table    sf.file_current    9.8MB          8.2MB          8.2KB           2,955          18,614
  Table    sf.dir_current     5.5MB          3.2MB          8.2KB             753           6,595
  Table    sf.dir_history     2.6MB        565.2KB          8.2KB           1,749               0
  Table    sf.file_history  163.8KB        114.7KB          8.2KB              48               0

  - table -       - rows since analyze - - last vacuum -    - last analyze - - running vacuum -
  sf.dir_current                       0                 2018-09-17 21:00:46
  sf.file_history                      0                 2018-09-17 21:00:46
  sf.dir_history                       0                 2018-09-17 21:00:46
  sf.file_current                      0                 2018-09-17 21:00:46

Sentry:  Not configured, using standard logging only

```
