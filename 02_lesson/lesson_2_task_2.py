# Проверка года на високосность
def is_year_leap(year):
    
    if year % 4 == 0:
        return True
    else:
        return False

year_to_check = 2024
result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")

print(f"год 2020: {is_year_leap(2020)}")
print(f"год 2023: {is_year_leap(2023)}")
print(f"год 2000: {is_year_leap(2000)}")
print(f"год 1900: {is_year_leap(1900)}")