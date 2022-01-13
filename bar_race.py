import bar_chart_race as bcr
import pandas as pd
df = pd.read_excel("C:\\Users\\dougl\\OneDrive\\Desktop\\dataset.xlsx", index_col='date', parse_dates=['date'])
df.tail

bcr.bar_chart_race(
    df=df,
    filename='C:\\Users\\dougl\\OneDrive\\Desktop\\contas.mp4',
    orientation='h',
    sort='desc',
    n_bars=11,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=100,
    interpolate_period=False,
    label_bars=True,
    bar_size=.55,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Custo Total: R$ {v.nlargest(11).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=5000,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12_r',
    title='',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)  