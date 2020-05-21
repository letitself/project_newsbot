#encoding = 'utf-8'
import pymorphy2 as morph 


def normal(item):
    lemma = ''
    for i in item:
        if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я") or i == "ё" or i == "Ё" or (i == '-' and lemma != ''):
            lemma += i
    lemma_info = Morph_Anal.parse(lemma)[0]
    lemma = lemma_info.normal_form
    if lemma not in freq_list and (lemma_info.tag.POS not in ['NPRO', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'COMP', None]):
        return lemma


def freq(text):
    all_words = {}
    for item in text:
        item = normal(item)
        if item != None and item in all_words.keys():
            all_words[item] += 1
        elif item != None:
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
                break
    return maximum


freq_list = ["имя", "представитель", "фамилия", 'быть', "более", "менее", "уже", "каждый", "тот", "наш", "этот", "свой", "ещё", "принять", 'который', 'весь', 'год', 'мочь', 'человек', 'такой', 'сказать', 'один', 'время', 'сам', 'когда', 'другой', 'говорить', 'знать', 'стать', 'первый', 'очень', 'два', 'день', 'новый', 'раз', 'можно', 'какой', 'самый', 'потом', 'надо', 'хотеть', 'слово', 'идти', 'большой', 'должен', 'место', 'иметь']
Morph_Anal = morph.MorphAnalyzer()


if __name__ == "__main__":
    with open('text.txt', encoding='utf-8') as f:
        text = f.read().split()
    print(freq(text))