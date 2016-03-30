from Tkinter import *
from ttk import Frame, Button, Style

global filename

class mainMenu(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		
		self.initUI()
		
	def initUI(self):
		crawlVar = IntVar()
		scanVar = IntVar()
		dnsVar = IntVar()
		emailVar = IntVar()
		self.filename = StringVar()
		self.parent.title("E-Z Security Audting")
		self.style = Style()
		self.style.theme_use("default")
		
		frame = Frame(self, borderwidth=1)
		frame.pack(side=TOP, fill=BOTH)
		
		self.pack(side=TOP, fill=BOTH)
		
		dnsButton = Checkbutton(self, text="DNS Recon", variable=dnsVar)
		dnsButton.pack(fill=X)
		scanButton = Checkbutton(self, text="Port Scan", variable=scanVar)
		scanButton.pack(fill=X)
		crawlButton = Checkbutton(self, text="Web Crawl", variable=crawlVar)
		crawlButton.pack(fill=X)
		emailButton = Checkbutton(self, text="Email Gathering", variable=emailVar)
		emailButton.pack(fill=X)

		lab = Label(self, width=15, text="Filename", anchor='w')
		ent = Entry(self,textvariable=self.filename)
		self.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, fill=X)
		
	def executeChecks(self):
		print self.filename.get()
		

def main():
	master = Tk()
	master.geometry("300x200+300+300")
	
	secApp = mainMenu(master)
	executeButton = Button(master, text="Run", command=secApp.executeChecks)
	executeButton.pack(side=LEFT)
		
	quitButton = Button(master, text="Quit", command=quit)
	quitButton.pack(side=RIGHT)
	master.mainloop()

main()
