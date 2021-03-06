Nutanix is a cloud computing software company that sells what it calls hyper-converged infrastructure appliances 
and software-defined storage. Nutanix was founded in 2009 by Dheeraj Pandey, Mohit Aron and Ajeet Singh. 
The engineers came from Citrix and Google. The storage design was inspired by [Google Distributed File System](https://en.wikipedia.org/wiki/Google_File_System) 
and AHV (Acropolis Hyper Visor) is KVM-based.

https://www.nutanix.com/

Nutanix is in direct competition with VMWare (and Cisco), and aims to simplify provisioning and maintaning the data centre infrastructure, from application deployment (via calm.io acquisition) to the integrated storage, to supporting non-Nutanix hardware, including Cisco UCS, and even allowing to run on a different hypervisor (and migrate off ESXi without having to rebuild VMs).

Other HCI solutions are

- HPE's acquisition of Springtivity
- Cisco's acquisition of Springpath


Todd and Asya had an introductory call with Nutanix.
Asya's meeting notes are [here]().
The slides presented by Nutanix are [here](https://github.com/Pomona-ITS/hpc/blob/0bade9fcc07f80f644ac345d5bbd3d1fe3f86a85/design/vendors/Nutanix/Materials/LA%20General%20Deck.pptx).

Asya had downloaded a community edition version of Nutanix to kick the tires.

Nutanix is attractive because it:

1. is easier to deploy and manage than VMWare
2. is compatible with VMWare
3. is hyperconverged, when you provision storage you provision compute and vice versa so the performance does not suffer
4. has been used in HPC successfully
5. has the developer tools/lifecycle tools; it is not pure infgrastructure
6. allows to integrate seamlessly with the public clouds and migrate/expand our workloads there when  necessary

https://www.nextplatform.com/2017/11/09/nutanix-expands-adds-breadth-cloud-platform/
