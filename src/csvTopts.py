# Run this file separate from ArcGIS window

import os,sys
folder = 'C:/Users/User1/Desktop/'
filename = 'coordinates'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.csv', '.pts')
       output = os.rename(infilename, newname)
