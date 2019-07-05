import sys
import os
import subprocess

if len(sys.argv) != 2:
    print("Provide Usession buddy username")
    sys.exit()
username = sys.argv[1]
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

def get_installed_packages():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    return(installed_packages)

installed_packages = get_installed_packages()
if not 'pip' in installed_packages:
    raise Exception("pip must be installed")

'''installing TermRecord'''
if os.path.isfile('conda.sh'):
    os.system('rm -f conda.sh')

os.system('pip install TermRecord')
os.system('echo "#!/bin/sh" > conda.sh')
os.system("echo username=%s >> conda.sh"%username)
os.system("cat conda.sh.bak >> conda.sh")
#os.system('cp -p conda.sh /etc/profile.d/')
#os.system('cp -p usession_post_buddy.py /usr/local/bin/')
#os.system('chmod +x /usr/local/bin/usession_post_buddy.py')
#os.system('chmod +x build_logout.sh %s'%username)

