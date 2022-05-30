from schedule import Schedule


class Student (Schedule):
    def __init__(self, university_name: str, institute_name: str, group_name: str, group_id: int,
                 schedule_list: dict, name : str, surname : str) -> None:
        """
        initializes Student object
        :param university_name:
        :param institute_name:
        :param group_name:
        :param group_id:
        :param schedule_list:
        :param name:
        :param surname:
        """
        super().__init__(university_name, institute_name, group_name, group_id, schedule_list)
        self._name = name
        self._surname = surname

    def __str__(self) -> str:
        return f"Student {self._name} {self._surname} of "+super().__str__()


