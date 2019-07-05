# usessionbuddy
Save and Share your Unix sessions easily. Go back in time and check your session history, search through your command history from your command line

#To install
git clone https://github.com/abhiphull/usessionbuddy

cd usessionbuddy
python setup.py <usession buddy username> <ip address from you are uploading your session and history>

#note:
1. Above command will copy conda.sh file to /etc/profile.d/ which will be run every time you login. Therefore before logging out, do ssh from another terminal window to make sure everything is fine.
2. If you can't login because of the conda.sh you can delete it by ssh host "rm -f /etc/profile.d/conda.sh"

#Requirements 

TermRecord to capture the session

#Usage:
1.  Usession Buddy captures the unix session using TermRecord. It starts recording the session as soon as user logs in. 
2.  Usession Buddy also captures the command history
3.  Both the session and command line history are uploaded to users account on Usession Buddy. These files are not public, therefore only Owner of the files can view these files.
4.  User has to have Usession Buddy account for the files to be uploaded.

