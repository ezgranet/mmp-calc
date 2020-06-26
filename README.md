# <img src="https://github.com/ezgranet/mmp-calc/blob/master/ballot-logo.png" alt="image of  ballot box" width="40">
  mmp-calc
  
  
Calculate MMP! 


`mmp-calc` is a free-and-open-source (MIT Licence) Python script for calculating the results of an election conducted using a form of mixed-member proportional (MMP) representation (also known as the Additional Member System in the UK).  

`mmp-calc` allows a user to enter the number of seats won in single-member constituencies, and then to calculate the allocation of proportional seats using either of the most frequently used electoral quotas: d'Hondt (as in eg Scotland) or St-Laguë (as in eg New Zealand).  There is no limit to the amount of parties or seats which can be calculated, other than the processing power of the machine using the script.  

# Installation and dependencies



# Example use

As a demonstration of how to use `mmp-calc`, we will calculate the regional (proportional) seats for the 'Highlands and Islands' region of the Scotland in the 2016 Scottish elections.  The vote and seat data used in this example come from the official House of Commons Library Briefing on the results of the election, [which can be accessed by clicking on this link](https://commonslibrary.parliament.uk/research-briefings/cbp-7599/?doing_wp_cron=1593138584.9657280445098876953125).   

In Scottish parliament elections, each region proportionally allocates 7 seats on the basis of the 'party' vote in that region, taking into account seats already won in the single-member plurality constituency seats (of which there are 8 in the Highlands and Islands region).   This is calculated using the d'Hondt formula of <img src="https://github.com/ezgranet/mmp-calc/blob/master/dhondt.png" alt="v/(2s+1)" width="50">.  There are no overhang or compensatory seats.

In the 2016 election, the Scottish National Party (SNP) won 6 of the 8 constituency seats in the Highlands and Islands region, while the remaining two were won by the Liberal Democrats (LD).  The remaining parties—the Conservatives (CON), Labour (LAB), the Greens (GRN) and the UK Independence Party (UKIP)—therefore won zero constituency seats.  


Now, using those seat numbers and the totals for party votes, we can use `mmp-calc` to determine how to allocate the seven regional seats.  The image below shows how you should format data in the script (using either an Excel spreadsheet or a CSV file), and is taken from the included file `sample-data.xlsx` (those with accessibility needs should open that file for the text of the data).  

<img src="https://github.com/ezgranet/mmp-calc/blob/master/input.png" alt="please see sample-data.xlsx for the text of this table" width="300">


The first row is given over to explanatory headers, and is ignored by `mmp-calc`.  Input in `mmp-calc` **must** follow the format used in the image below.  **Column 1 should include the names of parties.  Column 2 should include the number of seats already won by each party.  Column 3 should include the relevant number of votes used for calculating the proportional tier of seats.** 



