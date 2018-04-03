Good morning!!!
 
Thanks for volunteering to kick around the Slack slash command we’ve been tinkering with. Some info below.
Please if you encounter weirdness, feel free to let me know or ignore it. This is supposed to be FUN. There is a small group of users kicking this around and learning what works.
 
The slash command is “/pom-tickets”.
 
/pom-tickets
Should show you a list of the tickets you are assigned to.
If you have not yet registered your Footprints username with the app, it should prompt you for that first. Then try /pom-tickets again.
 
/pom-tickets [Footprints username]
Ex: /pom-tickets acc04747
Should show you the open tickets assigned to any Footprints username you specify.
 
/pom-tickets search [search string, no quotes needed]
Ex: /pom-tickets search Oh my God help me
Note the keyword “search” before the search string. That’s needed.
Should show you open tickets containing that search string in either the title or ticket description.
Searches are cross-workspace – both the Service Desk and Change Management workspaces get searched.
 
/pom-tickets cab
Should show you the tickets currently in “Awaiting CAB Approval” status.
 
/pom-tickets [Ticket Number]
Should show you a pretty full representation of the Footprints ticket specified. It needs to be an open ticket.
It will have three buttons at the bottom:
                “Subscribe” – will subscribe you to the ticket, and Slackbot will give you an update whenever something changes to it.
                “DM Assignees” – will open up a group DM session in Slack with any assignees that have registered with the App.
                “Create Channel” will create a channel for the ticket, automatically invite yourself and the assignees, and subscribe the channel to the ticket.
Any assignees that have registered with this App will have their Slack username show up in the ticket as a linkable Slack action.
The ticket title will be a direct link to the ticket in Footprints.
 
/pom-tickets subscribe [ticket number | assignee]
Will subscribe you to either a ticket or to an assignee, whichever one you specify.
Assignees can be either a Footprints username or even a Footprints Team name. (Like “IS Team”, or “Infrastructure Services Team”).
When you subscribe to a ticket, you’ll get a Slackbot DM if something changes in the ticket.
When you subscribe to an assignee, you will get a notification only at ticket creation.
(If you specify neither a ticket number nor an assignee, a dialog will open asking you.)
(The dialog has a secret easter egg – if you specify a #channel_name, it will subscribe the channel to the assignment, instead of you.)
There are no limits to the number of subscriptions you can have.
 
/pom-tickets subscribed
Should show you a list of any open tickets that you are subscribed to.
 
/pom-tickets register
Should open a dialog for you to register your Slack username with your Footprints username.
Technically you could register anyone’s Slack username with their Footprints username, it doesn’t have to be your own.
 
MASSIVE DISCLAIMER
Please don’t be discouraged with little pink Slack error messages. The Slack platform renders a “timeout was reached” error if it doesn’t hear back within 3 seconds. You _will_ see that every once in a while. There could be occasional other wonkiness as well.
Also nearly all results are limited to tickets in a non-closed, non-resolved status that were created in the previous 30 days. If there is an older ticket, sorry.
The app does its best to make every command cross-workspace in Footprints – both the Service Desk and Change Management.
Screenshots sent to me of problems are always, always welcome. I may not get to it for days, or weeks, but I deeply appreciate the feedback.
Sometimes we do development and it all breaks for a moment or two or twenty. Sorry. Slack has no sandbox for us. We do regression test every once in a while to make sure it all works.
 
Usage Thoughts:
One thing I have enjoyed is subscribing myself (or a channel) to the teams I typically work with. This has been helpful in helping me keep one eye on the various tickets coming through for us. If a ticket shows up that is of particular interest, I will click “subscribe” on it, and get handy updates that way. This has been helpful in allowing me to use Slack to stay aware of things I care about, versus the massive flood of non-stop emails that Footprints buries me in every day which I simply route to the garbage at this point in the interest of survival. I’ve also found it a nice way to search for tickets in meetings. One of my favorite features is a small gray line of text placed at the bottom of each ticket alert that tells me why Slackbot is alerting me – “… bc you have subscribe to acc04747,” for example.
 
Ideas For the Future:
An “unsubscribe” command.
A “help” command.
Make most of this content available in a blog post somewhere.
 
Thanks again!!!!
Andrew
