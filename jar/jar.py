class Jar:
    def __init__(self,capacity=12):
        if capacity < 0 :
            raise ValueError("Enter a positive integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self._size}"

    def deposit(self,n):
        if self._size + n > self.capacity:
            raise ValueError("Cookie Jar's capacity is full")
        self._size +=n

    def withdraw(self,n):
        if n > self._size:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)
if __name__ == "__main__":
    main()





