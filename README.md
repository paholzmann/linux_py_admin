# linux_py_admin
Python script to create, delete, and manage Linux/Debian users, set permissions, assign roles, log changes, and import users from CSV/Excel. Streamlines user management for admins and DevOps.
## Functionality
### 1. Custom single user management
#### Basic Operations
    python -m main manage-users add-single-user userName
    python -m main manage-users remove-single-user userName
    python -m main manage-users set-password userName
#### Groups
    python -m main manage-users add-single-user-to-groups userName groupNames rights
    python -m main manage-users remove-single-user-from-groups userName groupNames rights
##### Update user data
    python -m main manage-users update-user-name oldUserName newUserName
    python -m main manage-users update-password oldUserName newUserName
    python -m main manage-users update-all oldUserName newUserName
### 2. Bulk user management from files
#### Add many users to System from CSV/JSON/Excel
    python -m main manage-users add-bulk-users --csv
    python -m main manage-users add-bulk-users --json
    python -m main manage-users add-bulk-users --excel

### 3. Utilities
#### 3.1 Create dummy users
    python -m main manage-users create-dummy-users n
#### 3.2 Show existing users
    python -m main manage-users show-existing
#### 3.3 Search users by name
    python -m main manage-users find-user userName

### 4. Reporting
#### Export all data
    python -m main export-all-data --csv
    python -m main export-all-data --json
    python -m main export-all-data --xlsx
    python -m main export-all-data --pdf


# ML/DS
Recommendation System for user roles based on similar users.
Risk-Score for user accounts.
Log-Analytics Dashboard
