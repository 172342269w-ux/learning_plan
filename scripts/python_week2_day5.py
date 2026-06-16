print("Week 2 Day 5")
print()

monitor_config = {
    "targets": [
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
}

print("Total targets:", len(monitor_config["targets"]))
print("First target name:", monitor_config["targets"][0]["name"])
print("First target owner:", monitor_config["targets"][0]["owner"])
print("This structure is close to what a later JSON file can store.")

print()
print("Your turn:")
print("- Add one target to monitor_config['targets'].")
print("- Change one owner.")
print("- Explain why a list is inside a dictionary here.")
