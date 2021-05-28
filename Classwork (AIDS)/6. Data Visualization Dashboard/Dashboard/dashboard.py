import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(20)
x = np.random.randint(1, 100, 100)
y = np.random.randint(1, 100, 100)

data = [go.Scatter(x=x, y=y, mode="markers")]

pyo.plot(data, filename="scatter.html")