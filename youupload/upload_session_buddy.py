#!/bin/python
import os
import sys
import argparse


CLI=argparse.ArgumentParser(add_help=True)
CLI.add_argument(
  "--upload_script_file", 
  type=int,
)
CLI.add_argument(
  "--username", 
  type=str,
)

CLI.add_argument(
  "--ip_address", 
  type=str,
)

CLI.add_argument(
  "--history_file", 
  type=str,
)

CLI.add_argument(
  "--session_file", 
  type=str,
)
CLI.add_argument(
  "--recorder_type", 
  type=str,
  required=True,
)

CLI.add_argument(
  "--dont_upload_sessionfile", 
  type=str,
)
args = CLI.parse_args()
upload_script_file = args.upload_script_file
username = args.username
ip_address = args.ip_address
recorder_type = args.recorder_type
dont_upload_sessionfile = args.dont_upload_sessionfile



if __name__ == '__main__':
    sf = args.session_file
    hf = args.history_file
    if recorder_type=="external":
        hf = hf
        sf = sf
        ubuddy(hf,sf,username,ip_address)
        sys.exit()

    with open('/tmp/sessions.info','r') as fp:
        lines = fp.read().splitlines()
        for line in lines:
            line = line.strip()
            rid = line
            if not hf:
                hf = '/tmp/usession.%s.history'%rid
            if not dont_upload_sessionfile or dont_upload_sessionfile is None:
                if not sf:
                    sf = '/tmp/usession.%s.html'%rid
            else:
                sf = None
            #scriptfile
            script_file = '/tmp/usession.%s.log'%rid
            #print(hf,sf,username,ip_address,script_file)
            if upload_script_file and sf and hf:
                os.system("curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=@%s -F sf=@%s -F username=%s -F ip_address=%s -F script_file=@%s http://api.usessionbuddy.com"%(hf,sf,username,ip_address,script_file))
            elif hf and sf:
                os.system("curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=@%s -F sf=@%s -F username=%s -F ip_address=%s http://api.usessionbuddy.com"%(hf,sf,username,ip_address))
            else:
                os.system("curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=@%s -F username=%s -F ip_address=%s http://api.usessionbuddy.com"%(hf,username,ip_address))
            break
                
