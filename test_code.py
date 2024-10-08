from tkinter import Tk,Button
import webbrowser
root = Tk()
bt = Button(root,text="Get facebook",command=lambda:webbrowser.open("https://www.facebook.com/MohamedGamal6"))
bt.pack()
root.mainloop()
