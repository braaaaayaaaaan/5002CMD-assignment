class Person:
    def __init__(self, name, gender, bio, is_public=True):
        """Represents an instance from the Person class"""
        self.name = name
        self.gender = gender
        self.bio = bio
        self.is_public = is_public   # True = public profile, False = private

    def display_full_profile(self):
        """Display full profile"""
        print()
        print("*" * 35)
        print("PERSON PROFILE".center(35))
        print("*" * 35)
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Bio: {self.bio}")
        print(f"Privacy: {'Public' if self.is_public else 'Private'}")
        print("*" * 35)
        print()

    def display_limited_profile(self):
        """
        Display limited profile
        Gender and bio attributes are hidden
        """
        print("---- PERSON PROFILE ----")
        print(f"Name: {self.name}")
        print(f"Privacy: Private (limited view)")
        print("------------------------")



