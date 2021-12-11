import pandas as pd


def count_people_field1_not_match_field2(field1, field2, data):
    res_count = 0
    for (f1, f2) in zip(data[field1], data[field2]):
        if not find_match(f1, f2) and not find_match(f2, f1):
            res_count += 1
    return res_count


def top(top_size, data, f_to_search, f_to_return, str_to_search):
    return data[data[f_to_search].str.lower().str.contains(
        str_to_search[:-2])][f_to_return].str.lower().value_counts().head(top_size)


def find_match(f1, f2):
    arr1 = f1.lower().replace('-', ' ').split()
    for word in arr1:
        if word in f2.lower():
            return True
    return False


works = pd.read_csv("works.csv").dropna()
count_prof_not_match_qualif = count_people_field1_not_match_field2("jobTitle", "qualification", works)
print("Из {} людей не совпадают профессия и должность у {}".format(works.shape[0], count_prof_not_match_qualif))

print("\nТоп образований людей, которые работают менеджерами")
print(top(5, works, "jobTitle", "qualification", "менеджер"))

print("\nТоп должностей людей, которые по диплому являются инженерами")
print(top(5, works, "qualification", "jobTitle", "инженер"))

