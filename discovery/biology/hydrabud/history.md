# History of Hydrabud build

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
