# This page is for documenting the effort to speed up annuity modeling using GPUs

Cole suggested we discuss the possibilities.

Participants:
Austin James Bell <Austin.Bell@pomona.edu>
David R Wallace <David.Wallace@pomona.edu>

Some of the examples of similar work done in the past several years:

[Introduction to Using Graphical Processing Units for Variable Annuity Guarantee Modeling](https://github.com/Pomona-ITS/hpc/blob/master/discovery/business/pdfsecret.com_introduction-to-using-graphical-processing-units-for-variable.pdf)
By Bryon Robidoux
2015

[Annuities Modeling with R](https://github.com/Pomona-ITS/hpc/blob/master/discovery/business/SpedicatoRInInsurance2015.pdf)
Giorgio Alfredo Spedicato, Ph.D C.Stat ACAS
29th June 2015

[Computational Finance](https://github.com/Pomona-ITS/hpc/blob/master/discovery/business/john-ashley-nvidia.pdf)
John Ashley with GPUs: What’s Next?
Solutions Architect, Financial Services
jashley@nvidia.com

[An Actuarial Programming Language](https://github.com/Pomona-ITS/hpc/blob/master/discovery/business/aml.pdf)
for Life Insurance and Pensions
IT University of Copenhagen, Denmark
October 3, 2013

Met: March 8 2018


Forwarded the materials with the details of usign R, helped install RStudio, and R. ~100 time speedup even before GPUs. Have the code, need to spend some time tweaking it for the GPUs.

Web Interface (Shiny) - Andrew's group, need to follow up.

Invited to Research Computing Office Hours.

- using an outsourced consultant
- Monte Carlo simulations
- randomized return
- standard distribution
- 5 1/2 to 6 % a year
- 2 randomizers: return and life expectancy
- efficient rate for different ages
- 1 individual 1000 times 2 min in Excel
- 800 whole portfolio
- web page with ability to model
- avg life span 18
- every iteration 1 calc 2 random
- 100 calc per life
- 
