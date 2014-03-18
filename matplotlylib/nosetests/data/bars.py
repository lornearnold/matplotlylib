D = dict(
    left=[0, 1, 2, 3, 4, 5],
    height=[10, 20, 50, 80, 100, 200],
    bottom=[0, 1, 2, 3, 4, 5, 6],
    width=[1, 4, 8, 16, 32, 64, 128],
    multi_left=[0, 10, 20, 30, 40, 50],
    multi_height=[1, 4, 8, 16, 32, 64],
    multi_bottom=[15, 30, 45, 60, 75, 90],
    multi_width=[30, 60, 20, 50, 60, 30]
)

VERTICAL_BAR = {
    'data': [{'bardir': 'v',
              'marker': {'color': '#0000FF', 'line': {'width': 1.0}},
              'opacity': 1,
              'type': 'bar',
              'xaxis': {},
              'yaxis': {},
              'x': [0.40000000000000002,
                    1.3999999999999999,
                    2.3999999999999999,
                    3.3999999999999999,
                    4.4000000000000004,
                    5.4000000000000004],
              'y': [10.0, 20.0, 50.0, 80.0, 100.0, 200.0]}],
    'layout': {'autosize': False,
               'hovermode': 'closest',
               'height': 480,
               'margin': {'b': 47, 'l': 80, 'pad': 0, 'r': 63, 't': 47},
               'showlegend': False,
               'width': 640,
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 6.0),
                         'showgrid': False,
                         'zeroline': False},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 200.0),
                         'showgrid': False,
                         'zeroline': False}}}

HORIZONTAL_BAR = {
    'data': [{'bardir': 'h',
              'marker': {'color': '#0000FF', 'line': {'width': 1.0}},
              'opacity': 1,
              'type': 'bar',
              'xaxis': {},
              'yaxis': {},
              'x': [0.40000000000000002,
                    1.3999999999999999,
                    2.3999999999999999,
                    3.3999999999999999,
                    4.4000000000000004,
                    5.4000000000000004,
                    6.4000000000000004],
              'y': [1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]}],
    'layout': {'autosize': False,
               'hovermode': 'closest',
               'height': 480,
               'margin': {'b': 47, 'l': 80, 'pad': 0, 'r': 63, 't': 47},
               'showlegend': False,
               'width': 640,
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 140.0),
                         'showgrid': False,
                         'zeroline': False},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 7.0),
                         'showgrid': False,
                         'zeroline': False}}}

H_AND_V_BARS = {
    'data': [{'bardir': 'v',
              'marker': {'color': '#008000', 'line': {'width': 1.0}},
              'opacity': 0.5,
              'type': 'bar',
              'xaxis': {},
              'yaxis': {},
              'x': [5.0, 15.0, 25.0, 35.0, 45.0, 55.0],
              'y': [1.0, 4.0, 8.0, 16.0, 32.0, 64.0]},
             {'bardir': 'h',
              'marker': {'color': '#FF0000', 'line': {'width': 1.0}},
              'opacity': 0.5,
              'type': 'bar',
              'x': [20.0, 35.0, 50.0, 65.0, 80.0, 95.0],
              'y': [30.0, 60.0, 20.0, 50.0, 60.0, 30.0]}],
    'layout': {'autosize': False,
               'hovermode': 'closest',
               'height': 480,
               'margin': {'b': 47, 'l': 80, 'pad': 0, 'r': 63, 't': 47},
               'showlegend': False,
               'width': 640,
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 60.0),
                         'showgrid': False,
                         'zeroline': False},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 100.0),
                         'showgrid': False,
                         'zeroline': False}}}


