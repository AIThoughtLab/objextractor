#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:59:18 2022

@author: Mohamed ABDUL GAFOOR
"""


import os

#
cwd = os.getcwd()
# location of the OBJ files
root_dir = cwd + "/objFiles/"
#save directory
thefile= open(cwd + "/mergedObj/whole.obj", 'w')

class objMerger:
    def __init__(self, Objpath, savepath):
        self.Objpath = Objpath
        self.savepath = savepath
        
    
    def merge(self):
        self.arr = os.listdir(self.Objpath)
        #print(arr)

        self.dict_ = {}

        for index, part in enumerate(self.arr):
            with open(root_dir+f"/{part}") as f:
                
               
                content = f.read()
                
                thefile.write("# {0}\n".format(part))
                thefile.write("\n")
                
                if index == 0:
                    # counting of vertices, vertex normal and faces
                    countvertex = 0
                    countvertexnormal = 0
                    countfaces = 0
                    for i in content.split('\n'):
                        if not i.startswith('vn') and i.startswith('v'):
                            countvertex = countvertex + 1
                            a, b, c = i.split(" ")[1:4]
                            thefile.write("v {0} {1} {2}\n".format(a, b, c))
                            
                            #thefile.write("Number of vertices are: {0}\n".format(countvertex))
                    
                        if i.startswith('vn'):       
                            countvertexnormal = countvertexnormal + 1
                            a, b, c = i.split(" ")[1:4]
                            #print(i.split(" ")[1:4])
                            thefile.write("vn {0} {1} {2}\n".format(a, b, c))
                    thefile.write("g {}\n".format(part))
                    thefile.write("s {}\n".format(index+1))
                           
                    for i in content.split('\n'):
                        if i.startswith('f'):
                            countfaces = countfaces + 1
                            a, b, c = i.split(" ")[1:4]
                            m1, n1 = a.split('//')
                            m2, n2 = b.split('//')
                            m3, n3 = c.split('//')
                            
                            if m1==n1 and m2==n2 and m3==n3:
                                thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(m1, m2, m3))
                            else:
                                print("found non matching faces..")
                                
                    self.dict_.update({f'{part}': [countvertex, countvertexnormal, countfaces]})
                
                if index != 0:
                    # counting of vertices, vertex normal and faces
                    countvertex = 0
                    countvertexnormal = 0
                    countfaces = 0
                    
                    for i in content.split('\n'):
                        if not i.startswith('vn') and i.startswith('v'):
                            countvertex = countvertex + 1
                            a, b, c = i.split(" ")[1:4]
                            thefile.write("v {0} {1} {2}\n".format(a, b, c))
                            
                            #thefile.write("Number of vertices are: {0}\n".format(countvertex))
                    
                        if i.startswith('vn'):       
                            countvertexnormal = countvertexnormal + 1
                            a, b, c = i.split(" ")[1:4]
                            #print(i.split(" ")[1:4])
                            thefile.write("vn {0} {1} {2}\n".format(a, b, c))
                    thefile.write("g {}\n".format(part))
                    thefile.write("s {}\n".format(index+1))
                           
                    for i in content.split('\n'):
                        if i.startswith('f'):
                            countfaces = countfaces + 1
                            a, b, c = i.split(" ")[1:4]
                            m1, n1 = a.split('//')
                            m2, n2 = b.split('//')
                            m3, n3 = c.split('//')
                            
                            if m1==n1 and m2==n2 and m3==n3:
                                
                                ## add countvertex from 1st obj
                                ## add countvertex from 1st obj and 2nd obj
                                ## add countvertex from 1st obj and 2nd obj and 3rd obj etc
                                total = 0
                                total_ = sum(k[0]+total for k in self.dict_.values())
                                #thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(int(m1)+dict_[arr[index-1]][0], int(m2)+dict_[arr[index-1]][0], int(m3)+dict_[arr[index-1]][0]))
                                thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(int(m1)+total_, int(m2)+total_, int(m3)+total_))

                            else:
                                print("found non matching faces..")
                    self.dict_.update({f'{part}': [countvertex, countvertexnormal, countfaces]})  
    
    
    
    
    
    
objMerger(root_dir, thefile).merge()   
# import os
# cwd = os.getcwd()
# print(cwd+"/objFiles/")
    
    
