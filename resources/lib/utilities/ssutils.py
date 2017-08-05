# -*- coding: utf-8 -*-
'''
    script.matchcenter - Football information for Kodi
    A program addon that can be mapped to a key on your remote to display football information.
    Livescores, Event details, Line-ups, League tables, next and previous matches by team. Follow what
    others are saying about the match in twitter.
    Copyright (C) 2016 enen92

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import datetime
from common_addon import *

def get_league_tables_ids():
	tables = []
	if addon.getSetting("t-nfl") == "true": tables.append(4391)
	if addon.getSetting("t-nba") == "true": tables.append(4387)
	if addon.getSetting("t-mlb") == "true": tables.append(4424)
	if addon.getSetting("t-nhl") == "true": tables.append(4380)
	if not tables:
		tables.append(4328)
	return tables

def get_league_id_no_games():
	if addon.getSetting("no-livescores-league") == "0": return 4391
	if addon.getSetting("no-livescores-league") == "1": return 4387
	if addon.getSetting("no-livescores-league") == "2": return 4424
	if addon.getSetting("no-livescores-league") == "3": return 4380
	

def translatematch(string):
	if string.lower() == "finished": return translate(32019)
	elif string.lower() == "halftime": return translate(32020)
	elif string.lower() == "postponed": return translate(32021)
	elif string.lower() == "not started": return translate(32022)
	else: return string

def get_timedelta_string(td):
	if td.days > 0:
		return "(" + str(td.days) + " " + get_days_string(td.days) + " " + translate(32054) + ")"
	else:
		hours = td.seconds/3600
		if hours > 0:
			minutes = (td.seconds - hours*3600)/60
			if minutes > 0:
				return "(" + str(hours) + " " + get_hour_string(hours) + " " + translate(32055) + " " + str(minutes) + " " + get_minutes_string(minutes) +  " " + translate(32054) + ")"
			else:
				return "(" + str(hours) + " " + get_hour_string(hours) + " " + translate(32054) + ")"
		else:
			minutes = td.seconds/60
			if minutes > 0:
				seconds = td.seconds - minutes*60
				return "(" + str(minutes) + " " + get_minutes_string(minutes) + " " +  translate(32055) + " " + str(seconds) + " " + get_seconds_string(seconds) + " " + translate(32054) + ")"
			else:
				return "(" + str(td.seconds) + " " + get_seconds_string(td.seconds) + " " + translate(32054) + ")"

def get_days_string(days):
	if days == 1:
		return translate(32056)
	else:
		return translate(32057)

def get_hour_string(hours):
	if hours == 1:
		return translate(32058)
	else:
		return translate(32059)

def get_minutes_string(minutes):
	if minutes == 1:
		return translate(32060)
	else:
		return translate(32061)

def get_seconds_string(seconds):
	if seconds == 1:
		return translate(32062)
	else:
		return translate(32063)
