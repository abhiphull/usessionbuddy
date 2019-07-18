import sys
import os
import subprocess

if len(sys.argv) != 3:
    print("Provide Usession buddy username as ist argument\n")
    print("Provide your server ip address as 2nd argument")
    sys.exit()
username = sys.argv[1]
ip_address = sys.argv[2]

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
try:
    tr = subprocess.check_output(['which TermRecord'],shell=True).strip().decode('utf-8')
except:
    print('TermRecord is not found')
    sys.exit()

trpath = "/".join(tr.split("/")[:-1])

##setting timeout for zsh and bash and screenrc

os.system('cp -p ~/.bashrc ~/.bashrc.usessionbuddy.bak')
os.system('cp -p ~/.zshrc ~/.zshrc.usessionbuddy.bak')
#os.system('echo "export TMOUT" >> ~/.bashrc')
#os.system('echo "export TMOUT" >> ~/.zshrc')
os.system('echo "idle 600 pow_detach" >> ~/.screenrc')
os.system('echo "#!/bin/sh" > conda.sh')
os.system('echo "export PATH=\$PATH:%s" >> conda.sh'%trpath)
os.system('echo "export PATH" >> conda.sh')
os.system("echo username=%s >> conda.sh"%username)
os.system("echo ip_address=%s >> conda.sh"%ip_address)
os.system("cat conda.sh.bak >> conda.sh")
os.system('cp -fp conda.sh /etc/profile.d/')
