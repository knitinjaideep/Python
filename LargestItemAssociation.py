from collections import deque, defaultdict


def largest_item_association(item_association):
    item_map = defaultdict(set)
    
    for item_pair in item_association:
        item_map[item_pair[0]].add(item_pair[1])
        item_map[item_pair[1]].add(item_pair[0])
    
    largest_group = []
    visited = set()

    for key, val in item_map.items():
        if key not in visited:
            curr_group = []
            q = deque()
            q.append(key)
            while q:
                curr = q.popleft()
                visited.add(curr)
                curr_group.append(curr)
                for neighbor in item_map[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
            if len(curr_group) > len(largest_group):
                largest_group = curr_group.copy()
    
    largest_group.sort()
    return largest_group

print(largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
print(largest_item_association([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))

#Example Walk through
#[['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]

#1st Iteration:
#when "for item_pair in item_associations" loop is executed the item_map dictionary is built. The dict values are shown below,

# item_map = {'item1': ('item2'), 'item2': ('item1'), 'item3':('item4'), 'item4': ('item3', 'item5'), 'item5': ('item4') }