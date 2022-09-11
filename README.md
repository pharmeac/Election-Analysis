# Election-Analysis

## Project Overview
A Colorado Board of Elections has given us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates that received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.9.12, Visual Studio Code 1.71.0
 
## Election-Audit Results
The analysis of the data shows that:
1. There were 369,711 votes cast in the congressional election.
2. The county results were:
   - Jefferson: 38,855 votes were cast, which was 10.5% of the total votes cast in the election.
   - Denver: 306,055 votes were cast, which was 82.8% of the total votes cast in the election.
   - Arapahoe: 24,801 votes were cast, which was 6.7% of the total votes cast in the election. 
3. The county with the largest number of votes cast was Denver.
4. The candidate results were:
   - Charles Casper Stockham received 85,213 votes, which was 23.0% of the total votes.
   - Diana DeGette received 272,892 votes, which was 73.8% of the total votes.
   - Raymon Anthony Doane received 11,606 votes, which was 3.1% of the total votes.
5. The winner of the election was Diana DeGette who received 73.8% of the total votes, and 272,892 votes.
 
 ## Election - Audit Summary
This script can be used for other elections, both at the state level, but also at the local or national level. By creating lists and dictionaries within   our Python code, we can analyze the data presented in a csv file by any data attribute column added to the file. We can also add additional analyses to understand the election trends more thoroughly.
   - We can modify the script to pull in any additional attributes provided in the csv file. For example, voting precinct.
   - We can modify the script to analyze the data in additional ways. For example, we could determine the winning candidate for each county.
 
