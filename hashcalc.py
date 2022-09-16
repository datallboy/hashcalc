#!/bin/python
charset = 36 # character set (i.e. lowercase + numbers = 36 possible characters)
length = 12 # how many characters the password is
hashes_per_second = 11013000000 # md5 hashrate for 1080 TI

combinations = charset ** length
time_in_seconds = round(combinations / hashes_per_second, 2)
time_in_minutes = round(time_in_seconds / 60, 2)
time_in_hours = round(time_in_minutes / 60, 2)
time_in_days = round(time_in_hours / 24, 2)
time_in_years = round(time_in_days / 365, 2)


print("Possible Combination: "+ str(combinations))
print("------------------------")
print("Seconds: " + str(time_in_seconds))
print("Minutes: " + str(time_in_minutes))
print("Hours:   " + str(time_in_hours))
print("Days:    " + str(time_in_days))
print("Years:   " + str(time_in_years))
