from task import Task, Score
import datetime


db = [
        {
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
        },
        {
            "id": 2,
            "max_score" : 0.5
            "score" : 0.3
            "title": "Sarah needs to create a presentation",
            "parent_task": "<1, 'Sarah Presenting at San Diego Python', score: 0.1>",
            "depends_on": None,
            "effort" : 0,
            "due_date" : None,
            "overdue" : False,
            "subtasks" : None,
            "parent_task" : None,
            "num_completed_subtasks" : 0,
            "deferred" : False,
            "taggings" : ['presenting', 'python', 'cloud-advocacy'],
            "stakeholders" : ['Sarah', 'David'] ,
        },
        {
            "id": 3,
            "title": "Sarah needs to practice the presentation",
            "parent_task": "<1, 'Sarah Presenting at San Diego Python', score: 0.1>",
            "max_score" : 0.5,
            "score" : 0.0,
            "depends_on": "<2, title: 'Sarah needs to create a presentation', score: 0.2>",
            "effort" : .9,
            "due_date" : datetime.datetime(2023, 6, 9),
            "overdue" : False,
            "subtasks" : None,
            "parent_task" : None,
            "num_completed_subtasks" : 0,
            "deferred" : False,
            "taggings" : ['presenting', 'python', 'cloud-advocacy'],
            "stakeholders" : ['Sarah', 'David'] ,
        },
    ]
