# <img src="https://github.com/ezgranet/mmp-calc/blob/master/ballot-logo.png" alt="image of  ballot box" width="50"> &nbsp; mmp-calc
  
  
Calculate MMP! 


`mmp-calc` is a free-and-open-source (MIT Licence) Python script for calculating the results of an election conducted using a form of mixed-member proportional (MMP) representation (also known as the Additional Member System in the UK).  

`mmp-calc` allows a user to enter the number of seats won in single-member constituencies, and then to calculate the allocation of proportional seats using either of the most frequently used electoral quotas: d'Hondt (as in eg Scotland) or St-Laguë (as in eg New Zealand).  There is no limit to the amount of parties or seats which can be calculated, other than the processing power of the machine using the script.  

## Installation and dependencies



## Example use

As a demonstration of how to use `mmp-calc`, we will calculate the regional (proportional) seats for the 'Highlands and Islands' region of the Scotland in the 2016 Scottish elections.  The vote and seat data used in this example come from the official House of Commons Library Briefing on the results of the election, [which can be accessed by clicking on this link](https://commonslibrary.parliament.uk/research-briefings/cbp-7599/?doing_wp_cron=1593138584.9657280445098876953125).   

In Scottish parliament elections, each region proportionally allocates 7 seats on the basis of the 'party' vote in that region, taking into account seats already won in the single-member plurality constituency seats (of which there are 8 in the Highlands and Islands region).   This is calculated using the d'Hondt formula of <img src="https://github.com/ezgranet/mmp-calc/blob/master/dhondt.png" alt="v/(2s+1)" width="50">.  There are no overhang or compensatory seats.

In the 2016 election, the Scottish National Party (SNP) won 6 of the 8 constituency seats in the Highlands and Islands region, while the remaining two were won by the Liberal Democrats (LD).  The remaining parties—the Conservatives (CON), Labour (LAB), the Scottish Greens (GRN) and the UK Independence Party (UKIP)—therefore won zero constituency seats.  


Now, using those seat numbers and the totals for party votes, we can use `mmp-calc` to determine how to allocate the seven regional seats.  The image below shows how you should format data in the script (using either an Excel spreadsheet or a CSV file), and is taken from the included file `sample-data.xlsx` (those with accessibility needs should open that file for the text of the data).  

<img src="https://github.com/ezgranet/mmp-calc/blob/master/input.png" alt="please see sample-data.xlsx for the text of this table" width="300">


The first row is given over to explanatory headers, and is ignored by `mmp-calc`.  Input in `mmp-calc` **must** follow the format used in the image below.  **Column 1 should include the names of parties.  Column 2 should include the number of seats already won by each party.  Column 3 should include the relevant number of votes used for calculating the proportional tier of seats.** 

With these data in place, we can now use the script to calculate the 7 regional seats! The easiest way to do this is to place `mmp-calc.py` in the directory containing your Excel spreadsheet/CSV file, and then `cd` into that directory.  Once that is done, type `python3 mmp-calc.py` into your terminal.

Then, simply respond to the prompts given by the script.  In our case, our input file is `sample-data.xlsx` (and is in the same directory as the script), so we type that when asked for our file path.  We want to use d'Hondt, so we type `dh` when asked for the system.  We need to calculate 7 seats, so we type `7` when asked how many seats we want to calculate.  We want our output in Excel format, so we request the file `hi-output` with the extension `XLSX`, and we want that file in the same directory as our input, so we leave the `File Path` question blank.  All of these steps are shown in the image below:


<img src="https://github.com/ezgranet/mmp-calc/blob/master/sample-use.png" alt="please see the paragraph above for the text of this image" width="750">


Now when we open the file `hi-output.xlsx` (included in the repository), we see the following results.  Please note that the image below was made by freezing the first two columns; `hi-output.xlsx` includes the quotas and seat allocations for every d'Hondt count.

<img src="https://github.com/ezgranet/mmp-calc/blob/master/output.png" alt="please see the spreadsheet for the text of this image" width="750">


As we can see, the SNP gained one regional seat, the Conservatives gained three, Labour gained two, and the Scottish Greens one.  The Lib Dems and UKIP gained none.  This, of course, is precisely what happened in real life! 


