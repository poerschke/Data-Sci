import pandas as pd
import numpy as np

from bokeh.models import *
from bokeh.plotting import *
from bokeh.io import *
from bokeh.tile_providers import *
from bokeh.palettes import *
from bokeh.transform import *
from bokeh.layouts import *



conflict_df=pd.read_csv("C:\\Users\\USER\\Desktop\\Estudo\\conflict_data_irq.csv")
conflict_df=conflict_df.loc[conflict_df['year'] == '2019']
conflict_df['latitude']=conflict_df['latitude'].astype('float')
conflict_df['longitude']=conflict_df['longitude'].astype('float')
conflict_df['fatalities']=conflict_df['fatalities'].astype('int64')
conflict_df=conflict_df.reset_index()
conflict_df=conflict_df.drop('index',axis=1)



def wgs84_to_web_mercator(df, lon, lat):
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

df=wgs84_to_web_mercator(conflict_df,'longitude','latitude')



scale=2000
x=df['x']
y=df['y']


x_min=int(x.mean() - (scale * 350))
x_max=int(x.mean() + (scale * 350))
y_min=int(y.mean() - (scale * 350))
y_max=int(y.mean() + (scale * 350))


tile_provider=get_provider(OSM)


plot=figure(
    title='2019 Iraq Conflict Events',
    match_aspect=True,
    tools='wheel_zoom,pan,reset,save',
    x_range=(x_min, x_max),
    y_range=(y_min, y_max),
    x_axis_type='mercator',
    y_axis_type='mercator'
    )

plot.grid.visible=True

map=plot.add_tile(tile_provider)
map.level='underlay'

plot.xaxis.visible = False
plot.yaxis.visible=False


def hex_map(plot,df, scale,leg_label='Hexbin Heatmap'):
  r,bins=plot.hexbin(x,y,size=scale*10,hover_color='pink',hover_alpha=0.8,legend_label=leg_label)
  hex_hover = HoverTool(tooltips=[('count','@c')],mode='mouse',point_policy='follow_mouse',renderers=[r])
  hex_hover.renderers.append(r)
  plot.tools.append(hex_hover)
  
  plot.legend.location = "top_right"
  plot.legend.click_policy="hide"

def bubble_map(plot,df,radius_col,lon,lat,scale,color='orange',leg_label='Bubble Map'):
  radius=[]
  for i in df[radius_col]:
    radius.append(i*scale)
  
  df['radius']=radius
    
  source=ColumnDataSource(df)
  c=plot.circle(x='x',y='y',color=color,source=source,size=1,fill_alpha=0.4,radius='radius',legend_label=leg_label,hover_color='red')

  tip_label='@'+radius_col
  lat_label='@'+lat
  lon_label='@'+lon

  circle_hover = HoverTool(tooltips=[(radius_col,tip_label),('Lat:',lat_label),('Lon:',lon_label)],mode='mouse',point_policy='follow_mouse',renderers=[c])
  circle_hover.renderers.append(c)
  plot.tools.append(circle_hover)

  plot.legend.location = "top_right"
  plot.legend.click_policy="hide"

hex_map(plot=plot,
        df=conflict_df, 
        scale=scale,
        leg_label='Iraq Conflict Events by Number of Events')

bubble_map(plot=plot,
           df=conflict_df,
           radius_col='fatalities', 
           leg_label='Iraq Conflict Events by Fatality',
           lon='longitude',
           lat='latitude',
           scale=scale)

show(plot)