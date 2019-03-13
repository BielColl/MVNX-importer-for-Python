# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:21:03 2019

@author: BIEL
"""
import untangle

def get_default_segment_index():
    index=['pelvis','l5','l3','t12','t8','neck','head','right_shoulder',
           'right_upper_arm','right_forearm','right_hand','left_shoulder',
           'left_upper_arm','left_forearm','left_hand','right_upper_leg',
           'right_lower_leg','right_foot','right_toe','left_upper_leg',
           'left_lower_leg','left_foot','left_toe']
    return index
def get_default_sensor_index():
    index=['pelvis','t8','head','right_shoulder','right_upper_arm','right_fore_arm',
           'right_hand','left_shoulder','left_upper_arm','left_fore_arm', 'left_hand',
           'right_upper_leg','right_lower_leg','right_foot',
           'left_upper_leg','left_lower_leg','left_foot']
    return index
def get_default_joint_index():
    index=['L5S1','L4L3','L1T12','T9T8','T1C7','C1Head','RightC7Shoulder',
           'RightShoulder','RightElbow','RightWrist','LeftC7Shoulder',
           'LeftShoulder','LeftElbow','LeftWrist', 'RightHip','RightKnee',
           'RightAnkle','RightBallFoot','LeftHip','LeftKnee','LeftAnkle',
           'LeftBallFoot']
    index=list(map(lambda x:x+'j',index))
    return index
def get_dictionary_from_class(obj):
    ll_atrib=dir(obj)
    d={}
    for attribute in ll_atrib:
        d[attribute]=getattr(obj,attribute)
    return d

def prepareline(line, tag, index, scaled):
    linep=line.split(' ')
    # Only the information of sensor, segments or joints pass through this function
    #First two lines: segments, 3rd line: sensors, 
    how_many_info={'position':3, 'orientation':4, 'velocity':3, 'acceleration': 3,
                   'angularVelocity': 3, 'angularAcceleration':3, 
                   'sensorMagneticField':3,'sensorOrientation': 4, 'sensorFreeAcceleration':3, 
                   'jointAngle':3, 'jointAngleXZY':3,'jointAngleErgo':3,
                   'centerOfMass':3, 'footContacts':1}
                    
    linep=list(map(lambda x: scaled*float(x), linep)) #pass to float
    if tag in how_many_info:
        n=how_many_info[tag]
    else:
        s='No tag <'+tag+'> in how_many_info'
        raise ValueError (s)
        
    linep=[linep[x:x+n] for x in range(0, len(linep),n)]
    if len(linep)!=len(index):
        print(linep)
        s='Error using '+tag
        raise ValueError (s)
    coord={}
    for i in range(len(index)):coord[index[i]]=linep[i]
    return coord
class MVNX_Index():
    def __init__(self, info):
        self.segment_index=get_default_segment_index()
        self.sensor_index=get_default_sensor_index()
        self.joint_index=get_default_joint_index()
        self.footContacts_index=['LeftFoot_Heel', 'LeftFoot_Toe','RightFoot_Heel', 'RightFoot_Toe']
        self.mass_index=['Center_Of_Mass']
        self.ergo_index=['jnt1','jnt2','jnt3','jnt4']
        self.info=info
    def __getitem__(self, tag):
        if tag in self.info:
            if tag in ['position','orientation','velocity','acceleration',
                   'angularVelocity', 'angularAcceleration']:
                return self.segment_index
            elif tag in ['sensorMagneticField','sensorOrientation','sensorFreeAcceleration']:
                return self.sensor_index
            elif tag in ['jointAngle', 'jointAngleXZY']:
                return self.joint_index
            elif tag=='jointAngleErgo':
                return self.ergo_index
            elif tag=='footContacts':
                return self.footContacts_index
            elif tag=='centerOfMass':
                return self.mass_index
            else:
                return None
class MVNX():
    def __init__(self,mvnx_root):
        self.xml_file=untangle.parse(mvnx_root)
        self.frames=self.xml_file.mvnx.subject.frames.frame
        self.frames=self.frames[3:]
        self.total_frames=len(self.frames)
        self.available_info=[i for i in get_dictionary_from_class(self.frames[3])]
        self.all_index=MVNX_Index(self.available_info)
        
        self.mvn_version=self.xml_file.mvnx.mvn['version']
        self.mvn_build=self.xml_file.mvnx.mvn['build']
        self.subject=self.xml_file.mvnx.subject._attributes

    def get_info(self,tag, scaled=1):
        if tag not in self.available_info:
            raise ValueError ('Not available info in MVNX')
        else:
            ll=[]
            for i in range(self.total_frames):
                s=getattr(self.frames[i],tag)
                s=getattr(s,'cdata')
                d=prepareline(s,tag, self.all_index[tag], scaled)
                ll.append(d)
        return ll
        