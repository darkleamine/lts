import os
import subprocess
class openshift:
       def __init__(self):
            pass

       def build(self):
           pass
       def config(self,dirctory,app_name):
           print ("derictory ", dirctory)
           list = [];
           list.append(dirctory)
           # subprocess.call(dirctory)
           os.chdir(dirctory)
           os.system("pwd")
           fichiers = os.listdir(dirctory)
           if "package.json" in fichiers:
               # donner le buildpack pour nodejs
               return "nodejs-0.10"
           elif "requirements.txt" in fichiers:
               # donner le buildpack pour python
               return "python-3.3"
           elif "composer.json" in fichiers:
               # donner le buildpack pour php
                return "php-5.3"


       def run(self,nom_app,runtime):

           try:
               apps = subprocess.getoutput("rhc app create "+nom_app+" "+runtime)
           except subprocess.CalledProcessError as e:
               raise RuntimeError(
                   "command apps '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))