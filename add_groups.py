import subprocess

groups = [
    "it",
    "hr",
    "marketing",
    "sales",
    "web_dev",
    "db_team",
    "support",
]

def group_exists(group_name):
    result = subprocess.run(
        ["getent", "group", group_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

for group in groups:
    if group_exists(group):
        print(f"Group exists already: {group}")
    else:
        print(f"Group added: {group}")
        subprocess.run(["sudo", "groupadd", group])

# git clone https://github.com/paholzmann/Linux.git
# cd Linux/tech_corp_project
# sudo python3 add_groups.py
