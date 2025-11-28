#!/data/data/com.termux/files/usr/bin/bash
echo "[+] Installing Yanz 404 Mobile Edition..."

# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install python -y
pkg install git -y
pkg install wget -y

# Install python packages
pip install requests --upgrade

# Download Yanz 404
wget https://raw.githubusercontent.com/yanz404/yanz404-mobile/main/yanz404_mobile.py -O yanz404.py

# Make executable
chmod +x yanz404.py

echo "[+] Installation complete!"
echo "[+] Run: python yanz404.py"
