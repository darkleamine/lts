import os
import subprocess
class ibm:
    def __init__(self):
           pass
           #,verifier_package_install,package_to_install,root_pwd
           #self.verifier_package_install=verifier_package_install
           #self.package_to_install=package_to_install
           #self.root_pwd=root_pwd
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

    def run(self):
       # os.system('cf api https://api.ng.bluemix.net')
        #os.system('cf login -a https://api.ng.bluemix.net -u koudjil1@live.fr -p "Darkle09&"')
        os.chdir('/home/ghost/Bureau/deploiment')
        os.system('cf login -u koudjil@live.fr -o koudjil@live.fr -p "Darkle09&" -s koudjil')
        #os.system('cf apps')
        os.system('cf push')


        ################################################################################################################
    def config(self):
        os.chdir("/home/ghost/PycharmProjects/pfe/configuration")
        Fichier = open('manifest.yml', 'w')
        #Fichier.write("--- \n")
        Fichier.write("applications: \n")
        Fichier.write("- name : cours-vhdl \n")
        Fichier.write("  host : koudjil19 \n")
        Fichier.write("  memory : 128M \n")
        Fichier.write("  path : /home/ghost/Bureau/deploiment \n")
        Fichier.write("  buildpack : https://github.com/cloudfoundry/staticfile-buildpack.git \n")
        #Fichier.write("  instances : 2 \n")
        Fichier.close()
        os.system('cp /home/ghost/PycharmProjects/pfe/configuration/manifest.yml /home/ghost/Bureau/deploiment')

#ibm_instance = ibm('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#ibm_instance.build('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#ibm_instance.config()
#ibm_instance.run()