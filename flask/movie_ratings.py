_ratings = [
    {
        "title": "Shrek",
        "rating": 7.9,
        "description": "A grumpy ogre embarks on a quest to rescue a princess and unexpectedly finds friendship and love.",
        "owner_review": "Still hilarious after all these years. The Donkey one-liners alone are worth the watch.",
        "length_seconds": 5400,
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True
    },
    {
        "title": "The Matrix",
        "rating": 8.7,
        "description": "A hacker discovers reality is a simulation and joins a rebellion against the machines controlling it.",
        "owner_review": "Perfect blend of action and philosophy. The lobby shootout is still unmatched.",
        "length_seconds": 8160,
        "cat_death": True,
        "violence": True,
        "loud_noises": True,
        "jump_scares": False
    },
    {
        "title": "Finding Nemo",
        "rating": 8.2,
        "description": "A timid clownfish crosses the ocean to rescue his son, helped by a forgetful but big-hearted friend.",
        "owner_review": "Gorgeous animation and genuinely moving. Dory steals every scene she's in.",
        "length_seconds": 6000,
        "cat_death": False,
        "violence": False,
        "loud_noises": True,
        "jump_scares": True
    },
    {
        "title": "Jurassic Park",
        "rating": 8.2,
        "description": "During a preview tour of a dinosaur theme park, the exhibits escape and guests fight to survive.",
        "owner_review": "The T. rex scene holds up better than most modern CGI. Pure blockbuster perfection.",
        "length_seconds": 7620,
        "cat_death": False,
        "violence": True,
        "loud_noises": True,
        "jump_scares": True
    },
    {
        "title": "Groundhog Day",
        "rating": 8.0,
        "description": "A cynical weatherman is forced to relive the same day over and over in a small Pennsylvania town.",
        "owner_review": "A comedy that sneakily becomes profound. Bill Murray at his absolute best.",
        "length_seconds": 6060,
        "cat_death": True,
        "violence": False,
        "loud_noises": False,
        "jump_scares": False
    }
]

ratings = {rating["title"]: rating for rating in _ratings}
