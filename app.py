from tkinter import *
ventana = Tk()
ventana.title("Aplicacion")
ventana.configure(background="white")

x1_entry = Entry(ventana, fg="black", font=("Calibri 20"), background="light green")
x1_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
x1_text = Label(ventana, fg="black", font=("Calibri 20"), text='X1', background="light green")
x1_text.grid(row=0, column=1, columnspan=2, padx=10, pady=5)
operacion = Label(ventana, fg="black", font=("Calibri 20"), text='', background="light green")
x1_text.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

ventana.mainloop()