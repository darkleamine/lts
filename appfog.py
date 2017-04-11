import os
import subprocess
class appfog:
    def __init__(self):
        pass
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell")
        ver = "./" + ver
        print(ver)
        list = []
        list.append(ver);
        list.append(pack);
        list.append("cf_cli_install.sh");
        list.append(pwd)
        print("list =")
        print(list)
        cmd = "".join(list)
        print ("cmd = " + cmd)
        subprocess.call(list)
    def run(self,email,pwd):
        list = []
        list.append('cf ');
        list.append('login -a ');
        list.append('https://api.ng.bluemix.net -u ');
        list.append(email);
        list.append(' -p ');
        list.append("\"" + pwd + "\"");
        a = "".join(list)
        print a
        os.system(a)
        os.system('cf push asma12')
    def config(self,dirctory):
        print ("derictory ", dirctory)
        list = [];
        list.append(dirctory)
        os.chdir(dirctory)
        os.system("pwd")
