from university import University


class Institute (University):

    def __init__(self, university_name: str, institute_name : str) -> None:
        """
        initializes institute object
        :param university_name:
        :param institute_name:
        """
        super().__init__(university_name)
        self._institute_name = institute_name

    def __str__(self) -> str:
        return f"Institute {self._institute_name} of " + super().__str__()