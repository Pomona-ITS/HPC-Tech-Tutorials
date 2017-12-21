# This is the page that summarizes the premise for President Starr's Research Infrastructure Setup 

## History:

View Description for Issue 72873 (Footprints)

Entered on 12/19/2017 at 9:32:30 AM PST (GMT-0800) by Todd Shimoda:
President Starr's research data will arrive from NYU on Thursday December 21 in an external hard drive, with a backup hard drive mirror. The data is encrypted to current Mac standards so it needs High Sierra to read.

 

The data will need to be stored locally. Access to the storage will be granted to Gabi, several of her non-Pomona research colleagues, and Pomona ITS staff (Pat, Asya, Todd). Depending on how the access is set up, non-Pomona staff may need sponsored accounts.

 

Also, Gabi's research colleague, Ed Vessel who works in Germany, will need a machine/workstation here at Pomona he could remote into to avoid the lag in data IO. The software used are Matlab and Freesurfer:

 

Summary of Requirements:
 Operating System: Linux, macOS
 Processor Speed: 2GHz at least
 RAM: 8GB recommended
 Graphics card: 3D graphics card with its own graphics memory & accelerated OpenGL drivers
 Size of installation package: 10GB
 Typical size of a processed subject: 300MB
Other requirements: Matlab (only needed to run FS-FAST, the fMRI analysis stream)

 

I assume this would have to be a Mac workstation to accommodate the requirements.

 

The contact at NYU is Bruce Padron:

 Bruce Richard Padron | IT Support Specialist | New York University College Of Arts & Science 
100 Washington Square East. Suite 920A | New York, NY 10003 | 212.998.8538 | brp226@nyu.edu | cas.nyu.edu

-----------------------------------------------------------------------------------------------------------
After a meeting with Todd, Julie, and Pat the following options were considered:

1) putting all this on Gabi’s workstation in her office with a USB attached RAID6 box and a container to run the software to isolate the remote researcher from Gabi's user environment. A security concern with the remote access from Germany was raised.

2) putting it all on a VM on our infrastructure which could  be slow and create problems for the existing VMs; plus the same security risk.
 
3) The AWS solution detailed below: 
 
The data (fMRI images, brain scans, 1,5 TB) is arriving from NYU tomorrow and will be decrypted and transferred from the shipping drives by Julie/Mel to a local network location determined by Pat (and shared with Asya for potential transfer to AWS S3).

A collaborator from Germany needs access to Matlab (could use free 30 day trial license) and FreeSurfer (fMRI processing software, free, open source) to generate the results for Gabi’s research.

Cole/Pat share the AWS credentials with Asya.

Gabi/German researcher share the details of the workflow. Command line, input/output parameters.

Asya:

Use Ansible or Chef as a template that could be reused later
Set up a separate IAM account for that user with only certain permissions
Give that user access to S3 bucket with the source data (fMRI images)
Build an EC2 instance with the parameters requested by Gabi with the software required and a local fast EBS volume that will get the data from the S3 bucket, run what is needed for analysis and save the results back to the S3 bucket from where they can be downloaded by Gabi later
The whole thing can be tagged with the project name for the cost analysis
It gets shut down when the analysis is done or when a more permanent solution is discovered

Can also enable logging for S3 and EC2 in CloudTrail and  demo an ELK (Elasticsearch) visualization of log data at the end of this exercise. AWS recently launched an ELK as a Service so no need to install locally. Or we can use logz.io. They have been doing this since 2015.
 
https://logz.io/blog/integrate-aws-cloudtrail-elk-stack/
 
Stanford had made FreeSurfer software available as a container so this environment could be imported from Stanford, versioned in GitHub for our needs (if we modify it in any way) and reproduced later on our infrastructure exactly the same as in AWS. There is a Singularity (a type of more secure than Docker container platform) setup at Biowulf (NIH) – this is similar to the setup we will have on our HPC when we build it!
 
https://hpc.nih.gov/apps/Freesurfer.html
 
