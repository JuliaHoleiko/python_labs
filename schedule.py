from group import Group


class Schedule (Group):

    def __init__(self, university_name: str, institute_name: str, group_name: str, group_id: int, schedule_list : dict) -> None:
        """
        initializes schedule object using dictionary (key : day of a week, values : dictionary (key : number of a lesson,
        values : list of lessons))
        :param university_name:
        :param institute_name:
        :param group_name:
        :param group_id:
        :param schedule_list:
        """
        super().__init__(university_name, institute_name, group_name, group_id)
        self._schedule_list = schedule_list

    def __str__(self) -> str:
        schedule_table = ""
        for day in self._schedule_list.keys():
            schedule_table += str(day) + ":\n"
            for les in self._schedule_list.get(day).keys():
                schedule_table += str(les) + "-lesson: "
                schedule_table += self._schedule_list.get(day).get(les) + " | "
            schedule_table += "\n"

        return super().__str__() +  "\n" +"Schedule:"+ "\n"+ schedule_table

