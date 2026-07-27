import socket
import uuid
import requests
import psutil
import subprocess
import platform
import netifaces

# ==========================================
# INTERNET STATUS
# ==========================================

def internet_status():

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Connected")

    except OSError:
        print("No Internet Connection")


# ==========================================
# HOST NAME
# ==========================================

def hostname():

    print("Hostname :", socket.gethostname())


# ==========================================
# LOCAL IP
# ==========================================

def local_ip():

    try:

        ip = socket.gethostbyname(socket.gethostname())

        print("Local IP :", ip)

    except Exception:

        print("Unable to Get Local IP")


# ==========================================
# PUBLIC IP
# ==========================================

def public_ip():

    try:

        ip = requests.get("https://api.ipify.org").text

        print("Public IP :", ip)

    except:

        print("Unable to Fetch Public IP")


# ==========================================
# MAC ADDRESS
# ==========================================

def mac_address():

    mac = ':'.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0,12,2))

    print("MAC Address :", mac)


# ==========================================
# NETWORK INTERFACES
# ==========================================

def network_interfaces():

    interfaces = psutil.net_if_addrs()

    print("Available Interfaces\n")

    for interface in interfaces:

        print(interface)


# ==========================================
# NETWORK STATS
# ==========================================

def network_statistics():

    stats = psutil.net_io_counters()

    print(f"Bytes Sent : {stats.bytes_sent}")

    print(f"Bytes Received : {stats.bytes_recv}")

    print(f"Packets Sent : {stats.packets_sent}")

    print(f"Packets Received : {stats.packets_recv}")


# ==========================================
# ACTIVE CONNECTIONS
# ==========================================

def active_connections():

    connections = psutil.net_connections()

    print("Active Connections :", len(connections))

    for connection in connections[:20]:

        print(connection)


# ==========================================
# DNS SERVERS
# ==========================================

def dns_servers():

    interfaces = netifaces.interfaces()

    print("DNS Information\n")

    for interface in interfaces:

        try:

            gateway = netifaces.gateways()

            print(gateway)

            break

        except:

            pass


# ==========================================
# DEFAULT GATEWAY
# ==========================================

def default_gateway():

    gateways = netifaces.gateways()

    default = gateways.get('default')

    print(default)


# ==========================================
# NETWORK ADAPTER STATUS
# ==========================================

def adapter_status():

    stats = psutil.net_if_stats()

    for adapter, value in stats.items():

        print("--------------------------------")

        print("Adapter :", adapter)

        print("Connected :", value.isup)

        print("Speed :", value.speed, "Mbps")

        print("MTU :", value.mtu)


# ==========================================
# IP CONFIG
# ==========================================

def ip_config():

    subprocess.run("ipconfig", shell=True)


# ==========================================
# ROUTING TABLE
# ==========================================

def routing_table():

    subprocess.run("route print", shell=True)


# ==========================================
# ARP TABLE
# ==========================================

def arp_table():

    subprocess.run("arp -a", shell=True)


# ==========================================
# NETWORK RESET
# ==========================================

def network_reset():

    subprocess.run("ipconfig /flushdns", shell=True)

    subprocess.run("ipconfig /release", shell=True)

    subprocess.run("ipconfig /renew", shell=True)

    print("Network Reset Completed")


# ==========================================
# SYSTEM INFO
# ==========================================

def network_system():

    print("System :", platform.system())

    print("Release :", platform.release())

    print("Version :", platform.version())

    print("Machine :", platform.machine())

import subprocess

# ==========================================
# WIFI NAME
# ==========================================

def wifi_name():

    try:

        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "SSID" in line and "BSSID" not in line:

                print(line.strip())

    except:

        print("Unable to Get WiFi Name")


# ==========================================
# SAVED WIFI PROFILES
# ==========================================

def saved_wifi_profiles():

    try:

        output = subprocess.check_output(
            "netsh wlan show profiles",
            shell=True,
            text=True
        )

        print(output)

    except:

        print("Unable to Get Profiles")


# ==========================================
# WIFI PASSWORD
# ==========================================

def wifi_password(profile):

    try:

        command = f'netsh wlan show profile name="{profile}" key=clear'

        output = subprocess.check_output(
            command,
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "Key Content" in line:

                print(line.strip())

                return

        print("Password Not Found")

    except:

        print("Unable to Get Password")


# ==========================================
# SCAN WIFI
# ==========================================

def scan_wifi():

    try:

        output = subprocess.check_output(
            "netsh wlan show networks mode=bssid",
            shell=True,
            text=True
        )

        print(output)

    except:

        print("Unable to Scan WiFi")


# ==========================================
# CONNECT WIFI
# ==========================================

def connect_wifi(profile):

    try:

        subprocess.run(
            f'netsh wlan connect name="{profile}"',
            shell=True
        )

        print("Connection Requested")

    except:

        print("Connection Failed")


# ==========================================
# DISCONNECT WIFI
# ==========================================

def disconnect_wifi():

    try:

        subprocess.run(
            "netsh wlan disconnect",
            shell=True
        )

        print("WiFi Disconnected")

    except:

        print("Unable to Disconnect")


# ==========================================
# DELETE WIFI PROFILE
# ==========================================

def delete_wifi_profile(profile):

    try:

        subprocess.run(
            f'netsh wlan delete profile name="{profile}"',
            shell=True
        )

        print("Profile Deleted")

    except:

        print("Unable to Delete Profile")


# ==========================================
# WIFI SIGNAL
# ==========================================

def wifi_signal():

    try:

        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "Signal" in line:

                print(line.strip())

    except:

        print("Unable to Get Signal")


# ==========================================
# WIFI CHANNEL
# ==========================================

def wifi_channel():

    try:

        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "Channel" in line:

                print(line.strip())

    except:

        print("Unable to Get Channel")


# ==========================================
# WIFI RADIO TYPE
# ==========================================

def wifi_radio():

    try:

        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "Radio type" in line:

                print(line.strip())

    except:

        print("Unable to Get Radio Type")


# ==========================================
# WIFI AUTHENTICATION
# ==========================================

def wifi_security(profile):

    try:

        command = f'netsh wlan show profile name="{profile}"'

        output = subprocess.check_output(
            command,
            shell=True,
            text=True
        )

        for line in output.split("\n"):

            if "Authentication" in line:

                print(line.strip())

            if "Cipher" in line:

                print(line.strip())

    except:

        print("Unable to Get Security")


# ==========================================
# HOTSPOT STATUS
# ==========================================

def hotspot_status():

    try:

        output = subprocess.check_output(
            "netsh wlan show hostednetwork",
            shell=True,
            text=True
        )

        print(output)

    except:

        print("Hosted Network Not Available")


# ==========================================
# WLAN DRIVER INFO
# ==========================================

def wifi_driver():

    try:

        output = subprocess.check_output(
            "netsh wlan show drivers",
            shell=True,
            text=True
        )

        print(output)

    except:

        print("Unable to Get Driver Information")    