# For documenting shell.cs.pomona.edu - the Academic DMZ VM with two interfaces, internal and external, owned by Michael Greenberg from CS

History is in the Footprints ticket 74241.

Internal: 192.168.2.64 (no name resolution yet, Pat is working on it). Can ssh from the internal (campus) network.

External: 134.173.93.18 (resolves to shell.cs.pomona.edu). This DNS server is managed by CS/Corey).

The following DNS servers needed to be in /etc/resolv.conf: 134.173.69.6 and 134.173.64.6.

Not using AD, local accounts only. So far two accounts: asya and mgreenberg, both in sudo.

Ansible is installed.

All the necessary files will be in GitHub and installable by Ansible to the best of effort.
