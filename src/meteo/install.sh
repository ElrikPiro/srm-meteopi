chmod +x ./meteopi.py
mkdir ~/.meteopi
cp ./meteopi.py ~/.meteopi/run.py
chmod +x ~/.meteopi/run.py
echo "@reboot $HOME/.meteopi/run.py" > /tmp/meteo.txt
crontab /tmp/meteo.txt
crontab -l
