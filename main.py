#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        node_heads = []
        for l in lists:
            head = ListNode(l[0])
            node_heads.append(head)
            tail = head
            for element in l[1:]:
                tail.next = ListNode(element)
                tail = tail.next
        merged_list = []
        minimum_value, position = node_heads[0], 0
        while True:
            node_index = 0
            minimum_value, position = node_heads[node_index].val, node_index
            while node_index < len(node_heads):
                if node_heads[node_index].val < minimum_value:
                    minimum_value, position = node_heads[node_index].val, node_index
                node_index += 1

            merged_list.append(minimum_value)
            if not (node_heads[position].next is None):
                node_heads[position] = node_heads[position].next
            else:
                del node_heads[position]

            if len(node_heads) == 0:
                break

        return merged_list

def test(given_list: object, expected: object) -> object:
    sol = Solution()
    test_result = sol.mergeKLists(given_list)

    print("Given list %r expected %r returned %r this is %r" % (
        given_list, expected, test_result, (test_result == expected)))


def test_all():
    test([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])



test([[1,4,5],[1,3,4],[2,6]],[1,1,2,3,4,4,5,6])
test_all()