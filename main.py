class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newName):
        self.name = newName
        print(f"Students name changed to: {self.name}")

    def change_age(self, newAge):
        self.age = newAge
        print(f"Student's age changed to: {self.age}")
    
    def add_track(self, addtrack):
        self.tracks = addtrack
        print(f"Student's tracks changed to {self.tracks}")

    def get_score(self):
        print(f"{self.name} score is: {self.score}")




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
