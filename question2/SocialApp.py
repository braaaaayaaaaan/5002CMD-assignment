from UDGraph import UDGraph
from Person import Person


def create_initial_people():
    """Represents existing users of the app"""
    p1 = Person("Alisa", "Female", "Loves sleeping", True)
    p2 = Person("Jack", "Male", "Tech-savvy and enthusiastic", True)
    p3 = Person("Rebecca", "Female", "Full-time blogger", False)
    p4 = Person("David", "Male", "Gym lover", True)
    p5 = Person("Emma", "Female", "Foodie", False)

    return [p1, p2, p3, p4, p5]


def init_social_graph(people):
    """Represents the overall network of graph"""
    graph = UDGraph()

    """
    Add existing users to the app
    using addVertex()
    """
    for person in people:
        graph.addVertex(person.name)

    """
    Represents existing following in the app
    using addEdge()
    """
    graph.addEdge("Alisa", "Jack")
    graph.addEdge("Jack", "Rebecca")
    graph.addEdge("Rebecca", "David")
    graph.addEdge("David", "Emma")
    graph.addEdge("Emma", "David")

    return graph


"""Menu Operations"""

def display_all_users(people):
    """Display all existing users"""
    print()
    print("*" * 35)
    print("List of Users".center(35))
    print("*" * 35)
    print()

    size = 1
    for p in people:
        print(f"{size}. {p.name}")

        size += 1


def view_profile(people_dict):
    """View the profile of existing users"""

    # Prompt to view user profile
    name = input("\nSelect User Profile: ").strip()

    # Check if the user exists or not
    if name not in people_dict:
        print("User Not Found.")
        return

    # Display user profile
    person = people_dict[name]
    person.display_full_profile()


def view_following(graph, user):
    """View following"""

    # List out user's following list
    print(f"\n{user}'s Following List:")

    following = graph.listOutgoingAdjacentVertex(user)

    # Check if user is following another user
    size = 1
    if not following:
        print("No following!")
    else:
        for f in following:
            print(f"{size}. {f}")
            size += 1


def view_followers(graph, user):
    """View followers"""
    print(f"\n{user}'s Followers List:")

    followers = graph.listIncomingAdjacent(user)

    # Check if user has followers or not
    size = 1
    if not followers:
        print("No followers!")
    else:
        for f in followers:
            print(f"{size}. {f}")
            size += 1


def add_user(people, people_dict, graph):
    """Add user to the app"""

    # Enter new user details
    name = input("Name: ")
    gender = input("Gender: ")
    bio = input("Bio: ")
    priv = input("Public profile? (y/n): ").lower() == "y"

    # Create a new instance of the Person class
    new_p = Person(name, gender, bio, priv)
    people.append(new_p)
    people_dict[name] = new_p

    # Add the user to the graph network
    graph.addVertex(name)

    # Display success message for adding user
    print("\nSuccessfully Added User!")


def follow_user(graph):
    """Allow user to follow each other"""

    # Prompt to enter user (from) and target user (to)
    user = input("\nUser Who Follows?: ")
    target = input("Which User to Follow?: ")

    # Follow users using addEdge()
    try:
        graph.addEdge(user, target)
        print(f"\nUpdate: {user} Now Follows {target}!")
    except ValueError as e:
        print(e)


def unfollow_user(graph):
    """Allow user to unfollow each other """

    # Prompt to enter user (from) and target user (to)
    user = input("User Who Unfollows?: ")
    target = input("Which User to Unfollow?: ")

    # Unfollow user using removeEdge()
    graph.removeEdge(user, target)
    print(f"Update: {user} Unfollowed {target}!")


def main():
    """Main Menu"""

    # Handles looping through the main menu
    terminate_menu = False

    # Retrieve existing users from the app
    people = create_initial_people()

    # Add existing users to the app
    graph = init_social_graph(people)
    people_dict = {p.name: p for p in people}

    while terminate_menu != True:
        print("*" * 35)
        print("SNAP-APP".center(35))
        print("*" * 35)

        print("1. List All Users")
        print("2. View User Profile")
        print("3. View User Following List")
        print("4. View User's Followers List")
        print("5. Add New User")
        print("6. Edit Follow")
        print("7. Edit Unfollow")
        print("0. Exit")
        print("*" * 35)

        choice = input("\nEnter Option: ")

        if choice == "1":
            display_all_users(people)
        elif choice == "2":
            view_profile(people_dict)
        elif choice == "3":
            name = input("Select User: ")
            view_following(graph, name)
        elif choice == "4":
            name = input("Select User: ")
            view_followers(graph, name)
        elif choice == "5":
            add_user(people, people_dict, graph)
        elif choice == "6":
            follow_user(graph)
        elif choice == "7":
            unfollow_user(graph)
        elif choice == "0":
            print("Exiting...")
            terminate_menu = True
            break
        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    main()
