log_lines = [
    "2025-05-12 10:14:03 | INFO | auth | User login successful",
    "2025-05-12 10:14:08 | WARN | auth | Invalid password attempt",
    "2025-05-12 10:15:21 | INFO | database | Connection established",
    "2025-05-12 10:16:02 | ERROR | database | Query failed",
    "2025-05-12 10:16:45 | INFO | auth | User logout",
    "2025-05-12 10:17:10 | WARN | network | Packet loss detected",
    "2025-05-12 10:17:55 | INFO | network | Connection stabilised",
    "2025-05-12 10:18:30 | ERROR | auth | Account locked",
    "2025-05-12 10:19:12 | INFO | database | Connection closed",
    "2025-05-12 10:20:01 | INFO | auth | User login successful",
    "2025-05-12 10:20:44 | WARN | database | Slow query detected",
    "2025-05-12 10:21:30 | INFO | network | New connection established",
    "2025-05-12 10:22:05 | ERROR | network | Connection timeout",
    "2025-05-12 10:22:48 | INFO | auth | Password reset completed"
]

def stringsplitter(x):
    for i in x:
        if type(i) == str:
            z = i.split("|")
            x.remove(i)
            x.append(z)


stringsplitter(log_lines)

print(log_lines)