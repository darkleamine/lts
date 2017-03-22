import os
import subprocess
class heroku:
    def __init__(self,verifier_package_install,package_to_install,root_pwd):
        self.verifier_package_install=verifier_package_install
        self.package_to_install=package_to_install
        self.root_pwd=root_pwd
        #remember
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
    def run(self):
        pass



        ################################################################################################################
    def config(self):
       pass

heroku_instance =heroku('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')
heroku_instance.build('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')