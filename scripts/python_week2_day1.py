print("Week 2 Day 1")
print()

monitor_target = {
    "name": "lenxuan",
    "url": "https://lenxuan.com",
    "check_ssl": False,
    "interval_minutes": 2,
    "owner": "lenxuan",
}
print("owner:", monitor_target["owner"])
print("Name:", monitor_target["name"])
print("URL:", monitor_target["url"])
print("Check SSL:", monitor_target["check_ssl"])
print("Interval minutes:", monitor_target["interval_minutes"])

print()
print("Your turn:")
print("- Change name.")
print("- Change url.")
print("- Change check_ssl.")
print("- Change interval_minutes.")
print("- Add one new field, for example owner.")
