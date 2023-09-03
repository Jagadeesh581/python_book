# Python Dates
# A date in Python is not a data type of its own, we can import 'datetime' module to work with dates as date objects.
import datetime


x = datetime.datetime.now()
# 2022-12-12 17:46:39.145697 (year, month, day, hour, minutes, seconds, microseconds).
print(x)
print(x.year)  # 2022
print(x.strftime("%A"))  # Monday (name of weekday)


# Creating Date Objects:
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
x = datetime.datetime(2022, 1, 1)
print(x)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).


# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string

print(x.strftime("%a"))  # %a	Weekday, short version	Sat
print(x.strftime("%A"))  # %A	Weekday, full version	Saturday
print(x.strftime("%w"))  # %w	Weekday as a number 0-6, 0 is Sunday	6
print(x.strftime("%d"))  # %d	Day of month 01-31	01
print(x.strftime("%b"))  # %b	Month name, short version	Jan
print(x.strftime("%B"))  # %B	Month name, full version	January
print(x.strftime("%m"))  # %m	Month as a number 01-12	01
print(x.strftime("%y"))  # %y	Year, short version, without century	22
print(x.strftime("%Y"))  # %Y	Year, full version	2022
print(x.strftime("%H"))  # %H	Hour 00-23	00
print(x.strftime("%I"))  # %I	Hour 00-12	12
print(x.strftime("%p"))  # %p	AM/PM	AM
print(x.strftime("%M"))  # %M	Minute 00-59	00
print(x.strftime("%S"))  # %S	Second 00-59	00
print(x.strftime("%f"))  # %f	Microsecond 000000-999999	000000
print(x.strftime("%z"))  # %z	UTC offset	+0100
print(x.strftime("%Z"))  # %Z	Timezone	CST
print(x.strftime("%j"))  # %j	Day number of year 001-366	001
print(
    x.strftime("%U")
)  # %U	Week number of year, Sunday as the first day of week, 00-53	00
print(
    x.strftime("%W")
)  # %W	Week number of year, Monday as the first day of week, 00-53	00
print(x.strftime("%c"))  # %c	Local version of date and time	Sat Jan  1 00:00:00 2022
print(x.strftime("%C"))  # %C	Century	20
print(x.strftime("%x"))  # %x	Local version of date	01/01/22
print(x.strftime("%X"))  # %X	Local version of time	00:00:00
print(x.strftime("%%"))  # %%	A % character	%
print(x.strftime("%G"))  # %G	ISO 8601 year	2021
print(x.strftime("%u"))  # %u	ISO 8601 weekday (1-7)	6
print(x.strftime("%V"))  # %V	ISO 8601 week number (01-53)	52
