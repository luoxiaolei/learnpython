#! /usr/bin/env python3
import requests,re,logging,os,sys,shutil

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start clearing dir...')
# 从命令行获取要清理的目录
logging.debug(len(sys.argv))
targetDir = ''

if len(sys.argv) < 2 : 
    print('请输入要真整理的文件路径...')
    targetDir = input()
else :
    targetDir = sys.argv[1]

print('你要整理的目录是：'+targetDir)

extensionTypeList = []
# 遍历该目录下的所有文件，记录文件后缀名

for folderName, subfolders, filenames in os.walk(targetDir):
    #print('当前目录是：' + folderName)

    for subfolder in subfolders:
        print('子目录是：' + subfolder)
    for filename in filenames:
        #print('子目录' + subfolder + '的文件' + filename)
        if '.' in filename:
            if filename.split('.')[1] not in extensionTypeList:
                extensionTypeList.append(filename.split('.')[1])

print(extensionTypeList)

# 在目录中创建后缀名的文件夹
for extension in extensionTypeList:
    if not os.path.exists(os.path.sep+'Users'+os.path.sep+'luoxiaolei'+os.path.sep+'test'+os.path.sep+extension+'dir'):
        os.makedirs(os.path.sep+'Users'+os.path.sep+'luoxiaolei'+os.path.sep+'test'+os.path.sep+extension+'dir')



# 将文件移动到命名为后缀名的文件夹中
