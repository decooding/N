class UserManager:
    def __init__(self):
        self.id = 0
        self.data = {}

    def addUser(self, name):
        self.id += 1
        self.data[self.id] = name
        return self.id

    def getUser(self, id):
        return self.data.get(id)

    def findUserByName(self, name):
        return [
            user_id for user_id, user_name in self.data.items() if user_name == name
        ]

    def deleteUser(self, id):
        if id in self.data:
            del self.data[id]
            return True
        return False


def main():
    userManager = UserManager()
    while True:
        command = (
            input("Enter command (add, get, find, delete, q to quit): ").strip().lower()
        )

        if command == "q":
            break

        elif command == "add":
            name = input("Enter name to add: ").strip()
            user_id = userManager.addUser(name)
            print(f"Added user {name} with ID {user_id}")

        elif command == "get":
            try:
                user_id = int(input("Enter user ID to get: ").strip())
                user = userManager.getUser(user_id)
                if user:
                    print(f"User with ID {user_id} is {user}")
                else:
                    print(f"No user found with ID {user_id}")
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif command == "find":
            name = input("Enter name to find: ").strip()
            user_ids = userManager.findUserByName(name)
            if user_ids:
                print(
                    f"User(s) with name {name} found with ID(s): {', '.join(map(str, user_ids))}"
                )
            else:
                print(f"No user found with name {name}")

        elif command == "delete":
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                if userManager.deleteUser(user_id):
                    print(f"Deleted user with ID {user_id}")
                else:
                    print(f"No user found with ID {user_id}")
            except ValueError:
                print("Invalid ID. Please enter a number.")

        else:
            print("Unknown command. Please enter add, get, find, delete, or q to quit.")


if __name__ == "__main__":
    main()