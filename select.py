import os, requests
version_on_pc=open('version.txt', 'r')
version=version_on_pc.read()
version_on_pc.close()
github_version=requests.get('https://raw.githubusercontent.com/Timtaran/Bombers/master/version.txt').text
if github_version != version:
  print(f'Please update "Bombers"\nYour version - {version}, GitHub version - {github_version}')
bomber=input("Select bomber\n0-b0mb3r by Denishnc|Don't working\n1-Impulse by LimerBoy\n2-Spammer by Cludeex\n3 Duplo-bomber by Batiscuff \n sh start_bomber.sh ")
os.system('clear')
bomber=int(bomber[0])
bomders=['sh b0mb3r.sh', 'sh Impulse.sh', 'python3 spammer.py', 'sh duplo-bomber.sh']
bomders_enter=['', 'Impulse.sh --target [number]', '', '']
if bomders_enter[bomber] != '':
  input(f"Number Selecting - {bomders_enter[bomber]}\n Press Enter To Continue...")
os.system(bomders[bomber])