def name_parser(name='name.txt'):
    f = open(name, "r")
    strings = f.read().split("\n")
    names = [i.split(":") for i in strings]  # format - phone:sender:text
    return names
