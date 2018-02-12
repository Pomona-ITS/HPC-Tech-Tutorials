# Jon Saposhnik's answers to my questions about Pascal vs Volta:

P3 EC2 is V100 (NVLink2) roughly $3.30 per hour per V100.  Jonathan or our technical decks we have should be able to help you if you’re having issues w NGC or AWS.
https://aws.amazon.com/blogs/aws/new-amazon-ec2-instances-with-up-to-8-nvidia-tesla-v100-gpus-p3/
 
To answer on Pascal vs Volta, it’s dependent on your workload.  We prefer customers get Volta since it’s optimized for AI and coding/experimentation seem headed so much in this direction. 

For HPC Centers, most are deciding on V100 due improved performance and its NVLink2, but some Universities run HPC w. lots of smaller long tail jobs not much strong or weak scaling for 80% of work.
They bid for most processors for the budget, so the older less expensive Pascal e.g. P100 12GB.  

Volta is faster to Pascal in all the FLOP precisions you mentioned below, adds Tensor Cores, and for HPC codes that stress memory bandwidth and transfer rates is better due to HBM2 and NVLink specs. 



We believe Tensor Cores supported in cuDNN and TensorRT will enable the DL community framework developers we work with and your CS departments algorithm research groups to do much faster modeling w Volta.
 
P100 16GB and V100 16GB  for Universities have large educational rebates of $1,500 each up to 64 units per cluster.
 
The deck attached is good reading for comparison of processors.
 
 
Thank you,
 
 
Regards,
 
Jon Saposhnik | NVIDIA Senior Account Manager | Research Universities
jsaposhnik@nvidia.com | Cell 949.212.6491
2018 NVIDIA GTC Conference, March 26-29 
Register and get 25% off using code NVJSAPOSHNIK
https://2018gputechconf.smarteventscloud.com/portal/registration/NVJSAPOSHNIK
