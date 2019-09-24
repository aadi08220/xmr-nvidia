import os

t='sudo apt-get update -y'
tt='sudo apt-get install -y tightvncserver'
ttt='sudo apt-get install -y aptitude tasksel'

tttt="sudo tasksel install gnome-desktop --new-install"

ttttt='sudo apt-get install -y xfce4 xfce4-goodies'

p='sudo dd if=/dev/zero of=/swapfile bs=1M count=1548'

pp='sudo chmod 600 /swapfile'
ppp='sudo mkswap /swapfile'
d='sudo swapon /swapfile'
de='sudo su'
dd='sudo echo "/swapfile none swap defaults 0 0" >> /etc/fstab'

c='sudo apt install -y chromium-browser'
cc='sudo apt install -y firefox'

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
os.system('exit')
os.system(c)
os.system(cc)
os.system('vncserver -geometry 1440x900')
