 
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
root =Tk()
root.title('Plotting Graphs ')
root.geometry('1000x500')
t=Text(root,height=10,width=50)
data =pd.read_csv('student_marks.csv',index_col=0)

def graph1():
	btn1.configure(bg='red',fg='blue')
	plt.hist(data.Maths,29,ec='red')
	plt.xlabel('Marks in Maths')
	plt.ylabel('No. of Students')
	plt.show()

def graph2():
	plt.hist(data.Physics,29,ec='red')
	btn2.configure(bg='red',fg='blue')
	plt.xlabel('Marks in Physics')
	plt.ylabel('No. of Students')
	plt.show()

def graph3():
	plt.hist(data.Chemistry,29,ec='red')
	btn3.configure(bg='red',fg='blue')
	plt.xlabel('Marks in Chemistry')
	plt.ylabel('No. of Students')
	plt.show()

def graph4():
	plt.hist(data.English,29,ec='red')
	btn4.configure(bg='red',fg='blue')
	plt.xlabel('Marks in English')
	plt.show()

def graph5():
	plt.hist(data.Biology,29,ec='red')
	btn5.configure(bg='red',fg='blue')
	plt.xlabel('Marks in Biology')
	plt.ylabel('No. of Students')
	plt.show()

def graph6():
	plt.hist(data.Economics,29,ec='red')
	btn6.configure(bg='red',fg='blue')
	plt.xlabel('Marks in Economics')
	plt.ylabel('No. of Students')
	plt.show()

def graph7():
	plt.hist(data.History,29,ec='red')
	btn7.configure(bg='red',fg='blue')
	plt.xlabel('Marks in History')
	plt.ylabel('No. of Students')
	plt.show()

def graph8():
	plt.hist(data.Civics,29,ec='red')
	btn8.configure(bg='red',fg='blue')
	plt.xlabel('Marks in Civics')
	plt.ylabel('No. of Students')
	plt.show()

def plot1():
	p1_btn.configure(bg='red',fg='blue')
	plt.plot(data.Maths)
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot2():
	plt.plot(data.Physics)
	p2_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot3():
	plt.plot(data.Chemistry)
	p3_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot4():
	plt.plot(data.English)
	p4_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot5():
	plt.plot(data.Biology)
	p5_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot6():
	plt.plot(data.Economics)
	p6_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot7():
	plt.plot(data.History)
	p7_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()
def plot8():
	plt.plot(data.Civics)
	p8_btn.configure(bg='red',fg='blue')
	plt.xlabel('Name of Student')
	plt.ylabel('Marks of Students')
	plt.show()

def head1():
	l1=Label(root,text=data.head(),font='Helvetica 18 bold')
	l1.place(x=550,y=300)
	
root.configure(bg='#c9c245')# #F98B89
# lab1=Label(root,font='Helvetica 24 bold',bg='#F77E21',text='Student Result Analysis Using Matplotlib')
# lab1.grid(row=1,column=100)
label1=Label(root,text='Student Result Analysis Using Matplotlib',font='Helvetica 20 bold',bg='#58a0c3')
label1.place(relx=0.5,rely=0.05,anchor='center')
btn1=Button(root,text='Show Graph of Maths',command=graph1,width=20)
btn2=Button(root,text='Show Graph of Physics',command=graph2,width=20)
btn3=Button(root,text='Show Graph of Chemistry',command=graph3,width=20)
btn4=Button(root,text='Show Graph of English',command=graph4,width=20)
btn5=Button(root,text='Show Graph of Biology',command=graph5,width=20)
btn6=Button(root,text='Show Graph of Economics',command=graph6,width=20)
btn7=Button(root,text='Show Graph of History',command=graph7,width=20)
btn8=Button(root,text='Show Graph of Civics',command=graph8,width=20)

p1_btn=Button(root,text='Show Plot Of Maths',command=plot1,width=20)
p2_btn=Button(root,text='Show Plot Of Physics',command=plot2,width=20)
p3_btn=Button(root,text='Show Plot Of Chemistry',command=plot3,width=20)
p4_btn=Button(root,text='Show Plot Of English',command=plot4,width=20)
p5_btn=Button(root,text='Show Plot Of Biology',command=plot5,width=20)
p6_btn=Button(root,text='Show Plot Of Economics',command=plot6,width=20)
p7_btn=Button(root,text='Show Plot Of History',command=plot7,width=20)
p8_btn=Button(root,text='Show Plot Of Civics',command=plot8,width=20)

btn1.place(x=10,y=60)
btn2.place(x=10,y=110)
btn3.place(x=10,y=160)
btn4.place(x=10,y=210)
btn5.place(x=185,y=60)
btn6.place(x=185,y=110)
btn7.place(x=185,y=160)
btn8.place(x=185,y=210)

p1_btn.place(x=380,y=60)
p2_btn.place(x=380,y=110)
p3_btn.place(x=380,y=160)
p4_btn.place(x=380,y=210)
p5_btn.place(x=560,y=60)
p6_btn.place(x=560,y=110)
p7_btn.place(x=560,y=160)
p8_btn.place(x=560,y=210)

# h_btn=Button(root,text='Show top 5 rows',command=head1)
# h_btn.place(x=280,y=280)
root.mainloop()
