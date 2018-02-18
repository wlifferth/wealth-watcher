import numpy

stores = {
        "5a88aafd6514d52c7774b52e": (10.0, 25.0, 20.0),
        "5a88abc26514d52c7774b530": (3.0, 50.0, 30.0),
        "5a88ac556514d52c7774b531": (5.0, 7.0, 3.0),
        "5a88ae836514d52c7774b536": (4.0, 21.0, 1.0),
        "5a88afc26514d52c7774b538": (3.0, 11.25, 0),
        "5a88b3cd6514d52c7774b53e": (3.0, 20.0, 50.0),
        "5a88b1196514d52c7774b53a": (2.0, 16.0, 3.0),
        "5a88b0b86514d52c7774b539": (4.0, 5.49, 3)
        }

consistents = {
        "5a88bb496514d52c7774b547": (1, 800.0),
        "5a88bad36514d52c7774b545": (6, 10.0)
        }

labels = ["Date", "Merchant", "Amount"]

print(",".join(labels))

for year in range(2017, 2018):
    for month in range(1, 13):
        for day in range(1, 31):
            for key, val in stores.items():
                if numpy.random.random() < val[0] / 30.0:
                    print("{}-{}-{},{},{:.2f}".format(year, month, day, key, 1 + abs(numpy.random.normal(val[1], val[2]))))
            for key, val in consistents.items():
                if day == val[0]:
                    print("{}-{}-{},{},{:.2f}".format(year, month, day, key, val[1]))

print("2017-2-10,5a88b5226514d52c7774b540,30.87")
print("2017-5-9,5a88ac556514d52c7774b531,492.42")
print("2017-7-27,5a88abc26514d52c7774b530,1300.76")
print("2017-10-1,5a88b58d6514d52c7774b541,10.99")
