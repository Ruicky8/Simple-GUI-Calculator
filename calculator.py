import tkinter as tk

root = tk.Tk()
root.title("Calculator")

#Calculator Entry
CalcE = tk.Entry(root, width = 35, borderwidth = 3)
CalcE.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

class Calculator:
	def __init__(self):
		self.fnumber = "NULL"
		self.snumber = "NULL"
		self.reset = 0
		self.operator = 0
	
	def delete(self):
		CalcE.delete(0, tk.END)
		self.fnumber = self.snumber = "NULL"
	
	def numberInput(self, number):
		if (self.reset == 1):
			Calc.delete()
			self.reset = 0
		CalcE.insert(tk.END, number)
	
	def equal(self):
		self.snumber = float(CalcE.get())
		CalcE.delete(0, tk.END)
		self.reset = 1
		if self.operator == 1:
			CalcE.insert(0, self.fnumber + self.snumber)
		elif self.operator == 2:
			CalcE.insert(0, self.fnumber - self.snumber)
		elif self.operator == 3:
			CalcE.insert(0, self.fnumber * self.snumber)
		elif self.operator == 4:
			CalcE.insert(0, self.fnumber / self.snumber)
		self.fnumber = float(CalcE.get())
		self.snumber = "NULL"

	def operate(self, operation):
		self.operator = operation
		if self.fnumber != "NULL":
			CalcE.delete(0, tk.END)
			self.reset = 0
		else:
			self.fnumber = float(CalcE.get())
			CalcE.delete(0, tk.END)

Calc = Calculator()

#-------------------------------------------------------------------------------
#Buttons
button0 = tk.Button(root, text = "0", padx = 25, pady = 25, command = lambda: Calc.numberInput(0))
button1 = tk.Button(root, text = "1", padx = 25, pady = 25, command = lambda: Calc.numberInput(1))
button2 = tk.Button(root, text = "2", padx = 25, pady = 25, command = lambda: Calc.numberInput(2))
button3 = tk.Button(root, text = "3", padx = 25, pady = 25, command = lambda: Calc.numberInput(3))
button4 = tk.Button(root, text = "4", padx = 25, pady = 25, command = lambda: Calc.numberInput(4))
button5 = tk.Button(root, text = "5", padx = 25, pady = 25, command = lambda: Calc.numberInput(5))
button6 = tk.Button(root, text = "6", padx = 25, pady = 25, command = lambda: Calc.numberInput(6))
button7 = tk.Button(root, text = "7", padx = 25, pady = 25, command = lambda: Calc.numberInput(7))
button8 = tk.Button(root, text = "8", padx = 25, pady = 25, command = lambda: Calc.numberInput(8))
button9 = tk.Button(root, text = "9", padx = 25, pady = 25, command = lambda: Calc.numberInput(9))
buttonAdd 			 = tk.Button(root, text = "+", padx = 25, pady = 25, command = lambda: Calc.operate(1))
buttonSubstract 	 = tk.Button(root, text = "-", padx = 25, pady = 25, command = lambda: Calc.operate(2))
buttonMultiplication = tk.Button(root, text = "*", padx = 25, pady = 25, command = lambda: Calc.operate(3))
buttonDivision 		 = tk.Button(root, text = "/", padx = 25, pady = 25, command = lambda: Calc.operate(4))
buttonC 			 = tk.Button(root, text = "C", padx = 25, pady = 25, command = lambda: Calc.delete())
buttonEqual 		 = tk.Button(root, text = "=", padx = 25, pady = 25, command = lambda: Calc.equal())
#-------------------------------------------------------------------------------
#Button grid
button0.grid(row = 4, column = 0)
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
buttonDivision.		 grid(row = 1, column = 3)
buttonMultiplication.grid(row = 2, column = 3)
buttonSubstract.     grid(row = 3, column = 3)
buttonC.			 grid(row = 4, column = 1)
buttonEqual.		 grid(row = 4, column = 2)
buttonAdd.			 grid(row = 4, column = 3)
#-------------------------------------------------------------------------------
MadeBy = tk.Label(root, text = "Made by Ruicky8")
MadeBy.grid(row = 5, column = 0, columnspan = 4)


root.mainloop()
