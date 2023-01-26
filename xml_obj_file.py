#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 01:12:33 2022

@author: Mohamed ABDUL GAFOOR
"""


from xml.dom import minidom




dom = minidom.parse('/home/m/Downloads/DIF_20220727_121151_0001.xml')
elements = dom.getElementsByTagName('Volume')
       

class VolumeExtraction:
    
    def __init__(self, nameRegion, path_):
        self.nameRegion = nameRegion
        self.path_ = path_
        
        
    def region(self):
        self.dom = minidom.parse(self.path_)
        self.elements = dom.getElementsByTagName('Volume')
        #print(f"There are {len(elements)} items:")
        
        for element in elements:
            #print(element.attributes['name'].value)
            if element.attributes['name'].value == self.nameRegion:
                #print(f"we found a {self.nameRegion}")
                
                # split the string by \n
                self.list_vertices = element.getElementsByTagName('Vertices')[0].firstChild.nodeValue.strip().split('\n')
                self.list_normals = element.getElementsByTagName('Normals')[0].firstChild.nodeValue.strip().split('\n')
                self.list_polygons = element.getElementsByTagName('Polygons')[0].firstChild.nodeValue.strip().split('\n')
                
                # call the formatting method
                # self.formatList(self.list_vertices)
                # self.formatList(self.list_normals)
                # self.formatList(self.list_polygons)
                
                ## polygon info was in interger... so apply special procedure to it not to have float.
                
                
                return self.formatList(self.list_vertices), self.formatList(self.list_normals), [[int(j) for j in i] for i in self.formatList(self.list_polygons)]
                
    
    def formatList(self, list_name):
        self.new_list = []
        self.list_name = list_name
        
        for i in list_name:
            self.new_list.append(i.strip())
        
        self.new_new_list = []
        for i in self.new_list:
            self.new_new_list.append(i.split(' '))        
        
        self.new_new_new_list = []
        for i in self.new_new_list:
            self.list1 = [x for x in i if x]
            self.new_new_new_list.append(self.list1)     
        
        self.finallist = []
        for k in self.new_new_new_list:
            self.lis = list(map(float, k))
            self.finallist.append(self.lis)
        #print(self.finallist)
        return self.finallist
