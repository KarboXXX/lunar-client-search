import os
print("starting installation... if you already installed it before, it will probably overwrite your changes.")
pth = os.path.dirname(os.path.abspath(__file__))
fpth = '/usr/share/lunarclient'

try: os.chdir(fpth)
except:
	os.mkdir(fpth)
	os.chdir(fpth)

print('placing {0} into {1}...'.format(pth + "/LunarClient.AppImage", fpth))
os.system('cp {0} {1}'.format(pth + "/LunarClient.AppImage", fpth))

print('placing {0} into {1}...'.format(pth + "/lunar-client.png", fpth))
os.system('cp {0} {1}'.format(pth + "/lunar-client.png", fpth))

print('opening /usr/share/applications to insert LunarClient.desktop into it.')
os.chdir('/usr/share/applications')
with open('LunarClient.desktop', 'w') as f:
	f.write("""[Desktop Entry]
Type=Application
Name=Lunar Client
Comment=A non official Minecraft Launcher.
Exec=/usr/share/lunarclient/LunarClient.AppImage
Icon=/usr/share/lunarclient/lunar-client.png
Terminal=false
Categories=Game;Application;
Keywords=minecraft;lunar;client;mine
""")