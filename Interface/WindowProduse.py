from tkinter import *
from tkinter import ttk


def startNewWindow(newWindow):
    newWindow.iconify()
    newWindow.deiconify()

    newWindow.title("Havana Bar")
    newWindow.geometry("500x500")
    #window.configure(width=500, height=500)
    newWindow.configure(bg='lightgrey')

    tableProduse(newWindow)

    newWindow.mainloop()

def tableProduse(newWindow):
    table_frame = Frame(newWindow)
    table_frame.pack()

    #scrollbar
    table_scroll = Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)

    table_scroll = Scrollbar(table_frame, orient='horizontal')
    table_scroll.pack(side=BOTTOM, fill=Y)

    my_table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set, xscrollcommand=table_scroll.set)

    my_table.pack()

    table_scroll.config(command=my_table.yview)
    table_scroll.config(command=my_table.xview)

    #Definire coloane
    my_table['columns'] = ('ID_produs', 'produs_nume', 'produs_pret', 'produs_stock')

    #formatare coloane
    my_table.column("#0", width=0, stretch=NO)
    my_table.column("ID_produs", anchor=CENTER, width=80)
    my_table.column("produs_nume", anchor=CENTER, width=80)
    my_table.column("produs_pret",anchor=CENTER,width=80)
    my_table.column("produs_stock",anchor=CENTER,width=80)

    my_table.heading("#0",text="",anchor=CENTER)
    my_table.heading("ID_produs", text="ID", anchor=CENTER)
    my_table.heading("produs_nume", text="Nume", anchor=CENTER)
    my_table.heading("produs_pret", text="Pret", anchor=CENTER)
    my_table.heading("produs_stock", text="Stock Produs", anchor=CENTER)

    #adaugareData

    #my_table.insert(parent='', index='end', iid=0, text='',
    #               values=('1', 'Timisoreana', '5', '40' ))
    #my_table.insert(parent='', index='end', iid=1, text='',
    #               values=('2', 'Holsten', '4', '30'))
    #...
    data = [
        [1,"Timisoreana",5,40],
        [2,"Holsten", 5, 30]

    ]

    global count
    count = 0
    for record in data:
        my_table.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3]))
        count+=1

    input_frame=Frame(newWindow)
    input_frame.pack()

    id = Label(input_frame,text="ID")
    id.grid(row=0,column=0)

    produs_nume = Label(input_frame,text="Nume produs")
    produs_nume.grid(row=0,column=1)

    produs_pret = Label(input_frame, text="Pret Produs")
    produs_pret.grid(row=0,column=2)

    produs_stock = Label(input_frame, text="Stock Produs")
    produs_stock.grid(row=0, column=3)

    id_entry = Entry(input_frame)
    id_entry.grid(row=1,column=0)

    produs_nume_entry = Entry(input_frame)
    produs_nume_entry.grid(row=1,column=1)

    produs_pret_entry = Entry(input_frame)
    produs_pret_entry.grid(row=1,column=2)

    produs_stock_entry = Entry(input_frame)
    produs_stock_entry.grid(row=1, column=3)

    def input_record():
        global count

        my_table.insert(parent='', index='end',iid=count, text='', values =(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(), produs_stock_entry.get()))
        count+=1

        id_entry.delete(0,END)
        produs_nume_entry.delete(0,END)
        produs_pret_entry.delete(0,END)
        produs_stock_entry.delete(0,END)

    #Buton
    input_button = Button(newWindow, text="Adaugare Produs",command=input_record)

    input_button.pack()

    my_table.pack()
