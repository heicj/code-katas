"""
MOO32
def human_years_cat_years_dog_years(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]
"""
def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat_age = 0
    dog_age = 0
    if human_years == 1:
        cat_age = 15
        dog_age = 15
    elif human_years ==2:
        cat_age = 24
        dog_age = 24
    else:
        cat_age = 24
        dog_age = 24
        for i in range(2, human_years):
            cat_age += 4
            dog_age += 5
        
    
    
    return [human_years,cat_age,dog_age]
    

