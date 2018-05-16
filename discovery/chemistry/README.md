# This is a page for documenting the progress of discovering the needs of the Chemistry department

## The follow up meeting May 15 2018

Clarifications:

- Gaussian version in use today is 09 and Gaussian is #1 priority because of a research student who is starting within 2 weeks. Bob Cave (and Robert Kingston who is implementing the Gaussian-related work according to Maduka) are managing the license acquisition process, the license is "site" and includes 5Cs. And is unlimited. Dan will introduce Todd and Asya to Bob and Robert to verify and get access to pricing/downloads/support. Gaussian uses a lot of scratch space. GBs. According to Dan in December there was talk of ITS having access to the Gaussian licenses. Asya checked with Steven Hurtdado - he does not recall. Need to follow up.

* Gaussian is very touchy about anyone using non-Gaussian software or comparing it to Gaussian in any way. While it is possible to evaluate the options we have to be careful because Gaussian is known to block whole colleges from using their software if even just one researcher using any competitor's software.

Asya had shared the new features in Gaussian 16 and GaussView 6 and likely the most exciting part is support for GPUs. We could install both 09 and 16 in HPC and gradually migrate what makes sense to migrate for speed up.
The links for more information are below.

- Spartan is indeed Windows, the license is fixed, 18 seats, costs $2,500 yearly. Talk to Steven Hurtado/ITS about possibly taking over.

- Schroedinger Maestro is token-based, 20 concurrent ones. Multiple programs but different usage. This could change in July-August. Dan will forward the information about the license. $1,500 a year?

- Sybil (sp?) for confirmational (sp?) searches. Expensive.

- None of the software ever gets patched. "If it works we leave it alone".

### The rough plan of action:

- Asya will build 2 VMs on existing Enterprise infrastructure, one for student(s), one for research (DAN).
These are meant to replace pauling and urey. The data will have to be migrated. The accounts will be created using AD. The ownership/permissions will need to be fixed.
- The new research student will test the environment (pauling and urey are the backup)
- Maduka and Dan will provide access to the installables for all the software, with the primary focus on Gaussian.
- Dan will make an intro to Bob and Robert at Harvey Mudd
- Asya and Todd will meet with Bob and Robert to discuss the HPC arrangement
- Maduka will continue collaborating with Dan after he leaves on June 30th so his account in AD will remain (sponsored) and he could continue using the HPC environment
- HPC environment will have both 09 and 16 and Asya will teach them how to choose
- We will benchmark with Maduka's examples and identify the ideal number of cores for each job
- We will need to procure Lynda for multi-node jobs (not currently used)




## The first meeting with Dan and Maduka were at the end of January 2018.

We learned that Maduka was shortly leaving for a full time position.

We discussed the following:

- simple process: account - GUI - submit jobs
- 2 x 24 core machines
- shell errors
- peak usage, not 100%
- Schroedinger - don't know how to set it up in HPC
- 3 research students
- new grant for a spectrometer
- 200 atom systems
- 10-20 / small molecule
- Mostly Windows
- Ghost files after job crash (read/write)
- Teaching inorganic course
- Biochemists
- Spartan ~20 seats, $2,500 yearly
- Lab Coordinator
- Data Management
- Bob Cave Harvey Mudd license for Gaussian?
- chemdraw


