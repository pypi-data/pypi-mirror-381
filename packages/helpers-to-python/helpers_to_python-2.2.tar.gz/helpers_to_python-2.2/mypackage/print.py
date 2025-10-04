import time
import colorama

def printMessageError(message, number):
    for SaveMessageError in range(number):
        print(colorama.Fore.RED + '[error]' + ' ' + colorama.Fore.YELLOW + message)
def printMessageWarning(message, number):
    for SaveMessageWarning in range(number):
        print(colorama.Fore.YELLOW + '[warning]' + ' ' + colorama.Fore.GREEN + message)
def stop(timeToStop, message_stop):
    time.sleep(timeToStop)
    exit(message_stop)
