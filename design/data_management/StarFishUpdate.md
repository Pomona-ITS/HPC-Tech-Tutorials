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
