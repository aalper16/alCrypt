import alCrypt as ac
from colorama import Fore, Back, Style
import os

while True:
    com = input(Fore.BLUE+'encode or decode: ')
    Style.RESET_ALL
    if com == 'encode':
        encode = input(Fore.GREEN+'encoding: ')
        Style.RESET_ALL
        print(Fore.RED+ac.encode(encode))
        Style.RESET_ALL

    elif com == 'decode':
        decode = input(Fore.GREEN+'decoding: ')
        Style.RESET_ALL
        print(Fore.RED+ac.decode(decode))
        Style.RESET_ALL

    elif com == 'encode_txt':
        filepath = input('file path: ')
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        encoded_txt = ac.encode(content)
        print(encoded_txt)
        save = input('save to file? y/n')
        if save == 'y':
            with open(filepath, 'w', encoding='utf-8') as writing:
                writing.write(encoded_txt)
        else:
            continue
    elif com == 'decode_txt':
        filepath = input('file path:')
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        decoded_txt = ac.decode(content)
        print(decoded_txt)
        save = input('save to file? y/n')
        if save == 'y':
            with open(filepath, 'w', encoding='utf-8') as writing:
                writing.write(decoded_txt)
        else:
            continue
    else:
        print('No commands.')