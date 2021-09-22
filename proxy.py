def proxy_parser(name='proxy.txt'):
    f = open(name, "r")
    strings = f.read().split("\n")
    proxies = [{"https": i} for i in strings]
    return proxies
