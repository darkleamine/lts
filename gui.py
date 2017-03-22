#/usr/bin/python2.7
from  Tkinter import *
import tkFileDialog
from ibm import *
root=Tk()
root.wm_minsize(400,200)

root.title("pfe")
#http://effbot.org/tkinterbook/photoimage.htm
aws_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/aws.png")
ibm_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/ibm.png")
heroku_photo=PhotoImage(file="/home/ghost/PycharmProjects/pfe/icone/heroku.png")
#les function de button


def repertoire():
    path = tkFileDialog.askdirectory(initialdir='/home/', title='Select your pictures folder')
    return path
########################################################################################################################
def heroku_fun():
    print("hello from heroku provider")
########################################################################################################################
def aws_fun():
    print("hello from aws provider")


########################################################################################################################
def ibm_fun():
     #verifieir l'installation de package
     Motdepasse = StringVar()
     name = StringVar()
     motdepasssys=StringVar()
     ibm_config = Tk()
     ibm_config.title("ibm")
     ibm_config.config()
     ibm_config.wm_minsize(250, 200)
     nom = Entry(ibm_config, textvariable=name)
     pwd = Entry(ibm_config, show="*", textvariable=Motdepasse)
     pwd_sys=Entry(ibm_config,show='*',textvariable=motdepasssys)
     nom_label = Label(ibm_config, text="nom", font='bold')
     pwd_label = Label(ibm_config, text="pwd", font='bold')
     pwd_sys_label = Label(ibm_config, text='pwd_sys', font='bold')


     get_inf=Button(ibm_config,text="done",command='print nom.get()')
     nom.grid(row=0,column=1)
     nom_label.grid(row=0, column=0)
     pwd.grid(row=1,column=1)
     pwd_label.grid(row=1, column=0)
     pwd_sys.grid(row=2,column=1)
     pwd_sys_label.grid(row=2,column=0)
     get_inf.grid(row=3,column=2)




     print ("pwd_sys",motdepasssys.get())
     ibm_instance =ibm()
     ibm_instance.build('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')



    #to change the entry in password use show option


########################################################################################################################


#create tow button and add there

aws_button = Button ( root,text="aws",image=aws_photo,width=100,height=50,command=aws_fun)
aws_button.place(x=10,y=10)
ibm_button = Button (root,text="ibm",image=ibm_photo,width=91,height=50,command=ibm_fun)
ibm_button.place(x=105,y=10)
heroku_button =Button(root,text="heroku",image=heroku_photo,width=100,height=50,command=heroku_fun)
heroku_button.place(x=210,y=10)
root.mainloop()
























































""""

 diectory_=Label(ibm_config,text="directory",font="bold")



####################################
 directory = Button(ibm_config,text="directory" ,command=repertoire())

 #path.grid(row=2, column=0)
 directory.grid(row=2, column=1)


 path =Label(ibm_config,text="al",width="30")
 def inf():
     print(Motdepasse," ",name)
 inf = Button(ibm_config, text="information", command=inf())
 inf.grid(row=2, column=2)


"""