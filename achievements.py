import keyboard as keys

class achievements:
    def __init__(self):
        self.progress={
            "Miku":False,
            "Nino":False,
            "Itsuki":False,
            "Ichika":False,
            "Yotsuba":False,
            "Jump":False,
            "Beginning":False,
            "Pacman":False,
            "Flash":False,
            "WrongKeyE":False,
            "Order":False
        }

    
    def unlock(self, name, messages):
        if not self.progress[name]:
            print(f"Achievement Unlocked!!: {messages}")
            self.progress[name] = True

    def checker(self, player, Sisters, Obstacles, width):
        Ichika, Nino, Miku, Yotsuba, Itsuki = Sisters
        if player.x - 2 <= Miku.x <= player.x + 2 and player.z - 0.1 <= Miku.z <= player.z + 0.1:
            self.unlock("Miku", "Love At First Lesson?")

        if player.x - width/3 != 0:
            self.unlock("Beginning", "Welcome to Huss Valley")

        if player.x >= width or player.x <= 0:
            self.unlock("Pacman", "Wakka Wakka")

        if player.jump and Yotsuba.x - 3 <= player.x <= Yotsuba.x + 3:
            self.unlock("Yotsuba", "Random Dude Vs. Lebron Nakano")

        if player.crouch and Nino.x - 1 <= player.x <= Nino.x + 1:
            self.unlock("Nino", "With The Sole Exception Of Nakano Nino Of Course")
        if Ichika.juke:
            self.unlock("Ichika", "Onee-Chan Wanted To Give You A Hug :(")
        if player.jump:
            self.unlock("Jump", "Jump Up, Superstar!")
        if Itsuki.x - 10 <= player.x <= Itsuki.x + 10:
            self.unlock("Itsuki", "Star Struck With The Star Pins")

        if keys.is_pressed("left shift"):
            self.unlock("Flash", "Assetto Corsa")

        if keys.is_pressed("e"):
            self.unlock("WrongKeyE", "Hahaha, Buddy Thought I Was Motivated Enough To Code Something For The E Key")

        if Ichika.z > Nino.z > Miku.z > Yotsuba.z > Itsuki.z:
            self.unlock("Order", "'Ichi, Ni, Mi, Yotsu, Itsu...' 'PICK A SYSTEM BRO'")
                
 
        
achieve = achievements()
