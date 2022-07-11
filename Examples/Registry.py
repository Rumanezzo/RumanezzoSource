import winreg
magic_const = 65536


i = 0
lines = 0
key_reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Console')
while True:
    try:
        t = winreg.EnumValue(key_reg, i)
        if 'ScreenBufferSize' in t:
            print(f'{i} -> {t} -> строк в буфере экрана - {t[1]//magic_const}')
        elif 'WindowSize' in t:
            print(f'{i} -> {t} -> строк на экране - {t[1]//magic_const}')
        i += 1
    except OSError:
        break
