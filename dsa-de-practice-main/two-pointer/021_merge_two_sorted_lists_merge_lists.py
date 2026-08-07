class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1, list2):
    """Merge two sorted linked lists into one sorted list.

    DE reframing: merge two sorted data streams into a single ordered stream.

    In a data engineering context, this merges two sorted
    data streams or partitions (e.g., merging sorted shards,
    combining ordered log segments from different sources).

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return dummy.next