import os
import subprocess
class pivotel:
    def __init__(self):
        pass
        #remember
        #ci on cas de confidencialite fait elemenier root_pwd


        ################################################################################################################
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell")
        ver="./"+ver
        print(ver)
        list = []
        list.append(ver);list.append(pack);list.append("cf_cli_install.sh");list.append(pwd)
        print("list =")
        print(list)
        #list.append("./");list.append(ver);list.append(" ");list.append(pack);list.append(" ");list.append(pwd)
        #subprocess.call(list)
        cmd="".join(list)
        print ("cmd = "+cmd)
        subprocess.call(list)
        #os.system('./verifier_la_instalation_des_logiciel.sh cf-cli cf_cli_install.sh darkle09')
        #os.system(cmd)
       # os.system('./%s %s %s'% (self.verifier_package_install,self.package_to_install,self.root_pwd))

        #os.system(cool)

        ################################################################################################################
    def run(self,email,pwd):
        #os.system('cf api https://api.ng.bluemix.net')
        #os.system('cf login -a https://api.ng.bluemix.net -u koudjil1@live.fr -p "Darkle09&"')
        list = []
        list.append('cf ');
        list.append('login -a ');
        list.append('https://api.run.pivotal.io -u ');
        list.append(email);
        list.append(' -p ');
        list.append("\"" + pwd + "\"");  # list.append(' -s koudjil')
        a = "".join(list)
        print a

        os.system(a)
        os.system('cf push asma12')


        ################################################################################################################
    def config(self,dirctory):
        print ("derictory ", dirctory)
        list = [];
        list.append(dirctory)
        # subprocess.call(dirctory)
        os.chdir(dirctory)
        os.system("pwd")


#pivotel_instance = pivotel('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#pivotel_instance.build('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#pivotel_instance.config()
#pivotel_instance.run()