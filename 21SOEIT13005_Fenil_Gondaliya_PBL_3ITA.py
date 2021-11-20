import os,shutil,datetime,time

path = "D:/_chk"
list = os.listdir(path)

for file_name in list:
    created = os.path.getctime(path+'/'+file_name)
    year,month,day,hour,minute,second = time.localtime(created)[:6]
    name,ext=os.path.splitext(file_name)

    if ext == '':
        continue
    
    if os.path.exists(path+'/'+str(year)+'/'+str(month)+"/"+str(day)+'/'+ext):
        shutil.move(path+'/'+file_name,path+'/'+str(year)+'/'+str(month)+"/"+str(day)+'/'+ext+'/'+file_name)
    else:    
        os.makedirs(path+'/'+str(year)+'/'+str(month)+"/"+str(day)+'/'+ext)
        shutil.move(path+'/'+file_name,path+'/'+str(year)+'/'+str(month)+"/"+str(day)+'/'+ext+'/'+file_name)