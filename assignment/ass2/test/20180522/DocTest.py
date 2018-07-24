


# Made By Jian Gao 2018/05/22
from frieze import *
def test_is_frieze_1():

    '''

    >>> f = Frieze('incorrect_input(less than 17 lines).txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input(greater than 51 rows).txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input(less than 3 lines).txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input(less than 5 rows).txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input_1.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input_2.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input_3.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('incorrect_input_4.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Incorrect input.
    >>> f = Frieze('not_a_frieze(N less 2)1.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze(N less 2)2.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze(right and left row different).txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_1.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_2.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_3.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_4.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_5.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_6.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_a_frieze_7.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('not_fully_repeated.txt')
    Traceback (most recent call last):
    ...
    frieze.FriezeError: Input does not represent a frieze.
    >>> f = Frieze('frieze_1.txt');f.analyse();f.display();
    Pattern is a frieze of period 15 that is invariant under translation only.
    >>> f = Frieze('frieze_2.txt');f.analyse();f.display()
    Pattern is a frieze of period 12 that is invariant under translation
            and vertical reflection only.
    >>> f = Frieze('frieze_3.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('frieze_4.txt');f.analyse();f.display()
    Pattern is a frieze of period 6 that is invariant under translation
            and glided horizontal reflection only.
    >>> f = Frieze('frieze_5.txt');f.analyse();f.display()
    Pattern is a frieze of period 8 that is invariant under translation
            and rotation only.
    >>> f = Frieze('frieze_6.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation,
            glided horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('frieze_7.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('test_frieze_1.txt');f.analyse();f.display()
    Pattern is a frieze of period 6 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('test_frieze_2.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation
            and vertical reflection only.
    >>> f = Frieze('test_frieze_3.txt');f.analyse();f.display()
    Pattern is a frieze of period 2 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('test_frieze_4.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation
            and rotation only.
    >>> f = Frieze('test_frieze_5.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('test_frieze_6.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and rotation only.
    >>> f = Frieze('test_frieze_7.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('test_frieze_8.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation
            and glided horizontal reflection only.
    >>> f = Frieze('2018050701.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and vertical reflection only.
    >>> f = Frieze('2018050702.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018050703.txt');f.analyse();f.display()
    Pattern is a frieze of period 10 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018050704.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation only.
    >>> f = Frieze('2018050705.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018050706.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018050801.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018050802.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018051001.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051101.txt');f.analyse();f.display()
    Pattern is a frieze of period 6 that is invariant under translation,
            glided horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051102.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018051103.txt');f.analyse();f.display()
    Pattern is a frieze of period 6 that is invariant under translation,
            glided horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051104.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation only.
    >>> f = Frieze('2018051105.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051106.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation,
            horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051201.txt');f.analyse();f.display()
    Pattern is a frieze of period 9 that is invariant under translation only.
    >>> f = Frieze('2018051202.txt');f.analyse();f.display()
    Pattern is a frieze of period 9 that is invariant under translation
            and horizontal reflection only.
    >>> f = Frieze('2018051301.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation,
            glided horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051302.txt');f.analyse();f.display()
    Pattern is a frieze of period 5 that is invariant under translation
            and rotation only.
    >>> f = Frieze('2018051303.txt');f.analyse();f.display()
    Pattern is a frieze of period 25 that is invariant under translation
            and vertical reflection only.
    >>> f = Frieze('2018051304.txt');f.analyse();f.display()
    Pattern is a frieze of period 25 that is invariant under translation
            and vertical reflection only.
    >>> f = Frieze('2018051401.txt');f.analyse();f.display()
    Pattern is a frieze of period 10 that is invariant under translation,
            glided horizontal and vertical reflections, and rotation only.
    >>> f = Frieze('2018051402.txt');f.analyse();f.display()
    Pattern is a frieze of period 19 that is invariant under translation
            and rotation only.
    >>> f = Frieze('2018051601.txt');f.analyse();f.display()
    Pattern is a frieze of period 24 that is invariant under translation only.
    >>> f = Frieze('2018051701.txt');f.analyse();f.display()
    Pattern is a frieze of period 8 that is invariant under translation only.
    >>> f = Frieze('2018051801.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation
            and rotation only.
    >>> f = Frieze('2018051802.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation
            and glided horizontal reflection only.
    >>> f = Frieze('2018051803.txt');f.analyse();f.display()
    Pattern is a frieze of period 4 that is invariant under translation only.
    >>> f = Frieze('linan.txt');f.analyse();f.display()
    Pattern is a frieze of period 3 that is invariant under translation only.
    >>> f = Frieze('linan_2.txt');f.display();f.analyse();
    Pattern is a frieze of period 6 that is invariant under translation
            and rotation only.
    >>> compare_two_files('frieze_1.tex','frieze_1.Author.tex')
    >>> compare_two_files('frieze_2.tex','frieze_2.Author.tex')
    >>> compare_two_files('frieze_3.tex','frieze_3.Author.tex')
    >>> compare_two_files('frieze_4.tex','frieze_4.Author.tex')
    >>> compare_two_files('frieze_5.tex','frieze_5.Author.tex')
    >>> compare_two_files('frieze_6.tex','frieze_6.Author.tex')
    >>> compare_two_files('frieze_7.tex','frieze_7.Author.tex')
    >>> compare_two_files('test_frieze_1.tex','test_frieze_1.Author.tex')
    >>> compare_two_files('test_frieze_2.tex','test_frieze_2.Author.tex')
    >>> compare_two_files('test_frieze_3.tex','test_frieze_3.Author.tex')
    >>> compare_two_files('test_frieze_4.tex','test_frieze_4.Author.tex')
    >>> compare_two_files('test_frieze_5.tex','test_frieze_5.Author.tex')
    >>> compare_two_files('test_frieze_6.tex','test_frieze_6.Author.tex')
    >>> compare_two_files('test_frieze_7.tex','test_frieze_7.Author.tex')
    >>> compare_two_files('test_frieze_8.tex','test_frieze_8.Author.tex')
    >>> compare_two_files('2018050701.tex','2018050701.Author.tex')
    >>> compare_two_files('2018050702.tex','2018050702.Author.tex')
    >>> compare_two_files('2018050703.tex','2018050703.Author.tex')
    >>> compare_two_files('2018050704.tex','2018050704.Author.tex')
    >>> compare_two_files('2018050705.tex','2018050705.Author.tex')
    >>> compare_two_files('2018050706.tex','2018050706.Author.tex')
    >>> compare_two_files('2018050801.tex','2018050801.Author.tex')
    >>> compare_two_files('2018050802.tex','2018050802.Author.tex')
    >>> compare_two_files('2018051001.tex','2018051001.Author.tex')
    >>> compare_two_files('2018051101.tex','2018051101.Author.tex')
    >>> compare_two_files('2018051102.tex','2018051102.Author.tex')
    >>> compare_two_files('2018051103.tex','2018051103.Author.tex')
    >>> compare_two_files('2018051104.tex','2018051104.Author.tex')
    >>> compare_two_files('2018051105.tex','2018051105.Author.tex')
    >>> compare_two_files('2018051106.tex','2018051106.Author.tex')
    >>> compare_two_files('2018051201.tex','2018051201.Author.tex')
    >>> compare_two_files('2018051202.tex','2018051202.Author.tex')
    >>> compare_two_files('2018051301.tex','2018051301.Author.tex')
    >>> compare_two_files('2018051302.tex','2018051302.Author.tex')
    >>> compare_two_files('2018051303.tex','2018051303.Author.tex')
    >>> compare_two_files('2018051304.tex','2018051304.Author.tex')
    >>> compare_two_files('2018051401.tex','2018051401.Author.tex')
    >>> compare_two_files('2018051402.tex','2018051402.Author.tex')
    >>> compare_two_files('2018051601.tex','2018051601.Author.tex')
    >>> compare_two_files('2018051701.tex','2018051701.Author.tex')
    >>> compare_two_files('2018051801.tex','2018051801.Author.tex')
    >>> compare_two_files('2018051802.tex','2018051802.Author.tex')
    >>> compare_two_files('2018051803.tex','2018051803.Author.tex')
    >>> compare_two_files('linan.tex','linan.Author.tex')
    >>> compare_two_files('linan_2.tex','linan_2.Author.tex')
    '''
    pass

from difflib import ndiff

def compare_two_files(file_1, file_2):
    diff = ndiff(open(file_1).readlines(), open(file_2).readlines())
    diff = [l for l in diff if l.startswith('+ ') or l.startswith('- ')]
    if len(diff):
        print(''.join(diff))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Done!')
