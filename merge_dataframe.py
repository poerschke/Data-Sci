import pandas as pd
import numpy as np
import cx_Oracle
import os
import getpass



print("[*] INFORME USUÁRIO E SENHA DO ORACLE")

user = input("\n\n\n[+] Usuário: ")
senha = getpass.getpass(prompt="[+] Senha: ", stream=None)

dsn = """(DESCRIPTION = (FAILOVER=ON)(LOAD_BALANCE=OFF)(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = *****)(PORT = ****)))(CONNECT_DATA = (SERVICE_NAME = *****)))"""
con = cx_Oracle.connect(user=user, password=senha, dsn=dsn, encoding="UTF-8")

data_referencia = input("[+] Data Referência (AAAAMMDD): ")
sql = f"SQL INDISPONÍVEL"



sheets = ['DigitacaoHoraExtraAtual.xlsx','DigitacaoHoraExtraPassado.xlsx','RHCaixa.xlsx','RHDESTAC.xlsx','RHFerias.xlsx','RHFUNC.xlsx','RHHEAdiant.xlsx','RHHEFolha.xlsx','RHHETrein.xlsx', 'RHFUNCtot.xlsx']

Todos	 			= pd.read_sql(sql, con)
RHFUNCtot           = pd.DataFrame()
HoraExtraAtual 		= pd.DataFrame()
HoraExtraPassado 	= pd.DataFrame()
RHCaixa 			= pd.DataFrame()
RHDESTAC 			= pd.DataFrame()
RHFerias			= pd.DataFrame()
RHFUNC 				= pd.DataFrame()
RHHoraExtraAdiant	= pd.DataFrame()
RHHoraExtraFolha	= pd.DataFrame()
RHHoraExtraTrein	= pd.DataFrame()


RHFUNCtot           = pd.read_excel(sheets[9],
    names = [
        'COD_FUNCIONARIO',
        'RHFUNCtot.ANO',
        'RHFUNCtot.MES',
        'RHFUNCtot.NOME',
        'RHFUNCtot.LOTACAO'     
    ],
    usecols = [0,1,2,4,5],
    dtype={
        'COD_FUNCIONARIO': str,
        'RHFUNCtot.ANO': str,
        'RHFUNCtot.MES': str,
        'RHFUNCtot.NOME': str,
        'RHFUNCtot.LOTACAO': str
    })

HoraExtraAtual 		= pd.read_excel(sheets[0], 
    names = [
        'HEA.COD_AGENCIA',
        'HEA.COD_DEPTO',
        'HEA.COD_EMPRESA_EMPREG',
        'COD_EMPREGADO',
        'HEA.COD_PROV_DESC',
        'HEA.QUANTIDADE',
        'HEA.TIPO',
        'HEA.DATA_CRIACAO',
        'HEA.COD_EMPRESA_USUARIO',
        'HEA.COD_EMPREGADO_USUARIO',
        'HEA.SITUACAO',
        'HEA.DATA_PROC',
        'HEA.ULT_ATUALIZACAO'
    ], 
    usecols=[1,2,5,6,7,8,9,10,11,12,13,14,15],
    dtype={
        'HEA.COD_AGENCIA': str,
        'HEA.COD_DEPTO': str,
        'HEA.COD_EMPRESA_EMPREG': str,
        'COD_EMPREGADO': str,
        'HEA.COD_PROV_DESC': str,
        'HEA.QUANTIDADE': float,
        'HEA.TIPO': str,
        'HEA.DATA_CRIACAO': str,
        'HEA.COD_EMPRESA_USUARIO': str,
        'HEA.COD_EMPREGADO_USUARIO': str,
        'HEA.SITUACAO': str,
        'HEA.DATA_PROC': str,
        'HEA.ULT_ATUALIZACAO': str
    })
    
    
HoraExtraPassado 	= pd.read_excel(sheets[1], 
    names = [
        'HEP.COD_EMPRESA',
        'HEP.COD_AGENCIA',
        'HEP.COD_DEPTO',
        'HEP.COD_EMPRESA_EMPREG',
        'COD_EMPREGADO',
        'HEP.COD_PROV_DESC',
        'HEP.QUANTIDADE',
        'HEP.TIPO',
        'HEP.DATA_CRIACAO',
        'HEP.COD_EMPRESA_USUARIO',
        'HEP.COD_EMPREGADO_USUARIO',
        'HEP.SITUACAO',
        'HEP.DATA_PROC',
        'HEP.ULT_ATUALIZACAO'
    ],
    usecols=[0,1,2,5,6,7,8,9,10,11,12,13,14,15],
    dtype={
        'HEP.COD_EMPRESA': str,
        'HEP.COD_AGENCIA': str,
        'HEP.COD_DEPTO': str,
        'HEP.COD_EMPRESA_EMPREG': str,
        'COD_EMPREGADO': str,
        'HEP.COD_PROV_DESC': str,
        'HEP.QUANTIDADE': float,
        'HEP.TIPO': str,
        'HEP.DATA_CRIACAO': str,
        'HEP.COD_EMPRESA_USUARIO': str,
        'HEP.COD_EMPREGADO_USUARIO': str,
        'HEP.SITUACAO': str,
        'HEP.DATA_PROC': str,
        'HEP.ULT_ATUALIZACAO': str
    })
    
    
RHCaixa 			= pd.read_excel(sheets[2], 
    names = [
        'COD_FUNCIONARIO',
        'RHC.120GRATIFIC_CAIXA',
        'RHC.125ABONO_DE_CAIXA'
    ],
    usecols=[2,3,4],
    dtype ={
        'COD_FUNCIONARIO': str,
        'RHC.120GRATIFIC_CAIXA': float,
        'RHC.125ABONO_DE_CAIXA': float    
    })
    
    
RHDESTAC 			= pd.read_excel(sheets[3], 
    names = [
        'COD_EMPREGADO',
        'RHD.NOME',
        'RHD.AF',
        'RHD.INICCUST',
        'RHD.FIMCCUST',
        'RHD.AG',
        'RHD.AGENCIA',
        'RHD.DP',
        'RHD.DV',
        'RHD.ST',
        'RHD.AR',
        'RHD.LOTACAO'
    ],
    usecols=[1,2,3,4,5,6,7,8,9,10,11,12],
    dtype ={
        'COD_EMPREGADO': str,
        'RHD.NOME': str,
        'RHD.AF': str,
        'RHD.INICCUST': str,
        'RHD.FIMCCUST': str,
        'RHD.AG': str,
        'RHD.AGENCIA': str,
        'RHD.DP': str,
        'RHD.DV': str,
        'RHD.ST': str,
        'RHD.AR': str,
        'RHD.LOTACAO': str
    })
    
    
RHFerias			= pd.read_excel(sheets[4], 
    names = [
        'COD_EMPREGADO',
        'RHF.INIFER',
        'RHF.FIMFER'
    ],
    usecols=[0,3,4],
    dtype={
        'COD_EMPREGADO': str,
        'RHF.INIFER': str,
        'RHF.FIMFER': str
    })
    
    
RHFUNC 				= pd.read_excel(sheets[5], 
    names = [
        'COD_FUNCIONARIO',
        'RHFUN.CODCCUS',
        'RHFUN.NOME',
        'RHFUN.LOTACAO',
        'RHFUN.FUNCAO',
        'RHFUN.NASC',
        'RHFUN.ADMISS',
        'RHFUN.SIT',
        'RHFUN.HORAS',
        'RHFUN.INIAFAS',
        'RHFUN.AF'
    ],
    usecols=[1,4,5,6,7,8,9,10,11,12,13],
    dtype={
        'COD_FUNCIONARIO': str,
        'RHFUN.CODCCUS': str,
        'RHFUN.NOME': str,
        'RHFUN.LOTACAO': str,
        'RHFUN.FUNCAO': str,
        'RHFUN.NASC': str,
        'RHFUN.ADMISS': str,
        'RHFUN.SIT': str,
        'RHFUN.HORAS': str,
        'RHFUN.INIAFAS': str,
        'RHFUN.AF': str
    })
    
    
RHHoraExtraAdiant	= pd.read_excel(sheets[6], 
    names = [
        'COD_FUNCIONARIO',
        'RHHEAD.202HORA_EXTRA(100)H',
        'RHHEAD.202HORA_EXTRA(100)V',
        'RHHEAD.206HORAS_EXTRAS(50)H',
        'RHHEAD.206HORAS_EXTRAS(50)V',
        'RHHEAD.211H_EXT_REP_REMUN_H',
        'RHHEAD.211H_EXT_REP_REMUN_V',
        'RHHEAD.225ADIC_NOT_S/HE(35)H',
        'RHHEAD.225ADIC_NOT_S/HE(35)V'
    ],
    usecols=[2,3,4,5,6,7,8,9,10],
    dtype={
        'COD_FUNCIONARIO': str,
        'RHHEAD.202HORA_EXTRA(100)H': float,
        'RHHEAD.202HORA_EXTRA(100)V': float,
        'RHHEAD.206HORAS_EXTRAS(50)H': float,
        'RHHEAD.206HORAS_EXTRAS(50)V': float,
        'RHHEAD.211H_EXT_REP_REMUN_H': float,
        'RHHEAD.211H_EXT_REP_REMUN_V': float,
        'RHHEAD.225ADIC_NOT_S/HE(35)H': float,
        'RHHEAD.225ADIC_NOT_S/HE(35)V': float
    })
    
    
RHHoraExtraFolha	= pd.read_excel(sheets[7], 
    names = [
        'COD_FUNCIONARIO',
        'RHHEFOL.202HORA_EXTRA(100)200',
        'RHHEFOL.206HORAS_EXTRAS(50)200',
        'RHHEFOL.206HORAS_EXTRAS(50)800',
        'RHHEFOL.206HORAS_EXTRAS(50)900',
        'RHHEFOL.209REM_HORAS_EXTRAS200',
        'RHHEFOL.209REM_HORAS_EXTRAS299',
        'RHHEFOL.211H_EXT_REP_REMUN_200',
        'RHHEFOL.211H_EXT_REP_REMUN_800',
        'RHHEFOL.211H_EXT_REP_REMUN_900',
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD000',
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD099',
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD800',
        'RHHEFOL.225ADIC_NOT_S/HE(35)200'
    ],
    usecols=[2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    dtype={
        'COD_FUNCIONARIO': str,
        'RHHEFOL.202HORA_EXTRA(100)200': float,
        'RHHEFOL.206HORAS_EXTRAS(50)200': float,
        'RHHEFOL.206HORAS_EXTRAS(50)800': float,
        'RHHEFOL.206HORAS_EXTRAS(50)900': float,
        'RHHEFOL.209REM_HORAS_EXTRAS200': float,
        'RHHEFOL.209REM_HORAS_EXTRAS299': float,
        'RHHEFOL.211H_EXT_REP_REMUN_200': float,
        'RHHEFOL.211H_EXT_REP_REMUN_800': float,
        'RHHEFOL.211H_EXT_REP_REMUN_900': float,
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD000': float,
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD099': float,
        'RHHEFOL.213HORAS_EXTRAS_DEC_JUD800': float,
        'RHHEFOL.225ADIC_NOT_S/HE(35)200': float
    })
    
    
RHHoraExtraTrein	= pd.read_excel(sheets[8], 
    names = [

        'RHHETREI.MOTIVO',
        'RHHETREI.COD_AGE',
        'RHHETREI.AGENCIA',
        'COD_FUNCIONARIO',
        'RHHETREI.EMPREGADO',
        'RHHETREI.H50(206)',
        'RHHETREI.H100(202)',
        'RHHETREI.REP_REM(211)',
        'RHHETREI.TOTAL'
    ],
    usecols=[2,3,4,5,6,7,8,9,10],
    dtype={
        'RHHETREI.MOTIVO': str,
        'RHHETREI.COD_AGE': str,
        'RHHETREI.AGENCIA': str,
        'COD_FUNCIONARIO': str,
        'RHHETREI.EMPREGADO': str,
        'RHHETREI.H50(206)': float,
        'RHHETREI.H100(202)': float,
        'RHHETREI.REP_REM(211)': float,
        'RHHETREI.TOTAL': float
})

RHFUNCtot.drop_duplicates(subset="COD_FUNCIONARIO", keep='first', inplace=True) 
Todos               = pd.merge(Todos, RHFUNCtot, how='left', on='COD_FUNCIONARIO')
Todos               = pd.merge(Todos, HoraExtraAtual, how='left', on='COD_EMPREGADO') 
Todos               = pd.merge(Todos, HoraExtraPassado, how='left', on='COD_EMPREGADO')
Todos               = pd.merge(Todos, RHDESTAC, how='left', on='COD_EMPREGADO')
Todos               = pd.merge(Todos, RHFerias, how='left', on='COD_EMPREGADO')
Todos               = pd.merge(Todos, RHFUNC, how='left', on='COD_FUNCIONARIO')
Todos               = pd.merge(Todos, RHHoraExtraAdiant, how='left', on='COD_FUNCIONARIO')
Todos               = pd.merge(Todos, RHHoraExtraFolha, how='left', on='COD_FUNCIONARIO')
Todos               = pd.merge(Todos, RHHoraExtraTrein, how='left', on='COD_FUNCIONARIO')


Todos.to_excel('resultado.xlsx', index=False)

print(Todos)
