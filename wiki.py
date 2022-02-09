import wikipedia

wikipedia.set_lang('uz')

def searchWiki(text):
    try:
        return wikipedia.summary(text)
    except:
        ans =  "Bu mavzuga oid maqola topilmadi!\n\n"
        ts = wikipedia.search(text)
        if len(ts)>0:
            ans += "Balkim buni qidirmoqchidursiz👇\n\n"
        for t in ts:
            ans += t + '\n'
        return ans
