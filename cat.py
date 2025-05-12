class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} speak Meaw"

cat1 = Cat("Whiskers")
cat2 = Cat("Milo")

print(cat1.speak())
print(cat2.speak())
