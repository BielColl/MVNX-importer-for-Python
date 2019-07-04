# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:21:22 2019

@author: BIEL
"""

import mvnx

#First, create an MVNX class, that will open the mvnx file 
data=mvnx.MVNX('example.mvnx')
                 
                 
#-------------------------------------------------------
#The class has different attributes: 
#                 - xml_file gives you the full xml fil as an untangle element
#                 - mvn_version and mvn_build are info of the MVN software 
#                 - available_info gives you a list of all the parameters that you have exported 
#                   (position, orientation,...)
#                 - all_index is an object that gives you the labels for the data,
#                   depending if the data is from sensors, joints, segments or others;
#                 - total_frames returns the number of frames captured by xsense,
#                 - subject is a dictionary with the capture information
#                 - frames is the most important one. It's a list of untangle elements
#                   each one containg all info (position, orientation) of a frame
#--------------------------------------------------------

position_info=data.get_info('position') #list of position info for each frame
             

pelvis=position_info[23]['pelvis'] 
#variable data contains the position of the origin of the pelvis segment at frame 23

print('Position of the pelvis at frame 23: ', pelvis)

# Data may be presented diferently depending of what information you extract
# For example: position gives a dictionary with 23 labels, each one containing
# a 1x3 list (corresponding to a xyz point). In the other hand, sensor orientations
# gives a dictionary with 17 labels (different ones), each one containing a 1x4 list.

# For more information, I recommend checking pages 95-96 in MVNX manual

# Using the MVNX library we can also plot data

mvnx.plotData(position_info, 'right_hand')

# For synchronization purposes, the MVNX library also contains a function to 
# detect claps by finding high peaks in the acceleration of the right hand

acceleration= data.get_info('acceleration')
res=mvnx.findClaps(acceleration, 'right_hand', n_claps=3, dataRange=[0,500])
print('Claps founded at frames ', res)
#mvnx.plotData(acceleration, 'right_hand')
