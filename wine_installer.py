import os
sudoPassword = ''#buraya şifrenizi yazın ## enter your password
command='wget http://archive.ubuntu.com/ubuntu/pool/main/libf/libffi/libffi6_3.2.1-4_amd64.deb'
os.system(command)
command='dpkg -i libffi6* '
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
command='dpkg --add-architecture i386'
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
command='wget -nc https://dl.winehq.org/wine-builds/winehq.key'
os.system(command)
command='apt-key add winehq.key'
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
f = open("sources.list", "w")
f.write("deb https://dl.winehq.org/wine-builds/debian/ buster main")
f.close()
command='cat sources.list /etc/apt/sources.list >> /etc/apt/sources.list'
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
command='apt update'
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
command='apt install --install-recommends winehq-stable'
os.system('echo %s|sudo -S %s' % (sudoPassword, command))
os.system('wine')
