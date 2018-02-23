# Questions and Follow Up

## 1) What is the difference between a CPU and a node? What is a core?


  ### A node is a physical server (or in some cases a VM (Virtual Machine)), which will have an OS (Operating System) and will be used for  specialized student workloads/Docker, compute/batch jobs or interactive access. A CPU can also be called a processor or a socket (a socket is a place on a motherboard that a CPU is plugged into). A physical/bare metal node or server can have 2/4/8 sockets in x86 architecture. A CPU can have up to 32/28 physical cores (AMD/Intel) or 64/56 virtual cores (with hyper-threading).


## 2) What technology is MongoDB? What is NOSQL? How is it different from Object Storage?


  ### MongoDB calls itself a database but it is commonly known as NoSQL or non-relational database or Not Only SQL, and it was created in 2007 to address the shortcomings or RDMBSs or Relational Databases. The NOSQL database uses key-value, wide column, graph, or document structures, as opposed to tables.  More information about the timeline and MongoDB itself is [here](https://www.mongodb.com/company). A lot more history about NoSQL is [here](https://en.wikipedia.org/wiki/NoSQL). These days there are dozens if not hundreds of databases and everything seems to be converging. The latest innovation is [multi-document ACID transactions](https://www.mongodb.com/blog/post/multi-document-transactions-in-mongodb?jmp=homepage), for instance.
 
 
  ### MongoDB and pretty much all the other databases are meant to organize data in some way to be able to query it and they all have specific tools for interacting with the data. Object Storage stared with [S3](https://aws.amazon.com/s3/) (an AWS service) as a way to solve the scalability, cost and the locking/access issues of the POSIX file systems, especially with unstructured data like multimedia, and it provides a very basic interface  - [REST API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) - for interacting with the data that requires programming skills or specialized clients.
 
 
  ### [Enterprise NoSQL for Dummies by Charlie Brooks](https://github.com/Pomona-ITS/hpc/blob/master/training/materials/Enterprise%20NoSQL%20for%20Dummies%20MarkLogic%20Charlie%20Brooks.pdf)
 

## 3) Biology software and physical/virtual cores. Hyper-threading - good or bad? How many cores to use? 
 
  ### 
 
 
4) Are the VMs "fixed"? Can you grow them on demand?

5) Thin provisioning in storage

6) Will we use Fiber Channel?

7) Can faculty compete in a student competition?

8) XSEDE and moving large datasets - what is the process?

9) Object storage - examples and use cases

10) Does the storage have to be geo-distributed? Multiple data centers?
