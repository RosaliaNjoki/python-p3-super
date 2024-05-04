class Student(User):
    def __init__(self, name, grade)
        self.name = name
        self.grade = grade


    def log_in(self):
        super().log_in()
        self.in_class = True