import fresh_tomatoes
import media

#Opens a text file containing movie info
with open('movie_list.txt', 'r') as myfile:
    #store the file contents into a variable
    data=myfile.read().replace('\n', '')
    
#stores the file contents in an array structure
moviesList = eval('['+data+']')
movies=[]
print moviesList

#add each movie from the file into the movies array
for m in moviesList:
    movie = m.split(',')
    movies.append(media.Movie(movie[0],movie[1],movie[2],movie[3]))
    movies.append
    
fresh_tomatoes.open_movies_page(movies)
