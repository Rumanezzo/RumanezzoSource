with open('Dictionary.txt', encoding='cp1251') as fin:
    for i in fin:
        s = i.split()[0].rstrip('\n')
        if s == s[::-1]:
            print(f'{s:12s} - {len(s):3d} <•••• читается одинаково в обе стороны!')
        if len(s) == len(set(s)) and len(s) > 4:
            print(f'{s:12s} - {len(s):3d} <•••• состоит из неповторяющихся букв!')

fin.close()
input('«Нажмите «Enter» для завершения ••••» ')
