

class ProfileSelector(object):
    def __init__(self):
        self.profiles = ["laptop", "desktop"]
        return self.get_profile()

    def get_profile(self):
        for i in range(len(self.profiles)):
            print("{}. {}".format(i+1, self.profiles[i]))
        selection = input("Select a profile by typing the number... ")
        return self.profiles[selection]


