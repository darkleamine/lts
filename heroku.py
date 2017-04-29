import os
import subprocess
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
    def run(self,email,pwd):
        auth = open("data.txt", "w")
        auth.write(email+'\n');auth.write(pwd);auth.close()
        #os.system('heroku  < data.txt ')
        login=subprocess.check_output(["heroku <data.txt"],shell=True)
        os.system('rm data.txt')
        #os.system('heroku create ')
        create=subprocess.check_output(['heroku create'],shell=True)
        #os.system('git push heroku master')
        #deploy=subprocess.check_output(['git push heroku master'])
        #os.system('heroku apps')
        apps=subprocess.check_output(['heroku apps'],shell=True)
        return login+create+apps#++deploy+apps

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