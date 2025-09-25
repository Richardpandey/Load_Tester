import pyfiglet
from termcolor import colored

def show_banner():
    banner = pyfiglet.figlet_format("Load_tester", font="jazmine")
    print(colored(banner, "green"))

    print (colored ("A Full Webiste Traffic Loader + Tester"))
    print()
    print (colored ("👤 Author: Richard | GitHub: Richardpandey", "green"))
    print()
    print (colored ("Version: 1.0", "green"))
    print()
    print(colored("------------------------------------------------------------\n", "white"))
    
