def Movie(link):
    with open(link,"r") as f: #Top-3 movies with the highest ratings in 2016?

        list_rating = []
        movie_name = []
        revenues = []
        actors = []
        directors = []
        rating = []
        genre = []
        movie_year = []

        index_year = 5
        index_rating = 7
        index_movie = 1
        index_revenue = 9
        index_actors = 4
        index_director = 3
        index_genre = 2

        for line in f:
            to_list = line[:-1].split(",")
            if ((to_list[0]).isdigit()):
                list_rating.append((int(to_list[5]),float(to_list[7])))
                movie_name.append(to_list[1])
                actors.append(to_list[4])
                directors.append(to_list[3])
                rating.append(to_list[7])
                movie_year.append((to_list[1], int(to_list[5])))
                genre.append(to_list[2])

                if(to_list[9] == ""):
                    revenues.append(0.0)
                else:
                    revenues.append(float(to_list[9]))

        each_after_strip = []           # put each line's movie actors in a tuple and append in the list
        for each in actors:
            each = each.split("|")
            after_strip = [every.strip() for every in each]
            each_after_strip.append(tuple(after_strip))

        #print(each_after_strip)

        actor_dict = {}                                  # In want of creating a dict that can set (key = actor ; value = genre played)
        for i in range(1000):                            # I apply this for loop and meanwhile below this loop
            for each_actor in each_after_strip[i]:       # count the number of genre that each actor play
                if(actor_dict.get(each_actor) == None):
                    actor_dict[each_actor] = []
        #print(actor_dict)
        for i in range(1000):
            for each in each_after_strip[i]:
                if(genre[i] not in actor_dict[each]):
                    actor_dict[each].append(genre[i])

        number_of_playing = []
        for actor_name in actor_dict:
            number_of_playing.append(len(actor_dict[actor_name]))
        #print(actor_dict)


        # 5
        max_playing_genre = max(number_of_playing)         # want to find the max number play and search its index to store in index_list
        tier_playing_genre = max(number_of_playing) -1     # and the second-tier is also by the same solution
        max_index_list = []                                # later store the index's corresponding name in the lists
        tier_index_list = []
        max_index_name = []
        tier_index_name = []

        for i in range(len(number_of_playing)):
            if (number_of_playing[i] == max_playing_genre):
                max_index_list.append(i)
            if (number_of_playing[i] == tier_playing_genre):
                tier_index_list.append(i)
        #print(max_index_list)
        #print(tier_index_list)

        for num in max_index_list:                               # find in the actor_dict index which is equall to max, tier num(index)
            max_index_name.append(list(actor_dict)[num])         # then store in the corresponding lists
        for num in tier_index_list:
            tier_index_name.append(list(actor_dict)[num])

        #print(max_index_name)
        #print(tier_index_name)



        # 4
        #print(directors)
        dict_name = {}

        for i in range(1000):                          # create a dict_name to put { director : [actor's name] }
            if (dict_name.get(directors[i]) == None):  # and store it in once 
                dict_name[directors[i]] = []

                for each in each_after_strip[i]:
                    if(each not in dict_name[directors[i]]):
                        dict_name[directors[i]].append(each)
            else:
                if (each not in dict_name[directors[i]]):
                    dict_name[directors[i]].append(each)

        #print(dict_name)
        list_num_of_actors = []                       # using list_num_of_actors to store each director's collaborating number
        for key in dict_name:                         # and then find the max number and the tier
            num = len(dict_name.get(key))             
            list_num_of_actors.append(num)

        #print(list_num_of_actors)
        name_top3 = []                               # find the biggest num's index 
                                                     # and print it
        top_three_actors_index = sorted(range(len(list_num_of_actors)), key=lambda i: list_num_of_actors[i])[-3:]
        for i in range(len(directors)):
            if (i == top_three_actors_index[0] or i== top_three_actors_index[1] or i == top_three_actors_index[2]):
                name_top3.append(directors[i])
        #print(name_top3)
        #print(top_three_actors_index)
        



        # 6 and 2
        #print(dict(movie_year))
        movie_actor = {}
        for j in range(1000):                       # creating a dict (novie_actor) like => movie:[] and want to store actors who played in
            for each_movie in movie_year:
                if(movie_actor.get(each_movie[0]) == None):
                    movie_actor[each_movie[0]] = []

        actors_dict = {}
        actors_revenue = {}

        for k in range(1000):                      # each_after_strip is tuples that each movie's actors who play
            for each_person in each_after_strip[k]:# and I used the loop to store each movie's who play
                if(each_person not in movie_actor[movie_year[k][0]]):
                    movie_actor[movie_year[k][0]].append(each_person)
        #print(movie_actor)

        for i in range(1000):                      # It's the opposie of the last one that means just reverse keys and values
            for each in each_after_strip[i]:       # Ex : Actors' name : [Movie they played]
                if(actors_dict.get(each) == None): # Meanwhile in #2 I create an empty-value dict for actors to store their revenues to count
                    actor_dict[each] = []
                    actors_revenue[each] = []

        #print(actors_revenue)                    # also I create actors_revenue to collect each actor's revenue append them in the
        #print(movie_actor)                       # corresponding dict value list
        count = 0
        for k,v in movie_actor.items():
            for each in v:
                actors_revenue[each].append(revenues[count])
            count += 1
        #print(actors_revenue)
        total_revenue = []

        for k,v in actors_revenue.items():       # then add up each revenues and append in total_revenue
            sum = 0                              # then find the max's index and print out
            times = len(v)
            for num in v:
                sum += num
            total_revenue.append(sum/times)

        #print(total_revenue)
        max_revenue = max(total_revenue)              # There's no individual revenue in this operation, instead;
        max_revunue_index1 = total_revenue.index(max_revenue)

        #print(total_revenue)                         # Only calculating those in the same movie and then add the revenue to the four people and then divide the times
        #print(max_revunue_index1)                     # Reason : Not sure about each actor's reputation and time they appeared in the movie, just divide number of movies they play
        remaining_revenue = total_revenue[max_revunue_index1+1:]
        #print(remaining_revenue)
        mmax = max(remaining_revenue)
        revenue2 = total_revenue[max_revunue_index1+1:]
        index2 = revenue2.index(mmax)
        index2 += (1+max_revunue_index1)
        #print(index2)
        wealth_money = total_revenue[max_revunue_index1]  # 936.63
        #print(wealth_money)

        wealthy_man = []
        for i in range(len(list(actors_revenue))):
            if (i == max_revunue_index1 or i == index2):
                wealthy_man.append(list(actors_revenue)[i])

        #print(wealthy_man)

        for k,v in movie_actor.items():
            for each in v:
                actor_dict[each].append(k)
        #print(actor_dict)


        every_playing_year = []                    # This is through actor_dict by checking each actor's playing movie
        for key_name in actor_dict:                # and we have movie_year( movie : year) tuples set to be seen through
            each_movie_year = []                   # so that every_playing_year can be shown in years that every actor played

            for each_movie in actor_dict[key_name]:
                each_movie_year.append((dict(movie_year)[each_movie]))
            every_playing_year.append(each_movie_year)

        #print(every_playing_year)
        difference = []                            # In order to find out the 1st, 2nd, 3rd maximum gap year
        for the_list in every_playing_year:
            MMax = max(the_list)
            mmin = min(the_list)
            difference.append(MMax-mmin)
        #print(difference)
        max_list = []
        tier_list = []
        third_list = []
        difference_max = max(difference)         #10 9 8
        difference_tier = max(difference) -1
        difference_third = max(difference) -2
        for i in range(len(difference)):            # I need to find each actor's biggest gap year with 1st, 2nd, 3rd
            if (difference[i] == difference_max):
                max_list.append(i)
            if (difference[i] == difference_tier):
                tier_list.append(i)
            if (difference[i] == difference_third):
                third_list.append(i)

        max_name_list = []
        tier_name_list = []
        third_name_list = []                        # Since I have 1st, 2nd, 3rd index,
        for i in range(len(list(actor_dict))):      # use for loop when i goes to corresponding index and then append to three kinds of lists
            if (i in max_list):                     # through the year difference
                max_name_list.append(list(actor_dict)[i])
            if (i in tier_list):
                tier_name_list.append(list(actor_dict)[i])
            if (i in third_list):
                third_name_list.append(list(actor_dict)[i])



        
        # 7  
        #print(each_after_strip)          # this is a bit onerous that burden the time-complexity but I deem it can be applied in tree
        direct_list = []                  # 1. search tuples containing Johnny Depp and append those name
        indirect_list1 = []               # 2. using those name to search tuples, if in them, then append
        new_remaining_list = []           # 3. do the same as (2.) and until the 6th time it will end the searching
        for each_set in each_after_strip:
            if('Johnny Depp' in each_set):
                for every_person in each_set:
                    if(every_person != 'Johnny Depp' and every_person not in direct_list):
                        direct_list.append(every_person)

        #print(direct_list)
        #print(each_after_strip)
        new_actor_list1 = []
        new_actor_list2 = []

        for direct_name in direct_list:
            for i in range(len(each_after_strip)):
                if (direct_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if(each_name not in new_actor_list1):
                            new_actor_list1.append(each_name)
        #print(new_actor_list1)
        collaboration = direct_list + new_actor_list1
        #print(collaboration)

        for the_name in collaboration:
            for i in range(len(each_after_strip)):
                if(the_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if(each_name not in collaboration):
                            new_actor_list2.append(each_name)
        #print(new_actor_list2)
        collaboration += new_actor_list2

        new_actor_list3 = []
        for the_name in collaboration:
            for i in range(len(each_after_strip)):
                if(the_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if(each_name not in collaboration):
                            new_actor_list3.append(each_name)

        #print(new_actor_list3)
        collaboration += new_actor_list3

        new_actor_list4 = []
        for the_name in collaboration:
            for i in range(len(each_after_strip)):
                if(the_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if(each_name not in collaboration):
                            new_actor_list4.append(each_name)

        #print(new_actor_list4)
        collaboration += new_actor_list4

        new_actor_list5 = []
        for the_name in collaboration:
            for i in range(len(each_after_strip)):
                if(the_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if(each_name not in collaboration):
                            new_actor_list5.append(each_name)

        #print(new_actor_list5)
        collaboration += new_actor_list5

        new_actor_list6 = []
        for the_name in collaboration:
            for i in range(len(each_after_strip)):
                if (the_name in each_after_strip[i] and "Johnny Depp" not in each_after_strip[i]):
                    for each_name in each_after_strip[i]:
                        if (each_name not in collaboration):
                            new_actor_list6.append(each_name)

        #print(new_actor_list6)             an empty list
        collaboration += new_actor_list6
        #print(collaboration)
        



        # 3
        position = []                     # use count_where_emma to find in the each_after_strip tuples, emma's index
        count_where_emma = 0              # and then be stored in position
        for each_tuple in each_after_strip:
            for every in each_tuple:
                if(every == "Emma Watson"):
                    position.append(count_where_emma)
                    #print(each_after_strip[count_where_emma])
            count_where_emma += 1

        #print(position)
        sum = 0.0                        # rating is each movie's rating so I find movies that emma played and
        quantities = len(position)       # add up in sum, divide to find the average
        for i in range(quantities):
            rr = float(rating[i])
            sum += rr


        kkk = 0
        #print(average_rating_emma)
        for i in position:
            kkk += ((float(rating[i])))
        average_rating_emma = kkk/len(position)
        print(average_rating_emma)

        # 1 
        each_set_rating = []                # store each in list_rating that comes from the toppest operation in line
        for each_set in list_rating:        # and to search in 2016's rating only
            if(each_set[0] == 2016):
                each_set_rating.append(each_set[1])

        top_three_rating = sorted(range(len(each_set_rating)), key=lambda i: each_set_rating[i])[-3:]

        top1 = (2016, each_set_rating[top_three_rating[2]])
        top2 = (2016, each_set_rating[top_three_rating[1]])
        top3 = (2016, each_set_rating[top_three_rating[0]])

        top1_index = list_rating.index(top1) #2
        top2_index = list_rating.index(top2) #4
        top3_index = list_rating.index(top3) #15



        print(f"1. Top 1 with the highest ratings in 2016 is : {movie_name[top1_index]}")
        print(f"1. Top 2 with the highest ratings in 2016 is : {movie_name[top2_index]}")
        print(f"1. Top 3 with the highest ratings in 2016 is : {movie_name[top3_index]}")

        print(f"2. The actor generating the highest average revenue is : {wealthy_man}")

        print(f"3. The average rating of Emma Watson’s movies is : {average_rating_emma}")
        print(f"4. Top-3 directors who collaborate with the most actors : {name_top3}")

        print(f"5. Top-1 actors playing in the most genres of movies : {max_index_name}")
        print(f"5. Top-2 actors playing in the most genres of movies : {tier_index_name}")

        print(f"6. Top 1 actors whose movies lead to the largest maximum gap of years : {max_name_list}")
        print(f"6. Top 2 actors whose movies lead to the largest maximum gap of years : {tier_name_list}")
        print(f"6. Top 3 actors whose movies lead to the largest maximum gap of years : {third_name_list}")

        print(f"7. All actors who collaborate with Johnny Depp in direct and indirect ways : {collaboration}")

link = "IMDB-Movie-Data.csv"
Movie(link)
