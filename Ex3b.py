survey_results = [5, 7, 3, 8]

survey_results = survey_results[:2] + [6] + survey_results[2:]
print(survey_results) # expected output: [5, 7, 6, 3, 8]