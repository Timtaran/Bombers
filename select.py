import os
bomber=input("Select bomber\n0-b0mb3r by Denishnc|Don't working\n1-Impulse by LimerBoy\n/start_bomber ")
os.system('clear')
bomber=int(bomber[0])
bomders=['sh b0mb3r.sh', 'sh Impulse.sh']
bomders_enter=['None', 'Impulse.sh --target [number]']
input(f"Number Selecting - {bomders_enter[bomber]}\n Press Enter To Continue...")
os.system(bomders[bomber])