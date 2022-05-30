from institute import Institute


class Group (Institute):
    def __init__(self, university_name: str, institute_name: str, group_name : str, group_id : int) -> None:
        """
        initializes group object
        :param university_name:
        :param institute_name:
        :param group_name:
        :param group_id:
        """
        super().__init__(university_name, institute_name)
        self._group_name = group_name
        self._group_id = group_id

    def __str__(self) -> str:
        return f"group {self._group_name}-{self._group_id} in " + super().__str__()
