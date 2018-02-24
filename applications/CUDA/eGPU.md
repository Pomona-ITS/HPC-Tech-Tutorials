# This is a place to describe experimentation with eGPU (external GPU) and R

Using a Bizon eGPU Enclosure with a MacBook Pro:

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

WebDriver-387.10.10.10.25.158.pkg
cudadriver_387.128_macos.dmg
NVDAEGPUSupport-v6.pkg

```

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

