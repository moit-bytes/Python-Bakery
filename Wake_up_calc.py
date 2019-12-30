# editor used was PyCharm
# import datetime module to fetch current date and time
# import time module to fetch functions such as sleep which allows us to pause statements for given time
# import sys module to write data on terminal window, used to animate reloading symbol
# Brief Variable description mentioned at the end of the code

import datetime, time, sys

# using try block to write the whole program
# so that if any unexpected error happens then it is fetched by except block and program does not terminate

try:

    # initializing now as the current state to seek current date, time, month, year objects
    now = datetime.datetime.now()
    c = 0
    mm = ""
    hh = ""

    # animate() - used to produce a cool reloading animation

    def animate():
        done = 'false'
        s = 0
        print("\n\t\t\t\t\t")
        while done == 'false':
            #stdout is used for the output of print() and expression statements and for the prompts of input()
            sys.stdout.write('\r Reloading... |')
            time.sleep(0.1)
            sys.stdout.write('\r Reloading... /')
            time.sleep(0.1)
            sys.stdout.write('\r Reloading... -')
            time.sleep(0.1)
            sys.stdout.write('\r Reloading... \\')
            time.sleep(0.1)
            s = s+1
            if(s == 10):
                done = 'true'
        sys.stdout.write('\rDone!     ')
        time.sleep(0.15)
        return ""

    # clear() - used to clear the terminal window

    def clear():
        for i in range(0, 12):
            print("\n")
        return ""

    # exit_cond - used to exit the program or re-run it

    def exit_cond():
        print("\n Press 0 to return back to main menu ----->")
        print(" Press 9 to exit the program         ----->  ")
        i1 = int(input(" Enter your choice = "))
        if(i1 == 0):
            # if user enters 0 then i am reloading the program
            animate()
            calling()
        elif(i1 == 9):
            clear()
            print("\n\n\t\t\t\t\t\t\t Thank You !!! For being with me :)")
        return ""

    # time_cov() - used to get the time in (hh:mm) format and split it into hours and mins.

    def time_conv(time):
        # globalization required to refer variable from outside
        global c
        global mm
        global hh
        c = 0
        mm = ""
        hh = ""
        # if the loop encounters ":" then it wouldn't do anything and goes on separating hours and mins
        for c in range(0, len(time)):
            if c > (time.index(':')):
                mm = mm + time[c]
            elif c < (time.index(':')):
                hh = hh + time[c]

    # display() - used to display the title screen or user screen with current date and time

    def display():
        print(
            "=========================================== Wake-Up-Time Calculator ======================================")
        print("\n", "Current Date = ", str(now.day), "/", str(now.month), "/",
              str(now.year), "\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
              "Current Time =", str(now.hour), ":", str(now.minute))
        # using now.hour to call the current hours and similarly now.minute and others.


    # wake_up() - takes sleeping time as input and returns wake up time

    def wake_up(user_time):
        # making variables global
        global c
        global mm
        global hh
        clear()
        time_conv(user_time)
        print(" Your Given time is = ", user_time)
        cycle = int(input(" Enter number of sleeping cycles you want to complete( but remember you must complete atleast 4 sleeping hours to have good health) = "))
        hh = int(hh)
        mm = int(mm)

        # converting hours into minutes and then adding it with the mins variable
        # Now adding the above with cycle*105 to get the final time
        # 105 is used because 90(each cycle duration) + 15(time b/w two successive cycle)

        t = (hh * 60) + mm + (cycle*105)

        print("\n\n The best time for you to wake up is :", end=" ")
        hh = t // 60
        mm = t % 60
        hh = hh % 24
        s2 = str(hh) + ":" + str(mm)
        if (hh >= 12):
            print(s2, " PM ")
        else:
            print(s2, " AM ")
        if(cycle < 4):
            print("\n Note : As you have chosen to sleep for less than 4 cycles so you should put a reminder to complete rest of your sleeping cycles")
        else:
            print("\n Task done :) Now you are ready to sleep at your specified time")
        print(exit_cond())
        return ""

    # sleep_into() - takes wake up time as input and returns sleeping time

    def sleep_into(user_time):
        global c
        global mm
        global hh
        clear()
        time_conv(user_time)
        print(" Your Given time is = ", user_time)
        cycle = int(input(" Enter number of sleeping cycles you want to complete( but remember you must complete atleast 4 sleeping hours to have good health) = "))
        hh = int(hh)
        mm = int(mm)

        # converting hours into minutes and then adding it with the mins variable
        # Now subtracting the above with cycle*105 to get the final time
        # 105 is used because 90(each cycle duration) + 15(time b/w two successive cycle)

        t = (hh * 60) + mm - (cycle * 105)

        print("\n\n The best time for you to sleep is :", end=" ")
        hh = t // 60
        mm = t % 60
        hh = hh % 24
        s2 = str(hh) + ":" + str(mm)
        if(hh >= 12):
            print(s2, " PM ")
        else:
            print(s2, " AM ")
        if (cycle < 4):
            print(
                "\n Note : As you have chosen to sleep for less than 4 cycles so you should put a reminder to complete rest of your sleeping cycles")
        else:
            print("\n Task done :) Now you are ready to wake up at your specified time")
        print(exit_cond())
        return ""

    # calling() - used to call the different functions according to user choices or inputs

    def calling():
        clear()
        display()
        print("\n\n Press 1 To Know The Best Time To Wake Up ")
        print("\n Press 2 To Know the Best Time to sleep")
        i = int(input("\n\n Please enter your choice = "))
        if (i == 1):
            clear()
            display()
            print("\n Welcome!! To The Waking Up Calculator")
            print("\n\n Press 1 To Provide your sleeping time")
            print("\n Press 2 To Read the current time as your sleeping time  ")
            c1 = int(input("\n\n Please enter your choice to know wake up time = "))
            if (c1 == 1):
                u_time = input("\n\n Please enter your sleeping time in hh:mm format = ")
                print(wake_up(u_time))
            elif (c1 == 2):
                u_time = (str(now.hour) + ":" + str(now.minute))
                print(wake_up(u_time))
        elif (i == 2):
            clear()
            display()
            print("\n Welcome!! To The Sleeping Time Calculator")
            timing = input("\n\n Please enter your wake up time in (hh:mm) format = ")
            sleep_into(timing)
        return ""
    # function call to just initiate the process or program
    calling()

# except block used to fetch errors produced by try block
# using except we can reload the program even if there was a wrong input at any instance
except:
    clear()
    print("\n Something Went Wrong Or U entered a wrong choice !!")
    animate()
    print("\n\n\n Redirecting you to Main Menu ------->")
    # making the above line to pause for 3 seconds
    time.sleep(3.0)
    calling()




# Brief Variable Description:

# mm - used to store minutes
# hh - used to store hours
# t - used to calculate the complete or new time
# s - acts as counter variable to stop iteration of while loop
# c - acts as counter variable in for loop to separate hours and minutes
# s2 - used to store the final time in(hh:mm) format
# i, i1, c1 - to take user inputs as their choices


