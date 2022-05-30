class University:

    def __init__(self, university_name : str, ) -> None:
        """
        initializes university obj
        :param university_name:
        """
        self._university_name = university_name


    def __str__(self) -> str:
        return f"University {self._university_name}"

