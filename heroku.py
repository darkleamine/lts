import os
import subprocess
from subprocess import CalledProcessError


class heroku:
    def __init__(self):
        pass
        #ci on cas de confidencialite fait elemenier root_pwd


        ################################################################################################################
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell/")
        ver="./"+ver
        print(ver)
        list = []
        list.append(ver);list.append(" ");list.append(pack);list.append(" ");list.append("heroku_install.sh");list.append(" ");list.append(pwd)
        print("list =")
        print(list)
        cmd="".join(list)
        print ("cmd = "+cmd)
        a=os.system('echo $PWD')
        print(a)
        os.system(cmd)


        ################################################################################################################
    def run(self,email,pwd,nom_app):
        auth = open("data.txt", "w")
        auth.write(email+'\n');auth.write(pwd);auth.close()
        #os.system('heroku  < data.txt ')
        try:
           login=subprocess.getoutput("heroku <data.txt")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command login '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('rm data.txt')
        #os.system('heroku create ')
        try:
            create=subprocess.getoutput("heroku create "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command create '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system('git remote -v')
        os.system('git remote set-url heroku https://git.heroku.com/'+nom_app+'.git')
        try:
            deploy = subprocess.getoutput("git push heroku master")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command deploy '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

        #os.system('heroku apps')
        try:
           apps=subprocess.getoutput("heroku apps")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command apps '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system("heroku open")
        return login,create,deploy,apps

        ################################################################################################################
    def config(self,dirctory):
          print ("derictory ", dirctory)
          list = [];
          list.append(dirctory)
          os.chdir(dirctory)
          os.system("pwd")
        ################################################################################################################


#heroku_instance =heroku('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')
#heroku_instance.build('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')