# <img src="https://github.com/ezgranet/mmp-calc/blob/master/images/ballot-logo.png" alt="image of  ballot box" width="75"> &nbsp; mmp-calc
  
  
Calculate MMP with an MMP calculator!


`mmp-calc` is a free-and-open-source app for calculating the results of an election conducted using a form of mixed-member proportional (MMP) representation (also known as the Additional Member System in the UK). 

`mmp-calc` allows a user to enter the number of seats won in single-member constituencies, and then to calculate the allocation of proportional seats using either of the most frequently used electoral quotas: d'Hondt (as in eg Scotland) or St-Laguë (as in eg New Zealand).  There is no limit to the amount of parties or seats which can be calculated, other than the processing power of the machine using the script.

The script has a `GUI` for `macOS` and `Windows` which can be found on the Releases page!   This is the *easiest* way to use the app!  You can also run  the script in `Python` directly, but that is harder.

## Example use


As a demonstration of how to use `mmp-calc`, we will calculate the regional (proportional) seats for the Highlands and Islands region in the 2016 Scottish Parliament elections.  The vote and seat data used in this example come from the official House of Commons Library Briefing on the results of the election, [which can be accessed by clicking on this link](https://commonslibrary.parliament.uk/research-briefings/cbp-7599/?doing_wp_cron=1593138584.9657280445098876953125).   

In Scottish parliament elections, each region proportionally allocates 7 seats on the basis of the 'party' vote in that region, taking into account seats already won in the single-member plurality constituency seats (of which there are 8 in the Highlands and Islands region).   This is calculated using the d'Hondt formula of <img src="https://github.com/ezgranet/mmp-calc/blob/master/images/dhondt.png" alt="v/(2s+1)" width="50">.  There are no overhang or compensatory seats.

In the 2016 election, the Scottish National Party (SNP) won 6 of the 8 constituency seats in the Highlands and Islands region, while the remaining two were won by the Liberal Democrats (LD).  The remaining parties—the Conservatives (CON), Labour (LAB), the Scottish Greens (GRN) and the UK Independence Party (UKIP)—therefore won zero constituency seats.  


Now, using those seat numbers and the totals for party votes, we can use `mmp-calc` to determine how to allocate the seven regional seats.  The image below shows how you should format data in the script (using an Excel spreadsheet), and is taken from the included file `sample-data.xlsx` (those with accessibility needs should open that file for the text of the data).  

<img src="https://github.com/ezgranet/mmp-calc/blob/master/images/input.png" alt="please see sample-data.xlsx for the text of this table" width="300">


The first row is given over to explanatory headers, and is ignored by `mmp-calc`.  Input in `mmp-calc` **must** follow the format used in the image above.  **Column 1 should include the names of parties.  Column 2 should include the number of seats already won by each party.  Column 3 should include the relevant number of votes used for calculating the proportional tier of seats.** 

With these data in place, we can now use the script to calculate the 7 regional seats! Open the GUI and select the excel file!

Then, simply respond to the prompts given by the GUI.  In our case, we select our input file from the provided prompt. We need to calculate 7 seats, so we type `7` when asked how many seats we want to calculate.  We want to use d'Hondt, so we type `dh` when asked for the formula. We will name our output file `hi-output.xlsx`, so we type that name under `save name`.  


Now when we open the file `hi-output.xlsx` (included in the repository), we see the following results.  Please note that the image below was made by freezing the first two columns; `hi-output.xlsx` includes the quotas and seat allocations for every d'Hondt count.

<img src="https://github.com/ezgranet/mmp-calc/blob/master/images/output.png" alt="please see the spreadsheet for the text of this image" width="750">


As we can see, the SNP gained one regional seat, the Conservatives gained three, Labour gained two, and the Scottish Greens one.  The Lib Dems and UKIP gained none.  This, of course, is precisely what happened in real life! 

## Credits and Licensing

This script was co-created by [Elijah Granet](https://github.com/ezgranet) and [Isaiah Granet](https://github.com/igranet), who are brothers.

The icon for the repo is the character `Unicode: U+1F5F3 BALLOT BOX WITH BALLOT` in the libre [`Symbola`](https://github.com/gearit/ttf-symbola) typeface by George Douros.

This software is licensed under the very permissive MIT Licence and may be used for any purpose.  Contributions and suggestions are gratefully welcomed.

