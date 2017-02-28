#coding:utf-8
import tkFileDialog
import Tkinter
import hashlib
from Tkinter import *
import os,sys
top = Tkinter.Tk()
top.geometry("350x120");
L = Tkinter.Label(text="文件hash1")
global filename
def calcMd5():
	global filename
	with open(filename,'rb') as f:
		md5obj = hashlib.md5()
		while True:
			content = f.read(1024)
			if not content:
				break
			md5obj.update(content)
		return md5obj.hexdigest()
def calcSha1():
	global filename
	with open(filename,'rb') as f:
		sha1obj = hashlib.sha1()
		while True:
			content = f.read(1024)
			if not content:
				break
			sha1obj.update(content)
		return sha1obj.hexdigest()
def getFileName():
	global filename
	filename= tkFileDialog.askopenfilename(initialdir="d:/")
	if filename:
		md5 = calcMd5()
		sha1 = calcSha1()
		fileEntry.delete(0,END)
		md5Entry.delete(0,END)
		sha1Entry.delete(0,END)
		fileEntry.insert(0,filename)
		sha1Entry.insert(0,sha1)
		md5Entry.insert(0,md5)
#component
btnChooseFile = Tkinter.Button(top,text="选择文件",command=getFileName)
Lfile = Tkinter.Label(top,text="文件名").grid(row=0)
Lmd = Tkinter.Label(top,text="md5").grid(row=1)
Lsha = Tkinter.Label(top,text="sha1").grid(row=2)
fileEntry = Tkinter.Entry(top,width=40) 
md5Entry = Entry(top,width=40)
# sizeEntry = Entry(top)
# sizeEntry.grid(row=3)
sha1Entry = Entry(top,width=40)
fileEntry.grid(row=0,column=1)
md5Entry.grid(row=1,column=1)
sha1Entry.grid(row=2,column=1)
btnChooseFile.grid(row=4,column=1,sticky=E)
mainloop()
