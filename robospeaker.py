#robo speaker
#robin
import os

if __name__ == '__main__':
        print("wlecome to RoboSpeaker ")
        while True:
            x = input("Enter what you want me to speak: ")
            if x=="q":
                  os.system("say 'bye bye user' ")
                  break
            command = f"say {x}"
            os.system(command)