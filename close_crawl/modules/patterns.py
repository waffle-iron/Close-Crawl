#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Patterns


TODO:
    Finish docs

"""


from re import compile as re_compile
from string import punctuation

street_address = re_compile(
    '(\d{1,4} [\w\s]{1,20}'
    '(?:st(reet)?|ln|lane|ave(nue)?|r(?:oa)?d'
    '|highway|hwy|sq(uare)?|tr(?:ai)l|dr(?:ive)?'
    '|c(?:our)?t|parkway|pkwy|cir(cle)?'
    '|boulevard|blvd|pl(?:ace)?|(apt|unit).[A-Z]{1}|'
    'ter(?:race)?)\W?(?=\s|$))', 2)

punctuation = punctuation.replace('#', '')

# case insensitive delimiter for Titles
TITLE_SPLIT_PAT = re_compile(" vs ", 2)

# pattern for Baltimore zip codes
ZIP_PAT = re_compile("2\d{4}")

# regex pattern to capture monetary values between $0.00 and $999,999,999.99
# punctuation insensitive
MONEY_PAT = re_compile('\$\d{,3},?\d{,3},?\d{,3}\.?\d{2}')

MONEY_STR = '\$\d{,3},?\d{,3},?\d{,3}\.?\d{2}'

NULL_ADDR = re_compile(
    '^('
    '(' + MONEY_STR + ')|'
    '(2\d{4})|'
    '(\d+)|'
    '(2\d{4}.*' + MONEY_STR + ')'
    ')$', 2)

STRIP_ADDR = re_compile('(balto|2\d{4}|md|' + MONEY_STR + ').*', 2)


def filter_addr(address):

    try:
        return ''.join(
            street_address.search(
                address.translate(None, punctuation)).group(0)
        )

    except AttributeError:
        return ''
