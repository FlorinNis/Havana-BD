from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import BazaDate.baza as baza

id=1

def startNewWindow(newWindow):
    newWindow.iconify()
    newWindow.deiconify()

    newWindow.title("Havana Bar")
    newWindow.geometry("500x600")
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
    #data = [
    #    [1,"Timisoreana",5,40],
    #    [2,"Holsten", 5, 30]
    #
    #]

    #baza.c.execute('''INSERT INTO produse_detalii (produs_id, pret, stock) values(?,?,?)''', (1, 5, 20))
    #baza.conn.commit()

    global count
    count = 0
    baza.c.execute('''SELECT produse.id, produse.nume, produse_detalii.pret, produse_detalii.stock
                               FROM produse INNER JOIN produse_detalii
                               ON produse.id = produse_detalii.produs_id''')

    for row in baza.c.fetchall():
        id, nume, pret, stock = row
        my_table.insert('', 'end', values=(id, nume, pret, stock))
        count += 1

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

        if id_entry.get() and produs_nume_entry.get():
            my_table.insert(parent='', index='end',iid=count, text='', values =(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(), produs_stock_entry.get()))
            count += 1

            baza.c.execute('''INSERT INTO produse (id, nume) values(?,?)''', (id_entry.get(),produs_nume_entry.get()))
            baza.c.execute('''INSERT INTO produse_detalii (produs_id, pret, stock) values(?,?,?)''', (id_entry.get(), produs_pret_entry.get(), produs_stock_entry.get()))
            baza.conn.commit()


            id_entry.delete(0,END)
            produs_nume_entry.delete(0,END)
            produs_pret_entry.delete(0,END)
            produs_stock_entry.delete(0,END)
        else:
            #messagebox.showerror("Error", "Va rog sa introduceti valorile in casete inainte sa adaugati")
            root = Tk()
            root.title("Error")
            label = Label(root, text="Va rog sa introduceti valorile in casete inainte sa adaugati!")
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
            button = Button(root, text="OK", command=lambda: root.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            root.mainloop()

    #Buton
    input_button = Button(newWindow, text="Adaugare Produs",command=input_record)
    input_button.pack()

    #Select Record
    def select_record():
        id_entry.delete(0, END)
        produs_nume_entry.delete(0, END)
        produs_pret_entry.delete(0, END)
        produs_stock_entry.delete(0, END)

        selected = my_table.focus()
        values = my_table.item(selected,'values')
        id_entry.insert(0,values[0])
        produs_nume_entry.insert(0,values[1])
        produs_pret_entry.insert(0,values[2])
        produs_stock_entry.insert(0,values[3])

    def actualizare_nume():
        if id_entry.get() and produs_nume_entry.get():
            selected = my_table.focus()
            my_table.item(selected,text="",values=(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(),produs_stock_entry.get()))

            baza.c.execute('''UPDATE produse SET nume = ? WHERE id = ?''', (produs_nume_entry.get(), id_entry.get()))
            baza.conn.commit()

            id_entry.delete(0, END)
            produs_nume_entry.delete(0, END)
            produs_pret_entry.delete(0, END)
            produs_stock_entry.delete(0, END)
        else:
            #messagebox.showerror("Error", "Nu puteti actualiza produsul! Nu au fost introduse date")
            root = Tk()
            root.title("Error")
            label = Label(root, text="Va rog sa introduceti valorile in casete inainte sa actualizati produsul!")
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
            button = Button(root, text="OK", command=lambda: root.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            root.mainloop()

    def actualizare_pret():
        if id_entry.get() and produs_pret_entry.get():
            selected = my_table.focus()
            my_table.item(selected,text="",values=(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(),produs_stock_entry.get()))

            baza.c.execute('''UPDATE produse_detalii SET pret = ? WHERE produs_id = ?''', (produs_pret_entry.get(), id_entry.get()))
            baza.conn.commit()

            id_entry.delete(0, END)
            produs_nume_entry.delete(0, END)
            produs_pret_entry.delete(0, END)
            produs_stock_entry.delete(0, END)
        else:
            #messagebox.showerror("Error", "Nu puteti actualiza produsul! Nu au fost introduse date")
            root = Tk()
            root.title("Error")
            label = Label(root, text="Va rog sa introduceti valorile in casete inainte sa actualizati produsul!")
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
            button = Button(root, text="OK", command=lambda: root.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            root.mainloop()

    def actualizareStock():
        if produs_stock_entry.get():
            selected = my_table.focus()
            my_table.item(selected, text="", values=(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(), produs_stock_entry.get()))

            stock_produse_detalii = baza.c.execute('''SELECT stock FROM produse_detalii WHERE produs_id = ?''', (id_entry.get(),))
            stock = stock_produse_detalii.fetchone()[0]
            baza.c.execute('''insert into stock_final (Stock_id, Stock_Initial, Stock_Final) values(?,?,?)''', (id_entry.get(), stock, produs_stock_entry.get()))
            baza.conn.commit()

            id_entry.delete(0, END)
            produs_nume_entry.delete(0, END)
            produs_pret_entry.delete(0, END)
            produs_stock_entry.delete(0, END)

    def actualizareStockMarfaNoua():
        if produs_stock_entry.get():
            selected = my_table.focus()
            my_table.item(selected, text="", values=(id_entry.get(), produs_nume_entry.get(), produs_pret_entry.get(), produs_stock_entry.get()))

            baza.c.execute('''UPDATE produse_detalii SET stock = ? WHERE produs_id = ?''', (produs_stock_entry.get(), id_entry.get()))
            baza.conn.commit()

            id_entry.delete(0, END)
            produs_nume_entry.delete(0, END)
            produs_pret_entry.delete(0, END)
            produs_stock_entry.delete(0, END)

    def raportFinalZi():

        #Adaugare in tabelul raport_final_zi
        baza.c.execute('''
                        INSERT INTO raport_final_zi (nume_produs, stock_vandut, profit)
                        SELECT p.nume, (sf.Stock_Initial - sf.Stock_Final), (sf.Stock_Initial - sf.Stock_Final) * pd.pret
                        FROM produse p
                        INNER JOIN stock_final sf ON p.id = sf.Stock_id
                        INNER JOIN produse_detalii pd ON p.id = pd.produs_id
                    ''')
        baza.conn.commit()

        Total = baza.c.execute('''SELECT SUM(profit) FROM raport_final_zi''')
        total = Total.fetchone()[0]


        raport = Tk()
        raport.title("Raport Final Zi")
        raport.geometry("500x500")
        raport.configure(bg='lightgrey')

        raport_frame = Frame(raport)
        raport_frame.pack()

        # scrollbar
        table_scroll = Scrollbar(raport_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        table_scroll = Scrollbar(raport_frame, orient='horizontal')
        table_scroll.pack(side=BOTTOM, fill=Y)

        raportTable = ttk.Treeview(raport_frame, yscrollcommand=table_scroll.set, xscrollcommand=table_scroll.set)

        raportTable.pack()

        table_scroll.config(command=raportTable.yview)
        table_scroll.config(command=raportTable.xview)

        # Definire coloane
        raportTable['columns'] = ('Nume Produs', 'Cantitate Vanduta', 'Profit')

        # formatare coloane
        raportTable.column("#0", width=0, stretch=NO)
        raportTable.column("Nume Produs", anchor=CENTER, width=80)
        raportTable.column("Cantitate Vanduta", anchor=CENTER, width=80)
        raportTable.column("Profit", anchor=CENTER, width=80)

        raportTable.heading("#0", text="", anchor=CENTER)
        raportTable.heading("Nume Produs", text="Nume Produs", anchor=CENTER)
        raportTable.heading("Cantitate Vanduta", text="Cantitate Vanduta", anchor=CENTER)
        raportTable.heading("Profit", text="Profit(RON)", anchor=CENTER)

        global count
        count = 0
        baza.c.execute('''SELECT raport_final_zi.nume_produs, raport_final_zi.stock_vandut, raport_final_zi.profit
                                       FROM raport_final_zi ''')

        for row in baza.c.fetchall():
            nume, stock, profit = row
            raportTable.insert('', 'end', values=(nume, stock, profit))
            count += 1


        raport.mainloop()

    #Butoane

    select_button = Button(newWindow, text="Selectare Produs", command=select_record)
    select_button.pack(pady=10)

    nume_button = Button(newWindow, text="Actualizare Nume",command=actualizare_nume)
    nume_button.pack(pady=10)

    pret_button = Button(newWindow, text="Actualizare Pret",command=actualizare_pret)
    pret_button.pack(pady=10)

    stock_button = Button(newWindow, text="Actualizare Stock Final Zi", command=actualizareStock)
    stock_button.pack(pady=10)

    stockPlus_button = Button(newWindow, text="Actualizare Stock Marfa Noua", command=actualizareStockMarfaNoua)
    stockPlus_button.pack(pady=10)

    raportFinal = Button(newWindow, text="Raport Final Zi", command=raportFinalZi)
    raportFinal.pack(pady=10)



    my_table.pack()
