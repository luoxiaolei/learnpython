#! python3

import requests,re,logging,os,sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start download png...')

#os.chdir(os.path.join('C:','Users','luo','Desktop'))
os.chdir(r'C:\Users\luo\Desktop')

logging.debug(os.getcwd())

sourceUrl = 'https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7'

pngUrlRegex = re.compile(r'https://.*\.PNG')

updateDateRegex = re.compile(r'\d{4}年\d{1,2}月\d{1,2}日')

response = requests.get(sourceUrl)

response.raise_for_status()

htmlSource = response.text

pngUrl = pngUrlRegex.search(htmlSource).group()

updateDate = updateDateRegex.search(htmlSource).group()

logging.debug('pngUrl:'+pngUrl+'\n'+'updateDate:'+updateDate)

pngResponse = requests.get(pngUrl)

for filename in os.listdir():
    if filename.endswith('.png') and filename == updateDate+'.png':
        logging.debug(filename)
        logging.debug('png existed')
        sys.exit()
    #else:
        #os.unlink(filename)
        #sys.exit()

file = open(updateDate+'.png','wb')


for chunk in pngResponse.iter_content(1024*5):#byte
    file.write(chunk)

file.close()

logging.debug('download completed...')
