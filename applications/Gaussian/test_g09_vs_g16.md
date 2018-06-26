# This is for documenting the experiment with a job Dan O'Leary runs on g09 with a new version of Gaussian with GPUs



 
```
The Gaussian command line for starting a job would be:
 
g09 SFG_4_endo_b3lyp631plusgdp_1_nqcc.gjf SFG_4_endo_b3lyp631plusgdp_1_nqcc.log &
 
 
at the top of the input file (*.gjf), you’ll see where you can adjust the number of processors and the allocation of memory for the job:
 
 
%nprocshared=23
%mem=40GB
%chk=SFG_4_endo_b3lyp631plusgdp_1_nqcc.chk
# nmr=(giao,spinspin) rb3lyp/6-31g(df,3p) output=pickett
 
Title Card Required
```



[Input File](https://github.com/Pomona-ITS/hpc/blob/master/applications/Gaussian/SFG_4_endo_b3lyp631plusgdp_1_nqcc.gjf)

Ran about an hour and a half. This is g09, 24 cores, 40 GB RAM, local VM disk, /tmp scratch

Log is [here](https://github.com/Pomona-ITS/hpc/blob/master/applications/Gaussian/SFG_4_endo_b3lyp631plusgdp_1_nqcc.log).
