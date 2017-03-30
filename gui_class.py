
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