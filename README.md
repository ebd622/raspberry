# Raspberry PI
## Short Introduction
- [What is a Raspberry Pi?](https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/)
- [Raspberry Pi Boards](https://www.raspberrypi.org/products/)
- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)



## Grove Base Hat for Raspberry Pi Zero
http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi_Zero/

## Install Raspbian OS
1. Download the Raspbian-[Image](https://downloads.raspberrypi.org/raspbian_full_latest) "With Desktop and recommended software based on Debian Buster".
<br/>(Other images can be found [here](https://www.raspberrypi.org/downloads/raspbian/))

2. Get the image on the SD Card using a formating tool like [Etcher](https://www.balena.io/etcher/)

3. Copy two config files to SD  Card, to the root folder:
* [ssh](config/ssh) (empty file)
* [wpa_supplicant.conf](config/wpa_supplicant.conf)

4. Edit *wpa_supplicant.conf* to specify wifi-network and password

5. Put the SD Card into Raspberry Pi

6. Power on Raspberry Pi

Here is the video instruction [How to Setup Raspberry Pi Zero](https://www.youtube.com/watch?v=3VO4vGlQ1pg&t=178s)

## SSH to Raspberry Pi
First try to ping Raspberry to make sure that it is up and running:
```bash
ping raspberrypi.local
```

Than try ssh:
```bash
ssh pi@raspberrypi.local
```
The default password is *raspberry*


## Set up remote Desktop (optional)
```bash
sudo apt-get install tightvncserver
sudo apt-get install xrdp
```

## Install packages

Updated installed packages:
```bash
sudo apt-get update

```
Install [gpiozero](https://gpiozero.readthedocs.io/en/stable/) library (if not installed yet)

```bash
sudo apt install python3-gpiozero
```

Install/update all dependencies and latest [grove.py](https://pypi.org/project/grove.py/):

```bash
curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
```
It make take some time (~15-20 min) to install/update all packages. At the end, when everything is successfully installed the follwing message should be printed:
```bash
Successfully installed grove.py-0.6
#######################################################
  Lastest Grove.py from github install complete   !!!!!
#######################################################
```




