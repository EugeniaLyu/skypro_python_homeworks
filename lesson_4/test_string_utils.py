import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('string, result', [('евгения', 'Евгения'), ('улица, аптека, фонарь', 'Улица, аптека, фонарь'), ('', ''), (' ', ' ')])
def test_capitilize_positive(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result


@pytest.mark.xfail
def test_capitilize_negative1():
    string_utils = StringUtils()
    res = string_utils.capitilize('анна-Мария')
    assert res == 'Анна-Мария'


@pytest.mark.xfail
def test_capitilize_negative2():
    string_utils = StringUtils()
    res = string_utils.capitilize('1406')
    assert res == '1406'


@pytest.mark.xfail
def test_capitilize_negative3():
    string_utils = StringUtils()
    res = string_utils.capitilize(1406)
    assert res == 1406


@pytest.mark.xfail
def test_capitilize_negative4():
    string_utils = StringUtils()
    res = string_utils.capitilize(None)
    assert res == None

@pytest.mark.parametrize('string, result', [('  Евгения', 'Евгения'), ('  1406', '1406'), ('    улица, аптека, фонарь', 'улица, аптека, фонарь'), (' ', '')])
def test_trim_positive(string, result):
       string_utils = StringUtils()
       res = string_utils.trim(string)
       assert res == result


@pytest.mark.xfail
def test_trim_negative1():
    string_utils = StringUtils()
    res = string_utils.trim('')
    assert res == ''


@pytest.mark.xfail
def test_trim_negative2():
    string_utils = StringUtils()
    res = string_utils.trim( 1406)
    assert res ==  1406


@pytest.mark.xfail
def test_trim_negative3():
    string_utils = StringUtils()
    res = string_utils.trim(None)
    assert res == None


@pytest.mark.parametrize('string, delimeter, result', [('', ',', []), ('аптека,улица,фонарь', ',', ["аптека", "улица", "фонарь"]), ('аптека:улица:фонарь', ':', ["аптека", "улица", "фонарь"])])
def test_to_list_positive(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.xfail
def test_to_list_negative1():
    string_utils = StringUtils()
    res = string_utils.to_list(1, 2, 3, 4, 5)
    assert res == [1, 2, 3, 4, 5]


@pytest.mark.xfail
def test_to_list_negative2():
    string_utils = StringUtils()
    res = string_utils.to_list(None)
    assert res == None


# @pytest.mark.parametrize('string, symbols, result', [('Евгения', 'Е', True), ('Евгения', 'Г', False)])
# def test_contains_positive(string, symbol, result):
#     string_utils = StringUtils()
#     res = string_utils.contains(string, symbol)
#     assert res == result

# @pytest.mark.parametrize('string, symbols, result', [('', '', ), (1406, 1), (None, None)])
# def test_contains_negative(string, symbols, result):
#     string_utils = StringUtils()
#     res = string_utils.contains(string, symbols)
#     assert res == result

# @pytest.mark.parametrize('string, symbols, result', [('Евгенyия', 'y', ''Евгения), ('Евгенияния', 'ния', 'Евгения')])
# def test_delete_symbol_positive(string, symbols, result):
    # string_utils = StringUtils()
#     res = string_utils.contains(string, symbols)
#     assert res == result

@pytest.mark.parametrize('string, symbol, result', [('Евгения', 'Е', True), ('Евгения', 'Я', False)])
def test_starts_with_positive(string, symbol, result):
     string_utils = StringUtils()
     res = string_utils.starts_with(string, symbol)
     assert res == result


@pytest.mark.xfail
def test_starts_with_negative1():
    string_utils = StringUtils()
    res = string_utils.starts_with('', '')
    assert res == True


@pytest.mark.xfail
def test_starts_with_negative2():
    string_utils = StringUtils()
    res = string_utils.starts_with(1406, 1)
    assert res == True

    
@pytest.mark.xfail
def test_starts_with_negative3():
    string_utils = StringUtils()
    res = string_utils.starts_with(None)
    assert res == True


@pytest.mark.parametrize('string, symbol, result', [('Евгения', 'я', True), ('Евгения', 'и', False)])
def test_end_with_positive(string, symbol, result):
     string_utils = StringUtils()
     res = string_utils.end_with(string, symbol)
     assert res == result


@pytest.mark.xfail
def test_end_with_negative1():
    string_utils = StringUtils()
    res = string_utils.end_with('', '')
    assert res == True


@pytest.mark.xfail
def test_end_with_negative2():
    string_utils = StringUtils()
    res = string_utils.end_with(1406, 6)
    assert res == True



@pytest.mark.xfail
def test_end_with_negative3():
    string_utils = StringUtils()
    res = string_utils.end_with(None)
    assert res == True


@pytest.mark.parametrize('string, result', [('', True), (' ', True), ('Евгения', False)])
def test_is_empty_positive(string, result):
     string_utils = StringUtils()
     res = string_utils.is_empty(string)
     assert res == result

@pytest.mark.xfail
def test_is_empty_negative1():
    string_utils = StringUtils()
    res = string_utils.is_empty(1406)
    assert res == False


@pytest.mark.xfail
def test_is_empty_negative1():
    string_utils = StringUtils()
    res = string_utils.is_empty(None)
    assert res == True


@pytest.mark.parametrize('lst, joiner, result', [([], ', ', ''), ([1, 2, 3, 4, 5], ', ', '1, 2, 3, 4, 5'), (['аптека', 'улица', 'фонарь'], ', ', 'аптека, улица, фонарь'), (['Анна', 'Мария'], '-', 'Анна-Мария')])
def test_list_to_string_positive(lst, joiner, result):
     string_utils = StringUtils()
     res = string_utils.list_to_string(lst, joiner)
     assert res == result


@pytest.mark.xfail
def test_list_to_string_negative():
    string_utils = StringUtils()
    res = string_utils.list_to_string(None)
    assert res == None
