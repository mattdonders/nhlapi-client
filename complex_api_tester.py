import logging

from nhlapi import NHLAPI

from nhlapi.models.teams import Teams, Team, Division
from nhlapi.models.schedule import Schedule

logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s - %(module)s.%(funcName)s (%(lineno)d) - %(levelname)s - %(message)s",
)

nhl_api = NHLAPI()

all_teams = nhl_api.teams.get()
logging.info("All Teams Objects: %s", all_teams)


first_team = all_teams.teams[0]
logging.info("All Teams [0] Object: %s", first_team)
logging.info("All Teams [0] Object (SubClasses): %s", first_team.__dict__)
print()

logging.info("All Teams [0] Id: %s", first_team.id)
logging.info("All Teams [0] Name: %s", first_team.name)
logging.info("All Teams [0] Venue: %s", first_team.venue)
logging.info("All Teams [0] Venue Time Zone: %s", first_team.venue.timeZone)

print("\n------------------------------------------------------------------\n")


single_team = nhl_api.teams.get(team_id=2)
logging.info("Single Team Object (Still Teams): %s", single_team)
# # logging.info("Single Team Keys: %s", dir(single_team))
# # print("Single Team __dict__: ", single_team.__dict__)
single_team = single_team[0]
logging.info("Single Team ID: %s", single_team.id)
logging.info("Single Team Name: %s", single_team.name)

print("\n------------------------------------------------------------------\n")

team_with_stats = nhl_api.teams.get_with_stats(team_id=3)
logging.info("Single Team Stats Object (Still Teams): %s", single_team)
# # logging.info("Single Team Keys: %s", dir(single_team))
# # print("Single Team __dict__: ", single_team.__dict__)
logging.info("Single Team Stats ID: %s", single_team.id)
logging.info("Single Team Stats Name: %s", single_team.name)
logging.info("Single Team Stats Object (SubClasses): %s", single_team.__dict__)

print("\n------------------------------------------------------------------\n")

schedule = nhl_api.schedule.get()
logging.info("Schedule Object: %s", schedule)
logging.info("Schedule Dates 0 Object: %s", schedule.dates[0])
# logging.info("Schedule Dates (0) Games: %s", schedule.dates[0].games)
logging.info("Schedule Date 0, Game 0: %s", schedule.dates[0].games[0])
logging.info("Schedule Date 0, Game 0, Status: %s", schedule.dates[0].games[0].status)
logging.info("Schedule Date 0, Game 0, Home Team: %s", schedule.dates[0].games[0].teams.home)
logging.info("Schedule Date 0, Game 0, Away Team: %s", schedule.dates[0].games[0].teams.away)

logging.info("Schedule Object With Sub-Classes")
print(schedule.__dict__)
print(schedule.dates[0].games[0].__dict__)

print("\n------------------------------------------------------------------\n")

expanded_schedule = nhl_api.schedule.get_fully_expanded()
logging.info("Expanded Schedule Object: %s", expanded_schedule)
logging.info("Expanded Schedule Dates 0 Object: %s", expanded_schedule.dates[0])
# logging.info("Schedule Dates (0) Games: %s", schedule.dates[0].games)
logging.info("Expanded Schedule Date 0, Game 1: %s", expanded_schedule.dates[0].games[1])
logging.info("Expanded Schedule Date 0, Game 1, Status: %s", expanded_schedule.dates[0].games[1].status)
logging.info(
    "Expanded Schedule Date 0, Game 1, Home Team: %s", expanded_schedule.dates[0].games[1].teams.home
)
logging.info(
    "Expanded Schedule Date 0, Game 1, Away Team: %s", expanded_schedule.dates[0].games[1].teams.away
)

home_team = expanded_schedule.dates[0].games[1].teams.home
home_record = home_team.leagueRecord
logging.info("Expanded Schedule Date 0, Game 1, Home Team Record: %s", home_record)

home_record_fmtd = home_team.leagueRecord.formatted
logging.info("Expanded Schedule Date 0, Game 1, Home Team Record: %s", home_record_fmtd)

logging.info("Expanded Schedule Object With Sub-Classes")
print(expanded_schedule.as_dict())
print(expanded_schedule.__dict__)
print(expanded_schedule.dates[0].games[1].__dict__)


print("\n------------------------------------------------------------------\n")

person = nhl_api.people.get(person_id=8475791)
logging.info("Person Object: %s", person)
logging.info("Person ID: %s", person.id)
logging.info("Person Full Name: %s", person.fullName)
logging.info("Person Primary Number: %s", person.primaryNumber)
logging.info("Person Current Team: %s", person.currentTeam)
logging.info("Person Current Team Dict: %s", person.currentTeam.as_dict())
logging.info("Person Position: %s", person.primaryPosition)
