import os
t= 'sudo apt update' 
tt= 'sudo apt upgrade -y'
ttt= 'sudo apt install -y snapd'
p= 'sudo apt-get install -y tightvncserver'
pp= 'sudo apt-get install -y aptitude tasksel'
ppp= 'sudo tasksel install gnome-desktop --new-install'
a= 'sudo apt-get install -y xfce4 xfce4-goodies'
aa= 'sudo apt install -y chromium-browser'
aaa= 'sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
d= 'sudo dpkg -i google-chrome-stable_current_amd64.deb'
dd= 'snap install opera'
os.system(t)
os.system(tt)
os.system(ttt)
os.system(p)
os.system(pp)
os.system(ppp)
os.system(a)
os.system(aa)
os.system(aaa)
os.system(d)
os.system(dd)


