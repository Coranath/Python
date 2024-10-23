## Author: Levi Moore
## Date: 10/23/2024
## Purpose: Take a 2024-10-08T19:53:17.167Z Time and change it to a 13 digit epoch time

import datetime

if __name__ == "__main__":

    timeString = "2024-10-08T19:53:17.167Z"

    dt = datetime.datetime(2020,1,1) #datetime class must be initialized as some date, doesn't matter when

    dt = dt.fromisoformat(timeString) #This is where it changes to our actual desired date and time

    print(dt) #This is formatted like this: "2024-10-08 19:53:17.167000+00:00"

    print(dt.timestamp()) #And this is formatted like this: "1728417197.167"

    print(dt.ctime()) #There are various other ways to output the date as well

    print(dt.isoformat())
