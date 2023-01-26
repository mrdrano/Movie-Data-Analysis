#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv("IMDB-Movie-Data.csv", na_values = 0)
df = pd.DataFrame(data)
df = df.fillna(0)


# In[2]:


#1
df1 = df[df["Year"] == 2016]
df1 = df1.nlargest(3,"Rating")
df1[["Title"]]


# In[4]:


#2
actor_revenue = {}
df2 = df[["Actors", "Revenue (Millions)"]]

namee = []  #蒐集actors的list

for name_list in df2["Actors"]:    #先將每個row出現的人名 變為字典中的key值 並把每個的value值預設成0
    for name in name_list.split("|"):
        name = name.strip()
        if name not in actor_revenue:
            actor_revenue[name] = 0
        if name not in namee:
            namee.append(name)
            
for actors, money in zip(df2["Actors"], df2["Revenue (Millions)"]):   #再來就是每個row的演員 對應到money 去除以4平分錢
    for name in actors.split("|"):
        name = name.strip()
        actor_revenue[name] += money/4
        
a_list = []
#計算演員演出的電影有幾部 去平分這個數量 就是average了
for actors in df2["Actors"]:
    a = [x.strip() for x in actors.split("|")]
    a_list.append(a)
    
i = 0   #這邊用來計算總共出現的次數
times = []
for name in (list(actor_revenue.keys())):
    i = 0
    for sublist in a_list:
        if name in sublist:
            i += 1
    times.append(i)

#除以總共出現的次數
for actor, tt in zip(list(actor_revenue.keys()), times):
    actor_revenue[actor] = actor_revenue[actor]/tt

final = []

my_revenues = sorted(actor_revenue, key= actor_revenue.get, reverse = True)
final.append(my_revenues[0])
k = 0
while 1:
    if actor_revenue[(my_revenues[0])] == actor_revenue[(my_revenues[k+1])]: #如果第一位的收入 等於2~n位的話 就印出來(相等並列)
        final.append(my_revenues[k+1])
        k += 1
    else:
        break
print(final)
#idx_revenue = list(actor_revenue.values()).index(max(list(actor_revenue.values())))
#print(list(actor_revenue.keys())[idx_revenue])


# In[26]:


#3
emma_rating = {"Emma Watson" : 0}
appearance = 0
df3 = df[["Actors","Rating"]]

for name_list, rating in zip(df3["Actors"], df3["Rating"]):
    list_name = []
    for name in name_list.split("|"):
        name = name.strip()
        list_name.append(name)
    
    if "Emma Watson" in list_name:
        appearance += 1
        emma_rating["Emma Watson"] += rating
print(emma_rating["Emma Watson"] / appearance)


# In[53]:


#4
director_actor = {}         #這兩個字典分別是導演 : 演員的list
director_actorNum = {}      #導演 : 演員的個數

df4 = df[["Director", "Actors"]]
for director in df4["Director"]:
    if director not in director_actor:
        director_actor[director] = []
        director_actorNum[director] = 0

for director, actors in zip(df4["Director"], df4["Actors"]):  #將合作過的演員 加入字典中，屬於導演的value list中
    actors = actors.split("|")
    for each_actor in actors:
        each_actor = each_actor.strip()
        if each_actor not in director_actor[director]:
            director_actor[director].append(each_actor)

for k,v in director_actor.items():        #遍歷導演將合作過的演員value list，計算長度後，加入字典中每個導演的value值 
    length = (len(v))
    director_actorNum[k] = (length)

my_directors = sorted(director_actorNum, key= director_actorNum.get, reverse = True)

#尋找是否有跟最高合作的數量 同樣數量的導演
dir_most = []
dir_most.append(my_directors[0])
k = 0
while 1:
    if director_actorNum[(my_directors[0])] == director_actorNum[(my_directors[k+1])]: #如果第一位的收入 等於2~n位的話 就印出來(相等並列)
        dir_most.append(my_directors[k+1])
        k += 1
    else:
        break

print(dir_most)


# In[7]:


#5
actor_genre = {} #創一個字典，用來存放每個演員演過的電影種類
actor_genreNum = {}
df5 = df[["Genre", "Actors"]]


for actors in df["Actors"]: #將每個演員都當作字典的key 然後value list是要存演出的電影種類
    for name in actors.split("|"):
        name = name.strip()
        if name not in actor_genre:
            actor_genre[name] = []
            actor_genreNum[name] = 0
                            #用來存放演員所出現過電影的種類
for actor, genre in zip(df["Actors"], df["Genre"]):
    name_list = [x.strip() for x in actor.split("|")]
    genre_list = genre.split("|")
    
    for nn in name_list:
        for gg in genre_list:
            if gg not in actor_genre[nn]:
                actor_genre[nn].append(gg)

for k,v in actor_genre.items():        #遍歷演員演出過的genre value list，計算長度後，加入字典中每個演員Num的value值 
    length = len(v)
    actor_genreNum[k] = (length)


my_genre = sorted(actor_genreNum, key= actor_genreNum.get, reverse = True)

#尋找是否有跟最高合作的數量 同樣數量的導演
genre_most = []
genre_sec = []
genre_most.append(my_genre[0])
k = 0
num_Max = actor_genreNum[my_genre[0]]

for i in range(1, len(my_genre)):
    if actor_genreNum[my_genre[0]] == actor_genreNum[my_genre[i]]:
        genre_most.append(my_genre[i])
    if (actor_genreNum[my_genre[0]]-1) == actor_genreNum[my_genre[i]]:
        genre_sec.append(my_genre[i])
    else:
        break
print(genre_most)
print(genre_sec)


# In[7]:


#6
actor_movie = {}
movie_year = {}
actor_year = {}
df6 = df[["Title", "Actors", "Year"]]

for actors, movie in zip(df["Actors"], df["Title"]):
    for name in actors.split("|"):
        name = name.strip()
        if name not in actor_movie:
            actor_movie[name] = []
            actor_movie[name].append(movie)
        else:
            actor_movie[name].append(movie)
            
for movie, year in zip(df["Title"], df["Year"]):
    movie_year[movie] = year
    
# 先找出誰演出的電影 再由電影去map到年分
for k,v in actor_movie.items():  # {"actor" : movie}
    for movie in actor_movie[k]:
        if k not in actor_year:
            actor_year[k] = []
            actor_year[k].append(movie_year[movie])
        else:
            actor_year[k].append(movie_year[movie])

year_difference = [] #再來 由這些出現的電影年份中 去找最大最小值 並相減 得到差多少
for name, year_list in actor_year.items():
    difference = max(actor_year[name]) - min(actor_year[name])
    year_difference.append(difference)
    
list1 = list(set(year_difference)) # set可以找到不重複的值 然後轉型成list
actor_list = list(actor_year.keys())  #在字典中取出 keys 也就是各個人名

#挑取前三位最大的gap year
top1 = list1[-1]
top2 = list1[-2]
top3 = list1[-3]
top1_name = []
top2_name = []
top3_name = []

#去比對哪些演員的年齡會等於top1 2 3 是的話就可以編入top1 2 3_name中 並且印出 
for i in range(len(year_difference)):
    if year_difference[i] == top1:
        top1_name.append(actor_list[i])
    if year_difference[i] == top2:
        top2_name.append(actor_list[i])
    if year_difference[i] == top3:
        top3_name.append(actor_list[i])

one = pd.DataFrame({"Top 1": top1_name})
two = pd.DataFrame({"Top 2": top2_name})
three = pd.DataFrame({"Top 3": top3_name})

#print(top1_name)
#print(top2_name)
print(one)
print(two)
print(three)


# In[8]:


df7 = df[["Actors"]]
name_list = []
for i in range(len(df7)):  #要將每一行的string給split掉 並且空格strip掉
    each = [x.strip() for x in df7["Actors"][i].split("|")]
    name_list.append(each) #放置在name_list中
    
#先找出Johnny Depp在的SubList 那些人名都要拿出
no_johnny1 = []
search_list1 = []
for name in name_list:
    if "Johnny Depp" not in name:   #subList中的遍歷查找Johnny 是否在裡面
        no_johnny1.append(name)     #沒的話 存在no_johnny1裡面 當作下次
    else:                           #遍歷尋找的List
        for nn in name:
            if nn != "Johnny Depp" and nn not in search_list1:
                search_list1.append(nn) #有直接/間接的 存在search_list中
#print(search_list1)                     #下次用這個去遍歷 尋找是否這些人存在
#print(no_johnny1)

search_list2 = []
no_johnny2 = []
for search_element in search_list1:
    for sub_list in no_johnny1:
        if search_element in sub_list:
            for nn in sub_list:
                if nn != search_element and nn not in search_list2:
                    search_list2.append(nn)
search_list3 = []
for subList in (no_johnny1):   #no_johnny1的每個subList去遍歷
    flag = 0
    for i in range(len(search_list2)):  #把search_list2的每個人 去判斷是否in 存在1人in the sublist時 flag訂為1
        if search_list2[i] in subList:
            flag = 1
            for nn in subList:
                if nn != search_list2[i] and nn not in search_list3:
                    search_list3.append(nn)
    if flag == 0:                       #只有當那個sublist被所有search_list2的人名遍歷結束 且都沒有在裡面時 再加入no_johnny2
        no_johnny2.append(subList)

#print(search_list3)  #因為search_list3是empty list 所以代表搜尋這些 if direct/indirect name in sublist完畢
search_list4 = []
no_johnny3 = []
for subList in (no_johnny2):  
    flag = 0
    for i in range(len(search_list3)): 
        if search_list3[i] in subList:
            flag = 1
            for nn in subList:
                if nn != search_list3[i] and nn not in search_list4:
                    search_list4.append(nn)
    if flag == 0:                       
        no_johnny3.append(subList)

search_list5 = []
no_johnny4 = []
for subList in (no_johnny3):   
    flag = 0
    for i in range(len(search_list4)):  
        if search_list4[i] in subList:
            flag = 1
            for nn in subList:
                if nn != search_list4[i] and nn not in search_list5:
                    search_list5.append(nn)
    if flag == 0:                      
        no_johnny4.append(subList)

search_list6 = []
no_johnny5 = []
for subList in (no_johnny4):   
    flag = 0
    for i in range(len(search_list5)):  
        if search_list5[i] in subList:
            flag = 1
            for nn in subList:
                if nn != search_list5[i] and nn not in search_list6:
                    search_list6.append(nn)
    if flag == 0:                      
        no_johnny5.append(subList)

search_list7 = []
no_johnny6 = []
for subList in (no_johnny5):   
    flag = 0
    for i in range(len(search_list6)):  
        if search_list6[i] in subList:
            flag = 1
            for nn in subList:
                if nn != search_list6[i] and nn not in search_list7:
                    search_list7.append(nn)
    if flag == 0:                      
        no_johnny6.append(subList)

#search_list7 出來是空的 所以到這邊就結束
total = search_list1 + search_list2 + search_list3 + search_list4 + search_list5 + search_list6 
print(total)


# In[ ]:




