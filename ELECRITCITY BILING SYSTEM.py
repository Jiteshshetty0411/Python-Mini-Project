# python program to create Electricity Biling System

#import everything from tkinter module
from tkinter import*
import random
import time
import datetime

width = 1350
height = 650

root = Tk()
root.geometry(str(width)+"x" + str(height) + "+0+0")
root.title("Electricity Biling System")

Tops = Frame(root, width=width, height=100, bd=4,relief='raise')
Tops.pack(side=TOP)

#main-frame
f1 = Frame(root, width=900, height=650, bd=8,relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=450, height=650, bd=8,relief='raise')
f2.pack(side=LEFT)
#sub-frame
f1a = Frame(f1, width=900, height=330, bd=8,relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=400, height=320, bd=8,relief='raise')
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8,relief='raise')
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8,relief='raise')
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8,relief='raise')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8,relief='raise')
f2ab.pack(side=LEFT)

lblInfo=Label(Tops, font=('arial',60,'bold'),text ="Electricity Biling System", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

#============
# CALCULATOR
#============
#I should've defined all of the variables associated with StringVar() here

#calculator's screen
text_Input=StringVar()
operator=""

def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=''
	text_Input.set('')

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=''

#calculator's buttons
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input,bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
#----------------------------------------------------
btn7 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=1,column=2)
btnPlus = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',command=lambda:btnClick("+")).grid(row=1,column=3)
#----------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=2,column=2)
btnSub = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',command=lambda:btnClick("-")).grid(row=2,column=3)
#----------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=3,column=2)
btnMult = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',command=lambda:btnClick("*")).grid(row=3,column=3)
#----------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='c',command=btnClearDisplay).grid(row=4,column=1)
btnEqual = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',command=btnEqualsInput).grid(row=4,column=2)
btnDiv = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',command=lambda:btnClick("/")).grid(row=4,column=3)

#==============
# BILL's INFO
#==============
CUSTOMERNO=StringVar()
AREACODE=StringVar()
METERREADERCODE=StringVar()
CONNECTEDLAOD=StringVar()
BILLNUMBER=StringVar()


lblCUSTOMERNO = Label(f1aa,font=('arial',13,'bold'),text='CUSTOMER NO',bd=16,justify='left')
lblCUSTOMERNO.grid(row=0,column=0)
txtCUSTOMERNO=Entry(f1aa,font=('arial',13,'bold'),textvariable=CUSTOMERNO,bd=10,insertwidth=2,justify='left')
txtCUSTOMERNO.grid(row=0,column=1)

lblAREACODE= Label(f1aa,font=('arial',13,'bold'),text='AREA CODE',bd=16,justify='left')
lblAREACODE.grid(row=1,column=0)
txtAREACODE=Entry(f1aa,font=('arial',13,'bold'),textvariable=AREACODE,bd=10,insertwidth=2,justify='left')
txtAREACODE.grid(row=1,column=1)

lblMETERREADERCODE= Label(f1aa,font=('arial',13,'bold'),text='METER READER CODE',bd=16,justify='left')
lblMETERREADERCODE.grid(row=2,column=0)
txtMETERREADERCODE=Entry(f1aa,font=('arial',13,'bold'),textvariable=METERREADERCODE,bd=10,insertwidth=2,justify='left')
txtMETERREADERCODE.grid(row=2,column=1)

lblCONNECTEDLAOD= Label(f1aa,font=('arial',13,'bold'),text='CONNECTED LAOD',bd=16,justify='left')
lblCONNECTEDLAOD.grid(row=3,column=0)
txtCONNECTEDLAOD=Entry(f1aa,font=('arial',13,'bold'),textvariable=CONNECTEDLAOD,bd=10,insertwidth=2,justify='left')
txtCONNECTEDLAOD.grid(row=3,column=1)

lblBILLNUMBER = Label(f1aa,font=('arial',13,'bold'),text='BILL NUMBER',bd=16,justify='right')
lblBILLNUMBER.grid(row=4,column=0)
txtBILLNUMBER=Entry(f1aa,font=('arial',13,'bold'),textvariable=BILLNUMBER,bd=10,insertwidth=2,justify='left')
txtBILLNUMBER.grid(row=4,column=1)


#==============
# BILL's COST
#==============
DATEOFCUSTOMERBILL=StringVar()
CostofENERGYCHARGE=StringVar()
CostofGOVTELECTRITCITYDUTY=StringVar()
CostofFIXEDCHARGE=StringVar()
CostofWHEELINGCHARGES=StringVar()

DATEOFCUSTOMERBILL.set(time.strftime("%d/%m/%y"))

lblDATEOFCUSTOMERBILL = Label(f1ab,font=('arial',13,'bold'),text='DATE OF CUSTOMER BILL',bd=16,anchor='w')
lblDATEOFCUSTOMERBILL.grid(row=0,column=0)
txtDATEOFCUSTOMERBILL=Entry(f1ab,font=('arial',13,'bold'),textvariable=DATEOFCUSTOMERBILL,bd=10,insertwidth=2,justify='left')
txtDATEOFCUSTOMERBILL.grid(row=0,column=1)

lblCostofENERGYCHARGE = Label(f1ab,font=('arial',13,'bold'),text='ENERGY CHARGE',bd=16,anchor='w')
lblCostofENERGYCHARGE.grid(row=1,column=0)
txtCostofENERGYCHARGE=Entry(f1ab,font=('arial',13,'bold'),textvariable=CostofENERGYCHARGE,bd=10,insertwidth=2,justify='left')
txtCostofENERGYCHARGE.grid(row=1,column=1)

lblCostofGOVTELECTRITCITYDUTY = Label(f1ab,font=('arial',13,'bold'),text='GOVT ELECTRITCITY DUTY',bd=16,anchor='w')
lblCostofGOVTELECTRITCITYDUTY.grid(row=2,column=0)
txtCostofGOVTELECTRITCITYDUTY=Entry(f1ab,font=('arial',13,'bold'),textvariable=CostofGOVTELECTRITCITYDUTY,bd=10,insertwidth=2,justify='left')
txtCostofGOVTELECTRITCITYDUTY.grid(row=2,column=1)

lblCostofFIXEDCHARGE= Label(f1ab,font=('arial',13,'bold'),text='FIXED CHARGE',bd=16,anchor='w')
lblCostofFIXEDCHARGE.grid(row=3,column=0)
txtCostofFIXEDCHARGE=Entry(f1ab,font=('arial',13,'bold'),textvariable=CostofFIXEDCHARGE,bd=10,insertwidth=2,justify='left')
txtCostofFIXEDCHARGE.grid(row=3,column=1)

lblCostofWHEELINGCHARGES= Label(f1ab,font=('arial',13,'bold'),text='WHEELING CHARGES',bd=16,anchor='w')
lblCostofWHEELINGCHARGES.grid(row=4,column=0)
txtCostofWHEELINGCHARGES=Entry(f1ab,font=('arial',13,'bold'),textvariable=CostofWHEELINGCHARGES,bd=10,insertwidth=2,justify='left')
txtCostofWHEELINGCHARGES.grid(row=4,column=1)

#=================
# BILL's SUMMARY
#=================
PAIDTAX=StringVar()
SUBTOTAL=StringVar()
TOTALBILLAMOUNT=StringVar()
PayReference=StringVar()

lblPAIDTAX = Label(f2aa,font=('arial',13,'bold'),text='PAID TAX',bd=8,anchor='w')
lblPAIDTAX.grid(row=2,column=0)
txtPAIDTAX = Entry(f2aa,font=('arial',13,'bold'),textvariable=PAIDTAX,bd=8,insertwidth=2,justify='left')
txtPAIDTAX.grid(row=2,column=1)

lblSUBTOTAL = Label(f2aa,font=('arial',13,'bold'),text='SUB TOTAL',bd=8,anchor='w')
lblSUBTOTAL.grid(row=3,column=0)
txtSUBTOTAL = Entry(f2aa,font=('arial',13,'bold'),textvariable=SUBTOTAL,bd=8,insertwidth=2,justify='left')
txtSUBTOTAL.grid(row=3,column=1)

lblTOTALBILLAMOUNT = Label(f2aa,font=('arial',13,'bold'),text='TOTAL BILL AMOUNT',bd=8,anchor='w')
lblTOTALBILLAMOUNT.grid(row=4,column=0)
txtTOTALBILLAMOUNT = Entry(f2aa,font=('arial',13,'bold'),textvariable=TOTALBILLAMOUNT,bd=8,insertwidth=2,justify='left')
txtTOTALBILLAMOUNT.grid(row=4,column=1)

PayReference=Button(root,padx=16,pady=16,bd=8,fg='black',font=('arial',13,'bold'),width=15,text='ID REFERENCE', command=PayReference)


#=====================
# BILL'S INFO BUTTONS
#=====================
from tkinter import messagebox

def iExit():
	qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	CUSTOMERNO.set("")
	AREACODE.set("")
	METERREADERCODE.set("")
	CONNECTEDLAOD.set("")
	BILLNUMBER.set("")
	PAIDTAX.set("")
	SUBTOTAL.set("")
	TOTALBILLAMOUNT.set("")
	CostofENERGYCHARGE.set("")
	CostofGOVTELECTRITCITYDUTY.set("")
	CostofFIXEDCHARGE.set("")
	CostofWHEELINGCHARGES.set("")

def PayReference():
	x = random.randint(1003412,69981223)
	randomRef = str(x)
	CUSTOMERNO.set("ID"+randomRef)


	y = random.randint(12345134,697812432)
	randomRef = str(y)
	BILLNUMBER.set("BILL"+randomRef)

	z =random.randint(1,10)
	randomRef = str(z)
	CONNECTEDLAOD.set(randomRef+"KW")

	s =random.randint(123,1234)
	randomRef = str(s)
	METERREADERCODE.set(randomRef)

	a =random.randint(400000,499999)
	randomRef = str(a)
	AREACODE.set(randomRef)

def CostOfOrder():
	ENERGYCHARGEPrice = float(METERREADERCODE.get())
	WHEELINGCHARGESPrice = float("250")
	GOVTELECTRITCITYDUTYPrice = float("250")
	FIXEDCHARGECost= float("100")
	
	ENERGYCHARGE = "RS " + str("%.2f"%((ENERGYCHARGEPrice*5.09)))
	CostofENERGYCHARGE.set(ENERGYCHARGE)
	
	GOVTELECTRITCITYDUTY = "RS " + str("%.2f"%((GOVTELECTRITCITYDUTYPrice*1.07)))
	CostofGOVTELECTRITCITYDUTY.set(GOVTELECTRITCITYDUTY)
	
	FIXEDCHARGE = "RS " + str("%.2f"%((FIXEDCHARGECost*0.50)))
	CostofFIXEDCHARGE.set(FIXEDCHARGE)
	
	WHEELINGCHARGES = "RS " + str("%.2f"%((WHEELINGCHARGESPrice*2.05)))
	CostofWHEELINGCHARGES.set(WHEELINGCHARGES)
	
	ToC = "RS " + str("%.2f"%((ENERGYCHARGEPrice*5.09)+(GOVTELECTRITCITYDUTYPrice*1.00)+(FIXEDCHARGECost*0.50)+(WHEELINGCHARGESPrice*2.05)))
	SUBTOTAL.set(ToC)
	
	Tax = "RS " + str("%.2f"%(((ENERGYCHARGEPrice*5.09)+(GOVTELECTRITCITYDUTYPrice*1.00)+(FIXEDCHARGECost*0.50)+(WHEELINGCHARGESPrice*2.05))*0.2))
	PAIDTAX.set(Tax)
	
	TaxPay = (((ENERGYCHARGEPrice*5.49)+(GOVTELECTRITCITYDUTYPrice*1.50)+(FIXEDCHARGECost*0.50)+(WHEELINGCHARGESPrice*2.05))*0.2)
	Cost = (((ENERGYCHARGEPrice*5.49)+(GOVTELECTRITCITYDUTYPrice*1.50)+(FIXEDCHARGECost*0.50)+(WHEELINGCHARGESPrice*2.05)))
	CostofItems = "RS " + str("%.2f"%(TaxPay+Cost))
	TOTALBILLAMOUNT.set(CostofItems)
	
	x=random.randint(10034,699812)
	randomRef=str(x)

		

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',13,'bold'),width=15,text='TOTAL COST', command = CostOfOrder).grid(row=0,column=0)

btnRefer=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',13,'bold'),width=15,text='ID REFERENCE', command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',13,'bold'),width=15,text='RESET',command=Reset).grid(row=1,column=0)

btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',13,'bold'),width=15,text='EXIT',command=iExit).grid(row=1,column=1)



root.mainloop()



