import pandas as pd
athletes = df[["Name","Sex"]].drop_duplicates()
athletes.to_csv("data/athletes.csv", index=False)

federations = df[["Federation","ParentFederation"]].drop_duplicates()
federations.to_csv("data/federations.csv", index=False)

meets = df[["Federation",
             "Date",
             "MeetCountry",
             "MeetState",
             "MeetTown",
             "MeetName",
             "Country",
             "State"]].drop_duplicates(subset=["Date","MeetName","Federation"])
meets.to_csv("data/meets.csv", index=False)

meet_performances = df
meet_performances.to_csv("data/meet_performances.csv",index=False)
