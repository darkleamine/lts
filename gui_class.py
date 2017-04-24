"""
from Tkinter import *

class SampleApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        # http://effbot.org/tkinterbook/photoimage.htm

        ibm_photo = PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/ibm.png")
        heroku_photo = PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/heroku.png")

        # les function de button
        def heroku_fun():
            print("hello from heroku provider")

        ########################################################################################################################


        def ibm_fun():
            print "hello from ibm provider"

        aws_photo = PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/aws.png")
        self.aws_button = Button(self, text="aws",width=100, height=50, command=self.aws_fun,font='bold')
        self.aws_button.place(x=10,y=10)




        #ibm_button = Button(self, text="ibm", image=ibm_photo, width=91, height=50, command=ibm_fun)
        #self.ibm_button.place(x=105, y=10)
        #heroku_button = Button(self, text="heroku", image=heroku_photo, width=100, height=50, command=self.heroku_fun)
        #self.heroku_button.place(x=210, y=10)

        #self.entry = Entry(self)
        #self.button = Button(self, text="Get", command=self.on_button)
        #self.button.pack()
        #self.entry.pack()

    def on_button(self):
             print(self.entry.get())
    def aws_fun (self):
        ibm_config = Tk()
        ibm_config.title("ibm")
        ibm_config.config()
        ibm_config.wm_minsize(250, 200)
        entree = Entry(ibm_config)
        entree.pack()
        def saisie():
            print entree.get()

        bou1 = Button(ibm_config, text='valider', command=saisie)
        bou1.pack()


w = SampleApp()
w.mainloop()
"""
#/usr/bin/python2.7
from  Tkinter import *
import tkFileDialog

from ibm  import *
from heroku import *
from pivotel import *
from engine_yard import *
class gui:

########################################################################################################################


     #ibm_instance.build('verifier_la_instalation_des_logiciel.sh', 'cf-cli', 'darkle09')

     def aff(self,pack,titre):

         print nom.get(),pwd.get(),pwd_sys.get(),"package =",pack;pathlabel.get()
         if(pack == pack_ibm and titre=='IBM'):
             ibm_instance = ibm()
             ibm_instance.build(ver_package_install, pack, pwd_sys.get())
             ibm_instance.config(pathlabel.get())
             ibm_instance.run(nom.get(),pwd.get())
         elif(pack == pack_heroku):
               heroku_instance = heroku()
               heroku_instance.build(ver_package_install,pack,pwd_sys.get())
               heroku_instance.config(pathlabel.get())
               #heroku_instance.run(nom.get(),pwd.get())
         elif(pack == pack_engine_yard):
               engine_yard_instance = engine_yard()
               engine_yard_instance.build(ver_package_install,pack,pwd_sys.get())
               engine_yard_instance.config(pathlabel.get())
               engine_yard_instance.run(nom.get(),pwd.get())
         else:
               pivotel_instance =pivotel()
               pivotel_instance.build(ver_package_install,pack,pwd_sys.get())
               pivotel_instance.config(pathlabel.get())
               pivotel_instance.run(nom.get(),pwd.get())
########################################################################################################################
     def repertoire(self,pathlabel):
        pathlabel.delete(0,END)
        dirc = tkFileDialog.askdirectory(initialdir='/home/ghost', title='Select your app folder')
        pathlabel.insert(0,dirc)
#to change the entry in password use show option
     def getinfo():
           #os.system('python gui.py >console.txt')
           #sys.stdout = open("console.txt", 'w+')
           sys.stdout =os.system('pwd')


########################################################################################################################
     def fun(self,pack,titre):
     #verifieir l'installation de package

         dirctory=StringVar()
         ibm_config = Tk()
         ibm_config.title("cloud provider "+titre)
         ibm_config.config()
         ibm_config.wm_minsize(250, 200)
         global nom,pwd,pwd_sys,pathlabel
         nom = Entry(ibm_config,bg="white")
         pwd = Entry(ibm_config, show="*",bg="white")
         pwd_sys=Entry(ibm_config,show='*',bg="white")
         nom_label = Label(ibm_config, text="email", font='bold')
         pwd_label = Label(ibm_config, text="pwd", font='bold')
         pwd_sys_label = Label(ibm_config, text='pwd_sys', font='bold')
         note = Label(ibm_config,text='root pwd pour install package '+pack,fg='red')
         pathlabel = Entry(ibm_config,bg="white",text='')
         browse =Button(ibm_config,text="directory",command=lambda :self.repertoire(pathlabel))
         get_inf=Button (ibm_config,text="done",command=lambda :self.aff(pack,titre))
         nom.grid(row=0,column=1)
         nom_label.grid(row=0, column=0)
         pwd.grid(row=1,column=1)
         pwd_label.grid(row=1, column=0)
         pwd_sys.grid(row=2,column=1)
         pwd_sys_label.grid(row=2,column=0)
         get_inf.grid(row=5,column=2)
         note.grid(row=3,column=1)
         pathlabel.grid(row=4,column=1)
         browse.grid(row=4,column=2)
         ibm_config.mainloop()
########################################################################################################################

     def __init__(self):
                 root=Tk()
                 root.wm_minsize(450,280)
                 root.wm_maxsize(600,600)
                 root.title("pfe")
#global pack

#http://effbot.org/tkinterbook/photoimage.htm
                 aws_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/aws.png")
                 ibm_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/ibm.png")
                 heroku_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/heroku.png")
                 pivotel_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/pivotel.png")

                 global pack_aws,pack_ibm,pack_pivotel,pack_heroku,pack_engine_yard,ver_package_install
                 ver_package_install = 'verifier_la_instalation_des_logiciel.sh'
                 pack_aws="awscli"
                 pack_ibm='cf-cli'
                 pack_pivotel=pack_ibm
                 pack_heroku='heroku'
                 pack_engine_yard='engineyard'
                 #utilisation de function lambda a cause de fonction avec argement declanche click sourie
                 aws_button = Button ( root,text="aws",image=aws_photo,width=100,height=50,command=lambda :self.fun(pack_aws,'Amazon AWS'))

                 aws_button.place(x=10,y=10)

                 ibm_button = Button (root,text="ibm",image=ibm_photo,width=91,height=50,command=lambda :self.fun(pack_ibm,'IBM'))

                 ibm_button.place(x=105,y=10)

                 heroku_button =Button(root,text="heroku",image=heroku_photo,width=100,height=50,command=lambda :self.fun(pack_heroku,'Heroku'))
                 heroku_button.place(x=210,y=10)
                 pivotel_button =Button(root,text="pivotel",image=pivotel_photo,width=100,height=50,command=lambda :self.fun(pack_pivotel,'Pivotel'))
                 pivotel_button.place(x=310,y=10)
                 engine_yard_button =Button(root,text="engine yard",image=pivotel_photo,width=100,height=50,command=lambda :self.fun(pack_engine_yard,'engine yard'))
                 engine_yard_button.place(x=10,y=70)
                 console = Text(root,bg="black",fg="white")
                 console.insert(END,'console.txt')
                 console.place(x=20,y=150,height=150,width=420)
                 root.mainloop()

gui =gui()
sys.stdout = open('ey.yml', 'w')























































