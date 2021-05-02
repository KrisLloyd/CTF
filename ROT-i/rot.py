ciphertext = "Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv krho{mckchd_zk_zpj_iiqmrwde}. Wyh tsi fmm nkjc pfp esj xjzpd tdh lay nbqs ph xmkt, dsql lee'm vhi ae vkmx libi"

def roti(s):
    x = []
    count = 0
    for i in range(len(s)):
        if s[i] in ["'", "!", "{", "}", "_", ".", ",", " "]:
            count += 1
            x.append(s[i])
            continue
        j = ord(s[i])
        if s[i].isupper():
            # ASCII 65 - 90
            for i in range(count):
                j -= 1
                if j == 64:
                    j = 90
            x.append(chr(j))
        else:
            # ASCII 97 - 122
            for i in range(count):
                j -= 1
                if j == 96:
                    j = 122
            x.append(chr(j))
        count += 1
    return ''.join(x)

print(roti(ciphertext))
