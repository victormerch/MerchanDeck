import webbrowser
import subprocess
import os
#--- Obejeto access de paginas web ---
class accessos:

    #--- Accessos Webs ---
    def youtube(self):
        webbrowser.open_new("https://www.youtube.com/")

    def netflix(self):
        webbrowser.open_new("https://www.netflix.com/browse")

    def twitch(self):
        webbrowser.open_new("https://www.twitch.tv/directory")

    def whatsapp(self):
        webbrowser.open_new("https://web.whatsapp.com/")

    def instagram(self):
        webbrowser.open_new("https://www.instagram.com/")

    def gmail(self):
        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

    def google(self):
        webbrowser.open_new("https://www.google.com/")


    #--- Accesso PC ---

        # - Sistema -

    def reiniciar(self):
        subprocess.call("shutdown -r")

    def cerrarSesion(self):
        subprocess.call("shutdown -l")

        # - Codigo


    def cmd(self):
        os.system('cmd')

    def java(self):
        os.startfile(r"C:\Users\Victo\Desktop\Eclipse IDE for Java Developers - 2020-06.lnk")

    def mysql(self):
        os.startfile(r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe")

    def vb(self):
        os.startfile(r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")

    def python(self):
        os.startfile(r"C:\Users\Public\Desktop\PyCharm Community Edition 2020.2 x64.lnk")

        # - Apps Desktop

    def discord(self):
        os.startfile(r"C:\Users\Victo\Desktop\Discord.lnk")

        # - Video Games

    def among(self):
        os.startfile(r"C:\Users\Victo\Desktop\Among Us.url")

    def minecraft(self):
        os.startfile(r"C:\Users\Public\Desktop\Minecraft Launcher.lnk")
























