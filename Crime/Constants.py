# Category
ARSON = 0
ASSAULT = 1
BAD_CHECKS = 2
BRIBERY = 3
BURGLARY = 4
DISORDERLY_CONDUCT = 5
DRIVING_UNDER_THE_INFLUENCE = 6
DRUG_NARCOTIC = 7
DRUNKENNESS = 8
EMBEZZLEMENT = 9 
EXTORTION = 10
FAMILY_OFFENSES = 11
FORGERY_COUNTERFEITING = 12
FRAUD = 13 
GAMBLING = 14
KIDNAPPING = 15
LARCENY_THEFT = 16
LIQUOR_LAWS = 17
LOITERING = 18
MISSING_PERSON = 19
NON_CRIMINAL = 20
OTHER_OFFENSES = 21
PORNOGRAPHY_OBSCENE_MAT = 22
PROSTITUTION = 23
RECOVERED_VEHICLE = 24
ROBBERY = 25
RUNAWAY = 26
SECONDARY_CODES = 27
SEX_OFFENSES_FORCIBLE = 28
SEX_OFFENSES_NON_FORCIBLE = 29
STOLEN_PROPERTY = 30
SUICIDE = 31
SUSPICIOUS_OCC = 32
TREA = 33
TRESPASS = 34
VANDALISM = 35
VEHICLE_THEFT = 36
WARRANTS = 37
WEAPON_LAWS = 38
category_num = 39

def Category2Int(category):
	if (category == "ARSON"):
		return ARSON
	elif (category == "ASSAULT"):
		return ASSAULT
	elif (category == "BAD CHECKS"):
		return BAD_CHECKS
	elif (category == "BRIBERY"):
		return BRIBERY
	elif (category == "BURGLARY"):
		return BURGLARY
	elif (category == "DISORDERLY CONDUCT"):
		return DISORDERLY_CONDUCT
	elif (category == "DRIVING UNDER THE INFLUENCE"):
		return DRIVING_UNDER_THE_INFLUENCE
	elif (category == "DRUG/NARCOTIC"):
		return DRUG_NARCOTIC
	elif (category == "DRUNKENNESS"):
		return DRUNKENNESS
	elif (category == "EMBEZZLEMENT"):
		return EMBEZZLEMENT
	elif (category == "EXTORTION"):
		return EXTORTION
	elif (category == "FAMILY OFFENSES"):
		return FAMILY_OFFENSES
	elif (category == "FORGERY/COUNTERFEITING"):
		return FORGERY_COUNTERFEITING
	elif (category == "FRAUD"):
		return FRAUD
	elif (category == "GAMBLING"):
		return GAMBLING
	elif (category == "KIDNAPPING"):
		return KIDNAPPING
	elif (category == "LARCENY/THEFT"):
		return LARCENY_THEFT
	elif (category == "LIQUOR LAWS"):
		return LIQUOR_LAWS
	elif (category == "LOITERING"):
		return LOITERING
	elif (category == "MISSING PERSON"):
		return MISSING_PERSON
	elif (category == "NON-CRIMINAL"):
		return NON_CRIMINAL
	elif (category == "OTHER OFFENSES"):
		return OTHER_OFFENSES
	elif (category == "PORNOGRAPHY/OBSCENE MAT"):
		return PORNOGRAPHY_OBSCENE_MAT
	elif (category == "PROSTITUTION"):
		return PROSTITUTION
	elif (category == "RECOVERED VEHICLE"):
		return RECOVERED_VEHICLE
	elif (category == "ROBBERY"):
		return ROBBERY
	elif (category == "RUNAWAY"):
		return RUNAWAY
	elif (category == "SECONDARY CODES"):
		return SECONDARY_CODES
	elif (category == "SEX OFFENSES FORCIBLE"):
		return SEX_OFFENSES_FORCIBLE
	elif (category == "SEX OFFENSES NON FORCIBLE"):
		return SEX_OFFENSES_NON_FORCIBLE
	elif (category == "STOLEN PROPERTY"):
		return STOLEN_PROPERTY
	elif (category == "SUICIDE"):
		return SUICIDE
	elif (category == "SUSPICIOUS OCC"):
		return SUSPICIOUS_OCC
	elif (category == "TREA"):
		return TREA
	elif (category == "TRESPASS"):
		return TRESPASS
	elif (category == "VANDALISM"):
		return VANDALISM
	elif (category == "VEHICLE THEFT"):
		return VEHICLE_THEFT
	elif (category == "WARRANTS"):
		return WARRANTS
	elif (category == "WEAPON LAWS"):
		return WEAPON_LAWS
	raise Exception("[Category2Int]Conversion Error - Invalid Category value " + category)

	
# DayOfWeek
Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
day_num = 7

def Day2Int(day):
	if (day == "Monday"):
		return Monday
	elif (day == "Tuesday"):
		return Tuesday
	elif (day == "Wednesday"):
		return Wednesday
	elif (day == "Thursday"):
		return Thursday
	elif (day == "Friday"):
		return Friday
	elif (day == "Saturday"):
		return Saturday
	elif (day == "Sunday"):
		return Sunday
	raise Exception("[Day2Int]Conversion Error - Invalid DayOfWeek value " + day)

	
# PdDistrict
BAYVIEW = 0
CENTRAL = 1
INGLESIDE = 2
MISSION = 3
NORTHERN = 4
PARK = 5
RICHMOND = 6
SOUTHERN = 7
TARAVAL = 8
TENDERLOIN = 9 
PD_num = 10

def PdDistrict2Int(PD):
	if (PD == "BAYVIEW"):
		return BAYVIEW
	elif (PD == "CENTRAL"):
		return CENTRAL
	elif (PD == "INGLESIDE"):
		return INGLESIDE
	elif (PD == "MISSION"):
		return MISSION
	elif (PD == "NORTHERN"):
		return NORTHERN
	elif (PD == "PARK"):
		return PARK
	elif (PD == "RICHMOND"):
		return RICHMOND
	elif (PD == "SOUTHERN"):
		return SOUTHERN
	elif (PD == "TARAVAL"):
		return TARAVAL
	elif (PD == "TENDERLOIN"):
		return TENDERLOIN
	raise Exception("[PdDistrict2Int]Conversion Error - Invalid PdDistrict value " + PD)