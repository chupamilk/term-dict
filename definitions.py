import os
import webbrowser

def writeText(text):
    file = open(os.path.expanduser("~/Projects/TermDict/words-texts"), 'a') 

    # remove the '$' sign
    if (text[0] == '$'):
        file.write(text[1:] + '\n')
    else:
        file.write(text + '\n')

    file.close()

def openDicts(text):
    # remove '%' sign from text
    if text[0] == '%': text = text[1:]

    deepl = 'https://www.deepl.com/translator' + '#de/en/' + text
    wiktionary = 'https://de.wiktionary.org/wiki/' + text
    duden = 'https://www.duden.de/suchen/dudenonline/' + text
    gt = 'https://translate.google.com/?sl=de&tl=en&text=' + text + '&op=translate'

    webbrowser.open(deepl, new=1)
    webbrowser.open_new_tab(wiktionary)
    webbrowser.open_new_tab(duden)
    webbrowser.open_new_tab(gt) 
