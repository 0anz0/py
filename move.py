import os
import shutil

os.chdir('.\\test')
dst = r'C:\Users\test\Desktop\python\test'
#source = r'.\from_folder'

#a
#files = os.listdir(source)

for i in range(5):
    number = str(i+1).zfill(6)
    os.makedirs('0000_0000_0000_'+str(number),exist_ok=True)
    folders = os.listdir(dst)
    print(folders[i])
    print('フォルダ作成')

    #new_path = shutil.move(f"{source}/0000_0000_0000_"+str(number)+".dkkey", folders)
    #print(new_path)
    





