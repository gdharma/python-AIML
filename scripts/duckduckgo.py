import duckduckgo

r = duckduckgo.query('DuckDuckGo')
if r.type == 'answer':
    print(r.results)