Following is a protocol that has been developed in order to convert **DIF** file format into a Unity
friendly **.obj** file so that it can be easily inserted into the Unity environment.

For more details on the structure of the **.xml** file; Please see the folder **xmlFiles**.


1. Put the **.xml** file in the xmlFiles directory. Then, if we run the **objCreator.py**, it will generate all **.obj** files for different regions.

2. Then run the **mergeAllOBJ.py**, it will help to combine all the **.obj** files in an appropriate order to create a whole structure. It will also generate a flip normal **.obj**. 
   This might be useful in some situations. But not necessary if you use the Unity URP (Universal Render Pipeline).
   
  
Make sure minidom is install.
PS: pip install minidom-ext
