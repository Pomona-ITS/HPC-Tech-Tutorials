# Data Management in HPC


Data Management in HPC/Research Computing is a very important topic for the following reasons:



1) Many diverse data sources and destinations

2) The data moves 3+ times: source - (local node disk or scratch/parallel file system) - NFS - object storage - cloud

3) There are hundreds or thousands of users

4) The workload is mostly automated or can be automated

5) The volumes of data are larger than normal (compared to just Home Direcrories)

6) Cost vs Performance is managed via multiple types of disk, some more expensive/smaller in capacity than others


The following tools are used for data management in HPC and non-HPC environments:


[Robinhood](https://github.com/cea-hpc/robinhood/wiki)


A MySQL/MariaDB-based scanner of the metadata (originally developed for Lustre file system and still supported by Lustre 
community), extended to work with NFS. It reads in UIDs, GIDs, creation/access times (if ATIME is enabled in Lustre), 
file/directory name, age, path and permissions. This essentially offloads things like du/df/ls which cost I/O and allows 
to query the database and create automatic policies for archival/moving between storage layers based on age or owner or 
type or extension. The first scan does everything, after that it is incremental.  
The main link is here: https://github.com/cea-hpc/robinhood/wiki. It is free, open source. 
Commercial support could be obtained. We can do a POC on a file system of interest (will require root).


[StarFish](http://www.starfishstorage.com/)


Metadata & Rules Framework For Large-Scale File Management


File Movement: Archive, Backup, Migrate

Reporting: Duplicate Deletion, Aging, Utilization / Ownership

File Processing: Hash Calculation, Metadata Extraction, Run Your Own Code

Largest pro: designed from scratch to support any and all environment or file system, vendor-agnostic

Largest con: not cheap, closed source, small-ish company (associated with Cambridge Computing)



[iRODS](https://irods.org/)

https://github.com/Pomona-ITS/hpc/blob/master/design/data_management/Screen%20Shot%202018-02-09%20at%2012.09.04%20PM.png


[IBM AFM](https://www.ibm.com/support/knowledgecenter/en/STXKQY_4.1.1/com.ibm.spectrum.scale.v4r11.adv.doc/bl1adv_afm.htm)
(for SpectraLogic aka GFPS integration with other file systems like the acquired object storage CleverSafe)

Active file management (AFM) is a scalable, high-performance, file system caching layer integrated with the GPFS™ cluster file system. AFM allows you to create associations from a local GPFS cluster to a remote cluster or storage, and to define the location and flow of file data to automate the management of the data.


Some file systems have their own tools, like Isilon, Panasas.


Traditional HSM
