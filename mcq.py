questions=[
    ["Whose incomplete autobiography is SATTAR BATSAR?", "Rabindranath Tagore", "Sarala Devi Chowdhurani", "Chittaranjan Das", "Bipinchandra Pal", 4],
    
    ["When the weekly magazine SOMPRAKASH first published?", "12th March, 1958", "16th August, 1837", "15th November, 1858", "2nd January, 1862", 3],
    
    ["JEEVANSMRITI memoir belongs to whom?", "Manikuntala Sen", "Narayan Sanyal", "Rabindranath Tagore", "Bipinchandra Pal", 3],
    
    ["BANGADARSHAN first published in...", "1818", "1858", "1872", "1875", 3],
    
    ["Who is the author of Ecological Imperialism?", "Stanley Jackson", "Elizabeth Whithcomb", "Ramchandra Guha", "Alfred Crosby", 4],
    
    ["Which one is the first Bengali political magazine?", "Somprakash", "Bangadarshan", "Probashi", "Hitobadi", 1],
    
    ["CALCUTTA CRICKET CLUB is established in...", "1792", "1813", "1854", "1867", 1],
    
    ["In which year Mohunbagan won the I.F.A shield for the first time?", "1913", "1912", "1911", "1910", 3],
    
    ["Who is the director of the film HARISHCHANDRA?", "Satyajit Ray", "Dadasahib Phalke", "Mrinal Sen", "Hritwik Ghatak", 2],
    
    ["Who is the writer of the play NABANNA?", "Utpal Dutta", "Surendra Binodini", "Bijon Bhattacharya", "Rajnikant Sen", 3],
    
    ["When WORLD ENVIROMENT DAY was first celebrated?", "12th Jan, 1989", "5th June, 1974", "1st May, 1923", "5th September, 1987", 2],
]

pts=0
pts1=0
for i in range(0, len(questions)):
    q=questions[i]
    print(f"\nQ{i+1}.", q[0])
    print(f"a. {q[1]}        b. {q[2]}")
    print(f"c. {q[3]}        d. {q[4]}")
    reply=int(input("Your Answer (1-4): "))
    if reply==q[-1]:
        print(f"\nCorrect Answer, +{pts1+5}points")
        pts1=pts1+5
        pts=pts + ((i+1)*5)
    else:
        print("Ohhhh...Wrong Answer")
        break
print(f"Total Score {pts}")