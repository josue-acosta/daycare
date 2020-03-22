from datetime import date, datetime, timedelta

birthday_from_iso = datetime.fromisoformat("2020-01-01T00:00:00.000+00:00")
# print(birthday_from_iso)


def calculate_age_group(birthday):
	today = date.today()
	months = ((today.year - birthday.year) * 12 ) + birthday.month
	age_group = None
	
	if months >= 36:
		age_group = 4
	elif months >= 12 and months < 36:
		age_group = 3
	elif months >= 6 and months < 12:
		age_group = 2
	elif months > 0 and months < 6:
		age_group = 1
	else:
		return "Could not calculate age group"

	print(f"age group: {age_group}")
	return age_group

calculate_age_group(birthday_from_iso)

# the birthday is save in the db as iso format
birthday_from_db = "2020-01-01T00:00:00.000+00:00"

# i removed the '+00:00' since python 3.6 doesn't understand %z
birthday = birthday_from_db[:-6]

# i formated the date string into a datetime data type so i can run python methods on it
birthday_object = datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S.%f')

# print(birthday)
# print(birthday_object.year)
# print(birthday_object.month)
# print(birthday_object.day)
# print(birthday_object.hour)
# print(birthday_object.minute)
# print(birthday_object.second)