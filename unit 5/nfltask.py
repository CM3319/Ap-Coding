scores = [85, 92, 78, 60, 88, 73]

def calculate_average_passing(score_list):
    total = 0
    passing_count = 0
    
    
    for score in score_list:
        total += score
        
        
        if score >= 70:
            passing_count += 1
    

    average = total / (score_list)
    
    return average, passing_count


avg, passing = calculate_average_passing(scores)

print("Average score:", avg)
print("Number of passing scores:", passing)