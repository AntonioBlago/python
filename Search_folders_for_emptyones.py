# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:26:15 2018

@author: AB_Admin
"""


'''
    For the given path, get the List of all files in the directory tree 
'''
def search_folder_for_emptyones(dirName):
        #self.dirName=dirName
    listOfFiles=[]
    listOfFiles = getListOfFiles(dirName)
    resultFile=csvwriter(listOfFiles,dirName)
    return  resultFile
        
    #def search_folder(self, dirName):
        


def getListOfFiles(dirName):
    import os
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    
    allFiles = list()
    
    for entry in listOfFile:
        
        fullPath = os.path.join(dirName, entry)
        
        if os.path.exists(fullPath) and os.path.isdir(fullPath):
            
            if not os.listdir(fullPath):
                if fullPath.find('_empty',0)==-1:
                    os.rename(fullPath, (fullPath+'_empty'))
                    allFiles.append([str(fullPath+'_empty')])
                    #print (allFiles)
                
                else:
                    allFiles.append([fullPath])
                #print("Directory is empty")
            elif os.listdir(fullPath):
                allFiles=allFiles+getListOfFiles(fullPath)
                
            else:
                pass
    return allFiles
    
def csvwriter(listOfFiles,dirName):
    import csv
    import datetime
    
    now = datetime.datetime.now()
    Date=now.strftime("%Y-%m-%d")
    
    CSV_name=str(dirName+'\\' +Date+'_emtpy_Folder_search'+'.csv')
    
    with open(CSV_name, 'w') as resultFile:
     wr = csv.writer(resultFile,delimiter=',')
     wr.writerows(listOfFiles)

    return resultFile

