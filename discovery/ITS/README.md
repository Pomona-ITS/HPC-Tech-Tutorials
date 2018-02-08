This is a place for ITS-related documentation, procedures, links to other resources 
as it pertains to HPC environment design, build and support.

1. AD, integration, user-creation

   Pat is in charge of AD. AD is Pomona only, no trusted relationships with any other ADs (HM has their own).
   When external users need an account on a Pomona Linux system they fill out a form (and are added to Pomona AD?).
   
   Currently the only server using the AD integration is RStudio. PAM/oddjob is used for auto-creation of user directories.
   The current list of users is here.
   All Pomona AD users have access to RStudio by default.

   a) The form for (external) user creation - Jonathan
   
   
   b) Windows Unix Services?
   

2. Logging and Monitoring

check_mk is currently used for up/down/service monitoring on the systems level
https://openmon.pomona.edu/

Managed by the Infrastructure team, to get access submit a ticket in FootPrints (Pat)

InterMapper is used for Network Monitoring (Pat)

VMWare vCenter is used for Virtual Infrastructure Management and Monitoring (Pat)

3. DR

4. Security
