# Create a class Counter with:

# An attribute count initialized to 0

# A method increment() that adds 1 to count

# A method decrement() that subtracts 1 from count

# A method display() that prints the current count

# Then, create an object of Counter and use a loop to:

# Increment it 3 times

# Decrement it 1 time

# Display the result

# Concepts: Class, Methods, Loops, Functions

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1

    def display(self):
        print (f"current count : {self.count}")


    
simple = Counter()
for i in range(10):
    simple.increment()

for i in range(5):
    simple.decrement()

simple.display()
