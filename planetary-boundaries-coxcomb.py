#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# PROGRAM: planetary-boundaries-coxcomb.py
#------------------------------------------------------------------------------
# Version 0.2
# 10 November, 2023
# Michael Taylor
# https://patternizer.github.io
# michael DOT a DOT taylor AT uea DOT ac DOT uk 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# IMPORT PYTHON LIBRARIES
#------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np

#------------------------------------------------------------------------------
# SETTINGS
#------------------------------------------------------------------------------

size = 1.0          # pie fraction (1 --> inner hole = 0 )
nsegments = 9
wedgeangle = 20
use_mask = True

nwedges = int( 360 / wedgeangle)

#------------------------------------------------------------------------------
# METHODS
#------------------------------------------------------------------------------

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

#------------------------------------------------------------------------------
# COLORMAP
#------------------------------------------------------------------------------

'''
# https://www.rapidtables.com/web/color/color-tester.html
# https://www.canaries.co.uk/_nuxt/img/ncfc-new.16dfd00.png 

color1 = tuple( hex_to_rgb("#E4E4E4")[i]/255.0 for i in range(3) ) # NCFC: light grey
color2 = tuple( hex_to_rgb("#FFF200")[i]/255.0 for i in range(3) ) # NCFC: yellow
color3 = tuple( hex_to_rgb("#038C40")[i]/255.0 for i in range(3) ) # NCFC: green
colorlist = [ 'silver', color2, color3 ]
cmap_stripes = LinearSegmentedColormap.from_list('testCmap', colors=colorlist, N=256)
'''

#------------------------------------------------------------------------------
# CONSTRUCT: coxcomb
#------------------------------------------------------------------------------

# SET: segment angles

val_array = np.ones([ nsegments, nwedges]) * wedgeangle

# INITIALISE: full chart colour scheme

# 0 WHITE         #ffffff
# 1 LIGHT GREY    #efefef
# 2 GREY          #d9d9d9
# 3 LIGHT GREEN   #2ba05f
# 4 GREEN         #268c53
# 5 LIGHT ORANGE  #f9a734
# 6 ORANGE        #ff7043
# 7 DARK ORANGE   #e13521

colors = ['#ffffff', '#efefef', '#d9d9d9', '#2ba05f', '#268c53', '#f9a734', '#ff7043', '#e13521']

colors1 = np.tile(colors[4], 18 )
colors2 = np.tile(colors[4], 18 )
colors3 = np.tile(colors[4], 18 )
colors4 = np.tile(colors[5], 18 )
colors5 = np.tile(colors[5], 18 )
colors6 = np.tile(colors[6], 18 )
colors7 = np.tile(colors[6], 18 )
colors8 = np.tile(colors[7], 18 )
colors9 = np.tile(colors[7], 18 )
color_array = np.vstack( [ colors1, colors2, colors3, colors4, colors5, colors6, colors7, colors8, colors9 ] )

# MASK: missing values (colors[4]='white')

if use_mask == True:

    '''
    # 2009
    
    color_array[2:,0] = colors[2]
    color_array[1:,1] = colors[2]
    color_array[1:,2] = colors[2]
    color_array[4:,3] = colors[2]
    color_array[4:,4] = colors[2]
    color_array[1:,6] = colors[2]
    color_array[4:,7] = colors[2]
    color_array[4:,8] = colors[2]
    color_array[2:,9] = colors[2]
    color_array[2:,10] = colors[2]
    color_array[6:,11] = colors[2]
    color_array[8:,12] = colors[2]
    color_array[3:,13] = colors[2]
    color_array[3:,14] = colors[2]
    color_array[1:,15] = colors[2]
    color_array[1:,16] = colors[2]
    color_array[2:,17] = colors[2]
    '''

    # 2023
    
    color_array[8:,0] = colors[0] # wedge starts at noon and runs anticlockwise
    color_array[7:,1] = colors[0]
    color_array[7:,2] = colors[0]
    color_array[8:,3] = colors[0]
    color_array[5:,4] = colors[0]
    color_array[5:,5] = colors[0]
    color_array[4:,6] = colors[0]
    color_array[4:,7] = colors[0]
    color_array[8:,8] = colors[0]
    color_array[8:,9] = colors[0]
    color_array[3:,10] = colors[0]
    color_array[3:,11] = colors[0]
    color_array[2:,12] = colors[0]
    color_array[2:,13] = colors[0]
    color_array[1:,14] = colors[0]
    color_array[1:,15] = colors[0]
    color_array[7:,16] = colors[0]
    color_array[7:,17] = colors[0]

#------------------------------------------------------------------------------
# PLOT: planetary boundaries chart
#------------------------------------------------------------------------------

cm = 1 / 2.54
fig, ax = plt.subplots(figsize=(5*cm,9*cm))   

for i in range( len(color_array )):
    ax.pie(val_array[i,:], startangle=90, radius=1+size*i, colors=color_array[i,:], wedgeprops=dict(width=size, edgecolor='w'))    
ax.set(aspect="equal")
plt.savefig('planetary-boundaries-2023.png', dpi=600, bbox_inches='tight')

#------------------------------------------------------------------------------
# PLOT: "blank" planetary boundaries chart
#------------------------------------------------------------------------------

colors0 = np.tile(colors[2], 18 )
color_array_blank = np.vstack( [ colors0, colors0, colors0, colors0, colors0, colors0, colors0, colors0, colors0 ] )

fig, ax = plt.subplots(figsize=(3*cm,3*cm))   
for i in range( len(color_array )):
    ax.pie(val_array[i,:], startangle=90, radius=1+size*i, colors=color_array_blank[i,:], wedgeprops=dict(width=size, edgecolor='k'))    
ax.set(aspect="equal")
plt.savefig('planetary-boundaries-blank.png', dpi=600, bbox_inches='tight')

#------------------------------------------------------------------------------
print('** END')


