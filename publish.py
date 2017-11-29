#!/usr/bin/python

# push slides for a talk to cern gitlab
# 
# TODO: document use case
# TODO: error handling
# TODO: more proper usage of python (e.g. git module instad of check_output)
# TODO: sanity checking if called from right directory and status of repo
# TODO: python3 compatibility
# WISH: symlinking and submodule handling for main repo

import os
import sys
from subprocess import check_output

WorldPublic = True
TrivialName = os.path.basename(os.getcwd())

if WorldPublic:
    out = check_output(["curl","--header","PRIVATE-TOKEN: "+os.environ["GITLABTOKEN"],"-X","POST","https://gitlab.cern.ch/api/v3/projects?name="+TrivialName+"&visibility_level=20"])
else:
    out = check_output(["curl","--header","PRIVATE-TOKEN: "+os.environ["GITLABTOKEN"],"-X","POST","https://gitlab.cern.ch/api/v3/projects?name="+TrivialName+"&visibility_level=0"])
    # TODO share with LHCb

import json
repo_conf = json.loads(out)
try:
    repo_conf["name"]
except:
    print "Oh help us"
    sys.exit(1)

try:
    import re
    #check_output(["git","remote","add",TrivialName,re.sub("7999","8443",re.sub('ssh://git','https://:',repo_conf["ssh_url_to_repo"]))])
    check_output(["git","remote","add","gitlab",re.sub("7999","8443",re.sub('ssh://git','https://:',repo_conf["ssh_url_to_repo"]))])
except:
    print("couldn't add remote")
    print(json.dumps(repo_conf, sort_keys=True, indent=2, separators=(',', ': ')))

#check_output(["git","subtree","split","--prefix="+os.path.basename(DirName),"-b",BranchName])
try:
    pushout = check_output(["git","push","gitlab","master:master"])
except: 
    print "push did ", pushout

try:
    qrgen = check_output(["qrencode","-o","QR.png",data['web_url']])
except:
    print "QR code generation did ", qrgen
try:
    convert = check_output(["convert","QR.png","-flatten","QR2.png"])
except:
    print "alpha channel removal did ", convert

# publication script
# Copyright (C) 2017  Paul Seyfert <pseyfert@cern.ch>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
