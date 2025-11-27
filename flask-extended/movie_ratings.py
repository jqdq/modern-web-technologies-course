_ratings = [
    {
        "title": "Shrek",
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True,
    },
    {
        "title": "Movie 2",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": True,
    },
    {
        "title": "Movie 3",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": False,
    },
    {
        "title": "Movie 4",
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": False,
    },
    {
        "title": "Shrek 2",
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True,
    },
]

ratings = {rating["title"]: rating for rating in _ratings}
