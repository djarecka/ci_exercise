import pdb

def reading_fromfile(filename):
    age_l = []
    dogs_l = []
    with open(filename) as f:
        next(f)
        for line in f:
            line_spl = line.rstrip().split(",")
            age_l.append(float(line_spl[0]))
            dogs_l.append(int(line_spl[1]))
    return age_l, dogs_l
            


def dogowners_average_age(age_l, dog_l):
    age_dog_l = []
    for i in range(len(age_l)):
        if dog_l[i] > 0:
            age_dog_l.append(age_l[i])
    age_av =  sum(age_dog_l) / len(age_dog_l)
    return age_av

def average_owners_age_fordogs(age_l, dog_l):
    age_dog_l = []
    for i in range(len(age_l)):
        if dog_l[i] > 0:
            age_dog_l += [age_l[i]] * dog_l[i]
    age_av =  sum(age_dog_l) / len(age_dog_l)
    return age_av


def main(filename="data/pets_data.txt"):
    age_l, dogs_l = reading_fromfile(filename)
    age_av_hum = dogowners_average_age(age_l, dogs_l)
    age_av_dog = average_owners_age_fordogs(age_l, dogs_l)
    print(age_av_hum) 
    print(age_av_dog)
    return age_av_hum, age_av_dog

if __name__ == "__main__":
    main()
