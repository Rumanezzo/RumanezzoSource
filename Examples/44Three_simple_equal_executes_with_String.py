def pause():
    input('Нажмите на Enter! -> ')


word = input('Вводи строчку текста без пробелов -> ')
print('1-й способ:')
for i in range(len(word)):
    print(word[i])
pause()
print('2-й способ:')
for smb in word:
    print(smb)
pause()
print('3-й способ:')
print(word.replace('', '\n'))
pause()
