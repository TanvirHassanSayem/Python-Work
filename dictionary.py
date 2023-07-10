
thisdict = {}


thisdict['brand']=  {
       'name': 'Buggatti',
       'Price': 10000000000000000
}

thisdict['brand2']=  {
       'name': 'Austin Martin',
       'Price': 10000000000  
}



import json

s=json.dumps(thisdict)

print(s)

            # with open ("D:\Python Work\work1,txt","w") as f:
    
             #  f.write(s)
    
with open ("D:\Python Work\work1,txt","r") as f:
    
    a1= f.read()
 
    print(a1) 