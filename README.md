1) setup raspberry-pi with LIRC and IR Transmitter / Receiver
https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581
Things required:
raspberry-pi, i got this working on raspberry-pi, model b.
IR LED/Transmitter and Receiver - don't remember which one, i got some old parts lying around,
and they seem to have embedded with proper circuit, thus eleminating need for transistor and
resistor required to derive the Transmitter/Receiver properly.
the components I have have, vcc, gnd and data pinout.

circuit:
3.3 of raspberry-pi to vcc of Transmitter/Receiver
gnd of raspberry-pi to gnd of Transmitter/Receiver
GPIO22 - data of IR Transmitter
GPIO23 - data of IR Receiver

Setup your raspberry-pi with LIRC
    sudo apt-get install lirc
add following to /etc/modules/ (you will need to use sudo)
    lirc_dev
    lirc_rpi gpio_in_pin=23 gpio_out_pin=22
update /etc/lirc/lirc_options.conf with following under [lircd], this step might not be exact same:
    driver          = default
    device          = /dev/lirc0
add following in /boot/config.txt:
    # LIRC
    dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
start or stop lircd with following:
    sudo /etc/init.d/lircd start/stop

Testing IR Receiver:
    sudo /etc/init.d/lircd stop
    mode2 -d /dev/lirc0
Now point remote towards IR Receiver and press few buttons, you should see something like following:
    space 16300
    pulse 95
    space 28794
    pulse 80
    space 19395
    pulse 83

Recording your TV remote buttons in a profile:
    sudo /etc/init.d/lircd stop
    irrecord -d /dev/lirc0 ~/lircd.conf
    # follow on screen instructions to configure remote, refer http://www.lirc.org/html/irrecord.html
    # Make a backup of the original lircd.conf file
    sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf
    # Copy over your new configuration file
    sudo cp ~/lircd.conf /etc/lirc/lircd.conf
    # Start up lirc again
    sudo /etc/init.d/lircd start
    # to add more keys to remote control config file:
    irrecord -u ~/lircd.conf

Testing IR Transmitter:
    # List all of the commands that LIRC knows for your remote
    # cat /etc/lirc/lircd.conf and find your remote control name
    irsend LIST <remote_control_name> ""
    # Send the KEY_POWER command once
    irsend SEND_ONCE <remote_control_name> KEY_POWER
    # Send the KEY_VOLUMEDOWN command once
    irsend SEND_ONCE <remote_control_name> KEY_VOLUMEDOWN
    # you can create small python scripts for various key press or key press sequences.
    # this will be useful later when integrating with google home.

Now that we have functional IR remote, you can keep the setup close enough to TV so that it is sure to be received by TV.
2) Setup raspberry-pi python server with google home (using IFTTT)
    # create a simple python server, that can handle POST, i took following as reference
    # https://gist.github.com/bradmontgomery/2219997
    # use a port number which is un-used and is not blocked by your host AP firewall.
    # in AP setting redirect, incoming request for the port to your raspberry-pi ip/mac address. this is AP dependent setting
    # find out public IP address if your home network. this will be needed later to configure IFTTT
    # in post handler, run various python script depending on content of POST request.
    # run the script to start your server that will trigger python script to simulate various button press of remote control.

    # sign up for IFTTT at https://ifttt.com/
    # create new applet https://ifttt.com/create
    # click +This
    # search for google assistant
    # click "say a simple phrase"
    # follow on-screen instructions
    # click "create trigger"
    # click "+That"
    # search for "webhooks"
    # click "make a web request"
    # url: http://<your public ip addr>:<port selected while creating server>/
    # method: post
    # content_type: plain/text
    # body: <some test to differentiate between various google assistant commands>
    # save

    # now try the newly create google assitant command, and monitor your python server logs to verify things are working
    # for different body content for a POST request you can simulate differnt button press via code.

3) running python script server at boot:
add path of python script in following file. preferably keep python script in /etc/init.d/
/etc/rc.local

4) find out which process is using port
sudo lsof -i :8080
