import asyncio

import aiohttp
from colorama import Fore, init
from prettytable import PrettyTable

from fpl import FPL

import sys

import csv
import re

#def split_match_info(match_string):
    # # Use regex to extract parts
    # match_pattern = r"(.+) vs\. (.+) - (\w{3} \d{1,2} \w{3}) (\d{2}:\d{2})"
    # match = re.match(match_pattern, match_string)

    # if match:
    #     home_team, away_team, date, time = match.groups()
    #     print(home_team, away_team, date, time)
    #     return home_team.strip(), away_team.strip(), date.strip(), time.strip()
    # else:
    #     return "","","",""

async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fixtures = await fpl.get_fixtures()

        striped_fixtures = []

        for i in range(1, len(fixtures),1):
            fixture = fixtures[i]
            print(str(fixture))
            # Example usage

            # Use regex to extract parts
            match_pattern = r"(.+) vs\. (.+) - (\w{3} \d{1,2} \w{3}) (\d{2}:\d{2})"
            match = re.match(match_pattern, str(fixture))

            if match:
                home_team, away_team, date, time = match.groups()
                striped_fixtures.append([date.strip(), time.strip(), home_team.strip(), away_team.strip()])
            else:
                striped_fixtrues.append(["","","",""])

            # Writing to CSV
        with open("fixtures.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time","Home Team", "Away Team"])  # Header
            writer.writerows(striped_fixtures)  # Data row

        print("Done")

if __name__ == "__main__":
    asyncio.run(main())