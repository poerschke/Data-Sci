import pandas as pd
import graphviz

planilha = 'rel.xlsx'

dados = pd.DataFrame()

dados = pd.read_excel(  planilha, 
                        names=[
                            'SOURCE_MODULE_REFERENCE', 
                            'DESTINATION_MODULE_REFERENCE', 
                            'ALOCACOES'
                        ],
                        usecols = [
                            0, 
                            1, 
                            2
                        ],
                        dtype = {
                            'SOURCE_MODULE_REFERENCE': str,
                            'DESTINATION_MODULE_REFERENCE': str,
                            'ALOCACOES': str
                        })


dot = graphviz.Digraph(comment="Grafo de alocações do ABC")

for i, linha in dados.iterrows():
    dot.edge(linha['SOURCE_MODULE_REFERENCE'], linha['DESTINATION_MODULE_REFERENCE'], label=linha['ALOCACOES'])

print(dot.source)
#dot.render('grafo.png', view=True)
