class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a nonnegative integer")
        self._capacity = capacity
        self._count = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._count

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("deposit amount must be a nonnegative integer")
        if self._count + n > self._capacity:
            raise ValueError("deposit would exceed capacity")
        self._count += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("withdraw amount must be a nonnegative integer")
        if n > self._count:
            raise ValueError("not enough cookies to withdraw")
        self._count -= n

    def __str__(self):
        return "🍪" * self._count
