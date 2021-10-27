import sqlite3
import pandas as pd


def citireTabelaDb(nume_db, nume_tabela, coloana_index):
    con = sqlite3.connect(nume_db)
    t = pd.read_sql_query("select * from " + nume_tabela, con, index_col=coloana_index)
    con.close()
    return t
