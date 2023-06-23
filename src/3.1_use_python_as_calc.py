# Encoding: UTF-8
# Standalone: yes (but need to be run in python shell)
# Description: This file is used to show how to use python as a calculator
#
# Usage: python 3.1_use_python_as_calc.py
#        python -i 3.1_use_python_as_calc.py

# 3.1.1 Numbers
print 2 + 2
print 50 - 5*6
print (50 - 5*6) / 4
print 8 / 5

print 17 / 3  # int / int -> int
print 17 / 3.0  # int / float -> float
print 17 // 3.0  # explicit floor division discards the fractional part
print 17 % 3  # the % operator returns the remainder of the division
print 5 * 3 + 2  # result * divisor + remainder

print 5 ** 2  # 5 squared
print 2 ** 7  # 2 to the power of 7

width = 20
height = 5 * 9
print width * height

print 4 * 3.75 - 1

tax = 12.5 / 100
price = 100.50
print price * tax
print price + _    # _ means the last printed expression
print round(_, 2)

# 3.1.2 Strings
print 'spam eggs'  # single quotes
print 'doesn\'t'  # use \' to escape the single quote...
print "doesn't"  # ...or use double quotes instead
print '"Yes," they said.'
print "\"Yes,\" they said."
print '"Isn\'t," they said.'

print '"Isn\'t," they said.'
s = 'First line.\nSecond line.'  # \n means newline
print s  # without print, \n is included in the output
print 'C:\some\name'  # here \n means newline!
print r'C:\some\name'  # note the r before the quote
print """\
Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
"""

# 3 times 'un', followed by 'ium'
print 3 * 'un' + 'ium'

print 'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')
print text

prefix = 'Py'
print prefix + 'thon'

word = 'Python'
print word[0]  # character in position 0

print word[5]  # character in position 5

print word[-1]  # last character

print word[-2]  # second-last character

print word[-6]

print word[0:2]  # characters from position 0 (included) to 2 (excluded)

print word[2:5]  # characters from position 2 (included) to 5 (excluded)

print word[:2] + word[2:]

print word[:4] + word[4:]

print word[:2]  # character from the beginning to position 2 (excluded)

print word[4:]  # characters from position 4 (included) to the end

print word[-2:]  # characters from the second-last (included) to the end

print word[42]  # the word only has 6 characters

print word[4:42] # display 'on'

print word[42:]  # no error but display nothing

print 'J' + word[1:] # concatenate strings with + operator diplays 'Jython'

print word[:2] + 'py' # concatenate strings with + operator diplays 'Pypy'

s = 'supercalifragilisticexpialidocious'

print len(s)


