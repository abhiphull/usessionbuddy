# usessionbuddy
Save and Share your Unix sessions easily. Go back in time and check your session history, search through your command history from your command line

#To install
git clone https://github.com/abhiphull/usessionbuddy

cd usessionbuddy
python setup.py <usession buddy username> <ip address from you are uploading your session and history>

#Note 1:
1. Above command will copy conda.sh file to /etc/profile.d/ which will be run every time you login. Therefore before logging out, do ssh from another terminal window to make sure everything is fine.
2. If you can't login because of the conda.sh you can delete it by ssh host "rm -f /etc/profile.d/conda.sh"

#Note 2:
  Add a TMOUT setting in your bashrc so as not to record idle sessions.
  
#Requirements 

TermRecord to capture the session

#Usage:
1.  Usession Buddy captures the unix session using TermRecord. It starts recording the session as soon as user logs in. 
2.  Usession Buddy also captures the command history
3.  Both the session and command line history are uploaded to users account on Usession Buddy. These files are not public, therefore only Owner of the files can view these files.
4.  User has to have Usession Buddy account for the files to be uploaded.
  a. Create account on http://usessionbuddy.com
  b. To upload files from your server; authenticate it from your server using following cmd line...
    curl -i --header 'Content-Type: multipart/form-data' -F "username=usessionbuddy username"  http://api.usessionbuddy.com/authenticate
5. If you don't want to set up auto upload by setup.py then once you have authenticated, you can also upload recorded session and command line history using...
    curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=<cmdline history file> -F sf=<script/termrecord session html file or video> -F "username="usessionbuddy username" -F "ip_address=ip adress of ur server" http://api.usessionbuddy.com

