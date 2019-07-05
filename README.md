# usessionbuddy
Save and Share your Unix sessions easily. Go back in time and check your session history, search through your command history from your command line

#To install
git clone https://github.com/abhiphull/usessionbuddy

cd usessionbuddy
python setup.py <usession buddy username> <ip address from you are uploading your session and history>

#note:
1. Above command will copy conda.sh file to /etc/profile.d/ which will be run every time you login. Therefore before logging out, do another
ssh from another terminal window to make sure everything is fine.
2. If you can't login because of the conda.sh you can delete it by ssh host "rm -f /etc/profile.d/conda.sh"

