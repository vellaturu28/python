import os
import time

curDir= os.getcwd()
print(curDir)

os.mkdir('Test')
os.rename('Test','Rename')
time.sleep(2)

os.rmdir('Rename')
