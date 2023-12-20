import pytest
from check_post import get_post
import yaml

# id_check = 93349
title_check = 'rr'


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['title'])
        print(item)
    assert title_check in res