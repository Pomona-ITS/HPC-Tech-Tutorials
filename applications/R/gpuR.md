# gpuR is the official R package for working with GPUs and CUDA

[This](https://cran.r-project.org/web/packages/gpuR/gpuR.pdf) is the official page for gpuR.

Install [R](https://www.r-project.org/) and [RTools](https://cran.r-project.org/bin/windows/Rtools/)(for building packages from source).

Install gpuR: 

```

> install.packages('gpuR')
Warning in install.packages("gpuR") :
  'lib = "C:/Program Files/R/R-3.4.3/library"' is not writable
--- Please select a CRAN mirror for use in this session ---
also installing the dependencies ‘mime’, ‘glue’, ‘magrittr’, ‘stringi’, ‘evaluate’, ‘highr’, ‘markdown’, ‘stringr’, ‘yaml’, ‘assertive.base’, ‘assertive.properties’, ‘assertive.types’, ‘assertive.numbers’, ‘assertive.strings’, ‘assertive.datetimes’, ‘assertive.files’, ‘assertive.sets’, ‘assertive.matrices’, ‘assertive.models’, ‘assertive.data’, ‘assertive.data.uk’, ‘assertive.data.us’, ‘assertive.reflection’, ‘assertive.code’, ‘knitr’, ‘Rcpp’, ‘assertive’, ‘RcppEigen’, ‘RViennaCL’, ‘BH’

Package which is only available in source form, and may need
  compilation of C/C++/Fortran: ‘gpuR’
Do you want to attempt to install these from sources?
y/n: 

```

Installed as personal library, might have to change that if we do standard software builds for people.


```
Number of platforms: 2
- platform: Intel(R) Corporation: OpenCL 2.1 
  - context device index: 0
    - Intel(R) HD Graphics 630
  - context device index: 1
    - Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- platform: NVIDIA Corporation: OpenCL 1.2 CUDA 9.1.83
  - context device index: 0
    - GeForce GTX 1080 Ti
  - context device index: 1
    - GeForce GTX 1050
checked all devices
completed initialization
*** arch - x64
Number of platforms: 2
- platform: Intel(R) Corporation: OpenCL 2.1 
  - context device index: 0
    - Intel(R) HD Graphics 630
  - context device index: 1
    - Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- platform: NVIDIA Corporation: OpenCL 1.2 CUDA 9.1.83
  - context device index: 0
    - GeForce GTX 1080 Ti
  - context device index: 1
    - GeForce GTX 1050
checked all devices
completed initialization
* DONE (gpuR)
In R CMD INSTALL

The downloaded source packages are in
        ‘C:\Users\asya_\AppData\Local\Temp\RtmpKgPnBK\downloaded_packages’


```

Load the gpuR library:


```
> library("gpuR")
Number of platforms: 2
- platform: Intel(R) Corporation: OpenCL 2.1 
  - context device index: 0
    - Intel(R) HD Graphics 630
  - context device index: 1
    - Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- platform: NVIDIA Corporation: OpenCL 1.2 CUDA 9.1.83
  - context device index: 0
    - GeForce GTX 1080 Ti
  - context device index: 1
    - GeForce GTX 1050
checked all devices
completed initialization
gpuR 2.0.0

Attaching package: ‘gpuR’

The following objects are masked from ‘package:base’:

    colnames, pmax, pmin, svd
```

List Contexts (OpenCL or CUDA with respective GPUs):

```
listContexts()
```

```
  context                                   platform platform_index
1       1          Intel(R) Corporation: OpenCL 2.1               0
2       2          Intel(R) Corporation: OpenCL 2.1               0
3       3 NVIDIA Corporation: OpenCL 1.2 CUDA 9.1.83              1
4       4 NVIDIA Corporation: OpenCL 1.2 CUDA 9.1.83              1
                                     device device_index device_type
1                  Intel(R) HD Graphics 630            0         gpu
2 Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz            0         cpu
3                       GeForce GTX 1080 Ti            0         gpu
4                          GeForce GTX 1050            0         gpu

```

Benchmarking CPU vs built-in 1050 vs eGPU (1080 Ti):

```
> setContext(1L)
> A <- vclMatrix(rnorm(10000), 100, 100)
> B <- vclMatrix(rnorm(10000), 100, 100)
> system.time(A %*% B) 
   user  system elapsed 
   1.53    0.09    1.62 
```

```
> setContext(2L)
> C <- vclMatrix(rnorm(10000), 100, 100)
> D <- vclMatrix(rnorm(10000), 100, 100)
> system.time(C %*% D) 
   user  system elapsed 
   2.50    0.00    2.51 
```
   
   
```
> setContext(3L)
> E <- vclMatrix(rnorm(10000), 100, 100)
> F <- vclMatrix(rnorm(10000), 100, 100)
> system.time(E %*% F) 
   user  system elapsed 
   0.56    0.05    1.05 
```
   
```
> setContext(4L)
> G <- vclMatrix(rnorm(10000), 100, 100)
> H <- vclMatrix(rnorm(10000), 100, 100)
> system.time(G %*% H) 
   user  system elapsed 
   0.01    0.00    0.01 
```
