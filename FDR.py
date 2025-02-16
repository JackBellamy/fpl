import asyncio

import aiohttp
from colorama import Fore, init
from prettytable import PrettyTable

from fpl import FPL

import sys
import pandas as pd
import csv


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fdr = await fpl.FDR()

    #fdr_table = PrettyTable()
    #fdr_table.field_names = [
    #    "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
    #    "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"]
    fdr_table = pd.DataFrame(columns=[
        "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
        "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"])

    for team, positions in fdr.items():
        row = [team]
        for difficulties in positions.values():
            for location in ["H", "A"]:
                #if difficulties[location] == 5.0:
                #    row.append(Fore.RED + "5.0" + Fore.RESET)
                #elif difficulties[location] == 1.0:
                #    row.append(Fore.GREEN + "1.0" + Fore.RESET)
                #else:
                row.append(f"{difficulties[location]:.2f}")

        fdr_table.loc[len(fdr_table)]= row#fdr_table.add_row(row)

    #fdr_table.align["Team"] = "l"
    with open("fdr.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
            "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
            "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"])
            
            for i in range(0,len(fdr_table)):
                writer.writerow(fdr_table.iloc[i])  # Data row
            #writer.writerows(fdr_table)

if __name__ == "__main__":
    asyncio.run(main())