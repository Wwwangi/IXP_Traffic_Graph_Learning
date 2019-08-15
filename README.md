# IXP_research

# 2019.8.8
1. Merged datasets IXPDB and PDB
2. Using the prefix (subnet) to find identical IXP in PCH and the merged datasets
3. Merge 3 datasets

mapping_all3_with_graph_url.csv and mapping_all3.ipynb are uploaded

In mapping_all3_with_graph_url.csv:
1. All comments and check dates are also attached.
2. Additional columns like 3 different names in 3 datasets are also provided to check if the IDs are perfectly matched. (Most of them work, but some entries are wrong → need further manual work, i think). 
3. Also, I find that the subnet API also provides a few information of graph urls in PCH, so I also added them to the final datasets in case that the graph url does not exist in PDB, you can check.
4. I add the creation time both in PDB and PCH, and the latest update time both in PCH and IXPDB in case you need. You can delete them if they are not necessary.


8.15
1. Checked the inconsistency (labeled red in the updated version of maaping_all3_with_graph_url.csv)
