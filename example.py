# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:21:22 2019

@author: BIEL
"""

import mvnx

#First, create an MVNX class, that will open the mvnx file 
xsense=mvnx.MVNX('Experiment#Sonia.mvnx')
                 
                 
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

position_info=xsense.get_info('position') #list of position info for each frame
             

data=position_info[23]['pelvis'] 
#variable data contains the position of the origin of the pelvis segment at frame 23

print(data)

# Data may be presented diferently depending of what information you extract
# For example: position gives a dictionary with 23 labels, each one containing
# a 1x3 list (corresponding to a xyz point). In the other hand, sensor orientations
# gives a dictionary with 17 labels (different ones), each one containing a 1x4 list.

# For more information, I recommend checking pages 95-96 in MVNX manual