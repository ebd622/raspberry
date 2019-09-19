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

3. Copy two config files to SD Card, to the root folder:
* File1
* File2

4. Put the SD Card into Raspberry Pi

5. Power on Raspberry Pi

Here is the video instruction [How to Setup Raspberry Pi Zero](https://www.youtube.com/watch?v=3VO4vGlQ1pg&t=178s)

## SSH to Raspberry Pi
TODO

## Set up remote Desktop
```bash
sudo apt-get install tightvncserver
sudo apt-get install xrdp
```
