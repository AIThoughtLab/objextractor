#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:34:10 2022

@author: Mohamed ABDUL GAFOOR
"""



"""
This file takes the input obj file and flip the normal values. 
"""

import os

cwd = os.getcwd()

file_obj= cwd + "/mergedObj/whole.obj"
file_obj_normalFlip = open(cwd + "/mergedObj/whole_flip_normal.obj", 'w')

def flip_normal(file_obj):

    with open(file_obj) as f:
        content = f.read()
        
        
        for line in content.split('\n'):
            if line.startswith('vn'):
                
                # create a list and revesere the sign
                a, b, c = line.split(" ")[1:4]
                #print(a, b, c)
                aa, bb, cc = [-i for i in [float(a), float(b), float(c)]]
                #print(aa, bb, cc)
                file_obj_normalFlip.write("vn {0} {1} {2}\n".format(aa, bb, cc))
                
            # if line.startswith('f'):
            #     a, b, c = line.split(" ")[1:4]
            #     m1, n1 = a.split('//')
            #     m2, n2 = b.split('//')
            #     m3, n3 = c.split('//')
                
            #     if m1==n1 and m2==n2 and m3==n3:
            #         file_obj_normalFlip.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(m3, m2, m1))
            #     else:
            #         print("found non matching faces..")
                
            else:
                file_obj_normalFlip.write(f"{line}\n")
    