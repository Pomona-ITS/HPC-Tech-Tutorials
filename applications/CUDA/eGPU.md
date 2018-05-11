# This is a place to describe experimentation with eGPU (external GPU) and R

## Using a Bizon eGPU Enclosure with a MacBook Pro:

```
  Model Identifier:	MacBookPro14,3
  Processor Name:	Intel Core i7
  Processor Speed:	3.1 GHz
  Number of Processors:	1
  Total Number of Cores:	4
  L2 Cache (per Core):	256 KB
  L3 Cache:	8 MB
  Memory:	16 GB
  Boot ROM Version:	MBP143.0169.B00
  SMC Version (system):	2.45f0
  Serial Number (system):	C02V42D2HTD9
  Hardware UUID:	17DE12D8-014F-5852-A338-BFB7CABCF3C0

```

```
macOS High Sierra 10.13.3
MacBook Pro (15-inch, 2017)
Processor 3.1 GHz Intel Core i7
Memory 16 GB 2133 MHz LPDDR3
Radeon Pro 560 4 GB
Intel HD Graphics 630 1536 MB
```

```
AKiTiO Thunder3 PCIe Box with NVIDIA GeForce 1080 (Asya's Personal eGPU)

  Vendor Name:	inXtron
  Device Name:	AKiTiO Thunder3 PCIe Box
  Vendor ID:	0x41
  Device ID:	0x305
  Device Revision:	0x1
  UID:	0x0041771E8D586700
  Route String:	1
  Firmware Version:	19.1
  Port (Upstream):
  Status:	Device connected
  Link Status:	0x2
  Speed:	Up to 40 Gb/s x1
  Current Link Width:	0x2
  Link Controller Firmware Version:	0.30.0
  Port:
  Status:	No device connected
  Link Status:	0x7
  Speed:	Up to 40 Gb/s x1
  Current Link Width:	0x1
  Link Controller Firmware Version:	0.30.0

```

```
CUDA Toolkit 9.1:

cuda_9.1.128_mac.dmg

```

```
Bizon Box and NVIDIA associated drivers:

WebDriver-387.10.10.10.25.158.pkg (the driver specified in the installation manual was too old and did not work with the latest update of High Sierra - 156)
cudadriver_387.128_macos.dmg
NVDAEGPUSupport-v6.pkg (again, there was a NVDAEGPUSupport-v7.pkg available)

```

CUDA Mac Installation Guide is [here](https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html).

```
AsyaShklyer-mac68:~ asaj2017$ /usr/bin/cc --version
Apple LLVM version 9.0.0 (clang-900.0.39.2)
Target: x86_64-apple-darwin17.4.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

```
AsyaShklyer-mac68:~ asaj2017$ kextstat | grep -i cuda
  182    0 0xffffff7f80f32000 0x2000     0x2000     com.nvidia.CUDA (1.1.0) 4329B052-6C8A-3900-8E83-744487AEDEF1 <4 1>
```

```
export PATH=/Developer/NVIDIA/CUDA-9.1/bin${PATH:+:${PATH}}
export DYLD_LIBRARY_PATH=/Developer/NVIDIA/CUDA-9.1/lib\
                         ${DYLD_LIBRARY_PATH:+:${DYLD_LIBRARY_PATH}}
```

```
AsyaShklyer-mac68:NVIDIA asaj2017$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2017 NVIDIA Corporation
Built on Tue_Dec_19_21:36:29_CST_2017
Cuda compilation tools, release 9.1, V9.1.128
```

```
AsyaShklyer-mac68:samples asaj2017$ sudo make -C 0_Simple/vectorAdd
Password:
/Developer/NVIDIA/CUDA-9.1/bin/nvcc -ccbin clang++ -I../../common/inc  -m64  -Xcompiler -arch -Xcompiler x86_64  -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_70,code=compute_70 -o vectorAdd.o -c vectorAdd.cu
/Developer/NVIDIA/CUDA-9.1/bin/nvcc -ccbin clang++   -m64  -Xcompiler -arch -Xcompiler x86_64  -Xlinker -rpath -Xlinker /Developer/NVIDIA/CUDA-9.1/lib  -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_70,code=compute_70 -o vectorAdd vectorAdd.o
mkdir -p ../../bin/x86_64/darwin/release
cp vectorAdd ../../bin/x86_64/darwin/release
```

```
make -C 0_Simple/vectorAddDrv
make -C 1_Utilities/deviceQuery
make -C 1_Utilities/bandwidthTest
```

```
sudo make
```

```
syaShklyer-mac68:release asaj2017$ ./deviceQuery
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

cudaGetDeviceCount returned 35
-> CUDA driver version is insufficient for CUDA runtime version
Result = FAIL
```

Ended up bricking the Mac because of incompatibilities and High Sierra issues and switched to Windows for now.



Side note: there is no nvidia-smi for Mac. There is another tools that is a good vizalaization tool called [XRG](http://www.gauchosoft.com/Products/XRG/). Had to be compiled so XCode and command line tools required.


## Reboot after the [announcement](https://support.apple.com/en-us/HT208544) that eGPUs are now officially supported on Macs and an OS update:

```

  Model Name:	MacBook Pro
  Model Identifier:	MacBookPro14,3
  Processor Name:	Intel Core i7
  Processor Speed:	3.1 GHz
  Number of Processors:	1
  Total Number of Cores:	4
  L2 Cache (per Core):	256 KB
  L3 Cache:	8 MB
  Memory:	16 GB
  Boot ROM Version:	MBP143.0173.B00
  SMC Version (system):	2.45f0
  Serial Number (system):	C02V42D2HTD9
  Hardware UUID:	17DE12D8-014F-5852-A338-BFB7CABCF3C0



```

```

  System Version:	macOS 10.13.4 (17E202)
  Kernel Version:	Darwin 17.5.0
  Boot Volume:	Macintosh HD
  Boot Mode:	Normal
  Computer Name:	asaj2017-mac68
  User Name:	Asya Shklyar (asaj2017)
  Secure Virtual Memory:	Enabled
  System Integrity Protection:	Disabled
  Time since boot:	4:46


```

XCode update



WebDriver-387.10.10.10.30.107.pkg (Recommended 103 did not work, said not OS compatible)
Reboot





Downloaded ( by guessing ) https://bizon-tech.com/a/nvidia-egpu-v9.zip


NVDAEGPUSupport-v9.pkg
Reboot

Download http://bizon-tech.com/bizonboxmac.zip
May 2017

References: 

https://egpu.io/forums/mac-setup/wip-nvidia-egpu-support-for-high-sierra/paged/41/#post-33831

https://egpu.io/forums/mac-setup/wip-nvidia-egpu-support-for-high-sierra/

https://www.tonymacx86.com/threads/nvidia-releases-alternate-graphics-drivers-for-macos-high-sierra-10-13-4-387-10-10-10-30.249039/



https://raw.githubusercontent.com/learex/macOS-eGPU/master/macOS-eGPU.sh

http://www.nvidia.com/object/macosx-cuda-9.0.214-driver.html



Giving up. Screenshots below.

![BizonBox software refusing to detect the eGPU](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%205.34.09%20PM.png)

![The latest NVIDIA Web driver Install Successful](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%205.44.35%20PM.png)

![NVIDIA EGPU Support driver Install Successful](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%205.50.15%20PM.png)

![The version of the BizonBox Device Manager](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%206.05.03%20PM.png)

![macOS eGPU script that sorta worked but no cigar 1](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%206.20.13%20PM.png)

![macOS eGPU script that sorta worked but no cigar 2](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%206.20.41%20PM.png)

![macOS eGPU script that sorta worked but no cigar 3](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-10%20at%206.23.37%20PM.png)

![After reboot and bricking the OS and a reinstall - 107 not compatible](https://github.com/Pomona-ITS/hpc/blob/master/applications/CUDA/Screen%20Shot%202018-05-11%20at%2011.05.32%20AM.png)

GRRRRRRR

On to the AMD EGPU:

[Sonnet eGFX Breakaway Puck Radeon RX 570 (Mac & Windows Compatible)](https://www.amazon.com/Sonnet-Breakaway-Radeon-Windows-Compatible/dp/B076MHMF3V) $599

