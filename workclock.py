from tkinter import *
import csv
import time

lastin = 0

def clockin():
	global lastin
	lastin = time.time()

def clockout():
	now = time.time()
	clocked = now - lastin
	intime = time.asctime(time.gmtime(lastin))
	outtime = time.asctime(time.gmtime(now))
	with open('mytime.csv', 'ab') as csvfile:
		timewriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
		timewriter.writerow([intime, outtime, clocked, e1.get()])

master = Tk()
Label(master, text="Description:").grid(row=0, padx=4, pady=4)

e1 = Entry(master)

e1.grid(row=0, column=1, padx=4, pady=4)

Button(master, text='Clock In', command=clockin).grid(row=3, column=0, sticky=W, padx=4, pady=4)
Button(master, text='Clock Out', command=clockout).grid(row=3, column=1, sticky=W, padx=4, pady=4)

master.title('WorkClock')
img = PhotoImage(file='clock-icon.png')
master.tk.call('wm', 'iconphoto', master._w, img)
mainloop()
