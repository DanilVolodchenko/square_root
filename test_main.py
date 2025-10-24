from typing import Any

import pytest

from main import solve


class TestSolve:
    def test_no_root(self) -> None:
        result = solve(1.0, 0.0, 1.0)

        expected_result = []

        assert result == expected_result, 'Нет корней'

    def test_two_root_mult_1(self) -> None:
        result = solve(1.0, 0.0, -1.0)

        expected_result = [1.0, -1.0]

        assert result == expected_result, 'Два корня кратности 1'

    def test_one_root_mult_2(self) -> None:
        result = solve(1.0, 2.0, 1.0)

        expected_result = [-1.0, -1.0]

        assert result == expected_result, 'Один корень кратности 2'

    def test_a_not_be_zero(self) -> None:
        with pytest.raises(ValueError):
            solve(0.0, 1.0, 1.0), 'Исключение ValueError'

    def test_discriminant_not_be_less_than_epsilon(self) -> None:
        result = solve(1.0, 2.000000001, 1.000000001)

        expected_result = [-1.0000000005, -1.0000000005]

        assert result == expected_result, 'Два корня кратности 1'

    @pytest.mark.parametrize('a, b, c, expected_result', [
        (1, 0, 1, []), (1, 0, -1, [1, -1]), (1, 2, 1, [-1, -1])
    ])
    def test_int_coefficient(self, a: int, b: int, c: int, expected_result: list) -> None:
        result = solve(a, b, c)

        assert result == expected_result, 'Коэффициенты типа int'

    @pytest.mark.parametrize('a, b, c', [
        ('1', '2', '3'), ([1, 2], (1, 2), {1, 2}), (complex(1), {1: 2}, frozenset({1, 2}))
    ])
    def test_any_types_coefficient(self, a: Any, b: Any, c: Any) -> None:
        with pytest.raises(TypeError):
            solve(a, b, c), 'Коэффициенты неправильного типа'
