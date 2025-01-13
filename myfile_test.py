import pytest
from myfile import myFunction

class TestMyFunction:
    def test_odd_array(self, capsys):
        arr = [1,2,3]
        output = myFunction(arr)

        assert output == 6

    def test_even_array(self, capsys):
        arr = [1,2,3,4]
        output = myFunction(arr)

        assert output == 1


