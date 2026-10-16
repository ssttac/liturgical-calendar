"""
This Python module will return the name, season, week number and liturgical
colour for any day in the Gregorian calendar, according to the liturgical
calendar of The Episcopal Church (USA) as set out in the 1979 Book of
Common Prayer (and its 2020 revisions) together with Lesser Feasts and
Fasts (2024).
"""

import sys
from datetime import datetime, date, timedelta
from functools import lru_cache
from .funcs import get_easter, get_advent_sunday, date_to_days, day_of_week, colour_code, colour_code_rgbw, season_week_name, sunday_name, liturgical_day
from .feasts import lookup_feast

##########################################################################

def _first_ember_days(year, month, anchor_day, target_weekdays):
    """
    Returns the set of (month, day) tuples for the first occurrences of each
    weekday in `target_weekdays` strictly after the anchor date.
    """
    anchor = date(year, month, anchor_day)
    anchor_dow = (anchor.weekday() + 1) % 7  # 0=Sunday
    result = set()
    for t in target_weekdays:
        delta = (t - anchor_dow) % 7
        if delta == 0:
            delta = 7
        d = anchor + timedelta(days=delta)
        result.add((d.month, d.day))
    return result

@lru_cache(maxsize=8)
def _calendar_observances(year):
    """Schedule commemorations together on the next weekday free of major feasts.

    Native commemorations precede transferred ones of equal rank. Major feasts
    occupy a day alone, so displaced lesser feasts wait past them (for example,
    Henry Martyn waits past Saint Luke on 19 October 2026).
    """
    appointments = {}
    pending = []
    # Include the preceding year so transfers across New Year are resolved.
    current = date(year - 1, 1, 1)
    end = date(year, 12, 31)
    while current <= end:
        easterm, easterd = get_easter(current.year)
        offset = (current - date(current.year, easterm, easterd)).days
        movable = lookup_feast(offset) or []
        fixed = lookup_feast(10000 + 100 * current.month + current.day) or []
        native = movable + fixed
        if current.month == 11 and current.weekday() == 3 and 22 <= current.day <= 28:
            native.append({ 'name': 'Thanksgiving Day', 'colour': 'white',
                            'url': 'https://en.wikipedia.org/wiki/Thanksgiving_(United_States)',
                            'prec': 7, 'type': 'Holy Day', 'source': 'BCP 1979',
                            'type_url': 'https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year' })
        sunday = current.weekday() == 6
        major = sorted((f for f in native if f['prec'] >= 7),
                       key=lambda f: f['prec'], reverse=True)
        observed = []
        newly_displaced = []
        if major and (not sunday or major[0]['prec'] >= 8):
            observed.append(major[0])
        elif not sunday:
            waiting_major = next((f for f in pending if f['prec'] >= 7), None)
            if waiting_major is not None:
                observed.append(waiting_major)
                pending.remove(waiting_major)
        blocked = sunday or bool(observed)
        for feast in native:
            if feast in observed:
                continue
            if blocked:
                newly_displaced.append(feast)
            else:
                observed.append(feast)
        if not blocked:
            observed.extend(pending)
            pending = []
        for feast in newly_displaced:
            carried = dict(feast)
            carried['name'] += ' (transferred)'
            pending.append(carried)
        appointments[current] = (tuple(observed), tuple(newly_displaced))
        current += timedelta(days=1)
    return appointments

_RESULT_KEYS = ('date', 'liturgical_day', 'sunday_name', 'season', 'season_url',
                'week', 'name', 'type', 'type_url', 'prec', 'source', 'martyr',
                'url', 'colour', 'colourcode', 'colourcode_rgbw', 'ember')


def _ordered_record(record: dict) -> dict:
    """Rebuild a record dict with its keys in _RESULT_KEYS order."""
    ordered = {key: record[key] for key in _RESULT_KEYS if key in record}
    ordered.update({key: value for key, value in record.items()
                    if key not in _RESULT_KEYS})
    return ordered


def liturgical_calendar(s_date: str, transferred: bool = False):
    """
    Return a precedence-ordered tuple of observance dictionaries for a date.

    Plain weekdays return one seasonal dictionary with an empty name.
    With transferred=True, return the unrendered feasts displaced on that date.
    """

    # s_date could in a variety of formats
    # We standardise to f_date as a Date
    if isinstance(s_date, datetime):
        # If datetime, strip it to the date
        f_date = s_date.date()
    elif isinstance(s_date, date):
        # If date, accept it
        f_date = s_date
    elif isinstance(s_date, str):
        # If string, try to parse a YYYY-MM-DD
        f_date = datetime.strptime(s_date, "%Y-%m-%d").date()
    else:
        # Otherwise use today's date
        f_date = date.today()

    # Extract the components from the date
    year = f_date.year
    month = f_date.month
    day = f_date.day
    dayofweek = day_of_week(year, month, day)

    # Calculate some values in Julian date
    days = date_to_days(year, month, day)
    easterm, easterd = get_easter(year)
    easterday = date_to_days(year, easterm, easterd)

    possibles = []

    # "The Church Year consists of two cycles of feasts and holy days: one is
    #  dependent upon the movable date of the Sunday of the Resurrection or
    #  Easter Day; the other, upon the fixed date of December 25, the Feast
    #  of our Lord's Nativity or Christmas Day."
    easter_point = days - easterday
    christmas_point = 0

    # We will store the amount of time until (-ve) or since (+ve) Christmas in
    # christmas_point. Let's make the cut-off date the end of February,
    # since we'll be dealing with Easter-based dates after that, and it
    # avoids the problems of considering leap years.
    if month > 2:
        christmas_point = days - date_to_days(year, 12, 25)
    else:
        christmas_point = days - date_to_days(year - 1, 12, 25)

    advent_sunday = get_advent_sunday(year)

    # The First Sunday after the Epiphany is the Baptism of our Lord, and
    # All Saints' Day may always be observed on the Sunday following
    # November 1 (BCP 1979, p. 15). Both are computed relative to Christmas.
    baptism_sunday = 12 + ((7 - day_of_week(year, 1, 6)) % 7 or 7)
    all_saints_sunday = -54 + (7 - day_of_week(year, 11, 1)) % 7

    # The Sundays in the Season after Pentecost are designated "Proper N"
    # where N = 1 is the Sunday closest to May 11 (BCP 1979, p. 157-158).
    may11 = date_to_days(year, 5, 11)
    m11dow = day_of_week(year, 5, 11)
    proper_anchor = may11 - m11dow if m11dow <= 3 else may11 + (7 - m11dow)

    # Break up the liturgical year into seasons, starting at Advent.
    # The Episcopal Church observes no Septuagesima ("before Lent") season:
    # the Epiphany season runs simply to Ash Wednesday.
    if christmas_point >= advent_sunday and christmas_point <= -1:
        season = 'Advent'
        season_url = 'https://en.wikipedia.org/wiki/Advent'
        weekno = 1 + (christmas_point - advent_sunday) // 7
    elif christmas_point >= 0 and christmas_point <= 11:
        # The Twelve Days of Christmas.
        season = 'Christmas'
        season_url = 'https://en.wikipedia.org/wiki/Christmastide'
        weekno = 1 + (christmas_point - dayofweek) // 7
    elif christmas_point >= 12 and easter_point <= -47:
        season = 'Epiphany'
        season_url = 'https://en.wikipedia.org/wiki/Epiphany_season'
        weekno = 1 + (christmas_point - 12 - dayofweek) // 7
    elif easter_point >= -46 and easter_point < -7:
        season = 'Lent'
        season_url = 'https://en.wikipedia.org/wiki/Lent'
        weekno = (easter_point + 50 - dayofweek) // 7
    elif easter_point >= -7 and easter_point < 0:
        season = 'Holy Week'
        season_url = 'https://en.wikipedia.org/wiki/Holy_Week'
        weekno = 0
    elif easter_point >= 0 and easter_point < 49:
        season = 'Easter'
        season_url = 'https://en.wikipedia.org/wiki/Eastertide'
        weekno = 1 + easter_point // 7
    elif easter_point >= 49 and easter_point < 56:
        # The week of the Day of Pentecost.
        season = 'Pentecost'
        season_url = 'https://en.wikipedia.org/wiki/Pentecost'
        weekno = 0
    else:
        # Season after Pentecost (Ordinary Time), from the first Sunday after
        # Pentecost to the last Sunday before Advent.
        season = 'Ordinary Time'
        season_url = 'https://en.wikipedia.org/wiki/Ordinary_Time'
        weekno = 1 + (days - dayofweek - proper_anchor) // 7
    weekno = int(weekno) if int(weekno) != 0 else None

    # Resolve fixed and movable observances, retaining every commemoration
    # appointed for this date, including those carried past a Sunday or feast.
    appointed, displaced = _calendar_observances(year)[f_date]
    if transferred:
        return tuple(_ordered_record(dict(feast)) for feast in displaced)
    possibles.extend(dict(feast) for feast in appointed)

    # Handle Sundays. Every Sunday has some designation.
    if weekno and dayofweek == 0:
        # Special Sundays are appended first so they win the stable sort over the
        # generic Sunday (both prec 8) when both are present.
        if christmas_point == advent_sunday:
            possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': "Advent Sunday", 'colour': 'purple' })
        elif christmas_point == advent_sunday - 7:
            possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': "Christ the King", 'colour': 'white' })
        elif christmas_point == baptism_sunday:
            possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': "The Baptism of our Lord", 'colour': 'white',
                               'url': 'https://en.wikipedia.org/wiki/Baptism_of_the_Lord' })
        elif christmas_point == all_saints_sunday:
            possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': "All Saints' Sunday", 'colour': 'white',
                               'url': 'https://en.wikipedia.org/wiki/All_Saints%27_Day' })
        else:
            if season == 'Ordinary Time':
                possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': f"Proper {weekno}" })
            else:
                possibles.append({ 'prec': 8, 'type': 'Sunday', 'name': season_week_name(season, weekno) })
    # So, which event takes priority? Stable sort keeps insertion order for ties.
    possibles = sorted(possibles, key=lambda x: x['prec'], reverse=True)

    # A Principal Feast replaces the generic Sunday designation.
    if possibles and possibles[0]['prec'] == 9:
        possibles = [feast for feast in possibles if feast.get('type') != 'Sunday']
    if not possibles:
        possibles = [{ 'name': '', 'prec': 1 }]

    # Render a Week name with or without number
    if season == 'Ordinary Time' and weekno and weekno > 0:
        week = f"Proper {weekno}"
    elif weekno and weekno > 0:
        week = f"{season} {weekno}"
    elif weekno and weekno < -1:
        weekno = abs(weekno)
        week = f"{weekno} {season}"
    elif weekno and weekno == -1:
        week = f"Sunday next {season}"
    else:
        week = season

    # The Titles of the Seasons, Sundays and Major Holy Days (BCP 1979, pp. 31-32)
    occupant = possibles[0] if possibles else None
    occupant_is_major = occupant is not None and occupant.get('prec', 0) >= 7
    fixed_today = lookup_feast(10000 + 100 * f_date.month + f_date.day)
    occupant_is_fixed_today = (occupant_is_major and bool(fixed_today)
                               and any(occupant.get('name') == feast['name'] for feast in fixed_today))
    if f_date.weekday() == 6 and not occupant_is_fixed_today:
        day_title = sunday_name(f_date)
    elif occupant is not None and occupant_is_fixed_today:
        # The day's own fixed feast (e.g. St Stephen on 26 December).
        day_title = liturgical_day(f_date, occupant['name'], True)
    elif occupant is not None and occupant_is_major:
        # A movable feast or fast, or a transferred observance.
        day_title = occupant['name']
    else:
        day_title = liturgical_day(f_date)

    results = []
    for result in possibles:
        # Append season info regardless
        result['season'] = season
        result['season_url'] = season_url
        result['week'] = week
        result['date'] = f_date
        result['sunday_name'] = sunday_name(f_date)
        result['liturgical_day'] = day_title
        # Gaudete and Laetare Sundays are rose
        if result['name'] == 'Advent 3':
            result['colour'] = 'rose'
            result['name'] = 'Gaudete Sunday'
            result['url'] = 'https://en.wikipedia.org/wiki/Gaudete_Sunday'
        elif result['name'] == 'Lent 4':
            result['colour'] = 'rose'
            result['name'] = 'Laetare Sunday'
            result['url'] = 'https://en.wikipedia.org/wiki/Laetare_Sunday'

        # If no colour is already set...
        if result.get('colour') is None:
            # Any feast (Principal, Holy Day, Lesser Feast, Commemoration) is
            # generally white, or red for martyrs, unless a colour is given in the
            # data (e.g. Good Friday "not given", Maundy Thursday "white").
            if result['prec'] >= 3 and result.get('type') != 'Sunday':
                if result.get('martyr'):
                    result['colour'] = 'red'
                else:
                    result['colour'] = 'white'
            else:
                # Not a feast day: set a default colour for the season
                if season == 'Advent':
                    result['colour'] = 'purple'
                elif season == 'Christmas':
                    result['colour'] = 'white'
                elif season == 'Epiphany':
                    result['colour'] = 'white'
                elif season == 'Lent':
                    result['colour'] = 'purple'
                elif season == 'Holy Week':
                    result['colour'] = 'red'
                elif season == 'Easter':
                    result['colour'] = 'white'
                else:
                    # Ordinary Time
                    result['colour'] = 'green'

        # Set colour code
        result['colourcode'] = colour_code(result['colour'])
        result['colourcode_rgbw'] = colour_code_rgbw(result['colour'])

        # Ember Days (BCP 1979, p. 17): the Wednesdays, Fridays and Saturdays
        # after the First Sunday in Lent, the Day of Pentecost, Holy Cross Day
        # (September 14), and December 13.
        result['ember'] = 0
        if dayofweek in [3, 5, 6]:
            if week in ['Lent 1', 'Pentecost']:
                result['ember'] = 1
            elif (month, day) in _first_ember_days(year, 9, 14, (3, 5, 6)):
                result['ember'] = 1
            elif (month, day) in _first_ember_days(year, 12, 13, (3, 5, 6)):
                result['ember'] = 1

        results.append(_ordered_record(result))
    return tuple(results)

def main():
    """
    Display liturgical info to a human user
    """

    # Read in args
    if len(sys.argv) > 1:
        mydate = sys.argv[1]
    else:
        mydate = None

    info = liturgical_calendar(mydate)
    for observance in info:
        for key, value in observance.items():
            print(key, ':', value)
        print()

if __name__ == '__main__':
    main()
