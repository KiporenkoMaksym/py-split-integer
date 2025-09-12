from app.split_integer import split_integer
import pytest


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10,\
    "Sum of the parts should be equal to 10"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3), \
    "Parts should be equal when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10], \
    "Parts should return equals to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(13, 3)), \
    "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 5)
    assert result.count(0) > 0, \
    "Zeros should be when value is less than number of parts"