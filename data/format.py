import os
path1='images'
path2='labels'

for i in os.listdir(path1):
    count_old=int(i.split(".")[0])
    houzhui=i.split('.')[1]
    count_old='{:06d}'.format(count_old)
    old_path=os.path.join(path1,i)
    new_path=os.path.join(path1,str(count_old)+'.'+houzhui)
    os.rename(old_path,new_path)
    m=1
    