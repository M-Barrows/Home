---
title: How To Create a Random Pairing Generator For Your Secret Holiday Gift Exchange - Python Edition!
layout: post
date: '2022-12-06'
excerpt: "How to create a script that will randomly pair individuals for gift giving this holiday season"
excerpt_separator:  <!--more-->
tags: 
    - Python
    - Automate The Boring Things
    - Holiday
    - Quick Reads

categories: 
    - Tutorial
---

A couple of years ago I [created a gift exchange randomizer in R](https://M-Barrows.github.io/Home/tutorial/2020/11/03/Creating-A-Random-Secret-Santa-Generator.html). Check out that article if you want more background on the goal and methods behind this tool. However, since it's been a couple of years and I'm now writing the majority of my work in Python, I thought it might be a good time for a refreshed attempt. 

My goal with this version was to keep it as close to stock Python as possible to make it as portable as possible for anyone stumbling across this post. After I was finished I was shocked that the Python version was over twice as long and subjectively far less readable than the R version. That said, I don't think this python version is horrendous. If I was willing to use external libraries I could likely increase the readability. Conversely, if I were to sacrifice readability and logging, I could likely trim a lot of the extra code from this version. 

All said and done - this is a fun little exercise and maybe next year I'll tackle it in a new language. 

You can find the code below or [here](https://gist.github.com/M-Barrows/f8357a7e88b5ac1d286964b0485713f4) on my GitHub.

Happy gifting and until next time! 🙋‍♂️📈



[GitHub](https://github.com/M-Barrows) | [Mastodon](https://hachyderm.io/@CodeAndCoffee) | [LinkedIn](www.linkedin.com/in/michaelabarrows)


``` python
example_input = {
    'familyA':[
        'A_person1',
        'A_person2',
        'A_person3',
        'A_person4',
        'A_person5'
    ],
    'familyB':[
        'B_person6',
        'B_person7'
    ],
    'familyC':[
        'C_person8',
        'C_person9',
        'C_person10',
        'C_person11'
    ],
    'familyD':[
        'D_person12'
    ]
}

# ^^^ Example input Family ^^^
# ---------------------------
# vvv Executable Code vvv

import random
import logging

def get_giftee_options(family_structure:dict,current_family:str,output:dict)->list:
    """Returns the giftees who are not in the same family that don't have an assigned gifter yet"""

    options = []
    for family, people in family_structure.items():
        if family is not current_family: 
            for person in people: 
                if person not in output.get('Giftees'):
                    options.append(person)
    return options

def assign_pairings(family_structure:dict) -> dict:
    """
    Select a random giftee for each gifter. Ensure the pair are not in the same family. 

    example: 
    >>> family_structure = {
        'familyA':[
            'A_p1',
            'A_p2',
        ],
        'familyB:[
            'B_p3',
            'B_p4'
        ]

    >>> assign_pairings(family_structure)
    {
        'Gifters': ['A_p1','A_p2','B_p3','B_p4'], 
        'Giftees':['B_p3','B_p4','A_p1','A_p2']
    }
    """
    output = {
        'Gifters':[],
        'Giftees':[]
    }
    for family,people in family_structure.items():
        for person in people:
            output.get('Gifters').append(person)
            try: 
                output.get('Giftees').append(random.choice(get_giftee_options(family_structure,family,output)))
            except IndexError:
                logging.warning('Could not generate even pairings. Re-running...')
    return output

def print_pairings(output:dict) -> None:
    """ 
    Prints pairings in a human-readable format

    example: 
    >>> print_pairings({'Gifters': ['P1','P2','P3'], 'Giftees':['P2','P3','P1']})
    P1 gives to P2
    P2 gives to P3
    P3 gives to P1
    """
    pairings = list()
    for i,x in enumerate(output.get('Gifters')):
        pairings.append((x,output.get('Giftees')[i]))
    print('\n🔀 Matches Generated! 🔀\n')
    for pairing in pairings:
        print(f'{" gives to ".join(pairing)}')
    print('\n🎁 Happy Gifting! 🎁')
    print('Tool developed with ❤ by https://github.com/M-Barrows')

if __name__ == '__main__': 
    output = assign_pairings(example_input)
    while len(output.get('Giftees')) != len(output.get('Gifters')):
        output = assign_pairings(example_input)
    print_pairings(output)

```