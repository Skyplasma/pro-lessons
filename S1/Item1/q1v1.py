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
    z = []
    for i in x:
        z.append(i.split("|"))
    return z

def clean_data(full_list):
    for outer_nest in range(len(full_list)):
        for inner_nest in range(len(full_list [outer_nest])):
            full_list [outer_nest][inner_nest] = full_list [outer_nest][inner_nest].strip()
    return full_list

def msg_type(full_list,data_select):
    for outer_nest in range(len(full_list)):
        print(sorted(full_list[outer_nest]))

nested_log = stringsplitter(log_lines)

secondary_list = clean_data(nested_log)
##print(msg_type(secondary_list,1))

print(list(filter(secondary_list,"INFO")))