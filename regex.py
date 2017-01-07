import re

##### match
print('re.match() matches a pattern at the beginning of a string')

# re.match(pattern, string, flags)
# matches the *beginning* of the string

regex = '\d'  #Match a digit

match = re.match(regex, '1. Go to gym')  # returns a match object, or None if no matches
# match will have a value if there is a match, or None if there is no match. None is considered False, a value for match is considered True.
if match:                            # Any match object is considered True, useful if you want to check if there was a match
    print('There was a match')
    # To get the text that matched the pattern, call group(0) on the match object
    print('match: ', match.group(0))    # Prints 1
    print('march: ', match.group())   #Group default value is 0 so this is a shortcut for match.group(0)
    # Can find the positions in the string that the regex pattern matches
    print(match.start(), match.end(), match.span())  # 0, 1, (0, 1)  The position the match started and ended, span is a tuple of both values

else:
    print('No match')

match = re.match(regex, 'Go to gym 1 time')   # No match, the digit is not at the beginning
# match will be None if there is no match. None is considered False
if match:
    print('There was a match')
    print(match.group(0))         # Need to test if there was a match before calling group()
else:
    print('No match')   # No match, digit not at the start.



### Search
print('re.search() finds the first match to the pattern anywhere in the string')

regex = '[abc]{2}'   # Match letter a or b or c twice in a row - so 'aa' or 'bb' or 'ab' or 'cb' ...
text = 'this string should actually have a match'      # Even though this string has several matches, only the first match will be returned. Others will be ignored
match = re.search(regex, text)
if match:
    print('match: ', match.group())   # group() default value is 0. Prints ac
    # Can find the positions in the string that the regex pattern matches
    print(match.start(), match.end(), match.span())  # 19, 21, (19, 21)  The position the match started and ended, span is a tuple of both values

regex = '[abc]'   # Match letter a or b or c
text = 'this string will not MATCH'  # no a, b or c - note regex are case sensitive!
match = re.search(regex, text)
if match:
    print('match: ', match.group(0))  #Again use group(0) to get the matched text
else:
    print('no match for ' + regex + " in " + text)


## A more complex regex pattern

regex = '\\bITEC [12]\d{3}-\d{2}\\b'   # The regex to match a word boundary is \b. But \ is a special character in a Python string, so need to escape it as \\

test_string_1 = 'I need to take ITEC 2950-02 Career Prep, to graduate'  # Expect this to match
test_string_2 = 'My office is in 3066-01'  # Matches the numbers, but not the ITEC part
test_string_3 = 'This string shouldn\'t match at all'  #Not a match
test_string_4 = 'The ITEC department is on the 3rd floor'  #Matches ITEC but nothing else
test_string_5 = 'itec 2905-01 is the software development capstone.'  #By default, regex are not case sensitive.
test_string_6 = 'gITEC 1005-013456 shouldn\'t match' # Not a match, need to include a word boundary
test_string_7 = 'This string has three matches, ITEC 1150-10, ITEC 2650-90 and ITEC 2454-90' # Only first match returned

match = re.search(regex, test_string_1)
print(match, test_string_1)
match = re.search(regex, test_string_2)
print(match, test_string_2)
match = re.search(regex, test_string_3)
print(match, test_string_3)
match = re.search(regex, test_string_4)
print(match, test_string_4)
match = re.search(regex, test_string_5)
print(match, test_string_5)
match = re.search(regex, test_string_6)
print(match, test_string_6)
match = re.search(regex, test_string_7)
print(match, test_string_7)



##### findall
print('re.findall() finds all matching strings for the regex pattern, and returns a list of those strings')
# findall returns a list of matching, non-overlapping, strings
match_strings = re.findall(regex, test_string_7)
print(match_strings)
for code in match_strings:
    print('A matched ITEC class code is ', code)



##### Compiling regular expresssions
print('re.compile() generates a compiled regex for faster comparisons and neater syntax, if performing many comparisons')

test = 'bark meow squeak'
comp_reg = re.compile('[abc]') #ignore case. Compiling regex makes them work faster, recommended if using many times
matches = comp_reg.search(test)    # Call search or match on your compiled regex
all_matches = comp_reg.findall(test)
print(matches.group())
print(all_matches)


##### Flags
print('Various flags alter how patterns are matched. See docs for more detail and examples')
# Flags alter the behavior of the regex, for example, whether matches should be case sensitive
# Can include flags in the regex pattern string, or as part of a comiled regex
# To do case-insensitive comparisons, use the re.I flag (same as re.IGNORECASE)

regex_ignorecase = '[abc](?i)'   # The (?i) part is the case-insensitive flag
match = re.search(regex_ignorecase, 'THIS COULD MATCH')
print(match)  # A match for C
match = re.search(regex_ignorecase, 'so could this')
print(match)  #Also a match for c

# Or as a comiled regex, a little neater

ci_regex = re.compile('[abc]', flags=re.IGNORECASE)
match = ci_regex.search('IS THIS A MATCH?')  #yes, matches A
print(match)
match = ci_regex.search('is this a match??')  # Also yes, matches a
print(match)

## Split
print('re.split() breaks a string by a regex pattern. Compare to string.split which splits by a defined separator')
# Break a string by a regex pattern

regex = '\d\.*\s'   # split a string every time there's a number, period, 0 or more whitespace characters
todo_items = '1. Buy milk 2. Walk dog 3.  assignments. 4. More stuff'
todo_list = re.split(regex, todo_items)
# Note there's an empty string at the start of the list.
print(todo_list) # ['', 'Buy milk ', 'Walk dog ', ' assignments. ', 'More stuff']

regex = '\d'  # Split on digits
string = 'aaaa1cccc2eeee4sssss'
parts = re.split(regex, string)
print(parts)        #  ['aaaa', 'cccc', 'eeee', 'sssss']

# Compare to python string split method, which breaks by a defined separator


##### Sub
print('re.sub() can make replacements based on a regex. Can also call a function for each match that will be replaced for more complex replacements')
# Make replacements based on a regex

regex = 'y|z'  # Match y or z
text = 'Remove y and z from this string please'
removed_yz = re.sub(regex, '*', text)   # Replaces x and y with *
print(removed_yz)   # Remove * and * from this string please

# Sub can also call a function on the thing is will be replacing, and replace
# the thing with the return value from the function  (neat!!)

def emphasizer(s):
    return s.group().upper() + '!!'

emphasized_yz = re.sub(regex, emphasizer, text)
print(emphasized_yz)   # Remove Y!! and Z!! from this string please


##### Groups
print('Use () parenthesis to group parts of of your regex pattern. You can then access the entire match, or any of the groups individually')
# Useful when you want to deal with different parts of a match separately

regex = '\\b([A-Z]{4}) ([12]{1}\d{3})-(\d{2})\\b'   # A general MCTC class code matcher - 4 uppercase letters, space, 1 or 2, 3 numbers, dash, 2 numbers; match on word boundaries

test1 = 'At MCTC there is a class ENGL 1000-80'
test2 = 'In the ITEC dept, ITEC 1100-01 is Infotech Concepts'

match = re.search(regex, test1)
print(match)
if match:
    print('Matches in groups ', match.groups())
    for group in match.groups():
        print(group)

match = re.search(regex, test2)
print(match)
if match:
    print('Matches in groups ', match.groups())
    print('The entire matched string is ', match.group())  # No argument: returns entire match
    print('The department matched is ', match.group(1))
    print('The class code matched is ', match.group(2))
    print('The section number matched is ', match.group(3))
    for group in match.groups():
        print(group)


#### Named groups
print('Named groups are similar, but as well as accessing matches by number, can access by name.')
# Similar to above, but easier to manage multiple groups

regex = '\\b(?P<department>[A-Z]{4}) (?P<code>[12]{1}\d{3})-(?P<section>\d{2})\\b'   # A general MCTC class code matcher - 4 uppercase letters, space, 1 or 2, 3 numbers, dash, 2 numbers; match on word boundaries

test1 = 'At MCTC there is a class ENGL 1000-80'
test2 = 'In the ITEC dept, ITEC 1100-01 is Infotech Concepts'

match = re.search(regex, test1)
print(match)
if match:
    print('Matches in groups ', match.groups())
    # Now can get the matched text by group name
    print('The department matched is ', match.group('department'))
    print('The class code matched is ', match.group('code'))
    print('The section number matched is ', match.group('section'))
    # Can still get entire match, or the groups by number
    print('The entire matched string is ', match.group())  # No argument: returns entire match
    print('The department matched is ', match.group(1))
    print('The class code matched is ', match.group(2))
    print('The section number matched is ', match.group(3))



# Much more regex can do. Read the docs. Groups are really useful, lookbehind and lookahead, and various other things
