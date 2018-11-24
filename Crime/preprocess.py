import csv, random, math, time, sys
from Constants import *

def dd2splits(x, y, unit=0.001):	
	delta_x = int((float(x) + 122.514) / unit)
	delta_y = int((float(y) - 37.708) / unit)
	return (delta_x, delta_y)
	
def ymd2dates(year, month, day):
	return (year - 2003) * 365 + month * 30 + day + int(year % 4 == 0) + (month / 2) - 2 * int(month > 1)
	
def hm2mins(hour, minute):
	return hour * 60 + minute

def max_x(unit=0.001):
	return int(0.148 / unit)
def max_y(unit=0.001):
	return int(0.112 / unit)

def day_cols():
	return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	
def PD_cols():
	return ["BAYVIEW", "CENTRAL", "INGLESIDE", "MISSION", "NORTHERN", "PARK", "RICHMOND",
	"SOUTHERN", "TARAVAL", "TENDERLOIN"]

def DOW2binary(dayofweek):
	result = list([0] * 7)
	result[dayofweek] = 1
	return result
	
def PD2binary(PD):
	result = list([0] * 10)
	result[PD] = 1
	return result
	


with open('crime_train_refined.csv', mode='rb') as original, open('crime_train_preprocessed.csv', mode='wb') as train:
	reader = csv.reader(original, delimiter=',')
	writer_train = csv.writer(train, delimiter=',', quotechar='"')
	is_first_row = True
	
	for row in reader:
		if (is_first_row):
			new_row = ["Category", "Dates", "Time"] + day_cols() + PD_cols() + ["X", "Y"]
			writer_train.writerow(new_row)
			is_first_row = False
			continue
		
		[date, category, _, dayofweek, pd, _, _, x, y] = row
		[year, month, day] = date.split(' ')[0].split('-')
		[hour, minute] = date.split(' ')[1].split(':')
		dates = ymd2dates(int(year), int(month), int(day))
		minutes = hm2mins(int(hour), int(minute))
		daylist = DOW2binary(Day2Int(dayofweek))
		PDlist = PD2binary(PdDistrict2Int(pd))
		new_row = [category, dates, minutes] + daylist + PDlist + [x, y]
		writer_train.writerow(new_row)
		progress += 1
