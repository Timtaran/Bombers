alias wait="python3 wait.py"
apt update
clear
pip3 install -r Impulse/requirements.txt
clear
echo "Starting Impulse..."
clear
python3 Impulse/impulse.py --method SMS --time 10000 --threads 60 --target