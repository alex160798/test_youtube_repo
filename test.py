print('Hello world!')

import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Вычисляем, является ли число палиндромом
        '''
        return str(x) == str(x)[::-1]

@pytest.mark.parametrize("input_value, expected", [
    (123, False),
    (111, True),
    (2222, True),
])

def test_palindrome(input_value, expected):
    sol = Solution()
    assert sol.isPalindrome(input_value) is expected
