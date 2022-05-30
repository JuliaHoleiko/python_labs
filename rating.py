from student import Student


class Rating:
    def __init__(self, student : Student, average_score : int) -> None:
        """
        initializes rating object using already created student object
        :param student:
        :param average_score:
        """
        self._student = student
        self._average_score = average_score

    def add_list_of_new_points(self, new_points: list) -> None:
        """
        calculate new average score using a list of points
        :param new_points:
        :return:
        """
        self._average_score = sum(new_points) / len(new_points)
        print( f"{self._student._name}'s  new average score is {self._average_score}")

    def __str__(self) -> str:
        return f"Average score - {self._average_score} of " +self._student.__str__()



