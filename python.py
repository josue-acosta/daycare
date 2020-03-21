from datetime import date, datetime

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

birthday_from_db = "2020-01-01T00:00:00.000+00:00"
birthday = birthday_from_db[:-6]

birthday_object = datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S.%f')

print(birthday)
print(birthday_object.year)
print(birthday_object.month)
print(birthday_object.day)
print(birthday_object.hour)
print(birthday_object.minute)
print(birthday_object.second)



# "2020-01-01T00:00:00.000+00:00"

# age group no. 1:     0 months  >  6 months
# age group no. 2: =>  6 months  > 12 months
# age group no. 3: => 12 months  > 36 months
# age group no. 4: => 36 months