class NestedIterator:
    """Iterates over a nested list structure using an explicit stack.

    Uses a stack-based iterative approach (not recursive) to flatten
    nested lists on demand.

    In a data engineering context, this flattens nested data
    structures (e.g., nested JSON arrays, hierarchical records)
    into a flat sequence for downstream processing.

    Args:
        nested_list: A list that may contain integers or other lists.
    """

    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]
        self._next = None

    def _advance(self):
        while self.stack:
            try:
                element = next(self.stack[-1])
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    self._next = element
                    return
            except StopIteration:
                self.stack.pop()
        self._next = None

    def next(self):
        if self._next is not None:
            result = self._next
            self._next = None
            return result
        self._advance()
        if self._next is not None:
            result = self._next
            self._next = None
            return result
        raise StopIteration

    def has_next(self):
        if self._next is not None:
            return True
        self._advance()
        return self._next is not None