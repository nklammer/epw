from epw import epw
a = epw()
a.read('USA_NY_New.York-Central.Park.725033_TMY3.epw')


d = a.headers
# print(d)

df = a.dataframe

# print(df.head())

df.to_csv('NYC_epw.csv')