import spacy

nlp = spacy.load('en_core_web_md')
movie_list= []
movies = open('movies.txt','r')
lines = movies.readlines()
for line in lines:
            temp = line.strip()
            temp = temp.split(":")
            movie_list.append(temp)
movies.close()

planet_Hulk = "Will he save the day or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet Sakaar where he can live in peace. Unfortunately, when Hulk lands on the planet Sakaar, he is sold into slavery and trained as a gladiator" 

model_sentence = nlp(planet_Hulk)
best_match_index = 0
best_match_ss = 0.0
for i in range(len(movie_list)):
    similarity = nlp(movie_list[i][1]).similarity(model_sentence)
    #print(movie_list[i], similarity)
    if similarity > best_match_ss:
        best_match_index = i
        best_match_ss = similarity

print(f"{movie_list[best_match_index][0]} is the closest match to Planet Hulk")
print(f"Its description is as follows: {movie_list[best_match_index][1]}")