#Niki
#Challenge 3
#Create a function that takes in a word as a string and returns all i.p. addresses that have that word in their log
#Init
# Security Log Entries
security_logs = [
    "System update", "Login success", "File synced", "Unauthorized access attempt", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized connection detected", "System update",
    "Login success", "Password changed", "Unauthorized access attempt", "File synced", "Login success",
    "Routine scan", "System update", "Unauthorized login attempt", "User logout", "File synced",
    "Login success", "Database backup", "System update", "Unauthorized port scan", "File deleted",
    "Login success", "Routine scan", "Unauthorized access attempt", "User logout", "File synced",
    "System update", "Login success", "File synced", "Unauthorized connection detected", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized access attempt", "System update",
    "Login success", "Password changed", "Unauthorized login attempt", "File synced", "Login success",
    "Routine scan", "System update", "Unauthorized port scan", "User logout", "File synced",
    "Login success", "Database backup", "System update", "Unauthorized access attempt", "File deleted",
    "Login success", "Routine scan", "Unauthorized connection detected", "User logout", "File synced",
    "System update", "Login success", "File synced", "Unauthorized access attempt", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized login attempt", "System update",
    "Login success", "Password changed", "Unauthorized port scan", "File synced", "Login success"
]

# Corresponding IP Addresses
log_ips = [
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "10.0.0.52", "192.168.1.12",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "10.0.5.112", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "10.0.0.52", "192.168.1.15", "192.168.1.45",
    "192.168.1.1", "192.168.1.1", "172.16.254.1", "192.168.1.12", "192.168.1.15",
    "192.168.1.45", "192.168.1.1", "192.168.1.1", "10.0.5.112", "192.168.1.15",
    "192.168.1.12", "192.168.1.1", "10.0.0.52", "192.168.1.12", "192.168.1.15",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "172.16.254.1", "192.168.1.12",
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "10.0.0.52", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "172.16.254.1", "192.168.1.15", "192.168.1.45",
    "192.168.1.1", "192.168.1.1", "10.0.5.112", "192.168.1.12", "192.168.1.15",
    "192.168.1.45", "192.168.1.1", "192.168.1.1", "10.0.0.52", "192.168.1.15",
    "192.168.1.12", "192.168.1.1", "172.16.254.1", "192.168.1.12", "192.168.1.15",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "10.0.0.52", "192.168.1.12",
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "172.16.254.1", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "10.0.5.112", "192.168.1.15", "192.168.1.45"
]
filtered_ips=[]
#Functions
def search(logs):
    for i in range(len(log_ips)):
        if logs in security_logs[i]:
            filtered_ips.append(log_ips[i])
    print(filtered_ips)
    filtered_ips.clear()
#Main
search("Unauthorized")
