# linux_py_admin
Python script to create, delete, and manage Linux/Debian users, set permissions, assign roles, log changes, and import users from CSV/Excel. Streamlines user management for admins and DevOps.
## Functionality
### User management
#### Basic operations
    python -m main manage-users add-single-user userName
    python -m main manage-users remove-single-user userName
    python -m main manage-users set-password userName
##### Update user data
    python -m main manage-users update-user-name oldUserName newUserName
    python -m main manage-users update-password oldUserName newUserName
    python -m main manage-users update-email oldUserEmail newUserEmail
#### Bulk add users from files
    python -m main manage-users add-bulk-users --csv
    python -m main manage-users add-bulk-users --json
    python -m main manage-users add-bulk-users --excel
### Group management
#### Basic operations
    python -m main manage-users add-single-user-to-groups userName groupName rights
    python -m main manage-users remove-single-user-from-groups userName groupNames rights
### Utilities
#### Create dummy users
    python -m main manage-users create-dummy-users n
#### Show existing users
    python -m main manage-users show-existing-users
#### Show existing groups
    python -m main manage-groups show-existing-groups
#### Search users by name
    python -m main manage-users find-user userName

### Reporting
#### Export all data of users and groups
    python -m main export-all-data --csv
    python -m main export-all-data --json
    python -m main export-all-data --xlsx
    python -m main export-all-data --pdf


# ML/DS
Recommendation System for user roles based on similar users.
Risk-Score for user accounts.
Log-Analytics Dashboard
