class Task:
    def __init__(self, _id, title, description, completed=False) -> None:
        self._id = _id
        self.title = title
        self.description = description
        self.completed = completed


    def to_dict(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }