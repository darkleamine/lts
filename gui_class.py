#!/usr/bin/python3.5
import tkinter
from tkinter import *
import tkinter.filedialog
from ibm  import *
from heroku import *
from pivotel import *
from openshift import *
class gui:

########################################################################################################################


     #ibm_instance.build('verifier_la_instalation_des_logiciel.sh', 'cf-cli', 'darkle09')

          def aff(self,pack,titre,nom_app):

              print (nom.get(),pwd.get(),pwd_sys.get(),"package =",pack,path_entry.get())
              console.delete(1.0, END)
              console_app.delete(1.0,END)
              if(pack == pack_ibm and titre=='IBM'):
                   ibm_instance = ibm()
                    #ibm_instance.build(ver_package_install, pack, pwd_sys.get())
                   ibm_instance.config(path_entry.get(),nom_app)
                   login,deploy,apps=ibm_instance.run(nom.get(),pwd.get(),nom_app)
                   console.insert(END, "***********************login********************************* *\n" + login + "\n")
                   console.insert(END, "***********************deploy**********************************\n" + deploy + "\n")
                   console_app.insert(END, "***********************apps************************************\n" + apps + "\n")
              elif(pack == pack_heroku):
                    heroku_instance = heroku()
                    #heroku_instance.build(ver_package_install,pack,pwd_sys.get())
                    heroku_instance.config(path_entry.get())
                    login,create,deploy,apps=heroku_instance.run(nom.get(),pwd.get(),nom_app)
                    console.insert(END,"***********************login********************************* *\n"+login+"\n")
                    console.insert(END,"**********create***********************************************\n"+create+"\n")
                    console.insert(END,"***********************deploy**********************************\n"+deploy+"\n")
                    console_app.insert(END,"***********************apps************************************\n"+apps+"\n")
              elif(pack == pack_engine_yard):
                  openshift_instance = openshift()
                  #openshift_instance.build(ver_package_install,pack,pwd_sys.get())
                  runtime=openshift_instance.config(path_entry.get())
                  openshift_instance.run(nom_app,runtime)
              else:
                  pivotel_instance =pivotel()
                  #pivotel_instance.build(ver_package_install,pack,pwd_sys.get())
                  pivotel_instance.config(path_entry.get(),nom_app)
                  login,deploy,apps=pivotel_instance.run(nom.get(),pwd.get(),nom_app)
                  console.insert(END, "***********************login********************************* *\n" + login+"\n")
                  console.insert(END, "***********************deploy**********************************\n" + deploy+"\n")
                  console_app.insert(END,"***********************apps************************************\n"+apps+"\n")

########################################################################################################################
          def repertoire(self,path_entry):
                      path_entry.delete(0,END)
                      console.delete(1.0, END)
                      dirc = tkinter.filedialog.askdirectory(initialdir='/home/ghost', title='Select your app folder')
                      path_entry.insert(0,dirc)
#to change the entry in password use show option


########################################################################################################################
          def fun(self,pack,titre):
           #verifieir l'installation de package

                dirctory=StringVar()
                ibm_config = Tk()
                ibm_config.title("cloud provider "+titre)
                ibm_config.config()
                ibm_config.wm_minsize(250, 200)
                global nom,pwd,pwd_sys,path_entry
                nom = Entry(ibm_config,bg="white")
                nom.insert(0,"koudjil10@gmail.com")
                pwd = Entry(ibm_config, show="*",bg="white")
                pwd.insert(0,"Darkle09&")
                pwd_sys=Entry(ibm_config,show='*',bg="white")
                pwd_sys.insert(0, "darkle09")
                nom_label = Label(ibm_config, text="email", font='bold')
                pwd_label = Label(ibm_config, text="pwd", font='bold')
                pwd_sys_label = Label(ibm_config, text='pwd_sys', font='bold')
                note = Label(ibm_config,text='root pwd pour install package '+pack,fg='red')
                path_label = Label(ibm_config,text="path",font='bold')
                path_entry = Entry(ibm_config,bg="white",text='')
                browse =Button(ibm_config,text="directory",command=lambda :self.repertoire(path_entry))
                get_inf=Button (ibm_config,text="done",command=lambda :self.aff(pack,titre,nom_app_entry.get()))
                nom_app_label=Label(ibm_config,text="app name",font='bold')
                nom_app_entry=Entry(ibm_config,bg="white")
                nom_app_entry.insert(0,"amine31")
                nom.grid(row=0,column=1)
                nom_label.grid(row=0, column=0)
                pwd.grid(row=1,column=1)
                pwd_label.grid(row=1, column=0)
                pwd_sys.grid(row=2,column=1)
                pwd_sys_label.grid(row=2,column=0)
                get_inf.grid(row=5,column=2)
                note.grid(row=3,column=1)
                path_label.grid(row=4,column=0)
                path_entry.grid(row=4,column=1)
                browse.grid(row=4,column=2)
                nom_app_label.grid(row=5,column=0)
                nom_app_entry.grid(row=5,column=1)
                ibm_config.mainloop()
########################################################################################################################

########################################################################################################################
          def __init__(self):
                 root=Tk()
                 root.wm_minsize(800,350)
                 root.wm_maxsize(800,350)
                 root.title("pfe")
#global pack

#http://effbot.org/tkinterbook/photoimage.htm
                 aws_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/aws.png")
                 ibm_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/ibm.png")
                 heroku_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/heroku.png")
                 pivotel_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/pivotel.png")


                 global pack_aws,pack_ibm,pack_pivotel,pack_heroku,pack_engine_yard,ver_package_install,console,console_app
                 ver_package_install = 'verifier_la_instalation_des_logiciel.sh'
                 pack_aws="awscli"
                 pack_ibm='cf-cli'
                 pack_pivotel=pack_ibm
                 pack_heroku='heroku'
                 pack_engine_yard='rhc'
                 #utilisation de function lambda a cause de fonction avec argement declanche click sourie
                 aws_button = Button ( root,text="aws",image=aws_photo,width=100,height=50,command=lambda :self.fun(pack_aws,'Amazon AWS'))



                 ibm_button = Button (root,text="ibm",image=ibm_photo,width=100,height=50,command=lambda :self.fun(pack_ibm,'IBM'))

                 aws_button.place(x=10, y=30)
                 ibm_button.place(x=10, y=105)

                 heroku_button =Button(root,text="heroku",image=heroku_photo,width=100,height=50,command=lambda :self.fun(pack_heroku,'Heroku'))
                 heroku_button.place(x=10,y=180)
                 pivotel_button =Button(root,text="pivotel",image=pivotel_photo,width=100,height=50,command=lambda :self.fun(pack_pivotel,'Pivotel'))
                 pivotel_button.place(x=10,y=260)
                 openshift_button =Button(root,text="engine yard",image=pivotel_photo,width=100,height=50,command=lambda :self.fun(pack_engine_yard,'engine yard'))
                 #openshift_button.place(x=10,y=70)
                 console = Text(root,bg="black",fg="white")
                 console.place(x=120,y=140,height=180,width=650)
                 application=Label(root,text='application',font="bold")
                 application.place(x=120,y=10)
                 terminal = Label(root, text='console', font="bold")
                 terminal.place(x=120,y=110)
                 console_app = Text(root, bg="black", fg="white")
                 console_app.place(x=120,y=30,height=80,width=650)
                 button_scrollbar = Scrollbar(console,bg="#696969",activebackground="#696969")
                 button_scrollbar.pack(side=RIGHT, fill=Y)
                 console.config(  yscrollcommand = button_scrollbar.set)
                 #button sendj

                 root.mainloop()

gui =gui()
























































