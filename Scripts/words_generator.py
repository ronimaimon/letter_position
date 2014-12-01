# coding=utf-8
__author__ = 'Roni'
import random

all_chars = [u'ב', u'ג', u'ד', u'ח', u'ט', u'כ', u'ל', u'מ', u'נ', u'ס', u'ע', u'פ', u'צ', u'ק', u'ר', u'ש', u'ת']


def cond_1():
    all_chars.append(u'מ')
    all_chars.append(u'ת')
    end_chars = all_chars[:]
    end_chars.remove(u'ת')
    end_chars.remove(u'מ')
    first_chars = [u'ל', u'מ', u'נ',u'ת']
    for i in range(1, 100):
        l1 = first_chars[random.randrange(len(first_chars))]
        l3 = all_chars[random.randrange(len(all_chars))]
        l2 = all_chars[random.randrange(len(all_chars))]
        l4 = end_chars[random.randrange(len(end_chars))]
        print "%s%s%s%s, %s%s%s%s" % (l1, l2, l3, l4, l1, l3, l2, l4)

def cond_2():
    first_chars = all_chars[:]
    first_chars.remove(u'ב')
    first_chars.remove(u'כ')
    first_chars.remove(u'ש')
    first_chars.remove(u'ת')
    first_chars.remove(u'מ')
    first_chars.remove(u'ל')
    first_chars.remove(u'נ')
    end_chars = [u'ה',u'ן',u'ם',u'ת']
    # end_chars = all_chars[:]
    # end_chars.remove(u'ת')
    # end_chars.remove(u'נ')
    # end_chars.remove(u'מ')
    for i in range(1, 50):
        l1 = first_chars[random.randrange(len(first_chars))]
        l3 = u'ז'
        l2 = all_chars[random.randrange(len(all_chars))]
        l4 = end_chars[random.randrange(len(end_chars))]
        print "%s%s%s%s, %s%s%s%s" % (l1, l2, l3, l4, l1, l3, l2, l4)


cond_2()



