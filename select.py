import os
bomber=input("Select bomber\n0-b0mb3r by Denishnc|Don't working\n1-Impulse by LimerBoy\n2-Spammer by cludeex\n sh start_bomber.sh ")
os.system('clear')
bomber=int(bomber[0])
bomders=['sh b0mb3r.sh', 'sh Impulse.sh', 'python3 spammer.py']
bomders_enter=['', 'Impulse.sh --target [number]', '']
if bomders_enter[bomber] != '':
  input(f"Number Selecting - {bomders_enter[bomber]}\n Press Enter To Continue...")
os.system(bomders[bomber])