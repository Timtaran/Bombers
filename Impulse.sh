alias wait="python3 wait.py"
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/LimerBoy/Impulse
pip3 install -r Impulse/requirements.txt
clear
echo "Starting Impulse..."
clear
python3 Impulse/impulse.py --method SMS --time 10000 --threads 15 --target