def get_parent(h, i):
    total_nodes = (2**h)-1
    
    if i>total_nodes:
        return -1
    else:
        size = (2**h)-1
        offset = 0
        while True:
            if size == 0:
                return -1
            
            size //=2

            left_node = offset+size

            right_node = left_node+size

            if i==left_node or i==right_node:
                return right_node+1

            if i>left_node:
                offset = left_node

def solution(h, q):
    if not q:
        return []
    ans = []
    for node in q:
        ans.append(get_parent(h, node))
    return ans

print(solution(5, [19, 14, 28]))
print(solution(3, [7, 3, 5, 1]))