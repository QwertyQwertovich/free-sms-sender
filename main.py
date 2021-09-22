from termcolor import cprint
from sender import send_message, send
from proxy import proxy_parser
from name import name_parser

test = False # is test


def main():
    cprint("FREE SMS SENDER v1.0", "green")
    cprint("Only 1 free sms per day from one ip!(use proxy for more)", "yellow")
    cprint("It also seems that only one sms per day can be sent to one phone number.", "yellow")
    print("Use proxy(https) (y/n):", end='')
    if input().lower() == "y":
        print("Input file name with proxies(e.g. proxy.txt):")
        print("data format - ip:port")
        proxy_dict = proxy_parser(name=input())
        print("Multiple users/messages(y/n)", end='')
        if input().lower() == "y":
            print("SPAM mode?(same text and number) (y/n):")
            if input().lower() == "y":
                print("Receiver phone:", end='')
                phone = input()
                print("Sender name:", end='')
                sender = input()
                print("Text:", end='')
                text = input()
                print("Messages count:")
                for i in range(max(int(input()), len(proxy_dict))):
                    send(phone, sender, text, test, proxy_dict[i], i=i + 1)
            else:
                print("Input file name with names(e.g. proxy.txt):")
                print("data format - phone:sender:text")
                names = name_parser(name=input())
                proxy_id = 0
                name_id = 0
                i = 0
                while name_id < len(names) and proxy_id < len(proxy_dict):
                    i = i + 1
                    send(names[name_id][0], names[name_id][1], names[name_id][2], test, proxy_dict[proxy_id], i=i)
                    name_id += 1
                    proxy_id += 1
        else:
            print("Receiver phone:", end='')
            phone = input()
            print("Sender name:", end='')
            sender = input()
            print("Text:", end='')
            text = input()
            send(phone, sender, text, test, proxy_dict[0])
    else:
        proxy_dict = None
        print("Receiver phone:", end='')
        phone = input()
        print("Sender name:", end='')
        sender = input()
        print("Text:", end='')
        text = input()
        send(phone, sender, text, test, proxy_dict)


main()
