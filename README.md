# linux_py_admin
Python script to create, delete, and manage Linux/Debian users, set permissions, assign roles, log changes, and import users from CSV/Excel. Streamlines user management for admins and DevOps.
## Functionality
### 1. Custom single Data

#### 1.1 Add single user to System
        python -m main manage-users add-single-user userName
1.2 Add single user to System groups
    python -m main manage-users add-single-user-to-groups userName groupNames
1.3 Remove single user from System
    python -m main manage-users remove-single-user userName
1.4 Remove single user from Group
    python -m main manage-users remove-single-user-from-groups userName groupNames
3. Custom file Data
2.1 Add many users to System
    python -m main 

4. Utilities
3.1 
3.2 Show existing users
    python -m main manage-users show-existing
