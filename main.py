from institute import Institute
from rating import Rating
from schedule import Schedule
from student import Student

from university import University


def main ():

    schedule_ir12 = {"monday" : {1 : "math", 2: "prog"}, "tuesday": {1 : "history", 2: "prog"},
                     "wednesday" : {1 : "math", 2: "prog"}, "thursday": {1 : "history", 2: "prog"},
                     "friday": {1: "math", 2: "prog"}
                     }
    schedule_ir13 = {"monday": {1: "english", 2: "prog"}, "tuesday": {1: "physics", 2: "prog"},
                     "wednesday": {1: "prog", 2: "prog"}, "thursday": {1: "english", 2: "prog"},
                     "friday": {1: "math", 2: "prog"}
                     }

    student1 = Student("Lpnu", "ICTA", "IR", 12, schedule_ir12, "Yuliia", "Holeiko")
    print (student1.__str__())
    student2 = Student("Lpnu", "ICTA", "IR", 13, schedule_ir13, "Ivan", "Ivanenko")
    print(student2.__str__())
    student1_rating = Rating(student1, 89)
    student2_rating = Rating(student2, 88)
    student1_rating.add_list_of_new_points((78, 97, 77, 67, 56))
    student2_rating.add_list_of_new_points((79, 96, 79, 66, 88))







if __name__ == '__main__':
    main()


