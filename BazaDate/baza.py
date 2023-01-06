import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS produse ( id INTEGER PRIMARY KEY, nume TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS produse_detalii (
                produs_id INTEGER NOT NULL,
                pret REAL,
                stock INTEGER,
                FOREIGN KEY (produs_id) REFERENCES produse(id)
            )''')
c.execute('''CREATE TABLE IF NOT EXISTS stock_final (
                Stock_id INTEGER NOT NULL,
                Stock_Initial INTEGER,
                Stock_Final INTEGER,
                FOREIGN KEY (Stock_Initial) REFERENCES produse_detalii(stock)
            )''')
c.execute('''CREATE TABLE IF NOT EXISTS raport_final_zi (
                nume_produs TEXT,
                stock_vandut INTEGER,
                profit REAL,
                FOREIGN KEY (nume_produs) REFERENCES produse(nume)
            )''')

#c.commit()
#c.close()