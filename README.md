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
1. SE	100		192	  Netnod Gothenburg	  Gothenburg	           Europe   (ROW1).
2. DK	294		193	  Netnod Copenhagen	  Malmo / Copenhagen	   Europe   (ROW2).
3. SE	102		194	  Netnod Sundsvall	  Sundsvall	             Europe   (ROW3).

How do we group them? 
1. They are all from the same IXP Netnod.
2. Row 1 and 3 are from same country but different cities.
3. Row 1 and 2 are from different countries.

Need further clarification.



#2019.8.1
1. Tried the json in related work and uploaded the mapped csv file (the url for related work: https://bitbucket.org/RKloti/a-comparative-look-into-public-ixp-datasets-partially/src/master/)
2. Tried to use the prefix to map the peeringDB and PCH. 
    The prefix of all IXPs of peeringDB are retrieved successfully (both IPv4 and IPv6). However, there are some problems for getting the prefix in PCH.
    The API only provides the information of subnets of one certain IXP. For example, if we want to get the subnets information of IXP with id 160, it is like this: https://www.pch.net/api/ixp/subnets/160
    And I got these information:
    [
  {
    "id": "189",
    "status": "Deprecated",
    "short_name": "AMS-IX",
    "version": "IPv4",
    "subnet": "193.148.15.0\\/24",
    "mlpa": "Unknown",
    "traffic": "0",
    "participants": "0",
    "established": "19971229",
    "traffic_url": "",
    "traffic_graph_url": "",
    "subnet_num": "1",
    "exchange_point_id": "160"
  },
  {
    "id": "346",
    "status": "Unknown",
    "short_name": "AMS-IX",
    "version": "IPv4",
    "subnet": "195.69.144.0\\/24",
    "mlpa": "Unknown",
    "traffic": "0",
    "participants": "0",
    "established": "20090000",
    "traffic_url": "",
    "traffic_graph_url": "",
    "subnet_num": "6",
    "exchange_point_id": "160"
  },
  .......
  
  I'm quite confused whether the 'subnet' field is the prefix we want or not. 
  I tried to send requests for all the IXPs and get all their subnets and created the temp.csv that contains (probably) the information of prefix of PCH. However, it seems that something gets wrong. They do not match each other.
  I will try to figure out what is going on.
