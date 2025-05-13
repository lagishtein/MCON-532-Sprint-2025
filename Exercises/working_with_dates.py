#getting the current date and time
from cgi import parse
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)

#creating specific dates
d = datetime(2025, 5, 7, 14, 30)
print("Specific Date:", d)

#Formatting with Dates with strftime()
print("Month-Day-Year:", now.strftime("%m-%d-%Y"))
print("Hour:Minute AM/PM:", now.strftime("%I: %M %p"))
print("Log Timestamp:", now.strftime("[%d,/%b/%Y: %H: %M: %S]"))



#Parsing Strings into Dates With strptime()
d1 = datetime.strptime("07-05-2025", "%d-%m-%Y")
d2 = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
d3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")

print(d1, d2, d3)


#Performing Date Calculations with timedelta
from datetime import timedelta

two_weeks = now + timedelta(weeks=2)
print("Two weeks from now:", two_weeks)

difference = two_weeks - now
print("Difference in days:", difference.days)



#Using Timezones
import pytz

utc_now = datetime.now(pytz.utc)
print("UTC Time:", utc_now)

from pytz import timezone
eastern = timezone('US/Eastern')
local_time = utc_now.astimezone(eastern)
print("Eastern Time:", local_time)




#Simplifying Dates with dateutil

#parsing with dateutil.parser
from dateutil import parser

dt1 = parser.parse("May 7, 2025 2:30 PM")
dt2 = parser.parse("2025-05-07T14:30:00Z")
print(dt1, dt2)

#Date Arithmetic with relativedelta
from dateutil.relativedelta import relativedelta

future = now + relativedelta(months=1, days=10)
print("Future date:", future)

#Recurring Dates with rrule
from dateutil.rrule import rrule, WEEKLY

for dt in rrule(WEEKLY, count= 4, dtstart=now):
    print("Next Weekly Date:", dt)


                        ## WORKING WITH DATES ##

#Exercise 1: Parse Dates
#use strptime() to parse:
def parse_dates():
    dd_mm_yyyy = datetime.strptime("07-05-2025", "%d-%m-%Y")
    datetime_object = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
    date_parsing3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")
    print(dd_mm_yyyy, datetime_object, date_parsing3)

#Excercise 2: Format Dates
#use strftime()
def format_dates():
    print("Today's date:", now.strftime("%m-%d-%Y"))
    print("Current time:", now.strftime("%I:%M %p"))
    print("Log-style timestamp",now.strftime("[%d/%b/%Y:%H:%M:%S]"))

#Exercise 3: GEt UTC and Local Time
def get_utc_and_local_time():
    current_UTC_time = datetime.now(pytz.utc)
    print("UTC Time:", current_UTC_time)

    la_timezone = timezone('America/Los_Angeles')
    local_time = current_UTC_time.astimezone(la_timezone)
    print("Time in Los Angeles:", local_time)

#Exercise 4: Time Difference
def time_difference():
    today = datetime(2025, 5, 7)
    date_two = datetime(2025, 12, 25)
    difference = date_two - today
    print("Difference in days:", difference.days)

#Excercise 5: Timezone Coversion
def timezone_conversion():
    utc_datetime = datetime.now(pytz.utc)
    print("UTC Time:", utc_datetime)
    asia = timezone('Asia/Tokyo')
    tokyo_timezone = utc_datetime.astimezone(asia)
    print("Time in Tokyo:", tokyo_timezone)
    europe = timezone('Europe/Paris')
    paris_timezone = utc_datetime.astimezone(europe)
    print("Time in Paris:", paris_timezone)

#Exercise 6: Datetime Comparison
def compare_datetimes():
    dt1 = parser.parse("2025-05-07T14:30:00")
    dt2 = parser.parse("2025-12-25T09:00:00")
    print("Datetime 1:", dt1)
    print("Datetime 2:", dt2)
    if dt1 > dt2:
        print("Later datetime:", dt1)
    else:
        print("Later datetime is:", dt2)

#Excercise 7: Timedelta
def timedelta():
    from datetime import date, timedelta
    today = date.today()
    in_three_weeks = today + timedelta(weeks=3)
    print("Today is:", today.isoformat())
    print("In three weeks it will be:", in_three_weeks.isoformat())
    three_months_ago = today - relativedelta(months=3)
    print("Three months ago was:", three_months_ago.isoformat())

parse_dates()
format_dates()
get_utc_and_local_time()
time_difference()
timezone_conversion()
compare_datetimes()
timedelta()