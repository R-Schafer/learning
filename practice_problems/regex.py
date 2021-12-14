# https://learning.oreilly.com/library/view/automate-the-boring/9781098122584/xhtml/ch07.xhtml#ch07lev1sec3
#Identifying phone numbers
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print(f'Phone number found: {chunk}')
# print('Done')

# regex
import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# NumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = NumRegex.search('My number is 451-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# escaping parenthese
# NumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = NumRegex.search('My number is (451) 555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# matching groups with a pipe |
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())
# mo2 = heroRegex.search(r'Tina Fey|Batman')
# print(mo2.group())

# another example of pipe |
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batman has a Batmobile')
# print(mo.group())
# print(mo.group(1))

# matching with optional mark ?
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search("The Adventures of Batman")
# print(mo1.group())
# mo2 = batRegex.search("The adventures of Batwoman")
# print(mo2.group())

# another example of ?
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search("My number is 415-555-4242")
# print(mo1.group())
# mo2 = phoneRegex.search("My number is 555-4242")
# print(mo2.group())

# matching zero or more with *
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search("The Adventures of Batman")
# print(mo1.group())
# mo2 = batRegex.search("The adventures of Batwoman")
# print(mo2.group())
# mo3 = batRegex.search("The adventures of Batwowowowoman")
# print(mo3.group())

# using repetitive braces
# haRegex = re.compile(r'(ha){1,5}')
# mo1 = haRegex.search('haha')
# print(mo1.group())
# mo2 = haRegex.search('hahahahaha')
# print(mo2.group())

# findall() method
# phoneNum = re.compile(r'\d\d\d-\d\d\d\d')
# mo = phoneNum.findall('phone: 729-1294 work: 723-7104')
# print(mo)

# different character classes
# xmasRegex = re.compile(r'\w+\s\w+')
# xmas = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies')
# print(xmas)

# define your own character case
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# vowel = vowelRegex.findall('RoboCop eats baby food. BABY FOOD!')
# print(vowel)

# another example
# vowelRegex = re.compile(r'[0-5.]')
# vowel = vowelRegex.findall('I have 4 cars. 1 egg. and 5 fingers.')
# print(vowel)

# using a caret will match characters NOT in the class
# letterRegex = re.compile(r'[^aeiouAEIOU]')
# letter = letterRegex.findall('RoboCop eats BABY FOOD!')
# print(letter)

# use the ^ and $ together to indicate that the entire string must match
# this example wants the string to begin and end with a number
# wholeStringIsNum = re.compile(r'^\d+$')
# number = wholeStringIsNum.search('123456789')
# print(number)

# this example wont work if you add a space or letter at the beginning or end
# wholeStringIsNum = re.compile(r'^\d+$')
# number = wholeStringIsNum.search('a123456789')
# print(number)

# the wildcard or dot .
# atRegex = re.compile(r'.at')
# at = atRegex.findall('The cat in the hat sat on the flat mat')
# print(at)

# matching everything with .*
# name = re.compile(r'First name: (.*) Last name: (.*)')
# mo = name.search('First name: Al Last name: Sweigart')
# print(mo.group(1))

# making regex case insensitive
# robocop = re.compile(r'robocop', re.I)
# mo = robocop.findall('RoboCop is ROBOCOP, is robocop.')
# print(mo)

# passing a substitution word in place of another word with sub()
# namesRegex = re.compile(r'Agent \w+', re.I)
# mo = namesRegex.sub('CENSORED', 'Agent Alice to agent Bob the case details.')
# print(mo)

# extracting phone numbers and emails from a bunch of text
import pyperclip
# phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

# email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol   
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')