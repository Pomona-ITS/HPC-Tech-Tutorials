# History of Hydrabud build

Thank you Todd!

 I think I missread your message. Sorry. Here is another question. According to my notes the Dell server for hydra2 is as follows:

hydra2
PowerEdge R730 Server 
RAM:  768 GB (24 x 32GB LRDIMM, 2133 MT/s, Quad Rank, x4 Data Width (370-ABUH))
Storage: 24 TB (8 x 6TB 7.2K RPM NLSAS 6Gbps 512e 3.5in Hot-plug Hard Drive (400-AGEE))

I don’t see the 24TB in hydra2. Am I sure I am missing something. 

Best, 

Daniel

[hygenome@hydra2 ~]$ df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VolGroup-lv_root
                      1.1T  630G  374G  63% /
tmpfs                 379G  220K  379G   1% /dev/shm
/dev/sda2             477M  165M  287M  37% /boot
/dev/sda1             200M  276K  200M   1% /boot/efi
/dev/mapper/VolGroup-lv_home
                       16T   15T  676G  96% /home



From: "Todd A. Shimoda" <Todd.Shimoda@pomona.edu>
Date: Friday, March 9, 2018 at 9:54 AM
To: Daniel Martinez <DEM04747@pomona.edu>, Asya Shklyar <Asya.Shklyar@pomona.edu>, Pat Flannery <pat@pomona.edu>
Subject: Re: Server space

Hi Daniel,
 
Sorry for the confusion. In Hydrabud, the directory Hydra was set up with 16 TB and the directory Hydra2 with 16 TB, for a total of 32TB. Currently the directory Hydra is 67% full, and Hydra2 is 43% full. So there is a total of about 14TB still available across the two directories. Is 14TB enough for what you need?
 
Hope that clarifies it.
Todd


Hi Todd,

Thank you for your prompt reply but I am afraid I am more confused now. 

Are you sure that hydrabud has only 16TB of space? 

Here is an email from you (dated December 11, 2014) when we bought the disks.  Below is the ticket from ITS talking about a 32TB hard drive. 

Thank you for your help Todd!

Cheers,

Daniel

##############
Hi Daniel, Anthony,

Here is the estimate for a 36TB dedicated server to be installed in the ITS data center which would use rsync to back up hydra.

1 x HP DL180 G6, quad core cpu, and 16GB of RAM @ $1500/ea
12 x Seagate 3T hard drives @ $125/ea
Total = $3000

Let me know if this will be okay to order for you.

Best, Todd
###############

TS Pomona Service Desk - Contact Version
 
Ticket Number:
42725
Subject:
Quote for backup server for Daniel Martinez lab
 
Click here to view Issue in Browser
 
Most Recent Note on this Issue:
Entered on 12/09/2014 at 14:00:49 PST (GMT-0800) by Todd Shimoda:
The Martinez lab requests a quote for a server that will be used to backup their Dell 720 server (hydra.pomona.edu). They will have a total of 32 TB hard drive memory in that server when their additional hard drives are installed.



Dear Asya, Todd, and Pat,

Greetings from Vienna! Hope things are going well for you in Claremont. 

I have been generating enormous amount of data so that I am running out of disk space on my servers. Hydra2 is at 98% and Hydrabud is getting full too. I am currently copying a large 3.5 T project directory from hydra2 to hydrabud to free more space so I can continue to work. 

I have a few questions about my server space. First, I seem to remember that hydrabud had some kind of partition so that there was a large disk space and a smaller one (I could be wrong about this).  When I look at the space usage in hydrabud with df, I see two large 16T directories called hydra and hydra2. Are these the two partitions? Is there any more space somewhere? In 2016, with the help of Anthony Nguyen, we purchased a 30TB disk array for hydrabud. I am not sure how to access that space. Below is an email from Pat about work he did on hydrabud when the new disk array was installed.

I am very sorry about my confusion. I hope that my questions make sense to you. 


```
root@hydrabud ~]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VolGroup-lv_root
                       50G   15G   32G  33% /
tmpfs                 7.8G   68K  7.8G   1% /dev/shm
/dev/sda1             477M   96M  356M  22% /boot
/dev/mapper/VolGroup-lv_home
                     1008G   73M  957G   1% /home
/dev/mapper/VolGroup-lv_hydra
                       16T   10T  5.0T  67% /hydra
/dev/mapper/VolGroup-lv_hydra2
                       16T  6.1T  8.9T  41% /hydra2

```

Another question is, is there any other space at IT where I could deposit data? I know we talked about using a “virtual” server. Could we do something similar for storage?  

Thank you very much for your help!

Best regards,

Daniel

##################################
Hello Daniel,

Hope you are doing well.  I have completed the build of the additional storage hardware for hydrabud.  I would like to schedule some downtime to install and configure if on the system so that you can start using it.  If we can do it during the normal operation day 9:00am – 5:00pm that would be preferred.  If there is an alternate time that would minimize impact on your operation please let me know. I expect it to take about an hour total.  

Here is what I need to completed:
Connect the storage container to the server.
Power up the server and go into the RAID controller configuration.
Configure the storage container.
Reboot the system.  

Once this is completed the container will auto build the drive set.  This will happen automatically in the background while the server is operational.

What you will need to complete after the rebuild:
Add the drive to the OS (LVM?) 
Set and configure the mount point for the new storage.

I say you, but that is whoever is managing the server configuration.  

Thank you,

Pat
