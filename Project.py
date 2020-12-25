import pickle  # importing the library for serialization and saving

# if you want to know the content of the dictionaries, just print them)
dict1 = {}  # username - key, article - content
dict2 = {}  # article - key, direct article reports list - content
dict3 = {}  # article - key, .txt file name - content
dict4 = {}  # username - key, user info - content
list1 = []  # anchor articles
dict6 = {}  # article - key, indirect article reports list - content
dict5 = {}  # username - key, user friend list - content

acc = ""  # stores the username of a current user


def save(dict1, dict2, dict3, dict4, dict5, dict6, list1):
    """This is made just to save the dicts into the .pickle
        serialized file. So whenever the data gets uploaded
        this function should be called"""
    pickle_out = open("dict1.pickle", "wb")
    pickle.dump(dict1, pickle_out)
    pickle_out.close()
    pickle_out = open("dict2.pickle", "wb")
    pickle.dump(dict2, pickle_out)
    pickle_out.close()
    pickle_out = open("dict3.pickle", "wb")
    pickle.dump(dict3, pickle_out)
    pickle_out.close()
    pickle_out = open("dict4.pickle", "wb")
    pickle.dump(dict4, pickle_out)
    pickle_out.close()
    pickle_out = open("dict5.pickle", "wb")
    pickle.dump(dict5, pickle_out)
    pickle_out.close()
    pickle_out = open("dict6.pickle", "wb")
    pickle.dump(dict6, pickle_out)
    pickle_out.close()
    pickle_out = open("list1.pickle", "wb")
    pickle.dump(list1, pickle_out)
    pickle_out.close()


def startup():
    """This function works once in the beginning of the program
        to fill the dictionaries with actual data from .picle files"""
    pickle_in = open("dict1.pickle", "rb")
    dict1 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("dict2.pickle", "rb")
    dict2 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("dict3.pickle", "rb")
    dict3 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("dict4.pickle", "rb")
    dict4 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("dict5.pickle", "rb")
    dict5 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("dict6.pickle", "rb")
    dict6 = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open("list1.pickle", "rb")
    list1 = pickle.load(pickle_in)
    pickle_in.close()
    return dict1, dict2, dict3, dict4, dict5, dict6, list1


def pr(facc):
    """This function is basically the UI of the system"""
    if facc != "":
        print("User:", facc)  # facc is changed depending on which user is logged in
    print("Create an account - 1")
    print("Login - 2")
    print("Add a friend - 3")
    print("Upload an article - 4")
    print("isFriend - 5")
    print("isDirectSource - 6")
    print("isSource - 7")
    print("Report - 8")
    print("DirectReport - 9")
    print("Anchor - 10")
    print("Article info - 11")
    print("User info - 12")
    print("Exit - 13")
    print("KOL Analysis - 14")
    print("Relevance between Friendship and Quoting - 15")


def NicePrintA(dict3, num):
    """Prints out the information about an article from attached .txt files"""
    article_label = dict3[num]
    file = open(article_label, "r")
    text = file.read()
    print(text)


def NicePrintU(dict1, dict4, dict5, user):
    """Prints out the information about a user from dictionaries"""
    if user in dict4 and user in dict5:
        print("Name:", dict4[user][0])
        print("Friends", len(dict5[user]), ":")
        for i in range(0, len(dict5[user]), 1):
            print(dict5[user][i])
        print("User's articles", len(dict1[user]), ":")
        for i in range(0, len(dict1[user]), 1):
            print(dict1[user][i])
    else:
        print("This user does not exist!")


def reg(dict1, dict4, dict5):
    """This function registrates the user and adds his/her info into the
        dictionaries. Also it has some protection and repitition checks"""
    username = input("Input the username for your account: ")
    username = username.lower()
    password = input("Create a password for your account: ")
    name = input("What is your full name: ")
    while True:
        if username in dict4:  # check for username repitition
            print("That username is already occupied!")
            username = input("Input another username for your account: ")
            username = username.lower()
        if len(password) < 9:  # check for the length of the password
            print("The password is too short!")
            password = input("Create another password for your account: ")
        else:
            dict1.update({username: []})
            dict4.update({username: [name, password]})
            dict5.update({username: []})
            save(dict1, dict2, dict3, dict4, dict5, dict6, list1)
            print("Your account has been registered!")
            break


def log(dict1, dict4, dict5):
    """This function looks for a user input's content in dictionaries
        and logins if the input is correct. The 'facc', which contains a username
        is created in this function (and returned)"""
    username = input("Input the username: ")
    password = input("Input the password: ")
    facc = ""
    while True:
        if username.lower() in dict4 and dict4[username][1] == password:
            print("You have successfully logged in!")
            facc = username
            break
        else:
            print("Username or password is not correct!")
            print("Exit login - 1")
            print("Try again - 2")
            finp = int(input())
        if finp == 1:
            break
            facc = ""  # no 'facc' if login is not correct
        else:
            username = input("Input the username: ")
            password = input("Input the password: ")
    return facc


def addFriend(dict1, dict4, dict5, facc):
    """Here a user adds friends and uploads new data into the dictionaries.
        Therefore, save() is used."""
    if facc != "":
        username = input("Input the username of the user: ")
        username = username.lower()
        if username != facc:
            if username not in dict5[facc]:
                if username in dict5:
                    dict5[username].append(facc)  # updated dict5
                    dict5[facc].append(username)  # uptaded for a friend also
                    save(dict1, dict2, dict3, dict4, dict5, dict6, list1)
                    print("The user is your friend now!")
                    return facc
                else:
                    print("The user does not exist!")
                    return facc
            else:
                print("The user is already your friend!")
                return facc
        else:
            print("You can not add yourself as a friend!")
            return facc
    else:
        print("You are not logged in!")
        print("Go to Login - 1")
        print("Exit to menu - 2")
        inp = int(input())
        if inp == 1:
            facc = log(dict1, dict4, dict5)
            return facc
        else:
            facc = ""
            return facc


def addArticle(facc, dict1, dict2, dict3, dict6, list1):
    """This function creates a .txt file using the user input. It asks for title, content, date of the articles
        Also, some dictionaries that contain an information about the articles get updated. This is important, because
        the dictionaries that store articles relationship (direct and indirect) also are modified."""
    key = ""
    article_label = str(len(dict2) + 1)
    article_label += ".txt"
    length = str(len(dict2) + 1)
    if facc == "":
        print("You are not logged in!")
        print("Go to Login - 1")
        print("Exit to menu - 2")
        inp = int(input())
        if inp == 1:
            facc = log(dict1, dict4, dict5)
            return facc
        else:
            facc = ""
            return facc
    else:
        print()
        title = input("Input the title of the article: " + "\n")
        content = input("Inout the content of the article: " + "\n")
        date = input("Input the creation date of the article: " + "\n")
        quote = input("Which article do you quote ? (Press Enter if this article is not a report)")
        if quote == "":
            list1.append(length)
            dict1[facc].append(length)
            dict2.update({length: []})
            dict3.update({length: article_label})
            dict6.update({length: []})
        else:
            if quote in dict2:
                dict1[facc].append(length)
                dict2.update({length: []})
                dict2[quote].append(length)
                dict3.update({length: article_label})
                dict6.update({length: []})
                for i in list1:
                    if quote in dict6[i]:  # this loop looks for the anchor of the quoted article
                        quote = i
                dict6[quote].append(length)
                for i in range(0, len(dict6[quote]),
                               1):  # this loop adds the 'new' article to every report article of the anchor
                    key = dict6[quote][i]
                    if key == length:
                        break
                    else:
                        dict6[key].append(length)

        full = "Username: " + facc + "\n" + "Date: " + date + "\n" + "Title: " + title + "\n" + "Content: " + "\n" + content
        output_file = open(article_label, "w")
        output_file.write(full)
        output_file.close()
        return facc


def isFriend(X, Y):
    if X in dict5:
        if Y in dict5.get(X):
            return True
        else:
            return False


def isDirectSource(A, B):
    if A in dict2:
        if B in dict2.get(A):
            return True
        else:
            return False


def isSource(A, B):
    if A in dict6:
        if B in dict6.get(A):
            return True
        else:
            return False


def Anchor(A):
    while True:
        for i in list1:
            for j in dict2.get(i):
                if j == A:
                    return i


def Report(A):
    return dict6.get(A)


def DirectReport(A):
    return dict2.get(A)


def kol(reports, authors_articles, threshold, percentage):
    '''This function aims to find KOL'''

    # determing influence of anchors
    anchor_influence = {}
    for a in reports.keys():
        anchor_influence[a] = len(reports[a])

    # determing influence of authors
    influence_author0 = {}
    for author in authors_articles.keys():
        influence_author0[author] = 0
    for b in anchor_influence.keys():
        for c in authors_articles.keys():
            for d in authors_articles[c]:
                if b == d:
                    influence_author0[c] = influence_author0[c] + anchor_influence[b]
    # arrange authors by influence
    influence_author = {}
    for d in range(0, len(influence_author0)):
        maxi = -1
        influencer = 0
        for e in influence_author0.keys():
            if influence_author0[e] > maxi:
                maxi = influence_author0[e]
                influencer = e
        influence_author[influencer] = influence_author0[influencer]
        del influence_author0[influencer]

    # get the qualified users and return kol list
    number = int(len(influence_author) * percentage)
    author_list = list(influence_author.keys())
    kol_list = []
    # the final threshold is the bigger one between the input threshold and the influence of the smallest influence within the percentage range
    if influence_author[author_list[number - 1]] > threshold:
        for k in influence_author.keys():
            if influence_author[k] >= influence_author[author_list[number - 1]]:
                kol_list.append(k)
    else:
        for h in influence_author.keys():
            if influence_author[h] >= threshold:
                kol_list.append(h)
    return kol_list


def report_friend(reports, authors_articles):
    '''Check if friends tend to quote each other'''

    is_friend = 0
    not_friend = 0
    new_reports = {}
    # delete articles with no reports
    for anchor0 in reports.keys():
        if len(reports[anchor0]) != 0:
            new_reports[anchor0] = reports[anchor0]
    for anchor in new_reports.keys():
        friend0 = "none"
        friend1 = "none"
        # find author of the anchor
        for author0 in authors_articles.keys():
            for article0 in authors_articles[author0]:
                if anchor == article0:
                    friend0 = author0
        for repo in new_reports[anchor]:
            # find author of the report
            for author1 in authors_articles.keys():
                for article1 in authors_articles[author1]:
                    if repo == article1:
                        friend1 = author1
            if isFriend(friend0, friend1):
                is_friend += 1
            elif not isFriend(friend0, friend1):
                not_friend += 1
    print("Number of reports made by friends:", is_friend)
    print("Number of reports made by strangers", not_friend)
    if is_friend > not_friend:
        print("So, friends tend to quote each other.")
    else:
        print("So, friends do not tend to quote each other")


dict1, dict2, dict3, dict4, dict5, dict6, list1 = startup()
pr(acc)
inp = int(input("What action to perform?"))

while True:
    """The main loop of the system which evaluates the input and calls functions. """
    if inp == 13:
        print("Bye bye")
        break
    if inp == 1:
        reg(dict1, dict4, dict5)
    if inp == 2:
        acc = log(dict1, dict4, dict5)
    if inp == 3:
        acc = addFriend(dict1, dict4, dict5, acc)
    if inp == 4:
        acc = addArticle(acc, dict1, dict2, dict3, dict6,
                         list1)  # facc and acc are the same, f - function acc. Just to make clear
    if inp == 5:
        pers1 = input("Please enter the name of 1st person")
        pers2 = input("Please enter the name of 2nd person")
        if pers1 not in dict5 or pers2 not in dict5:
            print("These people not found in the system!")
        else:
            if isFriend(pers1, pers2):
                print("They are friends")
            else:
                print("They are not friends")
    if inp == 6:
        sour1 = input("Please enter the Source name")
        sour2 = input("Please enter the report name")
        if sour1 not in dict2 or sour2 not in dict2.get(sour1):
            print("You entered wrong articles!")
        else:
            if isDirectSource(sour1, sour2):
                print(sour1, " is a direct source of", sour2)
            else:
                print(sour1, " is not a direct source of", sour2)
    if inp == 7:
        sour1 = input("Please enter the Source name")
        sour2 = input("Please enter the report name")
        if sour1 not in dict6 or sour2 not in dict6.get(sour1):
            print("You entered wrong articles!")
        else:
            if isSource(sour1, sour2):
                print(sour1, " is a source of", sour2)
            else:
                print(sour1, " is not a source of", sour2)
    if inp == 8:
        sour = input("Please enter the articles which quotes you want to see: ")
        if sour not in dict6:
            print("You entered wrong article")
        else:
            if len(dict6.get(sour)) != 0:
                print(Report(sour))
            else:
                print("This article does not have quotes")
    if inp == 9:
        sour = input("Please enter the articles which quotes you want to see: ")
        if sour not in dict2:
            print("You entered wrong article")
        else:
            if len(dict2.get(sour)) != 0:
                print(DirectReport(sour))
            else:
                print("This article does not have quotes")
    if inp == 10:
        sour = input("Please enter the name of article which anchor you want to find")
        if Anchor(sour) != None:
            print(Anchor(sour), " is your anchor")
        else:
            print(sour, "does not have anchor")
    if inp == 11:
        num = input("Which article you want to print: ")
        if num not in dict3:
            print("Incorrect input!")
        else:
            NicePrintA(dict3, num)
    if inp == 12:
        username = input("Which user's info you want to print: ")
        NicePrintU(dict1, dict4, dict5, username)
    if inp == 14:
        threshold = eval(input("Please enter the threshold of the influence:"))
        percentage = eval(input("Please enter the percentage of the users who can qualified as KOL in decimal:"))
        KOL = kol(dict6, dict1, threshold, percentage)
        if len(KOL) != 0:
            print("The key opinion leaders are:", end=" ")
            for leader in KOL:
                print(leader, end=" ")
            print("\n")
        else:
            print("There is no qualified key opinion leader.")
    if inp == 15:
        report_friend(dict6, dict1)

    pr(acc)
    inp = int(input("What action to perform?"))
print(dict1)
print()
print(dict2)
print()
print(dict3)
print()
print(dict6)  # just for checking the functions' correctness
