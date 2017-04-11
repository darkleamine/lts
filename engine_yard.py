import os
import subprocess
class engine_yard():
    def __init__(self):
        pass
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell")
        ver = "./" + ver
        print(ver)
        list = []
        list.append(ver+" ");
        list.append(pack+" ");
        list.append("ey_install.sh ");
        list.append(pwd)
        print("list =")
        print(list)

        cmd = "".join(list)
        print ("cmd = " + cmd)
        #subprocess.call(list)
        os.system(cmd)
    def run(self,email,pwd):
        auth = open("data.txt", "w")
        auth.write(email + '\n');
        auth.write(pwd);
        auth.close()
        os.system('ey init')
        os.system("ey login <data.txt")
        os.system('rm data.txt')
        os.system("ey deploy --app=https://cloud.engineyard.com/apps/52360/environments")
        os.system("ey launch")
    def config(self,dirctory):
        print ("derictory ", dirctory)
        list = [];
        list.append(dirctory)
        # subprocess.call(dirctory)
        os.chdir(dirctory)
        os.system("pwd")




#engine_yard_instance =engine_yard()
#engine_yard_instance.build("verifier_la_instalation_des_logiciel.sh","engineyard","darkle09")
#engine_yard_instance.run("koudjil10@gmail.com","Darkle09&")
#engine_yard_instance.config()