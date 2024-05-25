from main import get_empty_data

def test_get_empty_data():
    lines = ['PassengerId,Survived,Pclass',
             '1,'',3',
             '1,'',''']
    assert get_empty_data(lines[2]) == (0,0)