from main import get_empty_data

def test_get_empty_data():
    lines = ['1,2,3',
             '1,'',3',
             '1,'',''']
    assert get_empty_data(lines) == (0,0)