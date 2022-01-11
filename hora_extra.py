from datetime import timedelta, date, time
import datetime
import time
import cx_Oracle
import getpass
import os

user    = ''
senha   = ''

user    = input("\n\n\n\tUsuário: ")
senha   = getpass.getpass(prompt="\tSenha: ", stream=None)

dsn     = """(DESCRIPTION = (FAILOVER=ON)(LOAD_BALANCE=ON)(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = ****)(PORT = ****)))(CONNECT_DATA = (SERVICE_NAME = ****)))"""
con     = cx_Oracle.connect(user=user, password=senha, dsn=dsn, encoding="UTF-8")

cur     = con.cursor()

sdate   = date(2016, 1,  1)
edate   = date(2021, 10, 30)



delta   = edate - sdate

arquivo = open("C:\\Users\\USER\\Desktop\\extracao_HE.txt", "a")
arquivo.write("COD_EMPRESA|COD_EMPREGADO|DATA_MARCA|E1|S1|E2|S2|JORNADA|HORA_EXTRA_ANALISTA|HORA_EXTRA_ESCRITURARIO|HORA_NEGATIVA_ANALISTA|HORA_NEGATIVA_ESCRITURARIO\n")
arquivo.close()


for i in range(delta.days + 1):
    day = sdate + timedelta(days = i)
    dia = str(day)
    dia = dia.replace('-', '')
    print(f"Buscando: {dia}")
    sql = f"""SELECT
                COD_EMPRESA,
                COD_EMPREGADO,
                DATA_MARCA,
                E1,
                S1,
                E2,
                S2,
                JORNADA,
                CASE WHEN ME_8 > 10 OR  HE_8 > 0 THEN LPAD(HE_8,2,0) || ':'|| LPAD(ME_8,2,0)
                ELSE '00:00' END AS HORA_EXTRA_ANALISTA,
                CASE WHEN ME_6 > 10 OR  HE_6 > 0 THEN LPAD(HE_6,2,0) || ':'|| LPAD(ME_6,2,0)
                ELSE '00:00' END AS HORA_EXTRA_ESCRITURARIO,
                CASE WHEN ME_8 < -10 OR HE_8 < 0 THEN '-' || LPAD( -1 * HE_8,2,0) || ':'|| LPAD(-1 * ME_8,2,0)
                ELSE '00:00' END AS HORA_NEGATIVA_ANALISTA,
                CASE WHEN ME_6 < -10 OR HE_6 < 0 THEN '-' || LPAD(-1 * HE_6,2,0) || ':'|| LPAD(-1 * ME_6,2,0)
                ELSE '00:00' END AS HORA_NEGATIVA_ESCRITURARIO
FROM
        (
        SELECT
                COD_EMPRESA,
                COD_EMPREGADO,
                DATA_MARCA,
                E1,
                S1,
                E2,
                S2,
                TO_CHAR(TO_TIMESTAMP(DATA_MARCA || ' ' || S1, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E1, 'YYYY-MM-DD:HH24:MI:SS') + TO_TIMESTAMP(DATA_MARCA || ' ' || S2, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E2, 'YYYY-MM-DD:HH24:MI:SS'), 'HH:MI') AS JORNADA,
                EXTRACT( HOUR FROM TO_TIMESTAMP(DATA_MARCA || ' ' || S1, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E1, 'YYYY-MM-DD:HH24:MI:SS') + TO_TIMESTAMP(DATA_MARCA || ' ' || S2, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E2, 'YYYY-MM-DD:HH24:MI:SS') - INTERVAL '8' HOUR) AS HE_8,
                EXTRACT( MINUTE FROM TO_TIMESTAMP(DATA_MARCA || ' ' || S1, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E1, 'YYYY-MM-DD:HH24:MI:SS') + TO_TIMESTAMP(DATA_MARCA || ' ' || S2, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E2, 'YYYY-MM-DD:HH24:MI:SS') - INTERVAL '8' HOUR) AS ME_8,
            EXTRACT( HOUR FROM TO_TIMESTAMP(DATA_MARCA || ' ' || S1, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E1, 'YYYY-MM-DD:HH24:MI:SS') + TO_TIMESTAMP(DATA_MARCA || ' ' || S2, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E2, 'YYYY-MM-DD:HH24:MI:SS') - INTERVAL '6' HOUR) AS HE_6,
            EXTRACT( MINUTE FROM TO_TIMESTAMP(DATA_MARCA || ' ' || S1, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E1, 'YYYY-MM-DD:HH24:MI:SS') + TO_TIMESTAMP(DATA_MARCA || ' ' || S2, 'YYYY-MM-DD:HH24:MI:SS') - TO_TIMESTAMP(DATA_MARCA || ' ' || E2, 'YYYY-MM-DD:HH24:MI:SS') - INTERVAL '6' HOUR) AS ME_6
        FROM
                (
                SELECT
                        COD_EMPRESA,
                        COD_EMPREGADO,
                        DATA_MARCA,
                        LPAD(TRUNC(MIN(ENTRADA) / 60), 2, 0) || ':' || LPAD(MOD(MIN(ENTRADA), 60), 2, 0) AS E1,
                        LPAD(TRUNC(MAX(ENTRADA) / 60), 2, 0) || ':' || LPAD(MOD(MAX(ENTRADA), 60), 2, 0) AS E2,
                        LPAD(TRUNC(MIN(SAIDA) / 60), 2, 0) || ':' || LPAD(MOD(MIN(SAIDA), 60), 2, 0) AS S1,
                        LPAD(TRUNC(MAX(SAIDA) / 60), 2, 0) || ':' || LPAD(MOD(MAX(SAIDA), 60), 2, 0) AS S2
                FROM
                        (
                        SELECT
                                COD_EMPRESA,
                                COD_EMPREGADO,
                                DATA_MARCA,
                                TIPO_MARCA,
                                CASE
                                        WHEN TIPO_MARCA = 'E' THEN HORA_MARCA
                                        ELSE NULL
                                END AS ENTRADA,
                                CASE
                                        WHEN TIPO_MARCA = 'S' THEN HORA_MARCA
                                        ELSE NULL
                                END AS SAIDA
                        FROM
                                TAB.TABELA
                        WHERE
                                COD_EMPRESA = 'B'
                                AND DATA_MARCA = TO_DATE('{dia}')
                        ORDER BY
                                DATA_MARCA ASC,
                                HORA_MARCA ASC )
                GROUP BY
                        COD_EMPRESA,
                        COD_EMPREGADO,
                        DATA_MARCA)
        WHERE
                E1 != E2
                AND S1 != S2)"""
                
    
    cur.execute(sql)
    rows = cur.fetchall()
    
    
    arquivo = open("C:\\Users\\USER\\Desktop\\extracao_HE.txt", "a")
    
    for linha in rows:
        arquivo.write(f"{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|{linha[5]}|{linha[6]}|{linha[7]}|{linha[8]}|{linha[9]}|{linha[10]}|{linha[11]}\n")
        
    arquivo.close()
    