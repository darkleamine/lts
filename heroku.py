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
        os.system('heroku  < data.txt > heroku.txt')
        os.system('rm data.txt')
        os.system('heroku apps >  /home/ghost/PycharmProjects/pfe/file_generation/heroku_app.txt')
        os.system('heroku create tranquil-eyrie-10770 >> /home/ghost/PycharmProjects/pfe/file_generation/heroku.txt')
        os.system('git push heroku master >> /home/ghost/PycharmProjects/pfe/file_generation/heroku.txt')
        #os.system('heroku apps')



        ################################################################################################################
    def config(self,dirctory):
          print ("derictory ", dirctory)
          list = [];
          list.append(dirctory)
          os.chdir(dirctory)
          os.system("pwd")
        ################################################################################################################
    def apps(self,file_heroku_app):
        list =[]
        file =open("/home/ghost/PycharmProjects/pfe/file_generation/heroku.txt")
        for line in file:
             list.append(line)

        print ("fichier contient ",list)
        return  list

#heroku_instance =heroku('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')
#heroku_instance.build('verifier_la_instalation_des_logiciel.sh','heroku','darkle09')