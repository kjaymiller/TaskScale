import dataclasses
import datetime

@dataclasses.dataclass
class Score:
    """
    max_score: int # The maximum score the task can have
    total: int # sum of all scores
        The total score is calculated by adding all the scores together.
        It cannot be higher than the max score.

    description: int # modifies the score based on if a description is present
        The description score is calculated by adding the description score to the total score.
        If the description is empty, the score is 0.

    due_date: int # modifies the score based on if the task exists

    overdue: int # modifies the score based on if the task is overdue

    subtasks: int # modifies the score based on the number of subtasks
        The more subtasks there are, the lower the max the score.

    num_completed_subtasks: int # modifies the score based on the number of completed subtasks
        The more completed subtasks there are, the higher the score.

    deferred: int # sets the max score to 0 if the task is deferred

    taggings: int # modifies the score based on the number of taggings and the number other tasks with the same taggings
        TODO: How to calculate this?

    stakeholders: int # modifies the score based on the number of stakeholders
        TODO: How to calculate this?

    effort: int # modifies the score based on the effort to complete the task
        TODO: How to calculate this?
    """
    total: int # sum of all scores
    description: int # modifies the score based on if a description is present
    due_date: int # modifies the score based on if the task exists
    overdue: int # modifies the score based on if the task is overdue
    subtasks: int # modifies the score based on the number of subtasks
    num_completed_subtasks: int # modifies the score based on the number of completed subtasks
    max_score: int # modifies the score based on the max score
    deferred: int # sets the score to 0 if the task is deferred
    taggings: int # modifies the score based on the number of taggings and the number other tasks with the same taggings
    stakeholders: int # modifies the score based on the number of stakeholders
    effort: int # modifies the score based on the effort to complete the task


@dataclasses.dataclass
class Task:
    id: primary_key,
    score: Score
    description: str
    due_date: datetime.datetime
    overdue: bool
    subtasks:  list["Task"]
    max_score: int 
    completed: bool
    parent: "Task"
    root: "Task"

      "id": 1,
            "title": "Sarah Presenting at San Diego Python",
            "max_score" : 0.5,
            "score" : 0.1,
            "description" : "Sarah will be presenting at San Diego Python on 2023-06-10 on Jupyter Notebooks, VS Code and Data Wrangler",
            "depends_on": None,
            "due_date" : datetime.datetime(2023, 6, 10),
            "overdue" : False,
            "subtasks" : ["<2, title: 'Sarah needs to create a presentation', score: 0.2>", '<3, title: "Sarah needs to practice the presentation", score: 0.3>']'],
            "parent_task" : None,
            "num_completed_subtasks" : 0,
            "deferred" : False,
            "taggings" : ['presenting', 'python', 'cloud-advocacy'],
            "stakeholders" : ['Sarah', 'David'] ,
            "effort" : .8,