"""
    update_pip.py

    Created by everpuck on 2018/05/18
    Copyright (c) 2018 EVER. All rights reserved
"""


import json
import subprocess


def run():
    ''' upgrade pip packages '''

    ret = subprocess.run('pip list -o --format=json', stdout=subprocess.PIPE, encoding='utf-8')
    pickage_list = json.loads(str(ret.stdout).strip())
    
    if not pickage_list:
        print('all package are up to date')
        return

    for _p in pickage_list:
        subprocess.run('pip install --upgrade ' + _p.get('name'), shell=True)


if __name__ == '__main__':
    run()
