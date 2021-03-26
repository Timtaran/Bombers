import os
bomber=input("Select bomber\n0-b0mb3r|Don't working\n1-Impulse\n/start_bomber ")
os.system('clear')
bomber=int(bomber[0])
bomders=['sh b0mb3r.sh', 'sh Impulse.sh']
os.system(bomders[bomber])