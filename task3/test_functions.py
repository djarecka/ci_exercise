import code_np as code
import numpy as np

def test_reading_fromfile():
    expected_age = [33, 44, 21, 66, 47, 31, 22, 51]
    expected_dogs = [4, 0, 1, 0, 1, 2, 0, 2]
    assert (code.reading_fromfile("data/pets_data.txt") == np.column_stack((expected_age, expected_dogs))).all()

def test_dogowners_average_age():
    age = [11, 45, 21, 19]
    dogs = [1, 2, 0, 1]
    data_arrays = np.column_stack((age, dogs)) # had to me added
    expected_age_av = 25
    assert code.dogowners_average_age(data_arrays) == expected_age_av

def test_average_owners_age_fordogs():
    age = [11, 45, 21, 19]
    dogs = [1, 2, 0, 1]
    data_arrays= np.column_stack((age, dogs)) # had to me added 
    expected_age_av = 30
    assert code.average_owners_age_fordogs(data_arrays) == expected_age_av

