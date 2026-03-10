from collectors.youtube_suggest import get_suggestions
from engine.keyword_expander import expand

base = "music"

keywords = get_suggestions(base)

for k in keywords:

    expanded = expand(k)

    print("Base:",k)

    print("Expanded:",expanded)
