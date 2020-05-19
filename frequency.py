#encoding = 'utf-8'
import pymorphy2 as morph 


def normal(item):
    lemma = ''
    for i in item:
        if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я") or i == "ё" or i == "Ё" or (i == '-' and lemma != ''):
            lemma += i
    lemma_info = morph.MorphAnalyzer().parse(lemma)[0]
    if lemma not in freq_dict and (lemma_info.tag.POS not in ['NPRO', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'COMP', None]):
        return lemma_info.normal_form 


def freq(text):
    all_words = {}
    for item in text:
        item = normal(item)
        if item in all_words.keys():
            all_words[item] += 1
        else:
            all_words[item] = 1
    n = 10   #number of pieces of pie
    maximum = [['', 0]] * n
    items = all_words.keys()
    for key in items:
        for i in range(n):
            if all_words[key] > maximum[i][1]:
                rshift = maximum[i]
                for j in range(i + 1, n):
                    maximum[j], rshift = rshift, maximum[j]
                maximum[i] = [key, all_words[key]]
    return maximum


freq_dict = ["имя", "фамилия", 'быть', "уже", "тот", "наш", "этот", "свой", "ещё", "принять", 'который', 'весь', 'год', 'мочь', 'человек', 'такой', 'сказать', 'один', 'время', 'сам', 'когда', 'другой', 'говорить', 'знать', 'стать', 'первый', 'очень', 'два', 'день', 'новый', 'раз', 'можно', 'какой', 'самый', 'потом', 'надо', 'хотеть', 'слово', 'идти', 'большой', 'должен', 'место', 'иметь']