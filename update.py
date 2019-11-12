import os
t= 'apt update' 
tt= 'apt upgrade -y'
ttt= 'apt install -y snapd'
p= 'apt-get install -y tightvncserver'
pp= 'apt-get install -y aptitude tasksel'
ppp= 'tasksel install gnome-desktop --new-install'
a= 'apt-get install -y xfce4 xfce4-goodies'
aa= 'apt install -y chromium-browser'
aaa= 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
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


