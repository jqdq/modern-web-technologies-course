_ratings = [
    {
        "title": "Shrek",
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True,
        "director": 1,
    },
    {
        "title": "Movie 2",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": True,
        "director": 2,
    },
    {
        "title": "Movie 3",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": False,
        "director": 2,
    },
    {
        "title": "Movie 4",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": False,
        "director": 3,
    },
    {
        "title": "Shrek 2",
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True,
        "director": 1,
    },
]

ratings = {rating["title"]: rating for rating in _ratings}
