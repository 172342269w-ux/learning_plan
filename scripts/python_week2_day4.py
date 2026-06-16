print("Week 2 Day 4")
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
    {
        "name": "shop-site",
        "url": "https://shop.example.com",
        "check_ssl": True,
        "interval_minutes": 3,
        "owner": "lenxuan",
    },
]

print("SSL enabled targets:")

for target in monitor_targets:
    if target["check_ssl"]:
        print("Name:", target["name"])
        print("URL:", target["url"])
        print()

print("Your turn:")
print("- Change one False check_ssl to True.")
print("- Run the file again and observe the new target appear.")
print("- Explain what the if is doing inside the loop.")
