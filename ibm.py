import os
import subprocess
class ibm:
    def __init__(self):
           pass



        ################################################################################################################
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell")
        ver="./"+ver
        print(ver)
        list = []
        list.append(ver);list.append(pack);list.append("cf_cli_install.sh");list.append(pwd)
        print("list =")
        print(list)

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

          list =[]
          list.append('cf ');list.append('login -a ');list.append('https://api.ng.bluemix.net -u ');list.append(email);list.append(' -p ');list.append("\""+pwd+"\"");#list.append(' -s koudjil')
          a="".join(list)
          print a
          #login = subprocess.check_output(['cf login -a https://api.ng.bluemix.net -u koudjil@live.fr -p "Darkle09&"'],shell=True)
          login = subprocess.check_output([a],shell=True)
          #os.system(a)
          deploy= subprocess.check_output(['git push heroku master'],shell=True)
          apps = subprocess.check_output(['cf apps'],shell=True)
          #os.system('cf push asma12')
          return login+deploy+apps

        ################################################################################################################
    def config(self,dirctory):
        #os.chdir("/home/ghost/PycharmProjects/pfe/configuration")
        #os.chdir(dirctory)7
        print ("derictory ",dirctory)
        list=[];list.append(dirctory)
        #subprocess.call(dirctory)
        os.chdir(dirctory)
        os.system("pwd")
        """
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
        """
#ibm_instance = ibm()
#ibm_instance.build('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#ibm_instance.config()
#ibm_instance.run()