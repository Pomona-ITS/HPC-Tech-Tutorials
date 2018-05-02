# This is the place for the interim networking information as the environment is built out

## The VLANs for storage (Pure)

RFC : Create VLAN for HPC enviorment
RFC #: 5815

Full Description:
Entered on 03/20/2018 at 2:42:04 PM PDT (GMT-0700) by Pat Flannery:
Addition of new network VLANs for HPC environment.

This request is for the creation of necessary VLANs to support HPC Iscsi storage networking

Create VLANs 322 (POM-HPC-ISCSI1) and 323 (POM-HPC-ISCSI2) on core switches No creation of SVI for these networks will be done at this time.

Create VLAN 324 (POM-HPC-MGMT), create SVI for the interface, Set ACL initial access to ITS-STAFF network.

IP address space allocated for these networks is:
VLAN322 10.34.0.0/16
VLAN323 10.36.0.0/16
VLAN324 10.38.0.0/16
