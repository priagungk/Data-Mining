#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 06:22:44 2018

@author: priagung
"""

import networkx as nx
import pandas as pd
from networkx.algorithms import bipartite

df = pd.read_excel("<Dir>")
G = nx.from_pandas_dataframe(df, '<Column_1>', '<Column_2>')
W = bipartite.weighted_projected_graph(G, df['Column_2'].unique())
X = nx.to_pandas_dataframe(W)
