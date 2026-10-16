"""
Tests for the liturgical calendar of The Episcopal Church (USA), as set out
in the 1979 Book of Common Prayer and Lesser Feasts and Fasts (2024).

Each test is driven by a concrete calendar date and asserts the name, season,
precedence and (where relevant) colour or Ember-day status that the library
reports for that date.
"""

from liturgical_calendar.liturgical import liturgical_calendar
from liturgical_calendar.feasts import lookup_feast


def test_christmas_day():
    """Christmas Day is a Principal Feast observed on 25 December."""
    result = liturgical_calendar("2025-12-25")[0]
    assert result["name"] == "The Nativity of Our Lord Jesus Christ"
    assert result["season"] == "Christmas"
    assert result["colour"] == "white"
    assert result["prec"] == 9


def test_easter_day():
    """Easter Day is a Principal Feast, the keystone of the movable cycle."""
    result = liturgical_calendar("2025-04-20")[0]
    assert result["name"] == "Easter Day"
    assert result["season"] == "Easter"
    assert result["colour"] == "white"
    assert result["prec"] == 9


def test_ash_wednesday_begins_lent():
    """Ash Wednesday (46 days before Easter) is a Major Fast that opens Lent."""
    result = liturgical_calendar("2025-03-05")[0]
    assert result["name"] == "Ash Wednesday"
    assert result["season"] == "Lent"
    assert result["colour"] == "purple"
    assert result["prec"] == 9


def test_good_friday_colour_not_given():
    """Good Friday has no liturgical colour ('not given')."""
    result = liturgical_calendar("2025-04-18")[0]
    assert result["name"] == "Good Friday"
    assert result["season"] == "Holy Week"
    assert result["colour"] == "not given"
    assert result["prec"] == 9


def test_presentation_takes_precedence_of_sunday():
    """The Presentation is one of the few fixed feasts that overrides a Sunday."""
    # 2 February 2025 falls on a Sunday; the Presentation (prec 9) wins.
    result = liturgical_calendar("2025-02-02")[0]
    assert result["name"] == "The Presentation of Our Lord Jesus Christ in the Temple"
    assert result["prec"] == 9
    assert result["colour"] == "white"


def test_fixed_major_feast_transfers_off_sunday():
    """A fixed Major Feast falling on a Sunday is transferred to the next day."""
    # 14 September 2025 is a Sunday: the day is the Sunday (Proper 19)...
    on_sunday = liturgical_calendar("2025-09-14")[0]
    assert on_sunday["prec"] == 8
    assert on_sunday["type"] == "Sunday"
    assert on_sunday["name"] == "Proper 19"
    # ...and Holy Cross Day is observed (transferred) on the following Monday.
    next_day = liturgical_calendar("2025-09-15")[0]
    assert next_day["name"] == "Holy Cross Day (transferred)"
    assert next_day["prec"] == 7
    assert next_day["colour"] == "white"


def test_all_saints_and_its_sunday():
    """All Saints (1 November) may also be observed on the following Sunday."""
    on_fixed_day = liturgical_calendar("2025-11-01")[0]
    assert on_fixed_day["name"] == "All Saints"
    assert on_fixed_day["prec"] == 9
    assert on_fixed_day["colour"] == "white"
    following_sunday = liturgical_calendar("2025-11-02")[0]
    assert following_sunday["name"] == "All Saints' Sunday"
    assert following_sunday["prec"] == 8


def test_gaudete_and_laetare_sundays_are_rose():
    """The Third Sunday of Advent and Fourth Sunday in Lent are rose."""
    for date, title in ("2025-12-14", "Gaudete"), ("2026-12-13", "Gaudete"), ("2027-12-12", "Gaudete"):
        gaudete = liturgical_calendar(date)[0]
        assert gaudete["name"] == f"{title} Sunday"
        assert gaudete["colour"] == "rose"
        assert gaudete["sunday_name"] == "Third Sunday of Advent"
        assert gaudete["liturgical_day"] == "Third Sunday of Advent"
        assert gaudete["colourcode"] == "#eb597a"
        assert gaudete["colourcode_rgbw"] == (255, 114, 177, 48)
    for laetare_date in "2025-03-30", "2026-03-15", "2027-03-07":
        laetare = liturgical_calendar(laetare_date)[0]
        assert laetare["name"] == "Laetare Sunday"
        assert laetare["colour"] == "rose"
        assert laetare["sunday_name"] == "Fourth Sunday in Lent"
        assert laetare["liturgical_day"] == "Fourth Sunday in Lent"
    # No other Sunday is rose.
    from datetime import date, timedelta
    for y in (2025, 2026, 2027):
        d = date(y, 1, 1)
        while d.year == y:
            if d.weekday() == 6:
                r = liturgical_calendar(d)[0]
                assert (r["colour"] == "rose") == (r["name"] in ("Gaudete Sunday", "Laetare Sunday"))
            d += timedelta(days=1)

def test_us_national_holy_days():
    """Independence Day (4 July) and Thanksgiving (4th Thursday in November)."""
    independence = liturgical_calendar("2025-07-04")[0]
    assert independence["name"] == "Independence Day (United States)"
    assert independence["prec"] == 7
    assert independence["colour"] == "white"
    thanksgiving = liturgical_calendar("2025-11-27")[0]
    assert thanksgiving["name"] == "Thanksgiving Day"
    assert thanksgiving["prec"] == 7
    # 2026's fourth Thursday in November is 26 November.
    thanksgiving_2026 = liturgical_calendar("2026-11-26")[0]
    assert thanksgiving_2026["name"] == "Thanksgiving Day"


def test_ember_days():
    """Ember days fall on Wed/Fri/Sat after Pentecost, Holy Cross, and 13 December."""
    # After the Day of Pentecost (8 June 2025).
    assert liturgical_calendar("2025-06-11")[0]["ember"] == 1
    assert liturgical_calendar("2025-06-13")[0]["ember"] == 1
    assert liturgical_calendar("2025-06-14")[0]["ember"] == 1
    # After Holy Cross Day (14 September 2025).
    assert liturgical_calendar("2025-09-17")[0]["ember"] == 1
    assert liturgical_calendar("2025-09-19")[0]["ember"] == 1
    assert liturgical_calendar("2025-09-20")[0]["ember"] == 1
    # After 13 December 2025.
    assert liturgical_calendar("2025-12-17")[0]["ember"] == 1
    # A plain non-ember weekday.
    assert liturgical_calendar("2025-06-16")[0]["ember"] == 0


def test_multiple_commemorations_share_a_date():
    """29 July and 7 September each carry two commemorations (stored as a tuple of dicts)."""
    assert liturgical_calendar("2025-07-29")[0]["name"] == "Mary and Martha of Bethany"
    assert liturgical_calendar("2024-07-29")[0]["name"] == "Mary and Martha of Bethany"
    # 2024-09-07 (Saturday): Kassiani (prec 4) outranks trial-use Élie Naud (prec 3).
    assert liturgical_calendar("2024-09-07")[0]["name"] == "Kassiani, Poet and Hymnographer, 865"
    # The public API exposes both commemorations, not just the winner.
    for value in ("2025-07-29", "2024-09-07"):
        results = liturgical_calendar(value)
        assert isinstance(results, tuple)
        assert len(results) == 2
        assert [item["prec"] for item in results] == [4, 3]
        assert results[1]["source"] == "LFF 2024 (trial use)"
        assert results[1]["type"] == "Commemoration"
    assert liturgical_calendar("2025-07-29")[1]["name"] == "The Ordination of the Philadelphia Eleven"
    assert liturgical_calendar("2024-09-07")[1]["name"] == "Élie Naud"
    # Both commemorations are present in the underlying lookup for each day.
    assert [f["name"] for f in lookup_feast(10729)] == [
        "Mary and Martha of Bethany",
        "The Ordination of the Philadelphia Eleven",
    ]
    assert [f["name"] for f in lookup_feast(10907)] == [
        "Kassiani, Poet and Hymnographer, 865",
        "Élie Naud",
    ]


def test_feast_overrides_overlapping_lff_saint():
    """A Principal Feast or Major Feast takes precedence over an LFF saint on the same day."""
    # Easter Day 2010 (4 April) falls on the date of Martin Luther King, Jr.
    # The Principal Feast (prec 9) overrides the LFF saint (prec 4).
    assert liturgical_calendar("2010-04-04")[0]["name"] == "Easter Day"
    assert liturgical_calendar("2010-04-04")[0]["prec"] == 9
    # Holy Cross Day (14 September 2025, a Sunday) transfers to 15 September,
    # where it overrides the LFF saint Catherine of Genoa.
    assert liturgical_calendar("2025-09-15")[0]["name"] == "Holy Cross Day (transferred)"
    assert liturgical_calendar("2025-09-15")[0]["prec"] == 7



def test_october_2026_episcopal_calendar():
    """Every October date matches the supplied Episcopal Church calendar image.

    Names retain library spelling and the explicit transfer suffix. Blank dates
    retain the API's singleton seasonal record. Sundays retain Proper numbering.
    """
    expected = {
        1: ("Thérèse of Lisieux, Monastic, 1897",),
        2: ("Remigius of Rheims, Bishop, c. 530",),
        3: ("John Raleigh Mott, Ecumenist and Missionary, 1955",),
        4: ("Proper 22",),
        5: ("Francis of Assisi, Friar and Deacon, 1226 (transferred)",),
        6: ("William Tyndale, Priest, 1536",),
        7: ("Birgitta of Sweden, Mystic, 1373",),
        8: ("",),
        9: ("Robert Grosseteste, Bishop, 1253",),
        10: ("Vida Dutton Scudder, Educator, 1954",),
        11: ("Proper 23",),
        12: ("Edith Cavell, Nurse, 1915", "Philip, Deacon and Evangelist (transferred)"),
        13: ("",),
        14: ("Samuel Isaac Joseph Schereschewsky, Bishop and Missionary, 1906",),
        15: ("Teresa of Avila, Mystic and Monastic Reformer, 1582",),
        16: ("Hugh Latimer and Nicholas Ridley, Bishops and Martyrs, 1555, and Thomas Cranmer, Archbishop of Canterbury, 1556",),
        17: ("Ignatius of Antioch, Bishop and Martyr, c. 115",),
        18: ("Proper 24",),
        19: ("Saint Luke the Evangelist (transferred)",),
        20: ("Cornelius the Centurion", "Henry Martyn, Priest and Missionary, 1812 (transferred)"),
        21: ("",),
        22: ("",),
        23: ("Saint James of Jerusalem, Brother of Our Lord Jesus Christ and Martyr, c. 62",),
        24: ("",),
        25: ("Proper 25",),
        26: ("Alfred, King, 899", "Tabitha (Dorcas) of Joppa (transferred)"),
        27: ("",),
        28: ("Saint Simon and Saint Jude, Apostles",),
        29: ("James Hannington, Bishop, and his Companions, Martyrs, 1885",),
        30: ("Maryam of Qidun, Monastic, fourth century",),
        31: ("",),
    }
    from datetime import date
    for day, names in expected.items():
        results = liturgical_calendar(f"2026-10-{day:02d}")
        assert isinstance(results, tuple)
        assert tuple(item["name"] for item in results) == names, day
        assert [item["prec"] for item in results] == sorted(
            (item["prec"] for item in results), reverse=True
        ), day
        for item in results:
            assert item["date"] == date(2026, 10, day)
            assert isinstance(item["colourcode"], str)
            assert isinstance(item["colourcode_rgbw"], tuple)
            if item["name"] and item.get("type") != "Sunday":
                assert item["source"] in ("BCP 1979", "LFF 2024", "LFF 2024 (trial use)")
    # Cached schedules must not be mutated by callers rendering or editing results.
    changed = liturgical_calendar("2026-10-05")
    changed[0]["name"] = "changed by caller"
    assert liturgical_calendar("2026-10-05")[0]["name"] == expected[5][0]


def test_sunday_name_titles():
    """sunday_name carries the BCP p. 31-32 title of the week's Sunday."""
    # Sundays carry their own title...
    assert liturgical_calendar("2026-10-25")[0]["sunday_name"] == "Twenty-Second Sunday after Pentecost"
    assert liturgical_calendar("2026-12-20")[0]["sunday_name"] == "Fourth Sunday of Advent"
    assert liturgical_calendar("2026-05-24")[0]["sunday_name"] == "Pentecost"
    assert liturgical_calendar("2026-05-31")[0]["sunday_name"] == "Trinity Sunday"
    assert liturgical_calendar("2026-11-22")[0]["sunday_name"] == "Last Sunday after Pentecost"
    assert liturgical_calendar("2026-04-05")[0]["sunday_name"] == "Easter Day"
    assert liturgical_calendar("2026-03-29")[0]["sunday_name"] == "Palm Sunday"
    assert liturgical_calendar("2026-02-15")[0]["sunday_name"] == "Last Sunday after the Epiphany"
    # ...and a weekday carries the title of the preceding (week's) Sunday.
    assert liturgical_calendar("2026-10-15")[0]["sunday_name"] == "Twentieth Sunday after Pentecost"
    assert liturgical_calendar("2026-05-27")[0]["sunday_name"] == "Pentecost"
    assert liturgical_calendar("2026-12-30")[0]["sunday_name"] == "First Sunday after Christmas Day"
    assert liturgical_calendar("2026-02-19")[0]["sunday_name"] == "Last Sunday after the Epiphany"
    # Feast-anchored weeks carry the feast's title (2023-12-29 is keyed to
    # Christmas itself, whence "Friday after Christmas").
    assert liturgical_calendar("2023-12-29")[0]["sunday_name"] == "Christmas"
    assert liturgical_calendar("2026-01-07")[0]["sunday_name"] == "Epiphany"


def test_liturgical_day_titles():
    """liturgical_day names each day per the BCP p. 31-32 titles."""
    # A weekday is named for its week's Sunday; the week's own Sunday title
    # needs no further wording.
    assert liturgical_calendar("2026-05-27")[0]["liturgical_day"] == "Wednesday after Pentecost"
    assert liturgical_calendar("2026-10-15")[0]["liturgical_day"] == "Thursday after the Twentieth Sunday after Pentecost"
    # Lesser feasts never displace the day's title.
    assert liturgical_calendar("2026-10-15")[0]["name"] == "Teresa of Avila, Mystic and Monastic Reformer, 1582"
    # Christmas-season weekdays follow Christmas itself.
    assert liturgical_calendar("2023-12-29")[0]["liturgical_day"] == "Friday after Christmas"
    # Holy Week and Easter Week carry their own titled days.
    assert liturgical_calendar("2026-03-30")[0]["liturgical_day"] == "Monday in Holy Week"
    assert liturgical_calendar("2026-04-06")[0]["liturgical_day"] == "Monday in Easter Week"
    assert liturgical_calendar("2026-04-02")[0]["liturgical_day"] == "Maundy Thursday"
    assert liturgical_calendar("2026-04-03")[0]["liturgical_day"] == "Good Friday"
    assert liturgical_calendar("2026-04-04")[0]["liturgical_day"] == "Holy Saturday"
    assert liturgical_calendar("2026-02-19")[0]["liturgical_day"] == "Thursday after Ash Wednesday"


def test_liturgical_day_leaves_lff_saints_alone():
    """Lesser Feasts change the name field but not the day's title."""
    result = liturgical_calendar("2023-12-29")[0]
    assert result["name"] == "Thomas Becket, Archbishop of Canterbury and Martyr, 1170"
    assert result["liturgical_day"] == "Friday after Christmas"


def test_liturgical_day_of_titled_holy_days():
    """A titled Holy Day carries its own title; transfers keep theirs."""
    assert liturgical_calendar("2026-12-26")[0]["liturgical_day"] == "Feast of St. Stephen"
    assert liturgical_calendar("2025-11-01")[0]["liturgical_day"] == "All Saints' Day"
    assert liturgical_calendar("2025-02-02")[0]["liturgical_day"] == "The Presentation of Our Lord Jesus Christ in the Temple"
    assert liturgical_calendar("2025-09-15")[0]["liturgical_day"] == "Holy Cross Day (transferred)"
    assert liturgical_calendar("2025-11-27")[0]["liturgical_day"] == "Thanksgiving Day"
    # The Sunday title remains that of the week's Sunday even when the fixed
    # feast is displaced from it (26 December 2021 is the First Sunday after
    # Christmas Day; St Stephen transfers away).
    assert liturgical_calendar("2021-12-26")[0]["liturgical_day"] == "First Sunday after Christmas Day"
    assert liturgical_calendar("2021-12-26")[0]["sunday_name"] == "First Sunday after Christmas Day"


def test_sunday_name_survives_movable_feasts():
    """A movable Principal Feast on a Sunday keeps the Sunday's own title."""
    assert liturgical_calendar("2026-05-24")[0]["liturgical_day"] == "Pentecost"
    assert liturgical_calendar("2026-05-31")[0]["liturgical_day"] == "Trinity Sunday"
    # Every field carries the two new keys on every record of the date.
    for item in liturgical_calendar("2026-12-26"):
        assert "sunday_name" in item
        assert item["liturgical_day"] == "Feast of St. Stephen"
