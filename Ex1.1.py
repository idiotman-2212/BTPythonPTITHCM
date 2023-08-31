# EX 1.1 Write a program to convert minutes into a number of years and days.
# Write a program to convert minutes into a number of years and days.
# Test Data
# Input the number of minutes: 3456789
# Expected Output : 6 years, 210 days
minute = int(input());

years = minute// (24*60*365);
days = (minute% (24*60*365))//(24*60);
print(years, "years," , days, "days");

