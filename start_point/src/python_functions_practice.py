def return_10():
  return 10

def add(num_1, num_2):
  return num_1 + num_2

def subtract(num_1, num_2):
  return num_1 - num_2

def multiply(num_1, num_2):
  return num_1 * num_2

def divide(num_1, num_2):
  return num_1 / num_2

def length_of_string(sentence):
  return len(sentence)

def join_string(string_1, string_2):
  return string_1 + string_2

def add_string_as_number(num_1, num_2):
  return int(num_1) + int(num_2)

def number_to_full_month_name(month_number):
  if month_number == 1:
    return "January"
  elif month_number == 2:
    return "February"
  elif month_number == 3:
    return "March"
  elif month_number == 4:
    return "April"
  elif month_number == 5:
    return "May"
  elif month_number == 6:
    return "June"
  elif month_number == 7:
    return "July"
  elif month_number == 8:
    return "August"
  elif month_number == 9:
    return "September"
  elif month_number == 10:
    return "October"
  elif month_number == 11:
    return "November"
  elif month_number == 12:
    return "December"

def number_to_short_month_name(month_number):
  short_month = number_to_full_month_name(month_number)

  return short_month[0:3]

def volume_calculator(length):
  volume = length * length * length
  return volume

  def reverse_name(string_name):
    return string_name[::-1]
