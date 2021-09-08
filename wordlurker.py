#!/usr/bin/python3.8

import requests
from bs4 import BeautifulSoup
from colorama import Style as Style2
from sty import RgbFg, Style, fg
import subprocess
import datetime
import platform
import re as re2
import time
from stem import Signal
from stem.control import Controller     

#qlqlq#

date = datetime.datetime.now()
date = date.strftime('%d/%m/%Y')

### URLS ###

lingueeEngspan = 'https://www.linguee.com/english-spanish/search?source=auto&query='
lingueeFrEng = 'https://www.linguee.com/french-english/search?source=auto&query='
lingueePortSpan = 'https://www.linguee.com/portuguese-spanish/search?source=auto&query='

baidu = 'https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb='




### COLORS ###

fg.brown = Style(RgbFg(229, 183, 59))
fg.blue = Style(RgbFg(115, 194, 251))
fg.darkb = Style(RgbFg(3, 80, 150))
fg.purp = Style(RgbFg(154, 0, 154))

re = Style2.RESET_ALL
red = "\033[31;1m" 
black = "\033[30;1m"
yellow = "\033[33;1m" 
green = "\033[32;1m"
bgreen = "\033[32m"


###### PROMPTS #########

prompt = f"{black}[{re}{red}wOrd{re}{fg.brown}lUrkEr{re}{black}]>>>{re}"

chiEng = f"{red}<ch{re}-{fg.blue}eng>{re}"
portSpan = f"{bgreen}<port{re}-{yellow}span>{re}"
portSpan2 = f"{bgreen}<port>{re}"
freng = f"{fg.darkb}<fr{re}-{fg.blue}eng>{re}"
freng2 = f"{fg.darkb}<fr>{re}"
engSpa = f"{fg.blue}<eng{re}-{yellow}span{re}"
multi = f"{fg.blue}<Multi{re}-{red}Lang>{re}"

####### NB PROMPTS ##########

chiNB = f"{red}<ch{re}-{fg.blue}eng>{re}{black}[{re}{red}n0te{re}{fg.blue}b00k{re}{black}]>>>{re}"

portnbp = f"{bgreen}<port{re}-{yellow}span>{re}{black}[{re}{bgreen}n0te{re}{yellow}b00k{re}{black}]>>>{re}"

frnbp = f"{fg.darkb}<fr{re}-{fg.blue}eng>{re}{black}[{re}{fg.darkb}n0te{re}{fg.blue}b00k{re}{black}]>>>{re}"

inv = f"{yellow}[{red}INVALID INPUT{yellow}]{re}"

###################### cachepaths #####################################################

pos = platform.node()

if pos == 'ballstr0m':

    print(f"{green}[SESSION STARTED ON {pos}]{re}\n")
    chcachepath = "/home/eduardo/Desktop/stuff/studies/0rganiz4tion/subjects/langs/offline/chineseOff/"

    frcachepath = "/home/eduardo/Desktop/stuff/studies/0rganiz4tion/subjects/langs/offline/frenchOff/"

    portcachepath = "/home/eduardo/Desktop/stuff/studies/0rganiz4tion/subjects/langs/offline/portugueseOff/"

    chnbpath = '~/Desktop/stuff/studies/0rganiz4tion/subjects/langs/chinese.txt'

    portnbpath = '~/Desktop/stuff/studies/0rganiz4tion/subjects/langs/portu.txt'

    frnbpath = '~/Desktop/stuff/studies/0rganiz4tion/subjects/langs/francais.txt'




elif pos == 'localhost':

    print(f"{green}[SESSION STARTED ON {pos}]{re}\n")
    chcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/chineseOff/"

    frcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/frenchOff/"

    portcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/portugueseOff/"

    chnbpath = '~/priv/0rganiz4tion/subjects/langs/chinese.txt'

    portnbpath = '~/priv/0rganiz4tion/subjects/langs/portu.txt'

    frnbpath = '~/priv/0rganiz4tion/subjects/langs/francais.txt'

elif pos == 'S3liny':

    print(f"{green}[SESSION STARTED ON {pos}]{re}\n")
    chcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/chineseOff/"

    frcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/frenchOff/"

    portcachepath = "~/priv/0rganiz4tion/subjects/langs/offline/portugueseOff/"


elif pos == 'parrot':

    print(f"{green} [SESSION STARTED ON {pos}]{re}\n")
    chcachepath = "/home/edd1e/stuff/0rganiz4tion/subjects/langs/offline/chineseOff/"

    frcachepath = "/home/edd1e/stuff/0rganiz4tion/subjects/langs/offline/frenchOff/"


    portcachepath = "/home/edd1e/stuff/0rganiz4tion/subjects/langs/offline/portugueseOff/"

    chnbpath = '/home/edd1e/stuff/0rganiz4tion/subjects/langs/chinese.txt'

    portnbpath = '/home/edd1e/stuff/0rganiz4tion/subjects/langs/portu.txt'

    frnbpath = '/home/edd1e/stuff/0rganiz4tion/subjects/langs/francais.txt'

elif pos == 'S3liny':
    print(f"{green} [SESSION STARTED ON {pos}]{re}\n")



else:
    print(f"{red}[HOST {pos} NOT REGISTERED]{re}\n")

#############################################################################################################







help1 = f"""
{red}wOrd{re}{fg.brown}lUrkEr{re}, the multi-language word definition/translation finder lil' machine !

Usage: {prompt} <Options>

Options:

select <param>  Select language pair

clear           Clears the screen

exit            Exits wordlurker

help            Shows this message

conj            Prompts to verb conjugation

cache           Prompts to cached word search

back            Go back to previous module

nb              Selects virtual n0teb00k

phelp           Shows pages available for search

Positional arguments for lang-pairs:

a               Prompts to page directory access

{fg.purp}tor{re}            Changes tor circuit


LANGUAGE PAIRS:

eng-span >>>> {fg.blue}English{re}-{yellow}Spanish{re}

fr-eng >>>> {fg.darkb}French{re}-{fg.blue}English{re}

port-span >>>> {bgreen}Portuguese{re}-{yellow}Spanish{re}

ch-eng >>>>> {red}Chinese{re}-{fg.blue}English{re}

"""

help2 = f"""

MODULE: [n0teb00k]>>>

Usage: [n0teb00k]>>> <Options>

Options:

clear           Clears the screen

exit            Exits wordlurker

help            Shows this message

back            Go back to previous module

phelp           Shows pages available for search

w               Prompts for sentence writing

c               Displays notebook 

g               Prompts for word grepping

adds            adds banner

"""

pageshelp = f"""
[LIST OF {green}AVAILABLE{re} {yellow}PAGES{re}]

1 ====== https://www.mdbg.net/  --> {chiEng}

2 ====== https://www.trainchinese.com/ --> {chiEng}

3 ====== https://www.linguee.com/   --> {multi}

4 ====== https://www.dicio.com.br/  --> {portSpan2}

5 ====== https://www.larousse.fr/dictionnaires/francais/ --> {freng2}

6 ====== https://resources.allsetlearning.com/ --> {red}<ch>{re}


"""


############### INIT FUNCTION #########################

def func():
    try:
        active1 = True
        mOptions = ['exit', 'clear', 'help', 'select', 'phelp', 'tor']
        lang = ['eng-span', 'fr-eng', 'port-span', 'ch-eng']

        while active1:
            getput = input(f"{prompt}")
            if getput == mOptions[2]:
                print(help1)

            elif getput == mOptions[4]:
                print(pageshelp)

            elif getput == mOptions[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            elif getput == f"{mOptions[3]} {lang[0]}":
                engspan()

            elif getput == f"{mOptions[3]} {lang[1]}":
                frnEng()
                
            elif getput == f"{mOptions[3]} {lang[2]}":
                portSp()

            elif getput == f"{mOptions[3]} {lang[3]}":
                chEng()

            elif getput == f"{mOptions[5]}":
                tor1()
            elif getput == f"{mOptions[5]} {mOptions[6]}":
                torcheck()

            else:
                print(f"{inv}\n\n")
            

    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
    
    except IndexError:  
        print(f"{red}[INDEX ERROR]{re}\n")
        func()

############### LANG-PAIRS ###############################

def engspan():
    try:
        
        pages = ['1', '2', '3']
        mOptions = ['exit', 'clear', 'help', 'phelp', 'back', 'cache']
        exit1 = True
        while exit1:
            getput = input(f"{engSpa}{prompt}")

            if getput == pages[2]:
                global session
                session = requests.session()
                iter1 = True
                while iter1:
                    iput2 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{engSpa}{prompt}")
                    
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':
                
                            global lingueeEngspan

                            if switch == True:

                                r = session.get(f'{lingueeEngspan}{iput2}', proxies=proxies)

                            elif switch == False:

                                r = session.get(f'{lingueeEngspan}{iput2}')


                            soup = BeautifulSoup(r.text, 'html.parser')

                            word = "You have sent too many requests causing Linguee to block your computer"
                            p1 = r"\b(?=\w)" + re2.escape(word) + r"\b(?!\w)"
                            r12 = re2.search(p1, soup.text)
                            if r12:
                                print(f"{red}[IP HAS BEEN BLOCKED]{re}\n\n{green}Trying to change IP...{re}\n")
                                time.sleep(5)
                                with Controller.from_port(port = 9051) as c:
                                    c.authenticate()
                                    c.signal(Signal.NEWNYM)
                                    session = requests.session()
                                ippa = re2.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
                                r1 = session.get('http://httpbin.org/ip', proxies=proxies)
                                ip1 = ippa.findall(r1.text)
                                print(f"Your IP is now {green}{ip1}{re}\n")
                        
                            else:
                                pass

                            #### FOREIGN MODE ####
                            for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                                for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                    for div2 in thing.find_all( 'div', { 'class': 'isForeignTerm', 'data-source-lang': 'ES' } ):
                                        for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                            for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                                for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                    for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                        for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                            print(f"{yellow}{a1.text}{re}")
                                                            for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                                print(f"{trans.text}\n")

                            #### MAIN MODE ####
                            for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                                for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                    for div2 in thing.find_all( 'div', { 'class': 'isMainTerm', 'data-source-lang': 'EN' } ):
                                        for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                            for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                                for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                    for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                        for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                            print(f"{yellow}{a1.text}{re}")
                                                            for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                                print(f"{trans.text}\n")

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False


            elif getput == mOptions[3]:
                print(pageshelp)

            elif getput == mOptions[4]:
                exit1 = False
                func()

            elif getput == mOptions[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions[2]:
                print(help1)

            elif getput == mOptions[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv} make sure you selected a page for this module, see {yellow}help{re}\n")


    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        engspan()

    except IndexError:
        print(f"{red}[INDEX ERROR]{re}\n")
        engspan()

def frnEng():
    try:
        pages = ['3', '5']
        mOptions = ['exit', 'clear', 'help', 'phelp', 'back', 'conj', 'nb', 'cache']
        global freng
        exit1 = True
        while exit1:
            getput = input(f"{freng}{prompt}")

            if getput == pages[0]:
                global session
                session = requests.session()
                iter1 = True
                while iter1:
                    iput2 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{freng}{prompt}")
                    
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':

                        if switch == True:

                            r = session.get(f'{lingueeFrEng}{iput2}', proxies=proxies)

                        elif switch == False:
                        
                            r = session.get(f'{lingueeFrEng}{iput2}')


                        soup = BeautifulSoup(r.text, 'html.parser')

                        word = "You have sent too many requests causing Linguee to block your computer"
                        p1 = r"\b(?=\w)" + re2.escape(word) + r"\b(?!\w)"
                        r12 = re2.search(p1, soup.text)
                        if r12:
                            print(f"{red}[IP HAS BEEN BLOCKED]{re}\n\n{green}Trying to change IP...{re}\n")
                            time.sleep(5)
                            with Controller.from_port(port = 9051) as c:
                                c.authenticate()
                                c.signal(Signal.NEWNYM)
                                session = requests.session()
                            ippa = re2.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
                            r1 = session.get('http://httpbin.org/ip', proxies=proxies)
                            ip1 = ippa.findall(r1.text)
                            print(f"Your IP is now {green}{ip1}{re}\n")
                        
                        else:
                            pass

                        #### FOREIGN MODE ####
                        for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                            for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                for div2 in thing.find_all( 'div', { 'class': 'isForeignTerm', 'data-source-lang': 'FR' } ):
                                    for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                        for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                            for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                    for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                        print(f"{yellow}{a1.text}{re}")
                                                        for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                            print(f"{trans.text}\n")

              
                        #### MAIN MODE ####
                        for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                            for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                for div2 in thing.find_all( 'div', { 'class': 'isMainTerm', 'data-source-lang': 'EN' } ):
                                    for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                        for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                            for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                    for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                        print(f"{yellow}{a1.text}{re}")
                                                        for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                            print(f"{trans.text}\n")


                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False

            elif getput == pages[1]:
                iter1 = True    
                while iter1:
                    iput2 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{freng2}{prompt}")
                   
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':
                
                        if switch == True:


                            r = requests.get(f'https://www.larousse.fr/dictionnaires/francais/{iput2}', proxies=proxies)

                        elif switch == False:

                            r = requests.get(f'https://www.larousse.fr/dictionnaires/francais/{iput2}')


                        #\ue82c

                        soup = BeautifulSoup(r.text, 'html.parser')

                        header = []
                        for div1 in soup.find_all( 'div', { 'class': 'row' } ):
                            for div2 in div1.find_all( 'div', { 'class': 'header-article' } ):
                                for h1 in div2.find_all( 'h2', { 'class': 'AdresseDefinition' } ):
                                    header = h1.text.replace('\ue82c', '')
                                    print(f"{yellow}{header}{re}")
                                for cat in div2.find_all( 'p', { 'CatgramDefinition' } ):
                                    print(f"{yellow}{cat.text}{re}\n")
                                    for def1 in div1.find_all( 'div', { 'id': 'definition' } ):
                                        for header2 in def1.find_all( 'h1', { 'class': 'TitrePage' } ):
                                            print(f"{green}{header2.text}{re}\n")
                                            for contE in def1.find_all( 'ul', { 'class': 'Definitions' } ):
                                                for cont in contE.find_all( 'li', { 'class': 'DivisionDefinition' } ):
                                                    print(f"{cont.text}\n")

                            for peut in div1.find_all( 'aside', { 'class': 'zone-listresult' } ):
                                for banner in peut.find_all( 'div', { 'class': 'banner-title' } ):
                                    print(f"{yellow}{banner.text}{re}\n")
                                for contp in peut.find_all( 'nav', { 'class': 'search' } ):
                                    for hs1 in contp.find_all( 'article', { 'class': 'sel' } ):
                                        for hs in hs1.find_all('h3'):
                                            print(f"{yellow}{hs.text}{re}")
                                    for contpr in hs1.find_all( 'p', { 'class': 'def' } ):
                                        print(f"{contpr.text}")
                                    for example in contp.find_all( 'article', { 'class': 'sous-article' } ):
                                        print(f"\n{green}{example.text}{re}")
                                    
                                    
                                    




                                    



                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False



            elif getput == mOptions[5]:

                iter1 = True
                while iter1:

                    iput2 = input(f"[{yellow}ENTER{re} THE VERB YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{freng2}{prompt}")
                    
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':

                        if switch == True:

                            r = requests.get(f'https://en.bab.la/conjugation/french/{iput2}', proxies=proxies)

                        elif switch == False:

                            r = requests.get(f'https://en.bab.la/conjugation/french/{iput2}')


                        soup = BeautifulSoup(r.text, 'html.parser')

                        for cont1 in soup.find_all( 'div', { 'class': 'conj-tense-wrapper' } ):
                            for h1 in cont1.find_all( 'div', { 'class': 'conj-block container result-block' } ):
                                print(f"\n{green}[[[[{h1.text}]]]]{re}")
                                for tense in cont1.find_all( 'div', { 'class': 'conj-tense-block' } ):
                                    for h2 in tense.find_all( 'h3', { 'class': 'conj-tense-block-header' } ):
                                        print(f"\n{yellow}{h2.text}{re}\n")
                                        for cont2 in tense.find_all( 'div', { 'class': 'conj-item' } ):
                                            for pron in cont2.find_all( 'div', { 'class': 'conj-person' } ):
                                                for verb1 in cont2.find_all( 'div', { 'class': 'conj-result' } ):
                                                    print(f"{pron.text} {verb1.text}")




                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False



            elif getput == mOptions[3]:
                print(pageshelp)


            elif getput == mOptions[7]:
                iter1 = True
                while iter1:

                    iput4 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{freng}{prompt}")

                    if iput4 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput4 != '#e':

                        p6 = subprocess.run(f'cat {frcachepath}{iput4}', stderr=subprocess.PIPE, shell=True)
                        p6er = p6.stderr
                        if p6er:
                            print(f"{red}[WORD NOT FOUND]{re}\n\n")

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False


            elif getput == mOptions[6]:
                frnb()


            elif getput == mOptions[4]:
                exit1 = False
                func()

            elif getput == mOptions[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions[2]:
                print(help1)

            elif getput == mOptions[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv} make sure you selected a page for this module, see {yellow}help{re}\n")

    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        frnEng()

    except IndexError:
        print(f"{red}[INDEX ERROR]{re}\n")
        frnEng()

def portSp():
    try:
        pages = ['1', '2', '3', '4', '7']
        mOptions = ['exit', 'clear', 'help', 'phelp', 'back', 'conj', 'nb', 'cache']
        
        global portSpan
        exit1 = True
        while exit1:
            getput = input(f"{portSpan}{prompt}")

            if getput == pages[2]:
                global session
                session = requests.session()
                iter1 = True
                while iter1:

                    iput2 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{portSpan}{prompt}")
                   
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':
                
                            if switch == True:

                                r = session.get(f'{lingueePortSpan}{iput2}', proxies=proxies)

                            elif switch == False:

                                r = session.get(f'{lingueePortSpan}{iput2}')

                            soup = BeautifulSoup(r.text, 'html.parser')
                            word = "You have sent too many requests causing Linguee to block your computer"
                            p1 = r"\b(?=\w)" + re2.escape(word) + r"\b(?!\w)"
                            r12 = re2.search(p1, soup.text)
                            if r12:
                                print(f"{red}[IP HAS BEEN BLOCKED]{re}\n\n{green}Trying to change IP...{re}\n")
                                time.sleep(5)
                                with Controller.from_port(port = 9051) as c:
                                    c.authenticate()
                                    c.signal(Signal.NEWNYM)
                                    session = requests.session()
                                ippa = re2.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
                                r1 = session.get('http://httpbin.org/ip', proxies=proxies)
                                ip1 = ippa.findall(r1.text)
                                print(f"Your IP is now {green}{ip1}{re}\n")
                        
                            else:
                                pass


                            portSpan = f"{yellow}<span{re}-{bgreen}port>{re}"

                            #### FOREIGN MODE ####
                            for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                                for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                    for div2 in thing.find_all( 'div', { 'class': 'isForeignTerm', 'data-source-lang': 'ES' } ):
                                        for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                            for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                                for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                    for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                        for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):

                                                            print(f"{yellow}{a1.text}{re}  {cont.text}\n")

                            #### MAIN MODE ####
                            for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                                for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                    for div2 in thing.find_all( 'div', { 'class': 'isMainTerm', 'data-source-lang': 'PT' } ):
                                        for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                            for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                                for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                    for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                        for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):

                                                            print(f"{yellow}{a1.text}{re}  {cont.text}\n")


                                    

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False


            elif getput == mOptions[6]:
                portnb()


            elif getput == pages[3]:
                session = requests.session()
                iter1 = True
                while iter1:

                    iput2 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{portSpan2}{prompt}")
                    
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':

                            if switch == True:

                                r = requests.get(f'https://www.dicio.com.br/{iput2}/', proxies=proxies)

                            elif switch == False:

                                r = requests.get(f'https://www.dicio.com.br/{iput2}/')


                            soup = BeautifulSoup(r.text, 'html.parser')


                            for div1 in soup.find_all( 'div', { 'id': 'wrapper' } ):
                                for div2 in div1.find_all( 'div', { 'class': 'container' } ):
                                    for div3 in div2.find_all( 'div', { 'id': 'content', 'class': 'row', 'data-sticky-container':'' } ):
                                        for div4 in div3.find_all( 'div', { 'class': 'col-xs-12 col-sm-7 col-md-8 parent-card' }):
                                            for div5 in div4.find_all( 'div', { 'class': 'card' } ):
                                                for h in div5.find_all( 'h1', { 'itemprop': 'name' } ):
                                                    print(f"{yellow}{h.text}{re}\n")
                                                    for p in div5.find_all( 'p', { 'class': 'significado textonovo', 'itemprop': 'description' } ):   
                                                        for span in p.find_all('span'):
                                                            print(f"{span.text}\n")

                            for div1 in soup.find_all( 'div', { 'id': 'wrapper' } ):
                                for div2 in div1.find_all( 'div', { 'class': 'container' } ):
                                    for div3 in div2.find_all( 'div', { 'id': 'content', 'class': 'row', 'data-sticky-container':'' } ):
                                        for div4 in div3.find_all( 'div', { 'class': 'col-xs-12 col-sm-7 col-md-8 parent-card' }):
                                            for div5 in div4.find_all( 'div', { 'class': 'card' } ):
                                                for h in div5.find_all( 'h1', { 'itemprop': 'name' } ):
                                                    for p in div5.find_all( 'p', { 'class': 'significado texto', 'itemprop': 'description' } ):   
                                                        for h3 in div4.find_all( 'h2', { 'class': 'tit-significado' } ):
                                                            for p2 in div4.find_all( 'p', { 'class': 'adicional' } ):
                                                                print(f"{yellow}{h3.text.strip()}{re}\n")
                                                                print(p2.text.strip())


                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False




                        
            elif getput == mOptions[5]:
                session = requests.session()
                iter1 = True
                while iter1:

                    iput2 = input(f"[{yellow}ENTER{re} THE VERB YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{portSpan2}{prompt}")
                    
                    if iput2 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput2 != '#e':

                        if switch == True:

                            r = requests.get(f'https://en.bab.la/conjugation/portuguese/{iput2}', proxies=proxies)

                        elif switch == False:

                            r = requests.get(f'https://en.bab.la/conjugation/portuguese/{iput2}')

                        soup = BeautifulSoup(r.text, 'html.parser')

                        for cont1 in soup.find_all( 'div', { 'class': 'conj-tense-wrapper' } ):
                            for h1 in cont1.find_all( 'div', { 'class': 'conj-block container result-block' } ):
                                print(f"\n{green}[[[[{h1.text}]]]]{re}")
                                for tense in cont1.find_all( 'div', { 'class': 'conj-tense-block' } ):
                                    for h2 in tense.find_all( 'h3', { 'class': 'conj-tense-block-header' } ):
                                        print(f"\n{yellow}{h2.text}{re}\n")
                                        for cont2 in tense.find_all( 'div', { 'class': 'conj-item' } ):
                                            for pron in cont2.find_all( 'div', { 'class': 'conj-person' } ):
                                                for verb1 in cont2.find_all( 'div', { 'class': 'conj-result' } ):
                                                    print(f"{pron.text} {verb1.text}")




                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False

                            


            elif getput == mOptions[7]:
                iter1 = True
                while iter1:

                    iput4 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{portSpan}{prompt}")

                    if iput4 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput4 != '#e':

                        p6 = subprocess.run(f'cat {portcachepath}{iput4}', stderr=subprocess.PIPE, shell=True)
                        p6er = p6.stderr
                        if p6er:
                            print(f"{red}[WORD NOT FOUND]{re}\n\n")

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False


            elif getput == mOptions[3]:
                print(pageshelp)

            elif getput == mOptions[4]:
                exit1 = False
                func()

            elif getput == mOptions[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions[2]:
                print(help1)

            elif getput == mOptions[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv} make sure you selected a page for this module, see {yellow}help{re}\n")

    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        portSp()

    except IndexError:
        print(f"{red}[INDEX ERROR]{re}\n")
        portSp()

def chEng():
    try:
        pages = ['1', '2', '3', '6']
        mOptions = ['exit', 'clear', 'help', 'phelp', 'back', 'nb', 'cache']
        args = ['a']
        exit1 = True

        while exit1:
            getput = input(f"{chiEng}{prompt}")

            if getput == pages[0]:
                global session
                session = requests.session()
                iter1 = True
                while iter1:

                    iput3 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")
            
                    if iput3 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput3 != '#e':

                        if switch == True:

                            r = session.get(f'{baidu}{iput3}', proxies=proxies)

                        elif switch == False:

                            r = session.get(f'{baidu}{iput3}')


                        soup = BeautifulSoup(r.text, 'html.parser')


                        for cell in soup.find_all( 'table', { 'cellspacing': '0', 'cellpadding': '0', 'border': '0' } ):
                            for tbody in cell.find_all( 'td', { 'class': 'resultswrap' } ):
                                for table in tbody.find_all( 'table', { 'class': 'wordresults'} ):
                                    for tbody2 in table.find_all('tbody'):
                                        for row in tbody2.find_all( 'tr', { 'class': 'row'} ):
                                            for head in row.find_all( 'td', { 'class': 'head' }):
                                                for det in row.find_all( 'td', { 'class': 'details' } ):
                                                    print(f"{yellow}{head.text}{re}   {det.text}")
                                                    print("\n")
                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False

                                        

            elif getput == pages[1]:
                session = requests.session()
                iter1 = True
                while iter1:

                    iput4 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")

                    if iput4 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput4 != '#e':
        
                        if switch == True:

                            r = session.get(f'https://www.trainchinese.com/v2/search.php?searchWord={iput4}&rAp=0&height=0&width=0&tcLanguage=en', proxies=proxies)

                        elif switch == False:

                            r = session.get(f'https://www.trainchinese.com/v2/search.php?searchWord={iput4}&rAp=0&height=0&width=0&tcLanguage=en')

                        soup = BeautifulSoup(r.text, 'html.parser')
                        
                        ### MAIN SEARCH ###
                        for div1 in soup.find_all( 'div', { 'class': 'container' } ):
                            for div2 in div1.find_all( 'div', { 'class': 'row' } ):
                                for div3 in div2.find_all( 'div', { 'class': 'col-md-10 col-md-offset-1' }) :
                                    for div4 in div3.find_all( 'div', { 'id': 'srch' } ):
                                        for div5 in div4.find_all( 'table', { 'class': 'table table-hover'} ):
                                            for tr in div5.find_all('tr'):
                                                for tr2 in tr.find_all( 'div', { 'class': 'leadXXL chinese' } ):
                                                    for tr3 in tr.find_all( 'span', { 'class': 'pinyin' } ):
                                                        for tr4 in tr.find_all( 'span', { 'style': 'color:#0066FF' } ):
                                                            print(f"{yellow}{tr2.text}{re}   {tr3.text} ->{tr4.text}\n")
                                                            




                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False

            elif getput == pages[2]:
                session = requests.session()
                iter1 = True
                while iter1:

                    iput4 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")

                    if iput4 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput4 != '#e':
        
                        if switch == True:

                            r = session.get(f'https://www.linguee.com/chinese-english/search?source=auto&query={iput4}', proxies=proxies)

                        elif switch == False:

                            r = session.get(f'https://www.linguee.com/chinese-english/search?source=auto&query={iput4}')


                        soup = BeautifulSoup(r.text, 'html.parser')

                    #### FOREIGN MODE ####
                        for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                            for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                for div2 in thing.find_all( 'div', { 'class': 'isForeignTerm', 'data-source-lang': 'ZH' } ):
                                    for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                        for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                            for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                    for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                        print(f"{yellow}{a1.text}{re}")
                                                        for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                            print(f"{trans.text}\n")
                                                        

                        #### MAIN MODE ####
                        for div in soup.find_all( 'div', { 'class': 'innercontent'} ):
                            for thing in div.find_all('div', { 'id': 'dictionary'} ):
                                for div2 in thing.find_all( 'div', { 'class': 'isMainTerm', 'data-source-lang': 'EN' } ):
                                    for div3 in div2.find_all( 'div', { 'class': 'exact' } ):
                                        for lemma in div3.find_all( 'div', { 'class': 'lemma featured' } ):
                                            for lemma2 in lemma.find_all( 'h2', { 'class': 'line lemma_desc' } ):
                                                for a1 in lemma2.find_all( 'a', { 'class': 'dictLink' } ):
                                                    for cont in lemma.find_all( 'div', { 'class': 'lemma_content' } ):
                                                        print(f"{yellow}{a1.text}{re}")
                                                        for trans in cont.find_all( 'div', { 'class': 'translation sortablemg featured' } ):
                                                            print(f"{trans.text}\n")
                        
                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False
            


            elif getput == mOptions[6]:
                iter1 = True
                while iter1:

                    iput4 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re} FOR](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")

                    if iput4 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput4 != '#e':

                        p6 = subprocess.run(f'cat {chcachepath}{iput4}', stderr=subprocess.PIPE, shell=True)
                        p6er = p6.stderr
                        if p6er:
                            print(f"{red}[WORD NOT FOUND]{re}\n\n")

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False
                        

################### MANAGING ALLSETLEARNING.COM ###############################

            elif getput == pages[3]:
            
                iter1 = True
                while iter1:

                    iput3 = input(f"[{yellow}ENTER{re} THE KEYWORD YOU WISH TO {green}SEARCH{re}](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")
            
                    if iput3 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput3 != '#e':

                        r = requests.get(f'https://resources.allsetlearning.com/gramwiki/?search={iput3}&title=Special%3ASearch&profile=default&fulltext=1')

                        soup = BeautifulSoup(r.text, 'html.parser')

                        for div1 in soup.find_all( 'ul', { 'class': 'mw-search-results' } ):
                            for li1 in div1.find_all( 'li', { 'class': 'mw-search-result' } ):
                                for head in li1.find_all( 'div', { 'class': 'mw-search-result-heading' } ):
                                    print(f"{yellow}{head.text}{re}\n")
                                for cont in li1.find_all( 'div', { 'class': 'searchresult' } ):
                                    print(f"{cont.text}")
                                    link = head.find_all('a')[0]
                                    print(f"\n{green}{link}{re}\n")

                    
                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False


################### ACCESSING A SPECIFIC PAGE IN ALLSETLEARNING.COM ##########################

            elif getput == f"{pages[3]} {args[0]}":
                iter1 = True
                while iter1:

                    iput3 = input(f"[{yellow}ENTER{re} THE PAGE URL YOU WISH TO {green}ACCESS{re}](enter {red}#e{re} to exit)\n\n{chiEng}{prompt}")
            
                    if iput3 == '#c':
                        p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p1x = p1.stdout
                        print(p1x)

                    elif iput3 != '#e':

                        r = requests.get(f'https://resources.allsetlearning.com/{iput3}')

                        soup = BeautifulSoup(r.text, 'html.parser')

                        for div1 in soup.find_all( 'div', { 'class': 'offset1 span10' } ):
                            for head1 in div1.find_all( 'div', { 'class': 'allset-page-heading' } ):
                                print(f"{yellow}{head1.text}{re}\n")
                            for mcont in div1.find_all( 'div', { 'class': 'mw-parser-output' } ):
                                p0 = mcont.find_all('p')[0].text
                                print(p0)
                                for dl1 in mcont.find_all('dl'):
                                    print(f"{bgreen}{dl1.text}{re}\n")

                                for head2 in mcont.find_all('h2')[1]:
                                    print(f"{yellow}{head2.text}{re}")
                                for cont in mcont.find_all('p')[1:]:
                                    print(cont.text)
                                

                    else:
                        print(f"{green}[DONE SEARCHING]{re}\n")
                        iter1 = False



            #########   IF NOTEBOOK IS BEING CALLED OUT   (NOTEBOOK INITIATES) ###########

            elif getput == mOptions[5]:
                chn0t()

            ##############################################################


            elif getput == mOptions[3]:
                print(pageshelp)

            elif getput == mOptions[4]:
                exit1 = False
                func()

            elif getput == mOptions[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions[2]:
                print(help1)

            elif getput == mOptions[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv} make sure you selected a page for this module, see {yellow}help{re}\n")

    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        chEng()

    except IndexError:  
        print(f"{red}[INDEX ERROR]{re}\n")
        chEng()


################## TOR HANDLING ########################

def checktor():
    try:
        global proxies
        global switch
        p12 = subprocess.run(f'curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p12s = p12.stdout
        p12s = p12s.decode()
        p12s = str(p12s)
        ippa = re2.compile(r'Congratulations')
        ip1 = ippa.findall(p12s)
        if ip1:
            print(f"{green}[NICE] Tor is enabled...{re}\n")
            proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
            }    
            switch = True       

        else:
            print(f"{red}[HMM] Tor is not enabled...{re}\n")
            switch = False
            

    except Exception as f:
        print(f)


def tor1():
    try:

        print(f"{green}[Changing TOR circuit...]{re}\n")
        time.sleep(3)
        with Controller.from_port(port = 9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
            session = requests.session()
        ippa = re2.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
        r1 = session.get('http://httpbin.org/ip', proxies=proxies)
        ip1 = ippa.findall(r1.text)
        print(f"Your IP is now {green}{ip1}{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")

    except Exception as g:
        print(g)


################# N0TEB00KS ################################

def chn0t():
    try:
        mOptions2 = ['exit', 'clear', 'help', 'phelp', 'back', 'w', 'c', 'g', 'adds']
        iter1 = True
        while iter1:
            getput = input(f"{chiNB}")
            if getput == mOptions2[3]:
                print(pageshelp)

            elif getput == mOptions2[4]:
                iter1 = False
                chEng()

            elif getput == mOptions2[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions2[2]:
                print(help2)

            elif getput == mOptions2[8]:
                subjects = ['1', '2', '3']
                l1 = "_" * 50
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} THE SUBJECT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{green}1)Grammar{re}\n{fg.blue}2)Vocabulary{re}\n{red}3)Class{re}\n\n{chiNB}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                    
                    elif p1 == subjects[1]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {fg.blue}VOCABULARY SECTION{re} [[{yellow}{date}{re}]]\n\" >> {chnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

    
                    elif p1 == subjects[0]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {green}GRAMMAR SECTION{re} [[{yellow}{date}{re}]]\n\" >> {chnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

                    elif p1 == subjects[2]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {red}CLASS SECTION{re} [[{yellow}{date}{re}]]\n\" >> {chnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {chnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")




                    elif p1 == "#e":
                        print(f"{green}[DONE BANNERING AROUND !]{re}\n")
                        iter2 = False
                    

            elif getput == mOptions2[5]:
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} WHAT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{chiNB}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif p1 != "#e":


                        word1 = p1.split(' ', 1)[0]
                        word2 = p1.split(' ', 1)[1]
                        p1 = f"{yellow}{word1}{re} {word2}"
                        p2 = subprocess.run(f'echo \"{p1}\n\" >> {chnbpath}', shell=True)
                        print(f"{green}[ACTION COMPLETED]{re}\n\n")



                    else:
                        print(f"{red}[SESSION TERMINATED]{re}\n\n")
                        iter2 = False



            elif getput == mOptions2[6]:
                print(f"[BEGINING OF {yellow}LIST{re}]\n")
                p3 = subprocess.run(f'cat {chnbpath}', shell=True)
                print(f"\n[END OF {yellow}LIST{re}]")

            elif getput == mOptions2[7]:
                iter3 = True
                while iter3:

                    iput5 = input(f"[ENTER THE {yellow}KEYWORD{re} YOU WISH TO LOOK FOR](enter {red}#e{re} to {red}exit{re})\n\n{chiNB}")

                    if iput5 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif iput5 != "#e":
                        
                        p4 = subprocess.run(f'grep -i --color \"{iput5}\" {chnbpath}', stdout=subprocess.PIPE, shell=True)
                        p4 = p4.stdout
                        print(f"{p4.decode()}\n")

                    else:
                        print(f"{red}[SESSION TERMINATED]{red}\n")
                        iter3 = False


            


            elif getput == mOptions2[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv}\n\n")


    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        chEng()

    except IndexError:
        print(f"{red}[LIST INDEX OUT OF RANGE]{re}\n")
        chn0t()

def portnb():

    try:
        mOptions2 = ['exit', 'clear', 'help', 'phelp', 'back', 'w', 'c', 'g', 'adds']
        iter1 = True
        while iter1:
            getput = input(f"{portnbp}")
            if getput == mOptions2[3]:
                print(pageshelp)

            elif getput == mOptions2[4]:
                iter1 = False
                portSp()

            elif getput == mOptions2[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions2[2]:
                print(help2)

            elif getput == mOptions2[8]:
                subjects = ['1', '2', '3']
                l1 = "_" * 50
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} THE SUBJECT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{green}1)Grammar{re}\n{fg.blue}2)Vocabulary{re}\n{red}3)Class{re}\n\n{portnbp}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                    
                    elif p1 == subjects[1]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {fg.blue}VOCABULARY SECTION{re} [[{yellow}{date}{re}]]\n\" >> {portnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

    
                    elif p1 == subjects[0]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {green}GRAMMAR SECTION{re} [[{yellow}{date}{re}]]\n\" >> {portnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

                    elif p1 == subjects[2]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {red}CLASS SECTION{re} [[{yellow}{date}{re}]]\n\" >> {portnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {portnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")




                    elif p1 == "#e":
                        print(f"{green}[DONE BANNERING AROUND !]{re}\n")
                        iter2 = False
                    

            elif getput == mOptions2[5]:
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} WHAT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{portnbp}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif p1 != "#e":


                        word1 = p1.split(' ', 1)[0]
                        word2 = p1.split(' ', 1)[1]
                        p1 = f"{yellow}{word1}{re} {word2}"
                        p2 = subprocess.run(f'echo \"{p1}\n\" >> {portnbpath}', shell=True)
                        print(f"{green}[ACTION COMPLETED]{re}\n\n")



                    else:
                        print(f"{red}[SESSION TERMINATED]{re}\n\n")
                        iter2 = False



            elif getput == mOptions2[6]:
                print(f"[BEGINING OF {yellow}LIST{re}]\n")
                p3 = subprocess.run(f'cat {portnbpath}', shell=True)
                print(f"\n[END OF {yellow}LIST{re}]")

            elif getput == mOptions2[7]:
                iter3 = True
                while iter3:

                    iput5 = input(f"[ENTER THE {yellow}KEYWORD{re} YOU WISH TO LOOK FOR](enter {red}#e{re} to {red}exit{re})\n\n{portnbp}")

                    if iput5 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif iput5 != "#e":
                        
                        p4 = subprocess.run(f'grep -i --color \"{iput5}\" {portnbpath}', stdout=subprocess.PIPE, shell=True)
                        p4 = p4.stdout
                        print(f"{p4.decode()}\n")

                    else:
                        print(f"{red}[SESSION TERMINATED]{red}\n")
                        iter3 = False


            


            elif getput == mOptions2[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv}\n\n")


    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        portnb()

    except IndexError:
        print(f"{red}[LIST INDEX OUT OF RANGE]{re}\n")
        portnb()

def frnb():
    try:
        mOptions2 = ['exit', 'clear', 'help', 'phelp', 'back', 'w', 'c', 'g', 'adds']
        iter1 = True
        while iter1:
            getput = input(f"{frnbp}")
            if getput == mOptions2[3]:
                print(pageshelp)

            elif getput == mOptions2[4]:
                iter1 = False
                frnEng()

            elif getput == mOptions2[1]:
                p1 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                p1x = p1.stdout
                print(p1x)

            elif getput == mOptions2[2]:
                print(help2)

            elif getput == mOptions2[8]:
                subjects = ['1', '2', '3']
                l1 = "_" * 50
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} THE SUBJECT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{green}1)Grammar{re}\n{fg.blue}2)Vocabulary{re}\n{red}3)Class{re}\n\n{frnbp}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                    
                    elif p1 == subjects[1]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {fg.blue}VOCABULARY SECTION{re} [[{yellow}{date}{re}]]\n\" >> {frnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

    
                    elif p1 == subjects[0]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {green}GRAMMAR SECTION{re} [[{yellow}{date}{re}]]\n\" >> {frnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")

                    elif p1 == subjects[2]:

                        p9 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)

                        p10 = subprocess.run(f'echo \"\n            {red}CLASS SECTION{re} [[{yellow}{date}{re}]]\n\" >> {frnbpath}', shell=True)

                        p11 = subprocess.run(f'echo \"\n{l1}\n\n\" >> {frnbpath}', shell=True)
                        iter2 = False
                        print(f"{green}[DONE]{re}\n")




                    elif p1 == "#e":
                        print(f"{green}[DONE BANNERING AROUND !]{re}\n")
                        iter2 = False
                    

            elif getput == mOptions2[5]:
                iter2 = True
                while iter2:

                    p1 = input(f"[{yellow}ENTER{re} WHAT YOU WISH TO WRITE] (Enter {red}#e{re} to {red}exit{re})\n\n{frnbp}")

                    if p1 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif p1 != "#e":


                        word1 = p1.split(' ', 1)[0]
                        word2 = p1.split(' ', 1)[1]
                        p1 = f"{yellow}{word1}{re} {word2}"
                        p2 = subprocess.run(f'echo \"{p1}\n\" >> {frnbpath}', shell=True)
                        print(f"{green}[ACTION COMPLETED]{re}\n\n")



                    else:
                        print(f"{red}[SESSION TERMINATED]{re}\n\n")
                        iter2 = False



            elif getput == mOptions2[6]:
                print(f"[BEGINING OF {yellow}LIST{re}]\n")
                p3 = subprocess.run(f'cat {frnbpath}', shell=True)
                print(f"\n[END OF {yellow}LIST{re}]")

            elif getput == mOptions2[7]:
                iter3 = True
                while iter3:

                    iput5 = input(f"[ENTER THE {yellow}KEYWORD{re} YOU WISH TO LOOK FOR](enter {red}#e{re} to {red}exit{re})\n\n{frnbp}")

                    if iput5 == "#c":


                        p4 = subprocess.run(['clear'], stdout=subprocess.PIPE, text=True)
                        p4x = p4.stdout
                        print(p4x)
                        

                    elif iput5 != "#e":
                        
                        p4 = subprocess.run(f'grep -i --color \"{iput5}\" {frnbpath}', stdout=subprocess.PIPE, shell=True)
                        p4 = p4.stdout
                        print(f"{p4.decode()}\n")

                    else:
                        print(f"{red}[SESSION TERMINATED]{red}\n")
                        iter3 = False


            


            elif getput == mOptions2[0]:
                print(f"[{yellow}STAY {red}F0CUSED{re}]\n\n")
                exit()

            else:
                print(f"{inv}\n\n")


    except KeyboardInterrupt:
        print(f"{red}[SESSION TERMINATED]{re}\n")
        exit()

    except EOFError:
        print(f"{red}[SESSION TERMINATED]{re}\n")

    except IOError:
        print(f"{red}[CONNECTION ERROR]{re}\n")
        frnb()

    except IndexError:
        print(f"{red}[LIST INDEX OUT OF RANGE]{re}\n")
        frnb()


if __name__ == "__main__":
    checktor()
    func()
