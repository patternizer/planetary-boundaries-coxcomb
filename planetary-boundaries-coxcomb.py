#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# PROGRAM: planetary-boundaries-coxcomb.py
#------------------------------------------------------------------------------
# Version 0.1
# 22 February, 2023
# Michael Taylor
# https://patternizer.github.io
# michael DOT a DOT taylor AT uea DOT ac DOT uk 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# IMPORT PYTHON LIBRARIES
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------------------------------
# SETTINGS
#------------------------------------------------------------------------------

size = 0.6

#------------------------------------------------------------------------------
# CONSTRUCT: coxcomb
#------------------------------------------------------------------------------

# SET: segment angles

val_array = np.ones([8,18]) * 20

# INITIALISE: full chart colour scheme

colors = ['#BBCFA5', '#7FA95D', '#FDB713', '#F47820', '#FFFFFF']
colors1 = np.tile(colors[0], 18 )
colors2 = np.tile(colors[1], 18 )
colors3 = np.tile(colors[1], 18 )
colors4 = np.tile(colors[2], 18 )
colors5 = np.tile(colors[2], 18 )
colors6 = np.tile(colors[3], 18 )
colors7 = np.tile(colors[3], 18 )
colors8 = np.tile(colors[3], 18 )
color_array = np.vstack( [ colors1, colors2, colors3, colors4, colors5, colors6, colors6, colors7, colors8 ] )

# MASK: missing values (colors[4]='white')

color_array[2:,0] = colors[4]
color_array[1:,1] = colors[4]
color_array[1:,2] = colors[4]
color_array[4:,3] = colors[4]
color_array[4:,4] = colors[4]
color_array[1:,6] = colors[4]
color_array[4:,7] = colors[4]
color_array[4:,8] = colors[4]
color_array[2:,9] = colors[4]
color_array[2:,10] = colors[4]
color_array[6:,11] = colors[4]
color_array[8:,12] = colors[4]
color_array[3:,13] = colors[4]
color_array[3:,14] = colors[4]
color_array[1:,15] = colors[4]
color_array[1:,16] = colors[4]
color_array[2:,17] = colors[4]


#------------------------------------------------------------------------------
# PLOT: planetary boundaries chart
#------------------------------------------------------------------------------

fig, ax = plt.subplots()
for i in range(8):
    ax.pie(val_array[i,:], radius=1+size*i, colors=color_array[i,:], wedgeprops=dict(width=size, edgecolor='w'))    
ax.set(aspect="equal")
plt.savefig('planetary-boundaries.png', dpi=300, bbox_inches='tight')

#------------------------------------------------------------------------------
print('** END')


