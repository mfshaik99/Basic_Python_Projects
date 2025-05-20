'''Method to create an alarm clock using Python'''
# 1. Import necessary libraries
# 2. Define a function to set the alarm clock.
# 3. Inside the function, create a loop to display options to the user.
# 4. Allow the user to set an alarm time in HH:MM format.
# 5. Validate the input time.
# 6. Use a while loop to check the current time against the alarm time.
# 7. If the current time matches the alarm time, play a sound.
# 8. Provide an option to exit the program.
# 9. Use exception handling to manage invalid inputs.
# 10. Test the program to ensure it works as expected


import datetime
import time
import winsound

def alarm_clock():
    while 1:
        print("\n******************************")
        print("Hello Friends welcome to my Alarm Clock")
        print("created by: Farhan Shaik")
        print("Alarm Clock")
        print("1. Set Alarm (HH:MM, 24-hour)")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            alarm_time = input("Enter alarm time (HH:MM, e.g., 14:30): ")
            # Parse alarm time (assumes valid HH:MM format)
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
                print("Invalid time! Hours (0-23), Minutes (0-59).")
                #continue
                print("******************************")
                break
            

            
            print(f"Alarm set for {alarm_time}. Waiting...")
            while True: 
                # Get current time
                current_time = datetime.datetime.now()
                if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
                    print("\n*** ALARM! Time's up! ***")
                    # Play 10 beeps of 1 second each (total 10 seconds)
                    for i in range(3):
                        winsound.Beep(1000, 1000)
                    break
                time.sleep(1)  # Check every second
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

alarm_clock()
