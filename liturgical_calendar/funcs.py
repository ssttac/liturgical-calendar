"""
Helper functions for date manipulation
"""

from datetime import date, timedelta
from dateutil.easter import easter
from .titles import HOLY_DAY_TITLES, OMIT_ARTICLE, SUNDAY_TITLES, WEEKDAY_NAMES, WEEKDAY_TITLES
def get_easter(year: int) -> tuple:
    """
    Returns the date easter occurs on for a given year as (month,day)

    Parameters
    ----------
      year: int
        The year to perform the calculation for
    Return
    ------
      month: int
        The month that Easter falls in
      day: int
        The day that Easter falls on
    """
    easter_date = easter(year)
    easter_month = easter_date.month
    easter_day = easter_date.day
    return easter_month, easter_day


def get_advent_sunday(year: int) -> int:
    """
    Return date of Advent Sunday, in days relative to Christmas day
    This is always negative as Advent Sunday is before Christmas day.

    The Sundays of Advent are always the four Sundays before Christmas
    Day, whether it occurs on a Sunday or a weekday (BCP 1979, p. 15).

    Parameters
    ----------
      year: int
        The year to perform the calculation for
    Return
    ------
      offset: int
        The numnber of days that Advent Sunday falls before Christmas day
    """
    day = day_of_week(year, 12, 25)
    if day == 0:
        # Christmas Day itself falls on a Sunday
        return -28
    return -(day + 3 * 7)

def date_to_days(year: int, month: int, day: int) -> int:
    """
    Convert a date from year,month,day to days since 1st January, 1 AD

    Parameters
    ----------
      year: int
        The year to convert
      month: int
        The month to convert
      day: int
        The day to convert
    Return
    ------
      offset: int
        The numnber of days since 1st January, 1 AD
    """
    # Define a start date as passed in
    f_date = date(year, month, day)
    epoch = date(1, 1, 1)
    delta = f_date - epoch
    return delta.days

def day_of_week(year: int, month: int, day: int) -> int:
    """
    Return day of week for any given date in year,month,day format
    between 0-6 where 0 is Sunday, i.e. the first day of the week
    Compare with:
      weekday() which is 0-6 and 0 is Monday
      isoweekday() which is 1-7 and 1 is Monday

    Parameters
    ----------
      year: int
        Year to perform the calculation for
      month: int
        Month to perform the calculation for
      day: int
        Day to perform the calculation for
    Return
    ------
      weekday: int
        Numerical day of the week in the range 0-6, where 0 is Sunday
    """

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Get ISO week day, in range 1-7
    weekday = f_date.isoweekday()

    # Rewrite 7=Sunday as 0=Sunday
    return 0 if weekday == 7 else weekday

def add_delta_days(days: int) -> tuple:
    """
    Convert days since 1st January, 1 AD back to year,month, day

    Parameters
    ----------
      days: int
        Days since 1st January, 1 AD
    Return
    ------
      year: int
        Year of the date [days] since 1st January, 1 AD
      month: int
        Month of the date [days] since 1st January, 1 AD
      day: int
        Day of the date [days] since 1st January, 1 AD
    """
    epoch = date(1, 1, 1)
    end_date = epoch + timedelta(days=days)
    return end_date.year, end_date.month, end_date.day

def _prev_sunday(f_date):
    """
    The Sunday on or before `f_date`

    Parameters
    ----------
      f_date: date
        Any calendar date
    Return
    ------
      sunday: date
        The nearest preceding Sunday
    """
    return f_date - timedelta(days=(f_date.weekday() + 1) % 7)

def liturgical_week(f_date: date) -> tuple:
    """
    Return the liturgical week which `f_date` falls in

    Parameters
    ----------
      f_date: date
        The date to compute for
    Return
    ------
      week: tuple
        A (cycle, week) pair
    """
    year = f_date.year
    easter_month, easter_day = get_easter(year)
    easter_day = date(year, easter_month, easter_day)

    # The Sunday on or before 25 December anchors the Christmas cycle, which
    # runs from the Sunday before Advent Sunday to the day before the Epiphany
    christmas_sunday = _prev_sunday(date(year, 12, 24))
    christmas_start = _prev_sunday(christmas_sunday - timedelta(days=28))
    easter_start = _prev_sunday(easter_day - timedelta(days=49))

    if f_date >= christmas_start or f_date < easter_start:
        anchor_year = year if f_date.month >= 10 else year - 1
        christmas_day = date(anchor_year, 12, 25)
        day_before = date(anchor_year, 12, 24)
        epiphany_day = date(anchor_year + 1, 1, 6)
        if f_date <= day_before:
            # Advent: the four Sundays before Christmas Day (BCP 1979, p. 15).
            week = round((_prev_sunday(f_date) - _prev_sunday(day_before)).days / 7) + 4
            return ('advent', week)
        elif f_date <= epiphany_day - timedelta(days=1):
            # Christmas Day and the Sundays after it.
            return ('christmas', (f_date - _prev_sunday(christmas_day)).days // 7)
        else:
            # Epiphany: its season runs to the Last Sunday after the Epiphany.
            return ('epiphany', (f_date - _prev_sunday(epiphany_day)).days // 7)
    else:
        # The Sunday in which `f_date` falls, counted from Easter Day.
        # Where week 7 is Easter Day to account for Lent
        week = round((_prev_sunday(f_date) - easter_day).days / 7) + 7
        return ('easter', week)


def season_week_name(season: str, weekno: int) -> str:
    """
    The short weekday-style designation of a liturgical week (e.g.
    "Advent 2", "Christmas 1", "Epiphany 3", "Lent 4", "Easter 2")

    Parameters
    ----------
      season: str
        Name of the liturgical season
      weekno: int
        Number of the week
    Return
    ------
      name: str
        Rendered designation of the week
    """
    sunday = None
    if not weekno:
        sunday = season
    elif weekno > 0:
        sunday = f"{season} {weekno}"
    elif weekno < 1:
        weekno = abs(weekno)
        sunday = f"{weekno} {season}"

    return sunday
def sunday_name(f_date: date):
    """
    The title of the Sunday which begins the liturgical week containing `f_date`

    Parameters
    ----------
      f_date: date
        The date to compute for
    Return
    ------
      name: str
        The title of the week's Sunday
    """
    cycle, week = liturgical_week(f_date)
    return SUNDAY_TITLES.get((cycle, week))

def liturgical_day(f_date: date, occupant_name: str = None, occupant_is_fixed: bool = False) -> str:
    """
    The title of the day, derived from the Titles of the Seasons, Sundays
    and Major Holy Days (BCP 1979, pp. 31-32)

    Parameters
    ----------
      f_date: date
        The date to compute for
      occupant_name: str | None
        The name of a major observance (Principal Feast, Holy Day or Major
        Fast) which the calendar observes on this date
      occupant_is_fixed: bool
        Whether that observance is the fixed feast of the date itself
    Return
    ------
      name: str
        The title of the day
    """
    if occupant_name is not None:
        if occupant_is_fixed:
            holy_day = HOLY_DAY_TITLES.get((f_date.month, f_date.day))
            if holy_day:
                return holy_day
            return occupant_name
        return occupant_name
    if f_date.weekday() == 6:
        return sunday_name(f_date)
    holy_day = HOLY_DAY_TITLES.get((f_date.month, f_date.day))
    if holy_day:
        return holy_day
    cycle, week = liturgical_week(f_date)
    special = WEEKDAY_TITLES.get((cycle, week), {}).get(WEEKDAY_NAMES[f_date.weekday()])
    if special:
        return special
    title = sunday_name(f_date)
    if not title:
        return WEEKDAY_NAMES[f_date.weekday()]
    if (cycle, week) in OMIT_ARTICLE:
        return f'{WEEKDAY_NAMES[f_date.weekday()]} after {title}'
    return f'{WEEKDAY_NAMES[f_date.weekday()]} after the {title}'
def colour_code(colour: str) -> str:
    """
    Accept a colour name and return a hex colour code,
    intended for use for display on a web page

    Parameters
    ----------
      colour: str
        The name of a colour
    Return
    ------
      code: str
        The corresponding hex code for the named colour
    """
    codes = {
        'white': '#fffff6',
        'red': '#ce0002',
        'rose': '#eb597a',
        'purple': '#664fa6',
        'green': '#279942',
        'not given': '#000000'
    }

    return codes.get(colour)

def colour_code_rgbw(colour: str) -> tuple:
    """
    Accept a colour name and return a RGBW colour code,
    intended for use for display on an RGBW smart lamp

    Parameters
    ----------
      colour: str
        The name of a colour
    Return
    ------
      code: tuple
        The corresponding RGBW code for the named colour
    """
    codes = {
        'white': (0, 0, 0, 255),
        'red': (255, 0, 0, 0),
        'rose': (255, 114, 177, 48),
        'purple': (86, 5, 255, 0),
        'green': (7, 255, 15, 0),
        'not given': (0, 0, 0, 0)
    }

    return codes.get(colour)
