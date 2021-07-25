'''
[[1,2,3],[4,5,6]]--> [1,2,3,4,5,6]
'''
import itertools
lst=[[1,2,3],[4,5,6]]
flat_list=list(itertools.chain(*lst))
print(flat_list)

