import os, os.path
import shutil
import re

file_names=[]
sfc = 0

test_all_data=''

for folder,sub_folders,files in os.walk(os.getcwd()):
    
    for sub_folder in sub_folders:
        sfc+=1
        
    for f in files:
        pass
        

loop_counter=0
number_counter=0
number_convert = ['One','Two','Three','Four','Five']

while loop_counter<5:
    for f_name in os.listdir(number_convert[number_counter]):
        if f_name.endswith('.txt'):
            print(f_name)
            with open(f'{number_convert[number_counter]}/{f_name}','r') as test_open_file:
                testline = test_open_file.readlines()  
                test_all_data=''.join(str(b) for b in testline)
                file_names+=[f]
                phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})') #This patterns searches for groups of digits
                results = re.search(phone_pattern,test_all_data)
                print(results)
     
    if results == None:
        #print('Phone number not Found')
        number_counter+=1 
        loop_counter+=1
        #print(loop_counter)
        print(number_counter)
    
              
        




