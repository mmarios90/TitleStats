import requests
from bs4 import BeautifulSoup
import operator

word_list = []
clean_list = []

def page1(url):

    print("\n news247 titles:")
    source_code = requests.get(url).text #connects url to webpage and returns it as text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll(class_='article__title bold'):
        content1 = post_text.find('a').get_text()
        content = str(content1)
        print(content1)
        words = content.lower().split()
        #print(words)
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)

    word_cleaner(word_list)
    print(len(word_list))
    print("--1--")

def page2(url):

    print("\n dikaiologitika.gr titles:")
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll(class_='newsroom__title'):
        content2 = post_text.find('a').get_text()
        content = str(content2)
        print(content2)
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    word_cleaner(word_list)
    print(len(word_list))
    print("--2--")

def page3(url):

    print("\n zoogla.gr titles:")
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll(class_='supertitle'):
        content3 = post_text.find('a').get_text()
        content = str(content3)
        print(content3)
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    word_cleaner(word_list)
    print(len(word_list))
    print("--3--")

def page4(url):

    print("\n lifo.gr titles:")
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll(class_='lf_inline'):
        content4 = post_text.find('a').get_text()
        content = str(content4)
        print(content4)
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    word_cleaner(word_list)
    print(len(word_list))
    print("--4--")

def page5(url):

    print("\n newsit.gr titles:")
    source_code1 = requests.get(url).text
    soup = BeautifulSoup(source_code1, "html.parser")

    for post_text in soup.findAll(class_='info'):
        content5 = post_text.find('a').get_text()
        content = str(content5)
        print(content5)
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    word_cleaner(word_list)
    print(len(word_list))
    print("--5--")


def word_cleaner (word_list):

    for word in word_list:
        trash = "!@$%^&*()_/–+-='\"<>?:-;\|.,«»"
        for i in range(0, len(trash)):
            word = word.replace(trash[i], "")
        if len(word) > 3:
                clean_list.append(word)


def word_counter (clean_list):

    word_count = {}
    for word in clean_list:
        if word not in word_count:
            word_count[word] = clean_list.count(word)
    print("\n")
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        x = len(clean_list)
        y = value/x*100
        print(key, value,"->", y, "%")


page1('https://www.news247.gr/latest')
page2('https://www.dikaiologitika.gr')
page3('https://www.zougla.gr')
page4('https://www.lifo.gr/now')
page5('https://www.newsit.gr')

print(clean_list)
print(len(clean_list))

word_counter(clean_list)

