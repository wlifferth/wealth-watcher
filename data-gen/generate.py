import numpy

stores = {
        "Walmart": (10.0, 25.0, 20.0),
        "Target": (3.0, 50.0, 30.0),
        "McDonalds": (5.0, 7.0, 3.0),
        "Weigels": (4.0, 21.0, 1.0),
        "Regal Cinema": (3.0, 11.25, 0),
        "Amazon": (3.0, 20.0, 50.0),
        "O'Charleys": (2.0, 16.0, 3.0),
        "17th Street Deli": (4.0, 5.49, 3)
        }

consistents = {
        "Rent": (1, 800.0),
        "Netflix": (6, 10.0)
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

print("2017-2-10,North Korean Missile Program,30.87")
print("2017-5-9,McDonalds,492.42")
print("2017-7-27,Target,1300.76")
print("2017-10-1,McDonalds,10.99,90210")
