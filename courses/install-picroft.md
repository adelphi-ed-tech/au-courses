% Intalling Picroft

<style>
.sourceCode { padding-top: 1em;padding-bottom: 1em;}
</style>

Installing and Configuring Mycroft
===================================


Please find these more detailed instructions on setting up and configuring
mycroft on your Raspberry Pi. To follow these instructions you will need
all of the equipment from the syllabus, including a card reader.

[See the full list here with links on where to get them.](https://mcuringa.github.io/adelphi-ed-tech-courses/intro-to-programming_python.html#required-hardware)

Step 0: Before you start
-------------------------

1. Gather all of the components you will need.
2. Create a mycroft account at <https://sso.mycroft.ai/new-account>, <small>you don't need a paid account</small>
3. Download and install Etcher on your computer (not the Pi): <https://www.balena.io/etcher/>
4. Download the Picroft OS "disk image", and save it to your computer (Downloads,
   Desktop, your CSC 602 folder, or anywhere else where you can find it easily).
   Disk image link: <https://mycroft.ai/to/picroft-image>. <small>don't worry about skipping the google security check.</small>

Step 1: Create a disk image
----------------------------
In this step we create a SD card that has a Operating System on it. This is
equivalent to (re)installing Windows or Mac OS, except it's actually a lot easier.
``Picroft_Buster-Keaton_2020-01-10.zip`` has a customized version of the linux
OS built for Raspberry Pi. This version comes with a wizard to set up Mycroft.

1. Insert an SD card into your card reader. If it's a removable reader,
   insert it into your computer.
2. Open the Etcher program that you downloaded.
3. Choose "flash from file" and choose the file ``Picroft_Buster-Keaton_2020-01-10.zip`` which you downloaded from Mycroft.
4. Select your SD card. It will probably be the only drive, but if you have
   other USB flash drives plugged in, you will have to select the right drive.
   You can tell that you have the right drive by the size (e.g. 16GB or 8GB).
5. Click "flash" and wait 4-10 minutes while the operating gets copied.

For more information, watch [this step-by-step video on creating a disk image with Etcher](https://www.youtube.com/watch?v=PijX8GDco-g).

Step 2: Boot the Raspberry Pi
-----------------------------
_We assume that you have a new Raspberry Pi Model 4._ If you have a Model 3,
we assume that you either know what you're doing or will reach out for help.

<img src="https://keytosmart.com/wp-content/uploads/2019/10/rpi-4-hardware-overview-1024x599.jpg" alt="rpi 4 schematic">

**Do not power on your Raspberry Pi until you have completed all of the other steps!**

1. Slide the SD card out of your card reader and insert it into the SD slot on your RPI.
2. Plug in your microphone, headphones/speakers, keyboard and mouse.
3. Connect your RPI to your monitor with the micro HDM cable. There are two
   HDMI out ports on your RPI. The small end of the cable plugs in here.
4. _ReSpeaker "Hat"._ If you are using the ReSpeaker 4-mic array recommended on
   the syllabus, you should line it up with the pins labeled,
   "40 pin General-purpose input/output Header" in the diagram above. Press the
   hat carefully but firmly until you can't see the pins anymore. The Hat will,
   basically, cover your RPI at this point. **Do not remove or add the ReSpeaker
   while your RPI is running.**
5. You are ready to boot the pi. Plug the USB-C cable into the RPI and then
   plug the other end into a power adapter. If at all possible, plug it into
   a higher powered adapter like an iPad charger, chromebook or macbook charger,
   or high-speed USB phone charger. Otherwise, you might not have enough power
   to run the RPI.

You should now see the small LED light near the USB-C port light up. Next,
you should see the RPI Boot Screen appear on your monitor.
[It will look something like this](https://raspberrycoulis.files.wordpress.com/2015/10/raspi2boot.jpg?w=1400).

After waiting a minute or so, if you don't see anything on your monitor/TV, you
should toggle through the "inputs" on your monitor to make sure it is configured
for the same HDMI port that your RPI is connected to.

_If you don't have a monitor and/or keyboard to use_, and are confident in your IT
skills, you can follow this guide to [ssh into mycroft](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft#ssh-into-picroft).

Step 3: Configure Mycroft
-------------------------

At this point you should see the Mycroft configuration wizard. To get started,
type `Y` and hit `enter` to start the wizard.

[Follow this guide from the mycroft documentation.](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft#setting-up-picroft)

Notes:

- you will need to know the _name_ of your wireless netowrk (SSID) as well as the password in order to connect to the internet. if you're not sure of the name, you can probably look at your phone or laptop to see the name of the network.
- for **audio output**, choose _headphones_ to use the headphone jack, _HDMI_ to use your monitor's speakers, or _USB_ to use USB speakers. If you're not sure, we're probably going to have to fix this later anyway.
- for **microphone**, choose option 5, _other_. Don't worry if you can't hear or record anything during the audio test at this point, just continue.
- to pair your device, even if you can't hear mycroft, you can read the pairing code on the console.
- log in here to add the device <https://home.mycroft.ai/devices/>. Follow the set-up wizard on the mycroft.ai website.

If you're not using ReSpeaker, there's a chance that your Mycroft is perfectly up and running at this point. Awesome. If not, keep reading...


Step 4: ReSpeaker Hat
---------------------
If you're using the mic array hat, there is one more step you have to take. If
you are using a different microphone, skip this step.

You can follow the detailed installation documentation here, or you can
follow these steps.

To get started, hit ``ctrl+c`` (control-c key combination) on your keyboard
in order to exit the Mycroft debugger.

Type these commands one at a time and then hit enter. Read the message that
appears on the console. If there's some kind of error message, you may
have mistyped the command. Do not enter the next command until the command
prompt is ready. You will see something like: ``(.venv) pi@picroft:~ $ _``
when it's ready for the next command.

_1. stop mycroft_

~~~~~~~~~~~~~~~~~~~{.bash}
mycroft-stop
~~~~~~~~~~~~~~~~~~~

_2. get the latest linux updates_

~~~~~~~~~~~~~~~~~~~{.bash}
sudo apt update
~~~~~~~~~~~~~~~~~~~

enter your password when prompted. the password is `mycroft`. you won't see any output while typing, just type it and hit enter.

_3. install linux updates_

~~~~~~~~~~~~~~~~~~~{.bash}
sudo apt upgrade
~~~~~~~~~~~~~~~~~~~

_4. get the latest respeaker code_. note that there are 3 es in `seeed` (it took me 4 tries to figure this out)

~~~~~~~~~~~~~~~~~~~{.bash}
git clone https://github.com/respeaker/seeed-voicecard.git
~~~~~~~~~~~~~~~~~~~

_5. open the files you just downloaded_

~~~~~~~~~~~~~~~~~~~{.bash}
cd seeed-voicecard
~~~~~~~~~~~~~~~~~~~

_6. run the respeaker installer_. This took a long time for me (15-20 minutes).

~~~~~~~~~~~~~~~~~~~{.bash}
sudo ./install.sh  --compat-kernel
~~~~~~~~~~~~~~~~~~~

_7. reboot your RPI with this command_

~~~~~~~~~~~~~~~~~~~{.bash}
sudo reboot
~~~~~~~~~~~~~~~~~~~


Step 5: Fix the audio
---------------------
There's a good chance that you followed all of these steps and your audio
still isn't working. You can take a look at the troubleshooting techniques
offered on [this page by the mycroft team](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/troubleshooting/audio-troubleshooting).


**fixing a USB mic**

For me, with my USB microphone, I solved the problem with these steps by editing
the file `/etc/mycroft/mycroft.conf`.

Launch the text editor with this command (enter your password, `mycroft`, when prompted):
`sudo nano /etc/mycroft/mycroft.conf`

Use the arrow keys to navigate the file, and then change the two lines to match this:

~~~~~~~~~~~~~~~~~~~{.json}
{
  "play_wav_cmdline": "aplay %1",
  "play_mp3_cmdline": "mpg123 %1",
  [...]
}
~~~~~~~~~~~~~~~~~~~

The stuff in the square brackets `[...]` just means the rest of the text in the file.
Leave that alone. Once you make the changes, hit ctrl-o to save and ctrl-x to quit.
Run the `mycroft-stop` command to shutdown mycroft. Run `mycroft-start debug`
to start it again in debug mode.


**fixing respeaker mic**

I fixed the respeaker issues with the same procedure, except with different
settings in the file `/etc/mycroft/mycroft.conf`. Make the file match this:

~~~~~~~~~~~~~~~~~~~{.json}
{
  "play_wav_cmdline": "aplay -Dhw:1,0 %1",
  "play_mp3_cmdline": "mpg123 -a hw:1,0 %1",
  [...]
}
~~~~~~~~~~~~~~~~~~~

Since we don't all have the exact same hardware, these settings might not
work for you, or there might be other changes needed. For example, you may
also need to [change the audio output with these instructions](https://www.raspberrypi.org/documentation/configuration/audio-config.md).

In general, if you're stuck on this step, post a message in `#code` and Daniel and I will find a time to work with you to straighten out the problem.
