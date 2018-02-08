# This is the summary page for Cisco.

The discussions are facilitated by Presidio so this page is for the technical details and Cisco-specific information.
The quotes are in Presidio folder.

UCS/UCLA using UCS for HPC (asked for actual use cases, follow up).

One example was given of Neuroimaging department using the reconfigurable hardware profiles. Asked for more details.

Cisco engineers had suggested we use 6248 (next gen / 40 GB) instead of the current network modules (10 GB?)

The recommended blade models for [HPC](https://blogs.cisco.com/datacenter/cisco-ucs-delivers-industry-leading-gpu-density) are:

1) half-width 2 socket [B200 M5](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/Cisco/technical_documentation/datasheet-c78-739296.pdf)

2) full width 4 socket [B480 M5](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/Cisco/technical_documentation/datasheet-c78-739280.pdf)

Both require the [5108](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/Cisco/technical_documentation/spec_sheet_c17-644224.pdf) chassis.

The slide deck describing the options available for HPC is [here](https://github.com/Pomona-ITS/hpc/blob/master/design/vendors/Presidio/UCS-Customer%20Update%20.pdf).

The 6U chassis can accommodate any combination of two blades:

4 full-width 
or 2 full-width and 4 half-width 
or 8 half-width
or 1 full-width and 6 half-width

There are 12 channels per socket so the 2 socket blade can have max 3 TB of RAM (128 GB modules)
and the 4 socket blade can have 6 TB (128 GB modules).
The most economical RAM modules are 32 GB.

During the discussions with the users majority did not ask for more than 768 GB (2 socket with 24 x 32 GB).
One user said they could use 1.5 TB (2 socket with 24 x 64 GB modules or 4 socket with 48 x 32 GB modules).
One user saw potentially using as much as 3 or 6 TBs of RAM but can work with 1.5 TB for now.

The latest generation of Intel CPU (Skylake, 28 core) is the M5 series.

The previous generation of Intel CPU (Broadwell) is M4 series.

Currently M5 does not support Volta GPUs (waiting for confirmation. We could wait till they are supported and them later
or go with a Silicon Mechanics system where V100 is supported.

Currently Cisco does not support AMD CPUs and Epyc (32 core) would have to be procured from another vendor if we wanted
the highest possible core count in a system. It may make sense to wait till the [next iteration of Epyc](https://www.forbes.com/sites/davealtavilla/2017/10/31/amds-next-gen-big-iron-epyc-server-cpu-rumored-to-pack-64-cores-and-boatloads-of-cache/#dced82c5cc60) (6 months?)
which will be 64 cores per socket (and use hyperthreading) so potentially up to 128 virtual cores per socket and
256 virtual cores in a 2 socket system.



After the Tech Day at the Cisco office in Irvine on February 7. *Add the slides here
we are considering HyperFlex as the potential platform for HPC, mainly because:

1) It is the next generation of hardware, comparable or better to the regular compute blades; M4 and M5 can be mixed, can add compute blades as well
2) It is truly converged because the compute and storage are in the same server, all-flash blades are available and the file system is [log structured](https://en.wikipedia.org/wiki/Log-structured_file_system) instead of VNX/Block
3) Integration with InterSight is better (if we end up managing multiple hypervisors and clouds it is a plus)
4) Tools like Tetration are really cool - packet level visibility into East-West (Host) traffic with a lightweigh C-based agent, machine learning and automatic policy suggestions that can be fed to SourceFire or StealthWatch, integration with Talos and more.



