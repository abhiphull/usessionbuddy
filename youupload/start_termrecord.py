#!/bin/python
import uuid
import os
import sh

rid = str(uuid.uuid4())


#history
hf = '/tmp/usession.%s.history'%rid
#session
sf = '/tmp/usession.%s.html'%rid
#scriptfile
tf = '/tmp/usession.%s'%rid
os.environ['HISTFILE'] = hf
os.system('echo %s > /tmp/sessions.info'%rid)
os.system('TermRecord -o %s --tempfile %s'%(sf,tf))
