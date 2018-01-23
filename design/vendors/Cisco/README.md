This is the summary page for Cisco.

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
