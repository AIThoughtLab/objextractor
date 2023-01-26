#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  11 12:35:39 2022

@author: Mohamed ABDUL GAFOOR
"""

import xml_obj_file
from mergeAllOBJ import objMerger
import Normals
import os

class modelExtractor:
    def __init__(self, part, whole, normal, path_to_xml, save_path_obj):
        self.part = part
        self.whole = whole
        self.path_to_xml = path_to_xml
        self.save_path_obj = save_path_obj
        self.normal = normal
        
        
    def extract(self):
        self.list_parts = ["Left Atrium", "Left Ventricle", "Right Atrium", "Right Ventricle", "Aorta", "Pulmonary Artery"]
        
        self.vList = []
        self.nList = []
        self.pList = []
        
        for i in self.list_parts:
            self.v, self.n, self.p = xml_obj_file.VolumeExtraction(i, self.path_to_xml).region()
            
            """ append each v list from Left Atrium", "Left Ventricle", "Right Atrium", "Right Ventricle", "Aorta", "Pulmonary Artery
            to vList.. similarly do it for n and p
            """
            self.vList.extend(self.v)
            self.nList.extend(self.n)
            self.pList.extend(self.p)
            
            if self.part:
                
                file = open(f'{self.save_path_obj}/{i}.obj', 'w')
                for item in self.v:
                  file.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))
    
                for item in self.n:
                  file.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))
    
                for item in self.p:
                  file.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2])) 
                  
    
                file.close()
                print(".obj parts have been generated!")
   
        if self.whole:
            cwd = os.getcwd()
            # location of the OBJ files
            root_dir = cwd + "/objFiles/"
            #save directory
            thefile= open(cwd + "/mergedObj/whole.obj", 'w')
            
            objMerger(root_dir, thefile).merge() 

        if self.normal:
            file_obj= os.getcwd() + "/mergedObj/whole.obj"
            Normals.flip_normal(file_obj)
            

cwd = os.getcwd()
savePath = cwd +"/objFiles"
xmlPath = cwd + "/xmlFiles/DIF_20220727_121151_0001.xml"

modelExtractor(True, True, True, xmlPath, savePath).extract()


