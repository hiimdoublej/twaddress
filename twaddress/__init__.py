# -*- coding: utf-8 -*-

name = "twaddress"


from twaddress import algo
from slugify import slugify
import re


def _to_eng(cut_result):
    code, city, road, village, address = cut_result

    result = [road, village, '%s %s' % (city, code), 'Taiwan (R.O.C.)']
    if address['巷']:
        result.insert(0, 'Ln. ' + address['巷'])
    if address['弄']:
        result.insert(0, 'Aly. ' + address['弄'])
    if address['號']:
        result.insert(0, 'No.' + address['號'])
    if address['樓']:
        result.insert(0, address['樓'])
    if address['室']:
        result.insert(0, address['室'])

    result_str = ', '.join(filter(lambda x: x, result))
    # replace remaining chinese chars
    pattern = '[\u4E00-\u9FA5]+'
    match = re.findall(pattern, result_str)
    print(f"match={match}")
    for m in match:
        result_str = result_str.replace(m, slugify(m,separator=' ', lowercase=False))
    return result_str
    


def get(address):
    return _to_eng(cut(address))


def cut(address):
    return algo.mms_cut(address)
