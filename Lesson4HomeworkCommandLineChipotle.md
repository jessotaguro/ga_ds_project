## Command Line Tasks

**1. Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. 
Think for a minute about how the data is structured. What do you think each column means? 
What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)**<br>
The rows represent items in orders. Each column is an attribute of that order such as the quantity of an item and what ingredients went into that item. <br>
`head chipotle.tsv`<br>
`tail chipotle.tsv`<br>
<br>
**2. How many orders do there appear to be?**<br>
4589?<br>
`uniq chipotle.tsv | wc -l`<br>
<br>
**3. How many lines are in this file?**<br>
4623<br>
`wc -l`<br>
<br><
**4. Which burrito is more popular, steak or chicken?**<br>
Chicken<br>
`grep "steak burrito" -i chipotle.tsv | wc -l`<br>
`grep "chicken burrito" -i chipotle.tsv | wc -l`<br>
<br>
**5. Do chicken burritos more often have black beans or pinto beans?**<br>
Black beans<br>
`grep "chicken burrito" -i chipotle.tsv | grep "black beans" -i | wc -l`<br>
`grep "chicken burrito" -i chipotle.tsv | grep "pinto beans" -i | wc -l`<br>
<br>
**6. Make a list of all of the CSV or TSV files in the [our class repo] (https://github.com/ga-students/DS-SEA-08). repo 
(using a single command). You will be working on your local repo on your laptop. Think about how wildcard characters 
can help you with this task.**<br>
`find . -name '*csv'`<br>
<br>
**7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files of 
[our class repo] (https://github.com/ga-students/DS-SEA-8).**<br>
 57?<br>
 `grep -r dictionary .. | wc -l`<br>
<br>
Optional: Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!
