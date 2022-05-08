from bs4 import BeautifulSoup
import requests
import json



def group_by_year(movies):
    years=[]
    keys={}
    
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
            keys.append(years)
            print(years)
                      
    movie_dict={i:[] for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(movies[i])
    # return movie_dict
    with open('top_movie_2.json','w') as file:
        json.dump(movie_dict,file,indent=4)
    return movie_dict
    
group_by_year(adventure)          
            

        
        
        
        
        