import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import cx_Oracle
import getpass
import os


def consulta(user, senha, sql):
    dsn = """(DESCRIPTION = (FAILOVER=ON)(LOAD_BALANCE=OFF)(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = *****)(PORT = ****)))(CONNECT_DATA = (SERVICE_NAME = ****)))"""
    con = cx_Oracle.connect(user=user, password=senha, dsn=dsn, encoding="UTF-8")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

user    = input("\n\n\n\tUsuário: ")
senha   = getpass.getpass(prompt="\tSenha: ", stream=None)


sql = """SQL NÃO DISPONÍVEL"""


dates = []
names = []
dados = consulta(user,senha,sql)

for dado in dados:
    dates.append(dado[0])
    names.append(f"[{dado[2]}x] {dado[1]} R${dado[3]}")

dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

levels = np.tile([-3, 3, -2, 2,-1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Linha do tempo de movimentações financeiras")

ax.vlines(dates, 0, levels, color="tab:blue", linestyles={'dashed'}, label=names)  
ax.plot(dates, np.zeros_like(dates), "-o",color="r", markerfacecolor="w")  

for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")


ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")



ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()