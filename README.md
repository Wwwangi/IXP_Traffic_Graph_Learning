# IXP_research

Prepare database for future graph learning

#2019.7.25 update
All the graph urls are checked manually:
1. Reasons are provided if the url is not OK. 
2. Some urls that got from the API do not give the graphs, but I found the graphs somewhere on the homepages of those urls. Those newly found links are written in the comment parts.
3. Some urls contain only one graph. More information(graphs) can be obtained if you click on that graph.
4. Some urls are just pointers to one ".png" image.
5. Some urls need users to login.
6. Other urls have problems such as "404 not found", "name not resolved", etc.
......
7. More specific reasons are all provided in the csv file.

Next step is to match the PCH ID (might be a bit difficult because the names of the IXPs are quite different in these three databases, should find some correlations) and to group them based on IXP → several links to the graphs of different countries/cities in a list(dictionary?) for one IXP (still confusing)

e.g.
if there are rows like these:
SE	100		192	  Netnod Gothenburg	  Gothenburg	           Europe   (ROW1).
DK	294		193	  Netnod Copenhagen	  Malmo / Copenhagen	   Europe   (ROW2).
SE	102		194	  Netnod Sundsvall	  Sundsvall	             Europe   (ROW3).

How do we group them? 
1. They are all from the same IXP Netnod.
2. Row 1 and 3 are from same country but different cities.
3. Row 1 and 2 are from different countries.

Need further clarification.
