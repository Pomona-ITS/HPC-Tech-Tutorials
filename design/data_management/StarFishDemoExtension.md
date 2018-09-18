# This is to document extending the demo (done on September 18 2018)

Hi Asya,

Please find attached a 60 day extension to your Starfish POC.

To activate:
1. Rename /opt/starfish/etc/license to license.old
2. Copy the attached file in as /opt/starfish/etc/license
3. Cycle Starfish services: service supervisord restart;service sf-agent restart
4. Verify that the license shows properly in the output of 'sf check-config'

If you have any questions, don't hesitate to contact us.

Dave
-- 
Dave Gold  |  Support Engineer  |  

dgold@starfishstorage.com | www.starfishstorage.com | 781-301-7505

Contact Support at support@starfishstorage.com or 781-301-7500, option 2
