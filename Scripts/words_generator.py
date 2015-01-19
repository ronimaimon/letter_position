# coding=utf-8
__author__ = 'Roni'
import random

all_chars = [u'ז', u'ג', u'ד', u'ח', u'ט', u'כ', u'ל', u'מ', u'נ', u'ס', u'ע', u'פ', u'צ', u'ק', u'ר', u'ש', u'ת']


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

class Matrix(object):
    def __init__(self):
        self._matrix = {}
        self._rows = []
        self._columns = []

    def build_matrix(self, row_values, column_values):
        self._rows = row_values
        self._columns = column_values

        for row in row_values:
            row_dict = {}
            for column in column_values:
                row_dict[column] = 0

            self._matrix[row] = row_dict

        self._rows = sorted(row_values)
        self._columns = sorted(column_values)

    def __str__(self):
        ret_str = u'{:<5}'.format(u'')

        for col in self._columns:
            ret_str += u"{:<5}".format(col)

        ret_str += unicode('\n')

        for row in self._rows:
            ret_str += u"{:<5}".format(row)

            for col in self._columns:
                ret_str += u"{:<5}".format(self._matrix[row][col])

            ret_str += unicode('\n')

        return ret_str

    def get_value(self, row, column):
        return self._matrix[row][column]

    def set_value(self, row, column, value):
        self._matrix[row][column] = value

    def add_value(self, row, column, value):
        self._matrix[row][column] += value

    def get_max_column(self, row):
        record = self._matrix[row]
        max_value = None
        max_column = None

        for col in record:
            if max_value is None:
                max_value = record[col]
                max_column = col
            elif record[col] > max_value:
                max_value = record[col]
                max_column = col

        return max_column

def build_distribution(characters, not_allowed):
    distribution = {}

    for char in characters:
        if char not in not_allowed:
            distribution[char] = 0

    return distribution

def next_char_balanced(distribution, not_allowed):
    max_value = 0

    max_list = []
    min_list = []

    for key in distribution:
        if key not in not_allowed:
            if distribution[key] > max_value:
                min_list.extend(max_list)
                max_list = []
                max_list.append(key)

                max_value = distribution[key]
            elif distribution[key] == max_value:
                max_list.append(key)
            else:
                min_list.append(key)

    if (len(min_list) == 0):
        min_list = max_list

    return_character = min_list[random.randrange(len(min_list))]
    distribution[return_character] += 1

    return return_character

def cond_2():
    initials_distribution = build_distribution(all_chars, u'שתמלנכ')
    middle_distribution   = build_distribution(all_chars, '')
    endings_distribution  = build_distribution(all_chars, u'תנמכצפ')

    fs_matrix = Matrix()
    st_matrix = Matrix()
    ft_matrix = Matrix()

    fs_matrix.build_matrix(all_chars, all_chars)
    st_matrix.build_matrix(all_chars, all_chars)
    ft_matrix.build_matrix(all_chars, all_chars)
    combinations = {}

    for i in xrange(300):
        l1 = next_char_balanced(initials_distribution, "")
        l2 = next_char_balanced(middle_distribution, [l1, fs_matrix.get_max_column(l1)])
        l3 = u'ב'
        l4 = next_char_balanced(endings_distribution, [l1, l2, st_matrix.get_max_column(l2), ft_matrix.get_max_column(l1)])

        fs_matrix.add_value(l1, l2, 1)
        st_matrix.add_value(l2, l4, 1)
        ft_matrix.add_value(l1, l4, 1)
        print u"{0}{1}{2}{3} {0}{2}{1}{3}".format(l1, l2, l3, l4)

    #print unicode(fs_matrix)

cond_2()

if __name__ == "main":
    m = Matrix()
    m.build_matrix(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'])
    print m

    m.set_value('a', 'b', 1)
    m.set_value('b', 'c', 2)

    print m

    print m.get_max_column('b')
    print m.get_max_column('a')
