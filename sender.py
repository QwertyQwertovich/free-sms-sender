import requests
from termcolor import cprint


def send_message(phone="0", sender="name", text="text", proxy=None, is_test=False):
    if is_test:
        key2 = "_test"
    else:
        key2 = ''
    if proxy is None:
        resp = requests.post('https://textbelt.com/text', {
            'phone': phone,
            'senderid': sender,
            'message': text,
            'key': 'textbelt' + key2,
        })
    else:
        resp = requests.post('https://textbelt.com/text', {
            'phone': phone,
            'senderid': sender,
            'message': text,
            'key': 'textbelt' + key2,
        }, proxies=proxy)
    return resp.json()


def send(phone, sender, text, is_test, proxy, i=0):
    try:
        ans = send_message(phone=phone, sender=sender, text=text, is_test=is_test, proxy=proxy)
        if ans['success']:
            cprint(str(i) + ": Success!", "green")
            return True
        else:
            cprint(str(i) + ": Error " + str(ans["error"]), "red")
            return False
    except Exception as e:
        cprint(str(i) + ": Error " + str(e), "red")
        return False
