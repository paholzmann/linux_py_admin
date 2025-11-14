from src.groups import Groups
from src.users import Users
from src.data_handler import CreateData, GetData

class Main:
    """
    
    """
    def __init__(self):
        """
        
        """
        self.groups = Groups()
        self.users = Users()
        self.data_handler = CreateData()

    def run_main(self):
        """
        
        """
        users = self.data_handler.generate_random_data(n=1000)
        for i, user in users.items():
            self.users.create_user(user_name=user["Username"])
        # self.data_handler.create_csv(data=users, filename="users.csv")

if __name__ == "__main__":
    main = Main()
    main.run_main()

# https://github.com/paholzmann/linux_py_admin.git
# cd linux_py_admin
# sudo python3 main.py