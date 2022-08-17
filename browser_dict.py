import sys

from definitions import *

# Important: 
# 1. If the text starts with '$' then 
#    the text should only be written to 
#    the 'words' file. 
# 2. If the text starts with '%' then
#    the text should only be translated
#    and not added to the words file.

text = ' '.join(sys.argv[1:])

# Only write to 'words'
if text[0] == '$':
    writeText(text)
elif text[0] == '%': # Only open the dictionaries 
    openDicts(text)
else:
    writeText(text)
    openDicts(text)
