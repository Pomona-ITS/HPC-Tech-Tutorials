# NVIDIA is the leading GPU manufacturer. [AMD]() is a competing GPU vendor and is listed in a separate folder.  
[Intel](https://arstechnica.com/gadgets/2017/11/intel-poaches-amds-top-gpu-architect-to-build-its-own-discrete-graphics-chips/) is also entering the comptetition with a new AMD-based GPU with shared CPU-GPU RAM.

[DGX Family Overview is here](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/NVIDIA/dgx-family-e-book-20170817-r13.pdf). Basically there are 2, a workstation and a rack-mountable server with different quantities of GPU cores and storage. Sold by vendors approved by NVIDIA (including Microway which we were considering for SuperMicro hardware
because Bowdoin used them.

DGX Workstation specs are [here](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/NVIDIA/dgx-station-data-science-supercomputer-datasheet-10232017.pdf). 

[IDC report on DGX Workstation](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/NVIDIA/IDC-Spotlight-on-DGX-Station.pdf).

DGX-1 rack-mountable system specs are [here](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/NVIDIA/NVIDIA-DGX-1-Volta-AI-Supercomputer-Datasheet%20(1).pdf).

The latest GPU architecture is called Volta.

The architectures before that were Pascal, Maxwell, Kepler. Since Volta just came out they are expensive.
Pascal-based cards may be more economical.

The brand name for the server cards is Tesla.

The actual models we are considering for our environment are V100 (Volta) and P100 (Pascal).

There are also blade versions of both and vGPU/Remote Desktop/App/Visualization versions of both.
