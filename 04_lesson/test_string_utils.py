import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# --- Тесты для метода capitalize ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("test123", "Test123"),
])
def test_capitalize_positive(input_str, expected):
    """Позитивные тесты: обычные строки с буквами."""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("123abc", "123abc"),
    ("!!!", "!!!"),
    ("  test", "  test"),  # пробелы в начале — capitalize не убирает
])
def test_capitalize_negative(input_str, expected):
    """Негативные тесты: пустые, пробельные, нечисловые/небуквенные строки."""
    assert string_utils.capitalize(input_str) == expected


# --- Тесты для метода trim ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    (" test ", "test "),
    ("a", "a"),
    ("   a   ", "a   "),
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты: строки с пробелами в начале."""
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("no_spaces", "no_spaces"),
    ("   ", ""),
    ("\tstart", "\tstart"),  # табуляция — не пробел, не удаляется
    ("\nnewline", "\nnewline"),  # перевод строки — не пробел
])
def test_trim_negative(input_str, expected):
    """Негативные тесты: без пробелов, только пробелы, спецсимволы."""
    assert string_utils.trim(input_str) == expected


# --- Тесты для метода contains ---
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Hello", "e", True),
    ("Python", "o", True),
    ("Test", "T", True),
    ("abc", "c", True),
])
def test_contains_positive(string, symbol, expected):
    """Позитивные тесты: символ точно есть в строке."""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("Hello", "z", False),
    ("", "a", False),
    ("test", "", False),  # пустой символ
    ("123", "x", False),
])
def test_contains_negative(string, symbol, expected):
    """Негативные тесты: символа нет, пустая строка, пустой символ."""
    assert string_utils.contains(string, symbol) == expected


# --- Тесты для метода delete_symbol ---
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello", "l", "Heo"),
    ("Python", "th", "Pyon"),
    ("Test123", "123", "Test"),
    ("aaa", "a", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные тесты: удаление существующих подстрок."""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # символа нет
    ("", "a", ""),  # пустая строка
    ("test", "", "test"),  # пустой символ — ничего не удаляем
    ("123", "abc", "123"),  # подстроки нет
    ("   ", " ", ""),  # удаление всех пробелов
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные тесты: символ отсутствует, пустые строки/символы."""
    assert string_utils.delete_symbol(string, symbol) == expected
