import code_np as code
import numpy as np
import pytest, pdb

@pytest.mark.parametrize("filename_incomplete", 
                        ["data/pets_data_incomplete1.txt", "data/pets_data_incomplete2.txt"])
def test_reading_fromfile_incompletedata(filename_incomplete):
    with pytest.raises(Exception):
        code.reading_fromfile(filename_incomplete)


def test_dogowners_average_age_wronginput():
    age = [11, 45, 21, -19]
    dogs = [1, 2, 0, 1]
    data_arrays= np.column_stack((age, dogs))
    with pytest.raises(Exception):
        code.dogowners_average_age(data_arrays)

def test_average_owners_age_fordogs_wronginput():
    age = [11, 45, 21, -19]
    dogs = [1, 2, 0, 1]
    data_arrays= np.column_stack((age, dogs))
    with pytest.raises(Exception):
        code.average_owners_age_fordogs(data_arrays)


