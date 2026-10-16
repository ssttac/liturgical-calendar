# Liturgical Calendar

This Python module returns the name, season, week number and liturgical color for any day in the Gregorian calendar. This is fork of [liturgical-app/liturgical-calendar](https://github.com/liturgical-app/liturgical-calendar) that has been readapted to the liturgical calendar of the Episcopal Church of the USA, using the 1979 Book of
Common Prayer and 2024 Lesser Feasts and Fasts.

The original project's algorithm is a direct port to Python of
[`DateTime::Calendar::Liturgical::Christian`](https://github.com/gitpan/DateTime-Calendar-Liturgical-Christian),
which was originally written in Perl and loaded with the calendar of the Episcopal
Church of the USA. It was fed with data from the Church of England's
[Calendar of saints](https://en.wikipedia.org/wiki/Calendar_of_saints_(Church_of_England))
and substantially modified to suit the Anglican calendar.

The output of this module was compared against the
[Church of England Lectionary](https://www.chpublishing.co.uk/features/lectionary),
which is taken to be the canonical source.

As described above, this project now fits the Episcopal Church calendar.

## Installation

This library is [published on PyPI](https://pypi.org/project/liturgical-calendar-tec/).

```console
pip install liturgical-calendar-tec
```

## Usage, as a command

Once installed, this can be run at the command line. Currently it prints
an object with various attributes. This portion of the module needs
improvement, although it is probably more useful as a library.

Specify the date in YYYY-MM-DD format, or leave blank to return info
for today.

```console
# Get info for today
$ liturgical_calendar
name : 
prec : 1
season : Epiphany
season_url : https://en.wikipedia.org/wiki/Epiphany_season
week : Epiphany 1
date : 2025-01-15
sunday_name : First Sunday after the Epiphany
liturgical_day : Wednesday after the First Sunday after the Epiphany
colour : white
colourcode : #fffff6
colourcode_rgbw : (0, 0, 0, 255)
ember : 0

# Get info for an arbitrary date
$ liturgical_calendar 2025-07-04
name : Independence Day (United States)
colour : white
url : https://en.wikipedia.org/wiki/Independence_Day_(United_States)
prec : 7
type : Holy Day
type_url : https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year
source : BCP 1979
season : Ordinary Time
season_url : https://en.wikipedia.org/wiki/Ordinary_Time
week : Proper 8
date : 2025-07-04
sunday_name : Third Sunday after Pentecost
liturgical_day : Independence Day
colourcode : #fffff6
colourcode_rgbw : (0, 0, 0, 255)
ember : 0
```

## Usage, as a library

```py
from liturgical_calendar import liturgical_calendar

# Get info for today (omitting the date defaults to today)
dayinfo = liturgical_calendar()

# Get info for an arbitrary date
# Date can be expressed as a string in YYYY-MM-DD format, a Datetime object, or a Date object
dayinfo = liturgical_calendar('YYYY-MM-DD')

# The result is a tuple of observances, highest precedence first
print(dayinfo[0]['name'])
print(dayinfo[0]['colour'])
```

## Development

This Python project is managed with Poetry. For local testing without installing, run

```console
poetry run liturgical_calendar
```

## Issues

If you find bugs (either in the code or in the calendar data), please
[create an issue on GitHub](https://github.com/ssttac/liturgical-calendar/issues).

Pull requests are always welcome, either to address bugs or add new features.
