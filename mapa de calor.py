import pandas as pd
import pydeck as pdk



cattle_df = pd.read_csv('c:\\users\\USER\\desktop\\estudo\\geo.csv')

COLOR_BREWER_BLUE_SCALE = [
    [240, 249, 232],
    [204, 235, 197],
    [168, 221, 181],
    [123, 204, 196],
    [67, 162, 202],
    [8, 104, 172],
]


view = pdk.data_utils.compute_view(cattle_df[["lng", "lat"]])
view.zoom = 6

cattle = pdk.Layer(
    "HeatmapLayer",
    data=cattle_df,
    opacity=0.9,
    get_position=["lng", "lat"],
    color_range=COLOR_BREWER_BLUE_SCALE,
    get_weight="PCLIENTES",
    pickable=False,
)




r = pdk.Deck(
    layers=[cattle],
    initial_view_state=view,
    map_provider="carto",
    map_style="light",
    tooltip={"text": "Concentração de clientes"},
)

r.to_html("c:\\users\\USER\\desktop\\estudo\\heatmap_layer.html")