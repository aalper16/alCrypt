
harfler = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p','q', 'r', 's', 'ş', 't', 'u', 'ü', 'v','w', 'x' ,'y', 'z', '?', '*', '/', '1','2','3','4','5','6','7','8','9','0','-','_','%','&','[',']','(',')','=','}','{','#','>','<','.',':',',',';',' ','Б']
def encode(e_content):
    length_content = len(e_content)
    result = ""
    for i in range(length_content):
        harf = e_content[i]
        place = harfler.index(harf)
        new_place = place + 1
        result += harfler[int(new_place)]
    return result


def decode(d_content):
    result = ""
    length_content_d = len(d_content)
    for i in range(length_content_d):
        harf_d = d_content[i]
        place_d = harfler.index(harf_d)
        new_place_d = place_d -1
        result += harfler[int(new_place_d)]
    return result

