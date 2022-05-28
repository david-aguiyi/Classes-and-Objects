class Student:
    # [assignment] Skeleton class. Add your code here

    name = ''
    age = 4
    tracks = []
    score = 90.9

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks.append(tracks)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#Expected Output
# print(Bob.name): Output = Peter
# print(Bob.age): Output = 34
# print(Bob.tracks): Output = ["FE","BE","UI/UX"]
# print(Bob.score): Output = 20.90
