import pydeck as pdk
import pandas as pd

dados = pd.DataFrame()

dados = pd.read_csv('c:\\users\\USER\\desktop\\estudo\\geo.csv')




view = pdk.data_utils.compute_view(dados[["lng","lat"]])

view.pitch = 150
view.bearing = 0

column_layer = pdk.Layer(
    "ColumnLayer",
    data=dados,
    get_position=["lng", "lat"],
    get_elevation="PCLIENTES",
    elevation_scale=100,
    
    radius=1000,
    get_fill_color=[3, 251, 3, 140],
    pickable=True,
    auto_highlight=True,
)

tooltip = {
    "html": "População: <b>{POP}</b><br>Clientes:<b>{PCLIENTES}% ({CLIENTES})</b><br>Clientes Ativos:<b>{C_Ativos}% ({ATIVOS})</b><br>Transações:<b>{TRANSACOES}</b><br>Movimentação Financeira:<b>R$ {MOV}</b>",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

r = pdk.Deck(
    layers = [column_layer],
    initial_view_state=view,
    tooltip=tooltip,
    map_provider="carto",
     map_style="light",
)

r.to_html("c:\\users\\USER\\desktop\\estudo\\column_layer.html")