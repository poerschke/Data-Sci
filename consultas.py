import cx_Oracle
import os
import getpass
from datetime import date, datetime, timedelta
from workalendar.america import Brazil
from calendar import monthrange


print("[*] INFORME USUÁRIO E SENHA DO ORACLE")

user = input("\n\n\n[+] Usuário: ")
senha = getpass.getpass(prompt="[+] Senha: ", stream=None)

tabelas = ['tabela1', 'tabela2', 'tabela3', 'tabela4']





def diasUteis(ano, mes):
	diasNoMes = monthrange(ano, mes)[1]
	if mes < 10:
		mes = f"0{mes}"
	inicio = f"{ano}-{mes}-01"
	fim = f"{ano}-{mes}-{diasNoMes}"

	cal = Brazil()
	uteis = 0
	carnaval1 = 0
	carnaval2 = 0

	for dia in cal.holidays(ano):
		if dia[1] == "Easter Sunday":
			carnaval1 = dia[0] - timedelta(days=48)
			carnaval2 = dia[0] - timedelta(days=47)
	for i in range(1, diasNoMes+1):
		d = i
		if d < 10 :
			d = f"0{i}"

		if cal.is_working_day(datetime.strptime(f"{ano}-{mes}-{d}", '%Y-%m-%d').date()):
			uteis += 1

		if datetime.strptime(f"{ano}-{mes}-{d}", '%Y-%m-%d').date() == carnaval1 :
			uteis -= 1

		if datetime.strptime(f"{ano}-{mes}-{d}", '%Y-%m-%d').date() == carnaval2 :
			uteis -= 1

	return uteis
    





def consulta(sql):
    dsn = """(DESCRIPTION = (FAILOVER=ON)(LOAD_BALANCE=OFF)(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = *****)(PORT = ****)))(CONNECT_DATA = (SERVICE_NAME = ****)))"""
    con = cx_Oracle.connect(user=user, password=senha, dsn=dsn, encoding="UTF-8")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows







def verifica_acesso(tabela, user, senha):
    sql = """SELECT * FROM """ + tabela + """ WHERE ROWNUM <= 1"""
    try:
        dsn = """(DESCRIPTION = (FAILOVER=ON)(LOAD_BALANCE=OFF)(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = *****)(PORT = ****)))(CONNECT_DATA = (SERVICE_NAME = ****)))"""
        con = cx_Oracle.connect(user=user, password=senha, dsn=dsn, encoding="UTF-8")
        cur = con.cursor()
    except cx_Oracle.DatabaseError:
        print("Nao conectou ao ORACLE, verifique usuário e senha e execute a aplicação novamente.")
        os._exit(1)
    else:
        try:
            cur.execute(sql)
            rows = cur.fetchall()
        except cx_Oracle.DatabaseError as e:
            errorObj, = e.args
            if errorObj.code == 942:
                print(f"[NOK] sem acesso {tabela}")
            else:
                print(f"[NOK] outro erro tabela {tabela}")
        else:
            print(f"[OK] com acesso a {tabela}")








def verifica_acessos():
    for tabela in tabelas:
        verifica_acesso(tabela, user, senha)
    menu()









def caixas_aberto():
    data_inicio = input("[+] Primeiro dia do mês (AAAAMMDD):\t")
    data_fim = input("[+] Último dia do mês (AAAAMMDD):\t")
    
    sql = """SQL INDISPONÍVEL"""
    linhas = consulta(sql)
    arquivo = open("caixa_aberto.txt", "w")
    arquivo.write("DATA_TRANSACAO|AGENCIA|MATRICULA|QTD_ABERTURAS_DE_CX_NO_DIA\n")
    for linha in linhas:
        arquivo.write(f"{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}\n")
    arquivo.close()
    print("Arquivo caixa_aberto.txt gravado com sucesso.")
    menu()
    
    
    
    
    


def contaFeriadosLocais(ano, mes, agencia):
    sql = """SELECT COUNT(*) FROM TABELA WHERE REGEXP_LIKE(DATA_AGENCIA, '^"""+ ano + mes +"""[0-9]{2}'||LPAD("""+agencia+""",4,0)||'$') AND TO_CHAR(TO_TIMESTAMP(TO_CHAR(substr(DATA_AGENCIA, 1,8)), 'YYYY/MM/DD'), 'd') NOT IN (1,7)"""
    linhas = consulta(sql)
    for linha in linhas:
        return int(linha[0])





        
    
    
    
def caixas_fechado():
    data_inicio = input("[+] Primeiro dia do mês (AAAAMMDD):\t")
    data_fim = input("[+] Último dia do mês (AAAAMMDD):\t")

    sql = """SQL INDISPONÍVEL"""
    

    linhas = consulta(sql)
    
    arquivo = open("caixa_fechado_mes.txt", "w")
    arquivo.write("ANO|MES|AGENCIA|MATRICULA|DIAS_ABERTURA_CX|DIAS CAIXA_55%\n")
    print("\nConsulta da abertura de caixas pronta.")
    
    
    print("\nCalculando os dias de caixa 55%, vai tomar um café e volta em 5 minutos")
    x = 0
    total = len(linhas)
    for linha in linhas:
        x += 1
        print(f"[{x} - {total}]", end="\r")
        arquivo.write(f"{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}")
        
        feriados = contaFeriadosLocais(str(linha[0]), str(linha[1]), str(linha[2]))
        
        dias = diasUteis(int(linha[0]), int(linha[1].strip()))
        dias_Cx_55 = (dias - feriados) * 0.55
        arquivo.write(f"|{dias_Cx_55:.2f}\n")
    arquivo.close()
    print("Arquivo caixa_fechado_mes.txt gravado com sucesso.")
    menu()




def gera_dias_uteis():
    ano = input("[+] Ano (AAAA):\t")
    mes = input("[+] Mês (MM):\t")
    
    sql = """SQL INDISPONÍVEL"""
    
    linhas = consulta(sql)
    arquivo = open("caixa_dias_uteis.txt", "w")
    arquivo.write("ANO|MES|AGENCIA|DIAS CAIXA_55%|DiasUteis\n")
    print("\nCalculando os dias de caixa 55%, vai tomar um copo de água e volte logo")
    x = 0
    total = len(linhas)
    for linha in linhas:
        x += 1
        print(f"[{x} - {total} Agências]", end="\r")
        arquivo.write(f"{ano}|{mes}|{linha[0]}")
        
        feriados = contaFeriadosLocais(ano, mes, linha[0])
        
        dias = diasUteis(int(ano.strip()), int(mes.strip()))
        dias_Cx_55 = (dias - feriados) * 0.55
        arquivo.write(f"|{dias_Cx_55:.2f}|{(dias - feriados)}\n")
    arquivo.close()
    print("arquivo caixa_dias_uteis.txt gerado com sucesso")




def menu():
    print("\n\nDesenvolvido por user\n\n-------------------- Menu --------------------\n0\tSair\n1\tVerificar acessos às tabelas\n2\tCaixas aberto por dia\n3\tCaixas fechado por mes\n4\tGera arquivo dias caixa\n")
    opcao = int(input("[+] Opção: "))
    print("----------------------------------------------\n")
    if opcao == 0:
        os._exit(1)
    elif opcao == 1:
        verifica_acessos()
    elif opcao == 2:
        caixas_aberto()
    elif opcao == 3:
        caixas_fechado()
    elif opcao == 4:
        gera_dias_uteis()
    else:
        menu()
        
        
menu()