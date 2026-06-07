# TB-Browser
The TB-browser is an Open Source Project that aims to make a daily drivable simple browser based on Chromium

This is only a V1 and the core functions are stable on Linux as currently its only available on linux because i havent ported it over to windows yet due to not having a windows PC or Dual boot

The Browser ist currently still simple only having the core functions:

URL Searchbar
Forward and Backwards
Refresh the Page
Working Tab system with automatically changing names to the website youre on

Also the base Browser is Duck Duck Go if youd like to change this you have to go into the TB_Broser.py file and change in the section of the start tab the URL to the desired start website

Also you can cgange your profile wich i after installation set to Default profile if you want to change that its also in the TB-Browser.py file

Another thing is that your going to have to change your path to the files as its currently only using set Pathways wich you will have to change in the TB_Browser.py file

Dependencies for the Project just run these in the console of most linux distros this project was made in Linux Mint Cinnamon and it works on here so here are the Dependencies just run them in the Terminal

sudo apt install qt6-webengine

It installs the actual engine based on chromium

sudo apt install PySide

Installs the python part thats used for the Browser
