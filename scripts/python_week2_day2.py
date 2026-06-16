print("Week 2 Day 2")
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

print("Total targets:", len(monitor_targets))
print("First target name:", monitor_targets[0]["name"])
print("Second target url:", monitor_targets[1]["url"])

print()
print("Your turn:")
print("- Change one target name.")
print("- Change one check_ssl value.")
print("- Add a third target.")
