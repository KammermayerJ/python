#!/usr/bin/env python3
import pytest
import birthnumber as bn

def test_convert_year():
    assert bn.convert_year(91) == 1991
    assert bn.convert_year(1) == 2001

def test_valid_num():
    assert bn.valid_num('785205/7554')
    assert not bn.valid_num('485205/7554')

def test_get_data():
    assert bn.get_data('785205/7554') == (1978, 52, 5, 7554)
    assert bn.get_data('780205/7554') == (1978, 2, 5, 7554)
