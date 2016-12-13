import numpy as np
import pdb


def reading_fromfile(filename):
    val_ar = np.genfromtxt(filename, delimiter=",", skip_header=1)
    if not np.isfinite(val_ar).all():
        raise Exception("some array values are not a number")
    return val_ar[:,:2]


def dogowners_average_age(array):
    if not (array[:,0] > 0).all():
        raise Exception("incorrect values for age")
    age_av =  array[np.where(array[:,1]>0),0].mean()
    return age_av


def average_owners_age_fordogs(array):
    if not (array[:,0] > 0).all():
        raise Exception("incorrect values for age")
    age_av =  np.average(array[np.where(array[:,1]>0),0],\
                         weights = array[np.where(array[:,1]>0),1])
    return age_av


def main(filename="pets_data.txt"):
    val_ar = reading_fromfile(filename)
    age_av_hum = dogowners_average_age(val_ar)
    age_av_dog = average_owners_age_fordogs(val_ar)
    print(age_av_hum)
    print(age_av_dog)
    return age_av_hum, age_av_dog

if __name__ == "__main__":
    main()
