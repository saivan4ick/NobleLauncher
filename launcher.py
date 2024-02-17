import minecraft_launcher_lib
import subprocess

print("""\n
███╗░░██╗░█████╗░██████╗░██╗░░░░░███████╗
████╗░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝
██╔██╗██║██║░░██║██████╦╝██║░░░░░█████╗░░
██║╚████║██║░░██║██╔══██╗██║░░░░░██╔══╝░░
██║░╚███║╚█████╔╝██████╦╝███████╗███████╗
╚═╝░░╚══╝░╚════╝░╚═════╝░╚══════╝╚══════╝
██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░░░░███████║██║░░░██║██╔██╗██║██║░░╚═╝███████║█████╗░░██████╔╝
██║░░░░░██╔══██║██║░░░██║██║╚████║██║░░██╗██╔══██║██╔══╝░░██╔══██╗
███████╗██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║███████╗██║░░██║
╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ by saivan | version 1.0""")

print("Minecraft Launcher CLI")

version = input('Enter Minecraft version: ')
username = input('Enter your username: ')
print("""\nNOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.
\nLegacy Launcher is in no way affiliated with Mojang Studios, nor should it be considered a project endorsed by Mojang Studios.""")
minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory='.noblelauncher')
options = {
	'username': username,
	'uuid': '',
	'token': ''
}
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory='.noblelauncher', options=options))