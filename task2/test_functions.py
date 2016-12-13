import code_nonp as code

def test_reading_fromfile():
    expected_age = [33, 44, 21, 66, 47, 31, 22, 51]
    expected_dogs = [4, 0, 1, 0, 1, 2, 0, 2]
    assert code.reading_fromfile("pets_data.txt") == (expected_age, expected_dogs)

def test_dogowners_average_age():
    age = [11, 45, 21, 19]
    dogs = [1, 2, 0, 1]
    expected_age_av = 25
    assert code.dogowners_average_age(age, dogs) == expected_age_av

def test_average_owners_age_fordogs():
    age = [11, 45, 21, 19]
    dogs = [1, 2, 0, 1]
    expected_age_av = 30
    assert code.average_owners_age_fordogs(age, dogs) == expected_age_av

