import os

t='sudo apt-get update'
tt='sudo apt-get install tightvncserver'
ttt='sudo apt-get install aptitude tasksel'

tttt="sudo tasksel install gnome-desktop --new-install"

ttttt='sudo apt-get install xfce4 xfce4-goodies'

p='sudo dd if=/dev/zero of=/swapfile bs=1M count=2048'

pp='sudo chmod 600 /swapfile'
ppp='sudo mkswap /swapfile'
d='sudo swapon /swapfile'
de='sudo su'
dd='sudo echo "/swapfile none swap defaults 0 0" >> /etc/fstab && exit'

c='sudo apt install chromium-browser'
cc='sudo apt install firefox'

os.system(t)
os.system(tt)
os.system(ttt)
os.system(tttt)
os.system(ttttt)

os.system(p)
os.system(pp)
os.system(ppp)
os.system(d)
os.system(de)
os.system(dd)
os.system(c)
os.system(cc)
os.system('cd')
os.system('sudo rm -rf *')
os.system('vncserver')
