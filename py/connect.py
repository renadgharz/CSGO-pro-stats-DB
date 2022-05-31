from sqlalchemy import create_engine
from secrets import credentials as creds

username = creds.get('user')
password = creds.get('pwd')
host = creds.get('hostname')
port = creds.get('port')

players_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Players'
players_engine = create_engine(players_conn)

teams_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Teams'
teams_engine = create_engine(teams_conn)

events_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Events'
events_engine = create_engine(events_conn)

leaderboards_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Leaderboards'
leaderboards_engine = create_engine(leaderboards_conn)

maps_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Maps'
maps_engine = create_engine(maps_conn)

matches_conn = f'mssql+pymssql://{username}:{password}@{host}:{port}/Matches'
matches_engine = create_engine(matches_conn)