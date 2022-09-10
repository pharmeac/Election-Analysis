#What is the score?
#88score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#else:
    #if score >= 80:
        #print('Your grade is a B.')
    #else:
        #if score >= 70:
            #print('Your grade is a C.')
        #else:
            #if score >= 60:
                #print('Your grade is a D.')
            #else:
                #print('Your grade is an F.')
# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
 #   print('Your grade is an A.')
#elif score >= 80:
 #   print('Your grade is a B.')
#elif score >= 70:
 #   print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
 #   print('Your grade is an F.')
    
#x = 0
#while x <= 5:
 #   print(x)
    #x = x + 1
     


#counties_dict["Denver"] = 463353
#counties_dict["Jefferson"] = 432438


#for county, voters in counties_dict:
#print(county & "county has" voters & "registered voters")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)