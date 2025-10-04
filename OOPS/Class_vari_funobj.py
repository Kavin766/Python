class First:
    name = "Hello"  # class variable

    def addnum(self):
        self.a = 34  # object variable
        self.b = 56
        self.c = self.a + self.b  # corrected: added self.
        print("Result:", self.c)

    def display(self):
        print("Res:", self.c)

obj1 = First()
obj1.addnum()
obj1.display()
class Second:
    name = "Hello"  # class variable

    def addnum(self):
        self.a = 34  # object variable
        self.b = 56
        self.c = self.a + self.b
        print("Result:", self.c)
        return self.c          # ✓ Now returning useful value!

    def display(self):
        print("Res:", self.c)
        return self.c          # ✓ Now returning useful value!

# Usage:
obj2 = Second()
hi1 = obj2.addnum()     # hi1 = 90
hi2 = obj2.display()    # hi2 = 90
print("Stored values:", hi1, hi2)  # Output: Stored values: 90 90

# Now we can use these values for calculations!
total = hi1 + hi2       # 90 + 90 = 180
print("Total:", total)  # Output: Total: 180