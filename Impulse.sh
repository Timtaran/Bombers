alias wait="python3 wait.py"
apt update
clear
pip3 install -r Impulse/requirements.txt
clear
echo "Starting Impulse..."
wait
clear
python3 Impulse/impulse.py --method SMS --time 10000 --threads 15 --target