#A program to help a small  business manage tasks assigned to each member of a team.
#The program allows for only the admin user to register new users and view statistics.
#In order to use the program the correct username and password must be entered.
#The program allows for the user to view all the tasks at once or only their tasks.
#The program also allows a user to add a task.



f = open('user.txt', 'r')
data = f.read()
split = data.split(', ')
valid_username = split[0]
valid_password = split[1]
username = input("Username:")
password = input("Password:")
attemps = 0

while attemps <= 3:
    if username == "admin":
        while True:
#Menu options provided to the user
            menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
s - statistics
e - exit
: ''').lower()
    #registering a new user (only for admin)
            if menu == 'r':
                new_username = input("Enter new username:")
                password = input("Enter a password:")
                confirmed_password = input("Re-enter the password:")
                
            #Writing the username and password to the user.txt file
                with open('user.txt', 'a+') as file:
                    if password == confirmed_password:
                        file.write('\n' + new_username + ", " + password)
                        print("New user has been added." '\n')
                    elif password != confirmed_password:
                        print("Passwords did not match, try again!" '\n')
                        
                file.close()

                
    #adding a new task
            elif menu == 'a':

            #Writing the new task to tasks.txt
                with open('tasks.txt', 'a+') as file:
                    assigned_to = input("Enter the username of the person to whom the task is assigned to:")
                    task_title = input("Enter the title of the task:")
                    description = input("Enter a description of the task:")
                    due_date = input("Enter the date that the task is due:")
                    current_date = input("Enter the current date:")
                    complete = input("Is the task complete: 'Yes'/'No:'")
                    file.write('\n' + assigned_to + ", " + task_title + ", " + description + ", " + current_date + ", " + due_date + ", " + complete)
                    print("Your task has been added to the 'tasks.txt' text file." '\n')

                file.close()

                
    #viewing all tasks
            elif menu == 'va':

                with open('tasks.txt', 'r') as f:
                    for line in f:
                        data = line.split(', ')
                        task = ("Task:" + '\t' + '\t' + data[1])
                        assigned_to = ("Assigned to:" + '\t' + '\t' + data[0])
                        date_assigned = ("Date assigned:" + '\t' + '\t' + data[3])
                        due_date = ("Due date:" + '\t' + '\t' + data[4])
                        task_complete = ("Task complete?" + '\t' + '\t' + data[5])
                        task_description = ("Task description:" + '\t' + data[2])           
                        print('\n' + assigned_to + '\n' + date_assigned  + '\n' + due_date + '\n' + task_complete + '\n' + task_description + '\n')

                f.close()

                
    #Viewing only the users' tasks who is logged in 
            elif menu == 'vm':
                with open('tasks.txt', 'r') as f:

                    for line in f:
                        data = line.split(', ')
                        if username == data[0]:
                            assigned_to = ("Assigned to:" + '\t' + '\t' + data[0])
                            date_assigned = ("Date assigned:" + '\t' + '\t' + data[3])
                            due_date = ("Due date:" + '\t' + '\t' + data[4])
                            task_complete = ("Task complete?" + '\t' + '\t' + data[5])
                            task_description = ("Task description:" + '\t' + data[2])           
                            print('\n' + assigned_to + '\n' + date_assigned  + '\n' + due_date + '\n' + task_complete + '\n' + task_description + '\n')

                f.close()

                
        #Viewing statistics (only for admin)
            elif menu == 's':

                with open('tasks.txt', 'r') as file1:
                    num = 0
                    for line in file1:
                        num += 1
                    print(f"Number of tasks: {num}")

                file1.close()

                with open('user.txt', 'r') as file2:
                    num = 0
                    for line in file2:
                        num += 1
                    print(f"Total number of users: {num}" '\n')

                file2.close()

                    
        #Exit
            elif menu == 'e':
                    print('Goodbye!!!')
                    exit()


                    
#If the username is not admin but is still valid
    if username == valid_username and password == valid_password:
        while True:
            menu = input('''Select one of the following Options below:
a - adding a task
va - view all tasks
vm - view my task
e - exit
: ''').lower()
    #Adding a new task
            if menu == 'a':

        #Writing the task to the tasks.txt file
                with open('tasks.txt', 'a+') as file:
                    assigned_to = input("Enter the username of the person to whom the task is assigned to:")
                    task_title = input("Enter the title of the task:")
                    description = input("Enter a description of the task:")
                    due_date = input("Enter the date that the task is due:")
                    current_date = input("Enter the current date:")
                    complete = input("Is the task complete: 'Yes'/'No:'")
                    file.write('\n' + assigned_to + ", " + task_title + ", " + description + ", " + current_date + ", " + due_date + ", " + complete)
                    print("Your task has been added to the 'tasks.txt' text file."'\n')
                file.close()
                
                
    #Viewing all tasks
            elif menu == 'va':
                with open('tasks.txt', 'r') as f:
                    for line in f:
                        data = line.split(', ')
                        task = ("Task:" + '\t' + '\t' + data[1])
                        assigned_to = ("Assigned to:" + '\t' + '\t' + data[0])
                        date_assigned = ("Date assigned:" + '\t' + '\t' + data[3])
                        due_date = ("Due date:" + '\t' + '\t' + data[4])
                        task_complete = ("Task complete?" + '\t' + '\t' + data[5])
                        task_description = ("Task description:" + '\t' + data[2])           
                        print('\n' + assigned_to + '\n' + date_assigned  + '\n' + due_date + '\n' + task_complete + '\n' + task_description)
                f.close()
                

    #Viewing all the tasks of the user who is logged in
            elif menu == 'vm':
                with open('tasks.txt', 'r') as f:
                    for line in f:
                        data = line.split(', ')
                        if username == data[0]:
                            assigned_to = ("Assigned to:" + '\t' + '\t' + data[0])
                            date_assigned = ("Date assigned:" + '\t' + '\t' + data[3])
                            due_date = ("Due date:" + '\t' + '\t' + data[4])
                            task_complete = ("Task complete?" + '\t' + '\t' + data[5])
                            task_description = ("Task description:" + '\t' + data[2])           
                            print('\n' + assigned_to + '\n' + date_assigned  + '\n' + due_date + '\n' + task_complete + '\n' + task_description)
                f.close()
    #Exits
            elif menu == 'e':
                print('Goodbye!!!')
                exit()
    else:
        attemps +=1
