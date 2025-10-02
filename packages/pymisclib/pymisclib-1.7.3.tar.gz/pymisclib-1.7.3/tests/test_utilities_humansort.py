#!/usr/bin/env python3
# vim: fileencoding=utf-8 ts=4
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: © Copyright 2025 by Christian Dönges. All rights reserved.
# SPDXID: SPDXRef-test-utilities-humansort-py

import pytest

from pymisclib.utilities import humansort


def test_a():
    input = ['12abc', '12aaa', 'aaa', '12', '11zzz', 'AAA', '12AAA']
    output = humansort(input)
    assert output == ['11zzz', '12', '12AAA', '12aaa', '12abc', 'AAA', 'aaa']


@pytest.mark.parametrize(
    'name,input,expected',
    [('empty', [], []),
     ('numeric-positive-integer',
      ['300', '10', '200', '3', '20', '100', '2', '30', '1'],
      ['1', '2', '3', '10', '20', '30', '100', '200', '300']),
     ('numeric-negative-integer',
      ['-300', '10', '200', '3', '-20', '100', '-2', '30', '1', '0'],
      ['-300', '-20', '-2', '0', '1', '3', '10', '30', '100', '200']),
     ('numeric-float',
      ['0.0', '-1.5', '5.39', '5.32', '5.3', '-10.5', '-11.2', '123.45'],
      ['-11.2', '-10.5', '-1.5', '0.0', '5.3', '5.32', '5.39', '123.45']),
     ('numeric-float and numeric-integer',
      ['0', '-1.5', '5.39', '-1', '5.32', '5.3', '6', '-10.5', '-11.2', '123.45'],
      ['-11.2', '-10.5', '-1.5', '-1', '0', '5.3', '5.32', '5.39', '6', '123.45']),
     ('zero-int and zero-float',
      ['0.000', '0', '0.0', '0.00'],
      ['0.000', '0', '0.0', '0.00']),
     ('alpha',
      ['zzz', 'foo', 'bar', 'baz', 'a', 'A', 'ZZ'],
      ['A', 'ZZ', 'a', 'bar', 'baz', 'foo', 'zzz']),
     ('unicode',
      ['ए', 'ऐ', 'ऍ', 'ĭ', 'äöü', 'ॐ', 'ÄöÜ', 'Äöü', 'Ĭ', 'ZZ'],
      ['ZZ', 'ÄöÜ', 'Äöü', 'äöü', 'Ĭ', 'ĭ', 'ऍ', 'ए', 'ऐ', 'ॐ']),
     ('alpha and integer',
      ['zzz', '100', 'foo', 'bar', '10', 'baz', 'a', '1', 'A', 'ZZ'],
      ['1', '10', '100', 'A', 'ZZ', 'a', 'bar', 'baz', 'foo', 'zzz']),
     ('alpha and float',
      ['zzz', '-100', 'foo', 'bar', '10.2', '10.3', 'baz', 'a', '1', 'A', 'ZZ'],
      ['-100', '1', '10.2', '10.3', 'A', 'ZZ', 'a', 'bar', 'baz', 'foo', 'zzz']),
     ('alpha+integer',
      ['baz', 'bar', 'bar0', 'foo10', 'foo3', 'bar10', 'BAR', 'bAr1', 'bar1', 'bar-5'],
      ['BAR', 'bAr1', 'bar', 'bar-5', 'bar0', 'bar1', 'bar10', 'baz', 'foo3', 'foo10']),
     ('alpha+float',
      ['baz', 'bar', 'bar0.0', 'bar-5.5', 'BAR4.0', 'bar10', 'bar10.7', 'bar-5.3'],
      ['BAR4.0', 'bar', 'bar-5.5', 'bar-5.3', 'bar0.0', 'bar10', 'bar10.7', 'baz']),
     ('alpha+integer and integer',
      ['baz', 'bar', 'foo300', 'foo10', 'foo3', '12', '5', 'bar10', 'bar1'],
      ['5', '12', 'bar', 'bar1', 'bar10', 'baz', 'foo3', 'foo10', 'foo300']),
     ('alpha+integer and float',
      ['baz', 'bar', '-1.5', '0.0', '12.9', '12.1', '12.0', 'bar10', 'bar1'],
      ['-1.5', '0.0', '12.0', '12.1', '12.9', 'bar', 'bar1', 'bar10', 'baz']),
     ('alpha+float and float',
      ['bar', '-1.5', '0.0', '12.9', '12.1', 'bar10.5', 'BAR10.4', 'bar10.0', 'bar11.2'],
      ['-1.5', '0.0', '12.1', '12.9', 'BAR10.4', 'bar', 'bar10.0', 'bar10.5', 'bar11.2']),
     ('integer+alpha and integer and alpha',
      ['12abc', '12aaa', 'aaa', '12', '11zzz', 'AAA', '12AAA'],
      ['11zzz', '12', '12AAA', '12aaa', '12abc', 'AAA', 'aaa']),
     ('everything',
      ['Z', 'z', '1.0', '-5', '2z', '1z', 'Z2.1', 'Z1', 'Z2', '1a2', '1a1',
       '1a2b2', '1a2b1', '1a1b1', 'z1', 'z1a'],
      ['-5', '1.0', '1a1', '1a1b1', '1a2', '1a2b1', '1a2b2', '1z', '2z', 'Z',
       'Z1', 'Z2', 'Z2.1', 'z', 'z1', 'z1a']),
     ])
def test_humansort(name: str, input: list[str], expected: list[str]):
    """Test human-sorting of strings."""
    output = humansort(input)
    assert output == expected


@pytest.mark.parametrize(
    'name,input,expected',
    [('alpha',
      ['zzz', 'foo', 'bar', 'baz', 'a', 'A', 'ZZ'],
      ['a', 'A', 'bar', 'baz', 'foo', 'ZZ', 'zzz']),
     ('unicode',
      ['ए', 'ऐ', 'ऍ', 'ĭ', 'äöü', 'ॐ', 'ÄöÜ', 'Äöü', 'Ĭ', 'ZZ'],
      ['ZZ', 'äöü', 'ÄöÜ', 'Äöü', 'ĭ', 'Ĭ', 'ऍ', 'ए', 'ऐ', 'ॐ']),
     ('alpha and integer',
      ['zzz', '100', 'foo', 'bar', '10', 'baz', 'a', '1', 'A', 'ZZ'],
      ['1', '10', '100', 'a', 'A', 'bar', 'baz', 'foo', 'ZZ', 'zzz']),
     ('alpha and float',
      ['zzz', '-100', 'foo', 'bar', '10.2', '10.3', 'baz', 'a', '1', 'A', 'ZZ'],
      ['-100', '1', '10.2', '10.3', 'a', 'A', 'bar', 'baz', 'foo', 'ZZ', 'zzz']),
     ('alpha+integer',
      ['baz', 'bar', 'bar0', 'foo10', 'foo3', 'bar10', 'BAR', 'bAr1', 'bar1', 'bar-5'],
      ['bar', 'BAR', 'bar-5', 'bar0', 'bAr1', 'bar1', 'bar10', 'baz', 'foo3', 'foo10']),
     ('alpha+float',
      ['baz', 'bar', 'bar0.0', 'bar-5.5', 'BAR4.0', 'bar10', 'bar10.7', 'bar-5.3'],
      ['bar', 'bar-5.5', 'bar-5.3', 'bar0.0', 'BAR4.0', 'bar10', 'bar10.7', 'baz']),
     ('alpha+float and float',
      ['bar', '-1.5', '0.0', '12.9', '12.1', 'bar10.5', 'BAR10.4', 'bar10.0', 'bar11.2'],
      ['-1.5', '0.0', '12.1', '12.9', 'bar', 'bar10.0', 'BAR10.4', 'bar10.5', 'bar11.2']),
     ('integer+alpha and integer and alpha',
      ['12abc', '12aaa', 'aaa', '12', '11zzz', 'AAA', '12AAA'],
      ['11zzz', '12', '12aaa', '12AAA', '12abc', 'aaa', 'AAA']),
     ('integer+alpha and integer and alpha',
      ['12abc', '12AAA', 'AAA', '12', '11zzz', 'aaa', '12aaa'],
      ['11zzz', '12', '12AAA', '12aaa', '12abc', 'AAA', 'aaa']),
     ('everything',
      ['Z', 'z', '1.0', '-5', '2z', '1z', 'Z2.1', 'Z1', 'Z2', '1a2', '1a1',
       '1a2b2', '1a2b1', '1a1b1', 'z1', 'z1a'],
      ['-5', '1.0', '1a1', '1a1b1', '1a2', '1a2b1', '1a2b2', '1z', '2z',
       'Z', 'z', 'Z1', 'z1', 'z1a', 'Z2', 'Z2.1']),
    ])
def test_humansort_ignore_case(name: str, input: list[str], expected: list[str]):
    """Test human-sorting of case-insensitive strings."""
    output = humansort(input, ignore_case=True)
    assert output == expected
