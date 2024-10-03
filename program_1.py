#miles = kilometers x 0.6214

#convert kilometers to miles
def conversion(kilometers):
	miles = kilometers * 0.6214
    #print miles
	print(f"That distance is {miles:.2f} miles.")

#get distance in kilometers
kilometers = int(input("Enter a distance in kilometers: "))

#run conversion
conversion(kilometers)