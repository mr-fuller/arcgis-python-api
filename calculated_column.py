import arcrest

username = [your username]
password = [your password]
# security handler
sh = arcrest.AGOLTokenSecurityHandler(username=username, password=password)
# Feature Layer for related table portion of hosted feature service
fl = arcrest.agol.FeatureLayer(url=[your feature service url])
# Feature Layer for Feature Class part of hosted feature service
fl2 = arcrest.agol.FeatureLayer(url=[your feature service url])
# set sql statement for query
sql= '1=1'
# Query the Table Feature Layer
resFeats = fl.query(where=sql, out_fields="*")
#Iterate through features in the table Feature Layer
for feat in resFeats:
    # get the value of the first field 
    field1 = feat.get_value([first field])
    # replace empty cells with zeros
    if field1 == None:
        field1 = 0.0
    # get the value of the second field 
    field2 = feat.get_value([second field])
    # replace empty cell with zero
    if field2 == None:
        field2 = 0.0
    # Calculate the difference in fields
    fertDiff = field2 - field1
    # Set the value of the field for difference
    feat.set_value([difference field], fertDiff)
# Update features, and print to check success
print(fl.updateFeature(features=resFeats))

# Query the Feature Class Feature Layer
resFeats2 = fl2.query(where=sql, out_fields="*")
#Iterate through features in the table Feature Layer
for feat in resFeats2:
    # get the value of the first field 
    field1 = feat.get_value([first field])
    # replace empty cells with zeros
    if field1 == None:
        field1 = 0.0
    # get the value of the second field 
    field2 = feat.get_value([second field])
    # replace empty cells with zeros
    if field2 == None:
        field2 = 0.0
    # Calculate the difference in fields
    fertDiff = field2 - field1
    # Set the value of the field for difference
    feat.set_value([difference field], fertDiff)
# Update features, and print to check success
print(fl2.updateFeature(features=resFeats2))
