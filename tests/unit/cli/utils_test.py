from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

from compose.cli.utils import human_readable_file_size
from compose.utils import unquote_path


class UnquotePathTest(unittest.TestCase):
    def test_no_quotes(self):
        assert unquote_path('hello') == 'hello'

    def test_simple_quotes(self):
        assert unquote_path('"hello"') == 'hello'

    def test_uneven_quotes(self):
        assert unquote_path('"hello') == '"hello'
        assert unquote_path('hello"') == 'hello"'

    def test_nested_quotes(self):
        assert unquote_path('""hello""') == '"hello"'
        assert unquote_path('"hel"lo"') == 'hel"lo'
        assert unquote_path('"hello""') == 'hello"'


class HumanReadableFileSizeTest(unittest.TestCase):
    def test_100b(self):
        assert human_readable_file_size(100) == '100 B'

    def test_1kb(self):
        assert human_readable_file_size(1024) == '1 kB'

    def test_1023b(self):
        assert human_readable_file_size(1023) == '1023 B'

    def test_units(self):
        assert human_readable_file_size((2 ** 10) ** 0) == '1 B'
        assert human_readable_file_size((2 ** 10) ** 1) == '1 kB'
        assert human_readable_file_size((2 ** 10) ** 2) == '1 MB'
        assert human_readable_file_size((2 ** 10) ** 3) == '1 GB'
        assert human_readable_file_size((2 ** 10) ** 4) == '1 TB'
        assert human_readable_file_size((2 ** 10) ** 5) == '1 PB'
        assert human_readable_file_size((2 ** 10) ** 6) == '1 EB'
