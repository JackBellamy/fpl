import asyncio

import aiohttp
from colorama import Fore, init
from prettytable import PrettyTable

from fpl import FPL

import sys
import pandas as pd
import numpy as np
import csv


async def main():
    # dataframe to store player history
    df = pd.DataFrame(columns=["Name", "Position", "Team"])
    # row counter
    row = 0

    # collecting data
    async with aiohttp.ClientSession() as session:
        _id = 0
        fpl = FPL(session)
        player_info = await fpl.get_player(_id +1)
        player_sum = await fpl.get_player_summary(_id +1)

    # player basic info - name, position, team
    player_name = player_info.web_name
    player_position = player_info.element_type
    player_team = player_info.team

    # iterate through player history
    week = 0
    # loop through the player history
    for week in range(0, len(player_sum.history)):
        # add to dataframe
        df.loc[row] = {"Name" : player_name, "Position" : player_position, "Team" : player_team}
        # weeks data
        items = player_sum.history[week].items()
        # iterate through the weeks data
        for key, value in items:
            # -------------------------here is where to add different functions to clean data-----------------
            # time format
            if key == "kickoff_time":
                value = value.split("T")[1].split(":")[0] + ":" + value.split("T")[1].split(":")[1]
            # add to dataframe
            #-------------------------------------------------------------------------------------------------
            # add to dataframe
            df.loc[row, key] = value
        # next week and row
        week += 1
        row += 1
    # save the dataframe
    df.to_csv('player_data.csv', index=False)
    

if __name__ == "__main__":
    asyncio.run(main())
    

# import asyncio

# import aiohttp
# from colorama import Fore, init
# from prettytable import PrettyTable

# from fpl import FPL

# import sys
# import pandas as pd
# import csv


# async def main():
#     async with aiohttp.ClientSession() as session:
#         fpl = FPL(session)
#         fdr = await fpl.FDR()

#     #fdr_table = PrettyTable()
#     #fdr_table.field_names = [
#     #    "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
#     #    "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"]
#     fdr_table = pd.DataFrame(columns=[
#         "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
#         "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"])

#     for team, positions in fdr.items():
#         row = [team]
#         for difficulties in positions.values():
#             for location in ["H", "A"]:
#                 #if difficulties[location] == 5.0:
#                 #    row.append(Fore.RED + "5.0" + Fore.RESET)
#                 #elif difficulties[location] == 1.0:
#                 #    row.append(Fore.GREEN + "1.0" + Fore.RESET)
#                 #else:
#                 row.append(f"{difficulties[location]:.2f}")

#         fdr_table.loc[len(fdr_table)]= row#fdr_table.add_row(row)

#     #fdr_table.align["Team"] = "l"
#     with open("fdr.csv", mode="w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow([
#             "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
#             "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"])
            
#             for i in range(0,len(fdr_table)):
#                 writer.writerow(fdr_table.iloc[i])  # Data row
#             #writer.writerows(fdr_table)

# if __name__ == "__main__":
#     asyncio.run(main())