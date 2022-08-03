import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("CHD3.csv")

fig = px.sunburst(
    data_frame=df,
    path=["", "Category", 'Symptom', "Type"],  # Root, branches, leaves
    color="",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    # maxdepth=-1,                        # set the sectors rendered. -1 will render all levels in the hierarchy
    # color="Victim's age",
    # color_continuous_scale=px.colors.sequential.BuGn,
    # range_color=[10,100],

    # branchvalues="total",               # or 'remainder'
    # hover_name="Unarmed",
    # # hover_data={'Unarmed': False},    # remove column name from tooltip  (Plotly version >= 4.8.0)
    # title="7-year Breakdown of Deaths by Police",
    # template='ggplot2',               # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
    #                                   # 'plotly_white', 'plotly_dark', 'presentation',
    #                                   # 'xgridoff', 'ygridoff', 'gridon', 'none'
)

fig.update_traces(textinfo='label')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()