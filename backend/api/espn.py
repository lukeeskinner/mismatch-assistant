from espn_api.basketball import League
import config

league = League(
    league_id=config.LEAGUE_ID,
    year=config.YEAR,
    espn_s2=config.ESPN_S2,
    swid=config.SWID
)


print(league.settings.name)


