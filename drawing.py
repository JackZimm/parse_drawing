import pandas as pd

data = {
  "Entry": ["* Reply", "John Doe", "Padmé Amidala", "* Reply", "Grogu", "Ahsoka Tano", "Bo-Katan Kryze", "* Reply", "Mando", "Pelli Motto", "Padmé Amidala", "Rey", "Princess Leia"]
}
def parse_function(test):
    final_contestants = []
    index = 0
    if type(test) == dict:
        lst = test['Entry']
        while index < len(lst):
            if lst[index] == "* Reply":
                index += 2
                continue
            else:
                final_contestants.append(lst[index])
                index += 1
        return final_contestants
    if type(test) == list:
        while index < len(test):
            if test[index] == "* Reply":
                index += 2
                continue
            else:
                final_contestants.append(test[index])
                index += 1
        return final_contestants
    else:
        print('Please enter either a dictionary or list.')            

final_list = parse_function(data)
df = pd.DataFrame(final_list)
df.to_excel('final_ballots.xlsx', index=False)
