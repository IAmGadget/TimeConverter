def convertTimeStampInSeconds(timestamp):
    totalSeconds = 0
    print(timestamp)
    for part in timestamp.split():
        if part[-1] == "w":
            print(f"{part[:-1]} weeks")
            totalSeconds += float(part[:-1]) * 604800

        if part[-1] == "d":
            print(f"{part[:-1]} days")
            totalSeconds += float(part[:-1]) * 86400

        if part[-1] == "h":
            print(f"{part[:-1]} hours")
            totalSeconds += float(part[:-1]) * 3600

        if part[-1] == "m":
            print(f"{part[:-1]} minutes")
            totalSeconds += float(part[:-1]) * 60

        if part[-1] == "s":
            print(f"{part[:-1]} seconds")
            totalSeconds += float(part[:-1])

    return {"seconds": totalSeconds}

x = convertTimeStamp("5s 2m 5d 22w") 
print(x['seconds']) # Will return the amount of seconds
