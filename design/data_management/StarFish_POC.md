# This page is for documenting StarFish POC

This is a software solution to querying POSIX metadata.

This [White Paper](https://github.com/Pomona-ITS/hpc/blob/master/design/data_management/Starfish%20Whitepaper.pdf) explains it very comprehensively.

Had a call with the vendor, waiting for the VM setup and a quote for 30 TB.

Targeting primarily CS data discovery but can expand as necessary.

## Pricing Discussion (No official quote yet):

2 factors: capacity and functionality

report - base module

file movement add-on

whole thing or reporter

start at 1 PB

annual - reporter - 1 PB - $53K

full blown - $130K


Discussed with COO, $10-15K is a possibility because we are small and they are interested in us as a customer.

Limited at 50-60 TB


## Instructions for POC Setup:

Hi Asya,

In preparation for Thursday's install, please download our install
script on the Starfish server using the following command:
wget "https://starfishstorage.bintray.com/files/stable/install-Starfish.sh?expiry=1532458131889&id=XJDs9T%2Bn9H8h7x79SSi1LRU1O4Ac6IorBo9XnwrRrJk%3D&signature=eUIMiV1sWVVAtOz0JTr9kJxvuxPBIzeKTfvhsj4NxkORDiTBuze4QEnIuJeA9PBkjXkrb%2BWurL0c1yghauFLtg%3D%3D"
-O install-Starfish.sh

You can also pull it down via a web browser via the following link:

  https://starfishstorage.bintray.com/files/stable/install-Starfish.sh?expiry=1532458131889&id=XJDs9T%2Bn9H8h7x79SSi1LRU1O4Ac6IorBo9XnwrRrJk%3D&signature=eUIMiV1sWVVAtOz0JTr9kJxvuxPBIzeKTfvhsj4NxkORDiTBuze4QEnIuJeA9PBkjXkrb%2BWurL0c1yghauFLtg%3D%3D

This URL is good for 7 days. Once we use the installer, you won't need
it again, since updates will be done via a standard rpm update (yum or
apt-get)

Also attached is a license file. This should be put into the same
directory as the installer is downloaded into, and is good through
September 17, 2018.


We'll use the following instructions for the install. It is a quick
install, please wait to run the following until our web meeting.

1. Run the following command to extract the installation script:

    bash install-Starfish.sh

2. Read the Starfish EULA and type 'yes' if you accept its conditions.
3. Answer the questions posed:

  Repository URL:
  Centos/Redhat 6 or 7:

    https://pomona%40starfishstorage:2ae4578c7647d82621bfc20c9b0202f92a92cf57@starfishstorage.bintray.com/starfish_yum_v4

  Ubuntu 14 or 16:

    https://pomona%40starfishstorage:2ae4578c7647d82621bfc20c9b0202f92a92cf57@starfishstorage.bintray.com/starfish_apt_v4

4. Verify Starfish via "sf check-config" command, redash and Starfish
GUI by connecting with a web browser to https:\\sfserver\redash and
https:\\sfserver respectively.

I've attached the install and configuration guides as well.

If you have any questions in the meantime, let me know.


--
Dave Gold  |  Support Engineer  |

dgold@starfishstorage.com | www.starfishstorage.com | 781-301-7505

Contact Support at support@starfishstorage.com or 781-301-7500, option 2
