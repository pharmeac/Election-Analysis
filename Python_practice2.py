


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for key,value in counties_dict.items():
   #print (f"{key} county has {value:,} registered voters")
    
#voting_data.dict = []
#for county, voters in counties_dict.items():
#    print(county, voters)

#voting_data = {"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", 
#"registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}
#for county, registered_voters in voting_data:
#    print (f'{voting_data} county has {registered_voters} registered voters')  
#for county, registered_voters in voting_data:
#    print(f"{county}, county has {registered_voters:,}")
    
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver",
#"registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict, registered_voters_dict in voting_data:
   #for value in county_dict, registered_voters_dict:
    #    print (f'{county_dict("county")} county has {registered_voters_dict("registered_voters"):,} registered voters')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver","registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print (f'{county} county has {voters:,} registered voters')

#for i in range(len(voting_data)):
 #   print(f'{voting_data[i]["county"]} county has {voters:,} registered voters.')
        
#for county, voters in voting_data:
 #   print (f'{county_dict} county has voters:, registered voters')
 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']} registered voters.")    