import wikipedia



def finder(querry):
    
    results = wikipedia.search(querry, results = 5)
    result_summary = wikipedia.summary(results[0])
    result_title = results[0]
    return [result_summary , result_title , results ]
    
