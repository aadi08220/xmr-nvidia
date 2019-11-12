import os

tt= 'sudo apt upgrade -y'

p= 'sudo apt-get install -y tightvncserver'

pp= 'sudo apt-get install -y aptitude tasksel'

ppp= 'sudo tasksel install gnome-desktop --new-install'

a= 'sudo apt-get install -y xfce4 xfce4-goodies'

aa= 'sudo apt install -y chromium-browser'

aaa= 'sudo apt install google-chrome-stable'

dd= 'wget https://download3.operacdn.com/pub/opera/desktop/64.0.3417.92/linux/opera-stable_64.0.3417.92_amd64.deb'
ddd='sudo dpkg -i opera*'
f='sudo apt install -y google-chrome-stable'


os.system(tt)
os.system(p)
os.system(pp)
os.system(ppp)
os.system(a)
os.system(aa)
os.system(aaa)
os.system(dd)
os.system(ddd)
os.system(f)


