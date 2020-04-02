import plotly.express as px
from myproject import db
from myproject.models import Animal




animals = Animal.query.all()

fe =animals[0].feedEfficiency
mp = animals[0].ch4_daily_mean
we = animals[0].waterEfficieny

fig = px.bar(x=["Feed Efficieny","Water Efficiency", "Methane Production"], y =[fe, we,mp ])
fig.update_layout(xaxis_type='category',
                  title_text='Bar chart with categorical axes')
fig.show()