def cleaner (dic):
    for dato in dic:
        if dic[dato].isnumeric():
            dic[dato] = int(dic[dato])
        elif not dic[dato]:
            dic[dato] = None
        elif isinstance(dic[dato], str):
            dic[dato] = dic[dato].strip()
        else:
            dic[dato] = None