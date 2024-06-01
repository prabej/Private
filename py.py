
def modules():
    print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m  REPOSITORY CHECK \x1b[37m')
    os.system('pkg update -y && pkg upgrade -y')
    os.system('clear')
    import requests
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m REQUESTS IS BEING INSTALLED \x1b[37m')
        os.system('pip install requests --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m')
    exit()
    import bs4
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m BS4 IS BEING INSTALLED \x1b[37m')
        os.system('pip install bs4 --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m')
    exit()
    import rich
    if ModuleNotFoundError:
        print('\x1b[37m •\x1b[38;5;196m ->\x1b[37m RICH IS BEING INSTALLED \x1b[37m')
        os.system('pip install rich --quiet')
        print('\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m')
print('sorry command became server down')
os.system('exit')
