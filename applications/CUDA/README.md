# This is a place for everything that has to do with CUDA

[CUDA](https://en.wikipedia.org/wiki/CUDA) is a parallel computing platform and application programming interface model created by [Nvidia](https://www.nvidia.com). 

CUDA was created for general computing on graphical processing units (GPUs). With CUDA, developers are able to dramatically speed up computing applications by harnessing the power of GPUs.

In GPU-accelerated applications, the sequential part of the workload runs on the CPU – which is optimized for single-threaded performance – while the compute intensive portion of the application runs on thousands of GPU cores in parallel. When using CUDA, developers program in popular languages such as C, C++, Fortran, Python and MATLAB and express parallelism through extensions in the form of a few basic keywords.

The CUDA Toolkit from NVIDIA provides everything you need to develop GPU-accelerated applications. The CUDA Toolkit includes GPU-accelerated libraries, a compiler, development tools and the CUDA runtime.

It should be mentioned that CUDA is a proprietary and non-open-source technology from NVIDIA and there is an alternative - OpenCL. Originally developed by Apple and now supported by Kronos Group. It is an open standard with implementations from multiple vendors. NVIDIA supports both CUDA andf OpenCL. AMD GPUs support only OpenCL. Some applications support both. More information is [here](https://create.pro/blog/opencl-vs-cuda/).

CUDA Docs are [here](https://docs.nvidia.com/cuda/).
