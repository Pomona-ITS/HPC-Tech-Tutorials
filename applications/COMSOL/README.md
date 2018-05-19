# This is the page for COMSOL-related information

[COMSOL Multiphysics](https://www.comsol.com/) is a cross-platform finite element analysis, solver and multiphysics simulation software. It allows conventional physics-based user interfaces and coupled systems of partial differential equations.

*from Wikipedia


License: Proprietary EULA


Developer(s): COMSOL Inc


Stable release: 5.3a / December 14, 2017; 4 months ago


## So far COMSOL is only known to be used in Geology ([Eric Grosfils](http://research.pomona.edu/eric-grosfils/publications/)).


### This is the history of our communications and the notes from testing and research that was done:


#### Eric sent the following files to us on January 3rd 2018:


"Todd and Asya,
 
Thanks for the chat this morning! Here are some of the resources I said I’d send along…
 
-- the [2007 paper](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/2007%20JVGR%20Grosfils.pdf) introduces the simple elastic problem we began with. We added a lot of bells and whistles subsequently, but this one lays out the methods etc fairly cleanly.
-- the [2015 paper](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/2015%20GSLSP%20Grosfils%20et%20al%20Elastic%20models%20of%20magma%20reservoir%20mechanics.pdf) summarizes a lot of the work we did from about 2005-2015 or so; written for a more focused volcanology audience, but should give you a sense for the range of things we’ve been doing
-- I won’t send you the viscoelastic papers and elastoplastic/analogue comparisons for the most recent caldera-focused work, but if you want to see that let me know
 
-- I have attached two sets of guidelines used in class… the [Day 2 Lab 12 PDF](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/Day%202%20Lab%2012%20COMSOL%20Inflation%20and%20failure.pdf) write-up is the students’ first introduction to COMSOL (I do a follow-up exercise with them that tests the failure idea; the Day 3 files attached are the ones there… some [brief text](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/Day%203%20Case%20Study.docx), a [Ppt file](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/Day%203%20Inflation%20and%20Unrest%20Case%20Study.pptx) I work through with them, and a starting [COMSOL model *.mph](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/Day%203%202015%20Test.mph)), and the [Day 2 Thermal Modeling PDF](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/Day%202%20Thermal%20Modeling%20in%20COMSOL.pdf) is the guts of the material from the subsequent week when the students work on a time-dependent model.
 
-- Finally, I have attached the [Hirsch Grant proposal](https://github.com/Pomona-ITS/hpc/blob/master/applications/COMSOL/HIRSCH%20GRANT%20APPLICATION.pdf) I submitted that received funding. That project did not commence in S2017 as hoped, so remains on my plate for this spring and coming summer if all goes well. This implementation might make a fun way to test how my local workstation compares with the HPC capabilities if we can get COMSOL interacting with the latter productively.
 
I’ll send a separate email e-introducing you to my local COMSOL contact, she’d be the place to start with respect to the parallelization process’ needs…
 
Cheers!
 
Eric
"



## It seems COMSOL still does not support GPUs or CUDA in a any way except for OpenGL


The official position as of 2016 (CEO Littmark) is the following:


From: http://www.digitaleng.news/de/comsol-conference-2016-performance-is-paramount/


"From a hardware standpoint, the audience was curious about GPU-based simulation. “We haven’t seen that we can do very much. We’ve been looking at it on and off for the last 10 years,” said Littmarck. However, he did add that Multiphysics is multi-threaded for simulation applications and that even non-GPU technology is rapidly advancing. “The hardware always gets better. If you can’t change your methods, just wait,” he said."


There was nothing about GPUs in the [2017 COMSOL conference](https://www.comsol.com/2017-user-presentations/multiphysics).


The most coherent response was from [Niklas Rom in 2013](https://www.comsol.jp/forum/thread/39402/cuda-and-comsol?last=2017-07-31T13:40:16Z):

"We are following the GPU hardware development closely and when we find that
GPUs become useful to solve problems in COMSOL, we will support them.


Currently we see a number of factors that limit the
usefulness of GPUs for solving COMSOL problems. The main solvers in COMSOL
are the direct solvers and the multigrid solvers. 


The direct solvers are very useful to handle strongly coupled smaller size
multiphysics problems, but they also require a lot of memory. Currently,
dedicated general purpose GPUs have about 5-16 GB of internal memory. This
corresponds to small problem sizes for the direct solvers, in the range
where they do not yield a high scalablity on GPUs.


For larger size problems, where multigrid is most efficient, the current
memory available in GPUs is not sufficient. In addition, multigrid solvers
use direct solvers on the coarsest grid, which also means that the
scalability of the coarse grid problem is limited on GPUs."


Still valid response in [2016](https://www.comsol.com/forum/thread/118491/comsol-support-for-gpu-acceleration-for-cfd-simulations?last=2016-07-08T12:31:46Z), apparently.


[NVIDIA GPU Applications catalog](https://www.nvidia.com/content/gpu-applications/PDF/gpu-applications-catalog.pdf) lists only OpenGL.


A [COMSOL Support article](https://www.comsol.com/support/knowledgebase/866/) has some good insights on the recommended hardware otherwise:


"COMSOL Multiphysics can take advantage of all of the available processors (CPU's) in a single shared-memory computer and will by default solve using all available resources, utilizing all CPU's in a single shared-memory computer in parallel. However, there is a computational cost to this parallelization that is a function of model size. Therefore, for models that will use less than 16GB of RAM, a single CPU computer is sufficient and recommended. For models that will use between 16-256GB RAM, a dual-CPU (two-socket) computer is recommended. For models needing more than 256GB RAM, solving on a distributed-memory computer (a cluster) becomes a good option. Please contact COMSOL Technical Support for personalized guidance if you anticipate solving models of such size.


There is no benefit, at this time, of using four-socket or eight-socket motherboard systems to solve very large problems, since these do have slower bus speed than two-socket systems. This slower bus speed outweighs the benefit of the additional sockets.


Number of Memory Channels


COMSOL Multiphysics models are typically very memory-intensive, they pass a lot of data back and forth between the CPU and the RAM memory. This is the primary bottleneck in simulation speed. To maximize the speed at which data is passed back and forth between the CPU and RAM, computers use multi-channel memory bus architecture. Having multiple channels lets data get passed back and forth over different channels at the same time, parallelizing the data transfer. Current generation mid-range CPU's have four memory channels. High-end CPU's have six memory channels.


Memory Speed


Different CPU's support different maximum memory speeds. The installed memory should match the maximum possible memory speed supported by the CPU. Most hardware vendors will do so by default.


The maximum memory speed also depends upon how many DIMM's are installed. For example, a typical four-channel single-CPU computer will have four banks (one for each memory channel) and each of these banks has four open slots for a total of 16 open slots. However, if more than two slots are used in any bank then the memory speed does get reduced. For example, if you want to install 16GB of RAM, then install either 4x4GB or 8x2GB DIMM's, rather than 16x1GB. Also, do not install 1x16GB or 2x8GB DIMM's since then some of the memory channels would be unused.


Number of Cores on the CPU


All CPU's have at least one core per memory channel. Having additional cores on the CPU will enable an additional level of parallelization, but this introduces an additional computational cost. In many cases there is only a marginal benefit (and sometimes even a decrease in performance) to using more than two cores per memory channel. Therefore, for a CPU with four memory channels, consider either a four-core or an eight-core CPU, but not substantially more.


If you already have a computer with substantially more than two cores per memory channel, you can change the number of cores used by COMSOL Multiphysics by supplying the option -np to the COMSOL Multiphysics start command or by changing Number of cores in Preferences under Multicore and Cluster Computing. For example, on a dual-CPU machine with 18 cores per processor there are a total of 36 cores and 8 memory channels. On this dual-CPU machine using only 16 cores often results in optimal performance. The optimal Number of cores setting can depend upon model type, solver choice, and model size.
"

Regarding single computer vs cluster use:


"To solve in parallel on a single computer, use the Batch Sweep functionality. Running parametric sweeps in parallel on a single computer is only advised if one instance of the model itself is relatively small. For example, if one instance of the model requires 3GB of RAM to solve, then it can make sense to run four simultaneous jobs on a 16GB RAM computer. For very small models, ~1GB RAM to solve, you may see an improvement running as many simultaneous jobs as there are cores. The relative speedup when using Batch Sweep is both model- and hardware-dependent.


To solve Parametric Sweeps in parallel on a cluster, use the Cluster Sweep functionality. There is no limit to the number of parallel jobs that you can run at once (up to the number of of available nodes on the cluster.) You can run on your own cluster or use a third-party cluster. COMSOL maintains a list of Technology Partners who provide on-demand computing resources for cluster computations. Each node of the cluster need only meet the requirements described for running a unique model. For further guidance on cluster hardware, see Knowledge Base 1116.


Always consider if you can avoid large sweeps by using the Optimization Module."


"Graphics


We recommend modern AMD FirePro or NVIDIA based dedicated graphics cards. A list of tested graphics cards can be found on the system requirements page. The larger the memory in the graphics card, the more complex models can be visualized. Note that just because a models require large amounts of RAM memory to solve does not necessarily mean it will require a large video card to display, and vice-versa. When using the FNL it is also advantageous to use Client-Server mode.


GPUs


General-purpose computing on graphics processing units (also referred to as GPGPU) or the Intel Phi Co-processor is currently not supported by COMSOL."
