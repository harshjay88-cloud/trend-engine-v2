modifiers = [
"remix",
"dj",
"nonstop",
"sad",
"rap",
"phonk",
"2026"
]

def expand(keyword):

    results = []

    for m in modifiers:

        results.append(f"{keyword} {m}")

    return results
