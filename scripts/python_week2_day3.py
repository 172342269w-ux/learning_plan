print("Week 2 Day 3")
print()

monitor_targets = [
    {
        "name": "main-site",
        "url": "https://example.com",
        "check_ssl": True,
        "interval_minutes": 5,
        "owner": "lenxuan",
    },
    {
        "name": "blog-site",
        "url": "https://blog.example.com",
        "check_ssl": False,
        "interval_minutes": 10,
        "owner": "lenxuan",
    },
]

for target in monitor_targets:
    print("Name:", target["name"])
    print("URL:", target["url"])
    print("Owner:", target["owner"])
    print()

print("Your turn:")
print("- Add one more target.")
print("- Run the file again and observe one more block.")
print("- Change one field and rerun.")
