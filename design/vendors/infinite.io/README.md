# [infinite.io](http://www.infinite.io/) is a metadata  accelerator


They were founded in 2015 and came out of stealth mode around 2017. Based in Austin, TX.


There are a couple of things that make them completely different from any other typical storage vendor.


They are a network device that sits in-line between your NFS-based files (only NFS is currently supported) and your users.


There is no change to the current environment. Paths are the same, names are the same. There is a one-time initial scan of all the data.


All metadata requests are intercepted before they make it to the NFS device which is known to speed up even All-Flash arrays.


They store all metadata in RAM, use 3 units in a cluster for reliability (which was requested by Intel) and can be used for just acceleration/servicng requests or also moving data itself that is not used to a slower layer.


I had a call with them on May 18th. They want to give us a demo unit but since we are a bit overwhelmed with testing Pure right now I said in 6 months.
The contacts are Edward McAllister [mailto:ed@creativetechagency.com] who is representing infinite.io and is their sales partner and John Nardo jnardo@infinite.io who is one of the original people at infinite.io.


Some of the happy customers they have are Chapman University, European Bioinformatics Institute, Virtual Instruments, Formula 1/Mercedes.


Their pricing is one time, not per TB. List price is $80K but heavily discounted for a college and an early adopter.


Pure Storage is a partner as well as Igneous and others.


MOPS - metadata operations per second - inverse of IOPS.


10 GB connections (Ethernet only) for now, but some customers are asking for 100 GB.


3 2U units per cluster, 12 ports each.


Founders came from Tipping Point acquired by 3com and then HP. Created first iSCSI.


Talking to a lot of large companies but are not aiming to get acquired.


Interested in speeding up EDA - Electronic Design Automation processes.


There is a limit of 600 million files per box. New release this summer will double it.


Will be able to do security in the future (since the technology is based on packet inspection).


Some anaytics exists, can visualize the metadata, needs to improve. Are aware.


Will send the slides.
