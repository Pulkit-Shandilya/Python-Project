import time
class Story:
    def Act1(self):
        print("You wake up in a dark room. You can hear the sound of water dripping.")
        print("There are two doors in front of you: one on the left and one on the right.")
        choice = input("Do you want to go left or right? ").lower()
        if choice == "left":
            self.LeftDoor()
        elif choice == "right":
            self.RightDoor()
        else:
            print("Invalid choice. Please try again.")
            self.Act1()