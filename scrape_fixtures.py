import asyncio

import aiohttp
from colorama import Fore, init
from prettytable import PrettyTable

from fpl import FPL

import sys

import csv
import re
from datetime import datetime

async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fixtures = await fpl.get_fixtures()

        striped_fixtures = []

        for i in range(1, len(fixtures),1):
            fixture = fixtures[i]
            # Example usage

            # Use regex to extract parts
            match_pattern = r"(.+) vs\. (.+) - (\w{3} \d{1,2} \w{3}) (\d{2}:\d{2})"
            match = re.match(match_pattern, str(fixture))

            home_team, away_team, date, time = match.groups()
            date_obj = datetime.strptime(date.strip(), "%a %d %b")

            # Format the datetime object to the desired format: %d-%m
            formatted_date = date_obj.strftime("%d-%m")
            striped_fixtures.append([formatted_date, time.strip(), home_team.strip(), away_team.strip()])

            # Writing to CSV
        with open("fixtures.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time","Home Team", "Away Team"])  # Header
            writer.writerows(striped_fixtures)  # Data row


if __name__ == "__main__":
    asyncio.run(main())