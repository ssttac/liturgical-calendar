"""
This is a massive function which effectively contains all of the data from
the Calendar of the Church Year of The Episcopal Church (USA), as found in
the 1979 Book of Common Prayer and in Lesser Feasts and Fasts (2024):
https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year
"""
def lookup_feast(datecode):
    """
    The feasts dict contains structured data. Most keys map to a single feast
    dict, but a date carrying more than one commemoration (29 July and
    7 September) maps to a tuple of dicts. The result is always returned as a
    list of annotated feast dicts (or None when the date has no feast).
    """
    feasts = {

        # Episcopal Holy Days are variously categorised as Principal Feasts,
        # Holy Days (Feasts of our Lord and other Major Feasts), Major Fasts,
        # Lesser Feasts, or Commemorations authorized for trial use.
        # The observance of Lesser Feasts or Commemorations is optional.
        # Principal Feasts (and the days of Holy Week) = prec 9
        # Sundays                                          = prec 8
        # Holy Days                                        = prec 7
        # Lesser Feasts                                    = prec 4
        # Commemorations (trial use, shown in [brackets])  = prec 3

        # Each entry records its calendar authority in 'source':
        #   BCP 1979            - the red-letter Calendar of the Church Year
        #   LFF 2024            - Lesser Feasts and Fasts, 2024
        #   LFF 2024 (trial use)- commemorations authorized by GC 2024 for
        #                         trial use, printed in [brackets] in LFF

        # Dates relative to Easter are encoded as the number of days after Easter.
        -46: { 'name': 'Ash Wednesday', 'colour':'purple', 'url': 'https://en.wikipedia.org/wiki/Ash_Wednesday', 'prec':9, 'type': 'Major Fast', 'source': 'BCP 1979' },
        -7: { 'name': 'The Sunday of the Passion: Palm Sunday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Palm_Sunday', 'prec':8, 'type': 'Sunday', 'source': 'BCP 1979' },
        -6: { 'name': 'Monday in Holy Week', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Monday', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        -5: { 'name': 'Tuesday in Holy Week', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Tuesday', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        -4: { 'name': 'Wednesday in Holy Week', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Wednesday', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        -3: { 'name': 'Maundy Thursday', 'colour':'white', 'url': 'https://en.wikipedia.org/wiki/Maundy_Thursday', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        -2: { 'name': 'Good Friday', 'colour':'not given', 'url': 'https://en.wikipedia.org/wiki/Good_Friday', 'prec':9, 'type': 'Major Fast', 'source': 'BCP 1979' },
        -1: { 'name': 'Holy Saturday', 'colour':'not given', 'url': 'https://en.wikipedia.org/wiki/Holy_Saturday', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        0 : { 'name': 'Easter Day', 'url': 'https://en.wikipedia.org/wiki/Easter', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        39: { 'name': 'Ascension Day', 'url': 'https://en.wikipedia.org/wiki/Ascension_Day', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        49: { 'name': 'The Day of Pentecost: Whitsunday', 'colour': 'red', 'url': 'https://en.wikipedia.org/wiki/Pentecost', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        56: { 'name': 'Trinity Sunday', 'url': 'https://en.wikipedia.org/wiki/Trinity_Sunday', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },

        # Dates relative to Christmas are encoded as 10000 + 100*m + d for simplicity.
        10101: { 'name': 'The Holy Name of Our Lord Jesus Christ', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Holy_Name_of_Jesus', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        10104: { 'name': 'Elizabeth Ann Seton, Vowed Religious and Educator, 1821', 'url': 'https://en.wikipedia.org/wiki/Elizabeth_Ann_Seton', 'prec':4, 'source': 'LFF 2024' },
        10105: { 'name': 'Sarah, Theodora, and Syncletica of Egypt, Desert Mothers, fourth-fifth century', 'prec':4, 'source': 'LFF 2024' },
        10106: { 'name': 'The Epiphany of Our Lord Jesus Christ', 'url': 'https://en.wikipedia.org/wiki/Epiphany_(Christian)', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        10108: { 'name': 'Harriet Bedell, Deaconess and Missionary, 1969', 'url': 'https://en.wikipedia.org/wiki/Harriet_Bedell', 'prec':4, 'source': 'LFF 2024' },
        10109: { 'name': 'Julia Chester Emery, Lay Leader and Missionary, 1922', 'url': 'https://en.wikipedia.org/wiki/Julia_Chester_Emery', 'prec':4, 'source': 'LFF 2024' },
        10110: { 'name': 'William Laud, Archbishop of Canterbury, 1645', 'url': 'https://en.wikipedia.org/wiki/William_Laud', 'prec':4, 'source': 'LFF 2024' },
        10112: { 'name': 'Aelred of Rievaulx, Monastic and Theologian, 1167', 'url': 'https://en.wikipedia.org/wiki/Ailred_of_Rievaulx', 'prec':4, 'source': 'LFF 2024' },
        10113: { 'name': 'Hilary of Poitiers, Bishop, 367', 'url': 'https://en.wikipedia.org/wiki/Hilary_of_Poitiers', 'prec':4, 'source': 'LFF 2024' },
        10114: { 'name': 'Richard Meux Benson, Priest, and Charles Gore, Bishop, 1915 and 1932', 'url': 'https://en.wikipedia.org/wiki/Richard_Meux_Benson', 'prec':4, 'source': 'LFF 2024' },
        10117: { 'name': 'Antony of Egypt, Monastic, 356', 'url': 'https://en.wikipedia.org/wiki/Anthony_the_Great', 'prec':4, 'source': 'LFF 2024' },
        10118: { 'name': 'The Confession of Saint Peter the Apostle', 'url': 'https://en.wikipedia.org/wiki/Confession_of_Peter', 'prec':7, 'source': 'BCP 1979' },
        10119: { 'name': 'Wulfstan of Worcester, Bishop, 1095', 'url': 'https://en.wikipedia.org/wiki/Wulfstan,_Bishop_of_Worcester', 'prec':4, 'source': 'LFF 2024' },
        10120: { 'name': 'Fabian, Bishop and Martyr, 250', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Pope_Fabian', 'prec':4, 'source': 'LFF 2024' },
        10121: { 'name': 'Agnes and Cecilia of Rome, Martyrs, 304 and c. 230', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Agnes', 'prec':4, 'source': 'LFF 2024' },
        10122: { 'name': 'Vincent of Saragossa, Deacon and Martyr, 304', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Vincent_of_Saragossa', 'prec':4, 'source': 'LFF 2024' },
        10123: { 'name': 'Phillips Brooks, Bishop, 1893', 'url': 'https://en.wikipedia.org/wiki/Phillips_Brooks', 'prec':4, 'source': 'LFF 2024' },
        10124: { 'name': 'Florence Li Tim-Oi, Priest, 1992', 'url': 'https://en.wikipedia.org/wiki/Florence_Li_Tim-Oi', 'prec':4, 'source': 'LFF 2024' },
        10125: { 'name': 'The Conversion of Saint Paul the Apostle', 'url': 'https://en.wikipedia.org/wiki/Conversion_of_Paul_the_Apostle', 'prec':7, 'source': 'BCP 1979' },
        10126: { 'name': 'Timothy and Titus, Companions of Saint Paul', 'url': 'https://en.wikipedia.org/wiki/Saint_Timothy', 'prec':4, 'source': 'LFF 2024' },
        10127: { 'name': 'John Chrysostom, Bishop and Theologian, 407', 'url': 'https://en.wikipedia.org/wiki/John_Chrysostom', 'prec':4, 'source': 'LFF 2024' },
        10128: { 'name': 'Thomas Aquinas, Friar and Theologian, 1274', 'url': 'https://en.wikipedia.org/wiki/Thomas_Aquinas', 'prec':4, 'source': 'LFF 2024' },
        10129: { 'name': 'Lili‘uokalani of Hawai‘i', 'url': 'https://en.wikipedia.org/wiki/Lili%CA%BBuokalani', 'prec':3, 'source': 'LFF 2024 (trial use)' },
        10131: { 'name': 'Marcella of Rome, Monastic and Scholar, 410', 'url': 'https://en.wikipedia.org/wiki/Saint_Marcella', 'prec':4, 'source': 'LFF 2024' },

        10201: { 'name': 'Brigid of Kildare, Monastic, c. 523', 'url': 'https://en.wikipedia.org/wiki/Brigid_of_Kildare', 'prec':4, 'source': 'LFF 2024' },
        10202: { 'name': 'The Presentation of Our Lord Jesus Christ in the Temple', 'url': 'https://en.wikipedia.org/wiki/Presentation_of_Jesus_at_the_Temple', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        10203: { 'name': 'Anskar, Bishop and Missionary, 865', 'url': 'https://en.wikipedia.org/wiki/Ansgar', 'prec':4, 'source': 'LFF 2024' },
        10204: { 'name': 'Manche Masemola, Martyr, 1928', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Manche_Masemola', 'prec':4, 'source': 'LFF 2024' },
        10205: { 'name': 'Agatha of Sicily, Martyr, c. 251', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Agatha_of_Sicily', 'prec':4, 'source': 'LFF 2024' },
        10206: { 'name': 'The Martyrs of Japan, 1597', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/26_Martyrs_of_Japan', 'prec':4, 'source': 'LFF 2024' },
        10208: { 'name': 'Bakhita (Josephine Margaret Bakhita), Monastic, 1947', 'url': 'https://en.wikipedia.org/wiki/Josephine_Bakhita', 'prec':4, 'source': 'LFF 2024' },
        10210: { 'name': 'Scholastica, Monastic, 543', 'url': 'https://en.wikipedia.org/wiki/Scholastica', 'prec':4, 'source': 'LFF 2024' },
        10211: { 'name': 'The Consecration of Barbara Clementine Harris, First Woman Bishop in the Anglican Communion, 1989', 'url': 'https://en.wikipedia.org/wiki/Barbara_Harris_(bishop)', 'prec':4, 'source': 'LFF 2024' },
        10212: { 'name': 'Theodora, Empress, c. 867', 'prec':4, 'source': 'LFF 2024' },
        10213: { 'name': 'Absalom Jones, Priest, 1818', 'url': 'https://en.wikipedia.org/wiki/Absalom_Jones', 'prec':4, 'source': 'LFF 2024' },
        10214: { 'name': 'Cyril and Methodius, Missionaries, 869 and 885', 'url': 'https://en.wikipedia.org/wiki/Cyril_and_Methodius', 'prec':4, 'source': 'LFF 2024' },
        10215: { 'name': 'Thomas Bray, Priest and Missionary, 1730', 'url': 'https://en.wikipedia.org/wiki/Thomas_Bray', 'prec':4, 'source': 'LFF 2024' },
        10217: { 'name': 'Janani Luwum, Archbishop and Martyr, 1977', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Janani_Luwum', 'prec':4, 'source': 'LFF 2024' },
        10218: { 'name': 'Martin Luther, Pastor and Reformer, 1546', 'url': 'https://en.wikipedia.org/wiki/Martin_Luther', 'prec':4, 'source': 'LFF 2024' },
        10219: { 'name': 'Agnes Tsao Kou Ying, Agatha Lin Zhao, and Lucy Yi Zhenmei, Catechists and Martyrs, 1856, 1858, and 1862', 'martyr':1, 'prec':4, 'source': 'LFF 2024' },
        10220: { 'name': 'Frederick Douglass, Social Reformer, 1895', 'url': 'https://en.wikipedia.org/wiki/Frederick_Douglass', 'prec':4, 'source': 'LFF 2024' },
        10222: { 'name': 'Margaret of Cortona, Monastic, 1297', 'url': 'https://en.wikipedia.org/wiki/Margaret_of_Cortona', 'prec':4, 'source': 'LFF 2024' },
        10223: { 'name': 'Polycarp of Smyrna, Bishop and Martyr, 156', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Polycarp', 'prec':4, 'source': 'LFF 2024' },
        10224: { 'name': 'Saint Matthias the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Matthias', 'prec':7, 'source': 'BCP 1979' },
        10225: { 'name': 'Emily Malbone Morgan, Lay Leader and Contemplative, 1937', 'url': 'https://en.wikipedia.org/wiki/Emily_Malbone_Morgan', 'prec':4, 'source': 'LFF 2024' },
        10226: { 'name': 'Photini, The Samaritan Woman, c. 67', 'url': 'https://en.wikipedia.org/wiki/Samaritan_woman_at_the_well', 'prec':4, 'source': 'LFF 2024' },
        10227: { 'name': 'George Herbert, Priest and Poet, 1633', 'url': 'https://en.wikipedia.org/wiki/George_Herbert', 'prec':4, 'source': 'LFF 2024' },
        10228: { 'name': 'Anna Julia Haywood Cooper, Educator, 1964', 'url': 'https://en.wikipedia.org/wiki/Anna_J._Cooper', 'prec':4, 'source': 'LFF 2024' },

        10301: { 'name': 'David of Wales, Bishop, c. 544', 'url': 'https://en.wikipedia.org/wiki/Saint_David', 'prec':4, 'source': 'LFF 2024' },
        10302: { 'name': 'Chad of Lichfield, Bishop, 672', 'url': 'https://en.wikipedia.org/wiki/Chad_of_Mercia', 'prec':4, 'source': 'LFF 2024' },
        10303: { 'name': 'John and Charles Wesley, Priests, 1791, 1788', 'url': 'https://en.wikipedia.org/wiki/John_Wesley', 'prec':4, 'source': 'LFF 2024' },
        10307: { 'name': 'Perpetua and Felicity, Martyrs, 202', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Perpetua_and_Felicity', 'prec':4, 'source': 'LFF 2024' },
        10309: { 'name': 'Gregory of Nyssa, Bishop and Theologian, c. 394', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nyssa', 'prec':4, 'source': 'LFF 2024' },
        10310: { 'name': 'Harriet Ross Tubman, Social Reformer, 1913', 'url': 'https://en.wikipedia.org/wiki/Harriet_Tubman', 'prec':4, 'source': 'LFF 2024' },
        10312: { 'name': 'Gregory the Great, Bishop and Theologian, 604', 'url': 'https://en.wikipedia.org/wiki/Pope_Gregory_I', 'prec':4, 'source': 'LFF 2024' },
        10313: { 'name': 'James Theodore Holly, Bishop, 1911', 'url': 'https://en.wikipedia.org/wiki/James_Theodore_Holly', 'prec':4, 'source': 'LFF 2024' },
        10315: { 'name': 'Vincent de Paul, Priest, and Louise de Marillac, Vowed Religious, Workers of Charity, 1660', 'url': 'https://en.wikipedia.org/wiki/Vincent_de_Paul', 'prec':4, 'source': 'LFF 2024' },
        10317: { 'name': 'Patrick of Ireland, Bishop and Missionary, 461', 'url': 'https://en.wikipedia.org/wiki/Saint_Patrick%27s_Day', 'prec':4, 'source': 'LFF 2024' },
        10318: { 'name': 'Cyril of Jerusalem, Bishop and Theologian, 386', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Jerusalem', 'prec':4, 'source': 'LFF 2024' },
        10319: { 'name': 'Saint Joseph', 'url': 'https://en.wikipedia.org/wiki/Saint_Joseph', 'prec':7, 'source': 'BCP 1979' },
        10320: { 'name': 'Cuthbert, Bishop, 687', 'url': 'https://en.wikipedia.org/wiki/Cuthbert_of_Lindisfarne', 'prec':4, 'source': 'LFF 2024' },
        10321: { 'name': 'Thomas Ken, Bishop, 1711', 'url': 'https://en.wikipedia.org/wiki/Thomas_Ken', 'prec':4, 'source': 'LFF 2024' },
        10322: { 'name': 'James De Koven, Priest, 1879', 'url': 'https://en.wikipedia.org/wiki/James_De_Koven', 'prec':4, 'source': 'LFF 2024' },
        10323: { 'name': 'Gregory the Illuminator, Bishop and Missionary, c. 332', 'url': 'https://en.wikipedia.org/wiki/Gregory_the_Illuminator', 'prec':4, 'source': 'LFF 2024' },
        10324: { 'name': 'Óscar Romero, Archbishop and Martyr, 1980, and the Martyrs of El Salvador', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/%C3%93scar_Romero', 'prec':4, 'source': 'LFF 2024' },
        10325: { 'name': 'The Annunciation of Our Lord Jesus Christ to the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Annunciation', 'prec':7, 'source': 'BCP 1979' },
        10326: { 'name': 'Harriet Monsell, Monastic, 1883', 'url': 'https://en.wikipedia.org/wiki/Harriet_Monsell', 'prec':4, 'source': 'LFF 2024' },
        10327: { 'name': 'Charles Henry Brent, Bishop, 1929', 'url': 'https://en.wikipedia.org/wiki/Charles_Henry_Brent', 'prec':4, 'source': 'LFF 2024' },
        10328: { 'name': 'James Solomon Russell, Priest, 1935', 'url': 'https://en.wikipedia.org/wiki/James_Solomon_Russell', 'prec':4, 'source': 'LFF 2024' },
        10329: { 'name': 'John Keble, Priest and Poet, 1866', 'url': 'https://en.wikipedia.org/wiki/John_Keble', 'prec':4, 'source': 'LFF 2024' },
        10330: { 'name': 'Mary of Egypt, Monastic, c. 421', 'url': 'https://en.wikipedia.org/wiki/Mary_of_Egypt', 'prec':4, 'source': 'LFF 2024' },
        10331: { 'name': 'John Donne, Priest and Poet, 1631', 'url': 'https://en.wikipedia.org/wiki/John_Donne', 'prec':4, 'source': 'LFF 2024' },

        10401: { 'name': 'Frederick Denison Maurice, Priest, 1872', 'url': 'https://en.wikipedia.org/wiki/Frederick_Denison_Maurice', 'prec':4, 'source': 'LFF 2024' },
        10402: { 'name': 'James Lloyd Breck, Priest, 1876', 'url': 'https://en.wikipedia.org/wiki/James_Lloyd_Breck', 'prec':4, 'source': 'LFF 2024' },
        10403: { 'name': 'Richard of Chichester, Bishop, 1253', 'url': 'https://en.wikipedia.org/wiki/Richard_of_Chichester', 'prec':4, 'source': 'LFF 2024' },
        10404: { 'name': 'Martin Luther King, Jr., Pastor and Martyr, 1968', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.', 'prec':4, 'source': 'LFF 2024' },
        10405: { 'name': 'Harriet Starr Cannon, Monastic, 1896', 'url': 'https://en.wikipedia.org/wiki/Harriet_Starr_Cannon', 'prec':4, 'source': 'LFF 2024' },
        10407: { 'name': 'Tikhon, Bishop and Ecumenist, 1925', 'url': 'https://en.wikipedia.org/wiki/Patriarch_Tikhon_of_Moscow', 'prec':4, 'source': 'LFF 2024' },
        10408: { 'name': 'William Augustus Muhlenberg, Priest, 1877', 'url': 'https://en.wikipedia.org/wiki/William_Augustus_Muhlenberg', 'prec':4, 'source': 'LFF 2024' },
        10409: { 'name': 'Dietrich Bonhoeffer, Pastor and Theologian, 1945', 'url': 'https://en.wikipedia.org/wiki/Dietrich_Bonhoeffer', 'prec':4, 'source': 'LFF 2024' },
        10410: { 'name': 'William Law, Priest, 1761', 'url': 'https://en.wikipedia.org/wiki/William_Law', 'prec':4, 'source': 'LFF 2024' },
        10411: { 'name': 'George Augustus Selwyn, Bishop, 1878', 'url': 'https://en.wikipedia.org/wiki/George_Selwyn_(Bishop_of_Lichfield)', 'prec':4, 'source': 'LFF 2024' },
        10414: { 'name': 'Zenaida, Philonella, and Hermione, Unmercenary Physicians, c. 100, c. 117', 'prec':4, 'source': 'LFF 2024' },
        10415: { 'name': 'Damien, Priest, 1889, and Marianne Cope, Monastic, 1918, of Hawai‘i', 'url': 'https://en.wikipedia.org/wiki/Father_Damien', 'prec':4, 'source': 'LFF 2024' },
        10416: { 'name': 'Peter Williams Cassey, Deacon, 1917, and Anna Besant Cassey, 1875', 'url': 'https://en.wikipedia.org/wiki/Peter_Williams_Cassey', 'prec':4, 'source': 'LFF 2024' },
        10417: { 'name': 'Kateri Tekakwitha, Lay Contemplative, 1680', 'url': 'https://en.wikipedia.org/wiki/Kateri_Tekakwitha', 'prec':4, 'source': 'LFF 2024' },
        10418: { 'name': 'Juana Inés de la Cruz, Monastic and Theologian, 1695', 'url': 'https://en.wikipedia.org/wiki/Juana_In%C3%A9s_de_la_Cruz', 'prec':4, 'source': 'LFF 2024' },
        10419: { 'name': 'Alphege, Archbishop of Canterbury and Martyr, 1012', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/%C3%86lfheah_of_Canterbury', 'prec':4, 'source': 'LFF 2024' },
        10421: { 'name': 'Anselm, Archbishop of Canterbury and Theologian, 1109', 'url': 'https://en.wikipedia.org/wiki/Anselm_of_Canterbury', 'prec':4, 'source': 'LFF 2024' },
        10422: { 'name': 'Hadewijch of Brabant, Poet and Mystic, thirteenth century', 'url': 'https://en.wikipedia.org/wiki/Hadewijch', 'prec':4, 'source': 'LFF 2024' },
        10423: { 'name': 'Toyohiko Kagawa, Social Reformer, 1960', 'url': 'https://en.wikipedia.org/wiki/Toyohiko_Kagawa', 'prec':4, 'source': 'LFF 2024' },
        10425: { 'name': 'Saint Mark the Evangelist', 'url': 'https://en.wikipedia.org/wiki/Mark_the_Evangelist', 'prec':7, 'source': 'BCP 1979' },
        10427: { 'name': 'Zita of Tuscany, Worker of Charity, 1271', 'url': 'https://en.wikipedia.org/wiki/Saint_Zita', 'prec':4, 'source': 'LFF 2024' },
        10429: { 'name': 'Catherine of Siena, Mystic and Prophetic Witness, 1380', 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Siena', 'prec':4, 'source': 'LFF 2024' },

        10501: { 'name': 'The Apostles Saint Philip and Saint James', 'url': 'https://en.wikipedia.org/wiki/Philip_the_Apostle', 'prec':7, 'source': 'BCP 1979' },
        10502: { 'name': 'Athanasius of Alexandria, Bishop and Theologian, 373', 'url': 'https://en.wikipedia.org/wiki/Athanasius_of_Alexandria', 'prec':4, 'source': 'LFF 2024' },
        10503: { 'name': 'Elisabeth Cruciger, Poet and Hymnographer, 1535', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_Cruciger', 'prec':4, 'source': 'LFF 2024' },
        10504: { 'name': 'Monica, Mother of Augustine of Hippo, 387', 'url': 'https://en.wikipedia.org/wiki/Monica_of_Hippo', 'prec':4, 'source': 'LFF 2024' },
        10505: { 'name': 'Martyrs of the Reformation Era', 'martyr':1, 'prec':4, 'source': 'LFF 2024' },
        10506: { 'name': 'George of Lydda, Soldier and Martyr, c. 304', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_George', 'prec':3, 'source': 'LFF 2024 (trial use)' },
        10508: { 'name': 'Julian of Norwich, Mystic and Theologian, c. 1417', 'url': 'https://en.wikipedia.org/wiki/Julian_of_Norwich', 'prec':4, 'source': 'LFF 2024' },
        10509: { 'name': 'Gregory of Nazianzus, Bishop and Theologian, 389', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nazianzus', 'prec':4, 'source': 'LFF 2024' },
        10511: { 'name': 'Johann Arndt and Jacob Boehme, Mystics, 1621 and 1624', 'url': 'https://en.wikipedia.org/wiki/Johann_Arndt', 'prec':4, 'source': 'LFF 2024' },
        10513: { 'name': 'Frances Perkins, Social Reformer, 1965', 'url': 'https://en.wikipedia.org/wiki/Frances_Perkins', 'prec':4, 'source': 'LFF 2024' },
        10515: { 'name': 'Pachomius of Tabenissi, Monastic, 348', 'url': 'https://en.wikipedia.org/wiki/Pachomius_the_Great', 'prec':4, 'source': 'LFF 2024' },
        10517: { 'name': 'Thurgood Marshall, Public Servant, 1993', 'url': 'https://en.wikipedia.org/wiki/Thurgood_Marshall', 'prec':4, 'source': 'LFF 2024' },
        10519: { 'name': 'Dunstan, Archbishop of Canterbury, 988', 'url': 'https://en.wikipedia.org/wiki/Dunstan', 'prec':4, 'source': 'LFF 2024' },
        10520: { 'name': 'Alcuin of York, Deacon, 804', 'url': 'https://en.wikipedia.org/wiki/Alcuin', 'prec':4, 'source': 'LFF 2024' },
        10521: { 'name': 'Lydia of Thyatira, Coworker of the Apostle Paul', 'url': 'https://en.wikipedia.org/wiki/Lydia_of_Thyatira', 'prec':4, 'source': 'LFF 2024' },
        10522: { 'name': 'Helena of Constantinople, Protector of the Holy Places, 330', 'url': 'https://en.wikipedia.org/wiki/Helena_(empress)', 'prec':4, 'source': 'LFF 2024' },
        10524: { 'name': 'Jackson Kemper, Bishop and Missionary, 1870', 'url': 'https://en.wikipedia.org/wiki/Jackson_Kemper', 'prec':4, 'source': 'LFF 2024' },
        10525: { 'name': 'Bede, Priest and Historian, 735', 'url': 'https://en.wikipedia.org/wiki/Bede', 'prec':4, 'source': 'LFF 2024' },
        10526: { 'name': 'Augustine, First Archbishop of Canterbury, 605', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Canterbury', 'prec':4, 'source': 'LFF 2024' },
        10528: { 'name': 'Mechthild of Magdeburg, Mystic, c. 1282', 'url': 'https://en.wikipedia.org/wiki/Mechthild_of_Magdeburg', 'prec':4, 'source': 'LFF 2024' },
        10531: { 'name': 'The Visitation of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Visitation_(Christianity)', 'prec':7, 'source': 'BCP 1979' },

        10601: { 'name': 'Justin, Martyr, 167', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Justin_Martyr', 'prec':4, 'source': 'LFF 2024' },
        10602: { 'name': 'Blandina and Her Companions, the Martyrs of Lyons, 177', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Blandina', 'prec':4, 'source': 'LFF 2024' },
        10603: { 'name': 'The Martyrs of Uganda, 1886', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Uganda_Martyrs', 'prec':4, 'source': 'LFF 2024' },
        10604: { 'name': 'John XXIII (Angelo Giuseppe Roncalli), Bishop, 1963', 'url': 'https://en.wikipedia.org/wiki/Pope_John_XXIII', 'prec':4, 'source': 'LFF 2024' },
        10605: { 'name': 'Boniface, Bishop and Missionary, 754', 'url': 'https://en.wikipedia.org/wiki/Saint_Boniface', 'prec':4, 'source': 'LFF 2024' },
        10608: { 'name': 'Melania the Elder, Monastic, 410', 'url': 'https://en.wikipedia.org/wiki/Melania_the_Elder', 'prec':4, 'source': 'LFF 2024' },
        10609: { 'name': 'Columba of Iona, Monastic, 597', 'url': 'https://en.wikipedia.org/wiki/Columba', 'prec':4, 'source': 'LFF 2024' },
        10610: { 'name': 'Ephrem of Nisibis, Deacon and Poet, 373', 'url': 'https://en.wikipedia.org/wiki/Ephrem_the_Syrian', 'prec':4, 'source': 'LFF 2024' },
        10611: { 'name': 'Saint Barnabas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Barnabas', 'prec':7, 'source': 'BCP 1979' },
        10612: { 'name': 'Enmegahbowh, Priest and Missionary, 1902', 'url': 'https://en.wikipedia.org/wiki/Enmegahbowh', 'prec':4, 'source': 'LFF 2024' },
        10613: { 'name': 'The First Book of Common Prayer, 1549', 'url': 'https://en.wikipedia.org/wiki/Book_of_Common_Prayer_(1549)', 'prec':4, 'source': 'LFF 2024' },
        10614: { 'name': 'Basil of Caesarea, Bishop and Theologian, 379', 'url': 'https://en.wikipedia.org/wiki/Basil_of_Caesarea', 'prec':4, 'source': 'LFF 2024' },
        10615: { 'name': 'Evelyn Underhill, Mystic and Writer, 1941', 'url': 'https://en.wikipedia.org/wiki/Evelyn_Underhill', 'prec':4, 'source': 'LFF 2024' },
        10616: { 'name': 'Joseph Butler, Bishop and Theologian, 1752', 'url': 'https://en.wikipedia.org/wiki/Joseph_Butler', 'prec':4, 'source': 'LFF 2024' },
        10617: { 'name': 'Marina the Monk, Monastic, fifth century', 'url': 'https://en.wikipedia.org/wiki/Marina_the_Monk', 'prec':4, 'source': 'LFF 2024' },
        10618: { 'name': 'Bernard Mizeki, Martyr, 1896', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Bernard_Mizeki', 'prec':4, 'source': 'LFF 2024' },
        10619: { 'name': 'Adelaide Teague Case, Educator, 1948', 'url': 'https://en.wikipedia.org/wiki/Adelaide_Teague_Case', 'prec':4, 'source': 'LFF 2024' },
        10622: { 'name': 'Alban, Martyr, c. 304', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Alban', 'prec':4, 'source': 'LFF 2024' },
        10624: { 'name': 'The Nativity of Saint John the Baptist', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_Saint_John_the_Baptist', 'prec':7, 'source': 'BCP 1979' },
        10626: { 'name': 'Isabel Florence Hapgood, Ecumenist, 1928', 'url': 'https://en.wikipedia.org/wiki/Isabel_Florence_Hapgood', 'prec':4, 'source': 'LFF 2024' },
        10628: { 'name': 'Irenaeus of Lyons, Bishop and Theologian, c. 202', 'url': 'https://en.wikipedia.org/wiki/Irenaeus', 'prec':4, 'source': 'LFF 2024' },
        10629: { 'name': 'The Apostles Saint Peter and Saint Paul', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Feast_of_Saints_Peter_and_Paul', 'prec':7, 'source': 'BCP 1979' },

        10701: { 'name': 'Pauli Murray, Priest, 1985', 'url': 'https://en.wikipedia.org/wiki/Pauli_Murray', 'prec':4, 'source': 'LFF 2024' },
        10702: { 'name': 'Moses the Black, Monastic and Martyr, c. 400', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Moses_the_Black', 'prec':4, 'source': 'LFF 2024' },
        10704: { 'name': 'Independence Day (United States)', 'colour': 'white', 'url': 'https://en.wikipedia.org/wiki/Independence_Day_(United_States)', 'prec':7, 'type': 'Holy Day', 'type_url': 'https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year', 'source': 'BCP 1979' },
        10706: { 'name': 'Eva Lee Matthews, Monastic, 1928', 'url': 'https://en.wikipedia.org/wiki/Eva_Lee_Matthews', 'prec':4, 'source': 'LFF 2024' },
        10708: { 'name': 'Priscilla and Aquila, Coworkers of the Apostle Paul', 'url': 'https://en.wikipedia.org/wiki/Priscilla_and_Aquila', 'prec':4, 'source': 'LFF 2024' },
        10711: { 'name': 'Benedict of Nursia, Monastic, c. 543', 'url': 'https://en.wikipedia.org/wiki/Benedict_of_Nursia', 'prec':4, 'source': 'LFF 2024' },
        10714: { 'name': 'Argula von Grumbach, Scholar and Church Reformer, c. 1554', 'url': 'https://en.wikipedia.org/wiki/Argula_von_Grumbach', 'prec':4, 'source': 'LFF 2024' },
        10717: { 'name': 'William White, Bishop, 1836', 'url': 'https://en.wikipedia.org/wiki/William_White_(bishop_of_Pennsylvania)', 'prec':4, 'source': 'LFF 2024' },
        10719: { 'name': 'Macrina of Caesarea, Monastic and Teacher, 379', 'url': 'https://en.wikipedia.org/wiki/Macrina_the_Younger', 'prec':4, 'source': 'LFF 2024' },
        10720: { 'name': 'Elizabeth Cady Stanton, Amelia Bloomer, and Sojourner Truth, Social Reformers, 1902, 1894, and 1883', 'url': 'https://en.wikipedia.org/wiki/Elizabeth_Cady_Stanton', 'prec':4, 'source': 'LFF 2024' },
        10721: { 'name': 'Maria Skobtsova, Monastic and Martyr, 1945', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Maria_Skobtsova', 'prec':4, 'source': 'LFF 2024' },
        10722: { 'name': 'Saint Mary Magdalene', 'url': 'https://en.wikipedia.org/wiki/Mary_Magdalene', 'prec':7, 'source': 'BCP 1979' },
        10723: { 'name': 'John Cassian, Monastic and Theologian, 435', 'url': 'https://en.wikipedia.org/wiki/John_Cassian', 'prec':4, 'source': 'LFF 2024' },
        10724: { 'name': 'Thomas à Kempis, Priest and Mystic, 1471', 'url': 'https://en.wikipedia.org/wiki/Thomas_%C3%A0_Kempis', 'prec':4, 'source': 'LFF 2024' },
        10725: { 'name': 'Saint James the Apostle', 'url': 'https://en.wikipedia.org/wiki/James_the_Greater', 'prec':7, 'source': 'BCP 1979' },
        10726: { 'name': 'The Parents of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Saint_Anne', 'prec':4, 'source': 'LFF 2024' },
        10727: { 'name': 'William Reed Huntington, Priest, 1909', 'url': 'https://en.wikipedia.org/wiki/William_Reed_Huntington', 'prec':4, 'source': 'LFF 2024' },
        10728: { 'name': 'Johann Sebastian Bach, Composer, 1750', 'url': 'https://en.wikipedia.org/wiki/Johann_Sebastian_Bach', 'prec':4, 'source': 'LFF 2024' },
        10729: (
            { 'name': 'Mary and Martha of Bethany', 'url': 'https://en.wikipedia.org/wiki/Mary_of_Bethany', 'prec':4, 'source': 'LFF 2024' },
            { 'name': 'The Ordination of the Philadelphia Eleven', 'prec':3, 'source': 'LFF 2024 (trial use)' },
        ),
        10730: { 'name': 'William Wilberforce, Social Reformer, 1833', 'url': 'https://en.wikipedia.org/wiki/William_Wilberforce', 'prec':4, 'source': 'LFF 2024' },
        10731: { 'name': 'Ignatius of Loyola, Priest and Spiritual Writer, 1556', 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Loyola', 'prec':4, 'source': 'LFF 2024' },

        10801: { 'name': 'Joseph of Arimathea', 'url': 'https://en.wikipedia.org/wiki/Joseph_of_Arimathea', 'prec':4, 'source': 'LFF 2024' },
        10803: { 'name': 'Joanna, Mary, and Salome, Myrrh-Bearing Women', 'url': 'https://en.wikipedia.org/wiki/Myrrhbearers', 'prec':4, 'source': 'LFF 2024' },
        10806: { 'name': 'The Transfiguration of Our Lord Jesus Christ', 'url': 'https://en.wikipedia.org/wiki/Transfiguration_of_Jesus', 'prec':9, 'type': 'Holy Day', 'source': 'BCP 1979' },
        10807: { 'name': 'John Mason Neale, Priest and Hymnographer, 1866', 'url': 'https://en.wikipedia.org/wiki/John_Mason_Neale', 'prec':4, 'source': 'LFF 2024' },
        10808: { 'name': 'Dominic, Priest and Friar, 1221', 'url': 'https://en.wikipedia.org/wiki/Saint_Dominic', 'prec':4, 'source': 'LFF 2024' },
        10809: { 'name': 'Edith Stein (Teresa Benedicta of the Cross), Philosopher, Monastic, and Martyr, 1942', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Edith_Stein', 'prec':4, 'source': 'LFF 2024' },
        10810: { 'name': 'Laurence of Rome, Deacon and Martyr, 258', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Lawrence_of_Rome', 'prec':4, 'source': 'LFF 2024' },
        10811: { 'name': 'Clare of Assisi, Monastic, 1253', 'url': 'https://en.wikipedia.org/wiki/Clare_of_Assisi', 'prec':4, 'source': 'LFF 2024' },
        10812: { 'name': 'Florence Nightingale, Nurse, 1910', 'url': 'https://en.wikipedia.org/wiki/Florence_Nightingale', 'prec':4, 'source': 'LFF 2024' },
        10813: { 'name': 'Jeremy Taylor, Bishop and Theologian, 1667', 'url': 'https://en.wikipedia.org/wiki/Jeremy_Taylor', 'prec':4, 'source': 'LFF 2024' },
        10814: { 'name': 'Jonathan Myrick Daniels, Martyr, 1965', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Jonathan_Myrick_Daniels', 'prec':4, 'source': 'LFF 2024' },
        10815: { 'name': 'Saint Mary the Virgin, Mother of Our Lord Jesus Christ', 'url': 'https://en.wikipedia.org/wiki/Mary,_mother_of_Jesus', 'prec':7, 'source': 'BCP 1979' },
        10820: { 'name': 'Bernard of Clairvaux, Monastic and Theologian, 1153', 'url': 'https://en.wikipedia.org/wiki/Bernard_of_Clairvaux', 'prec':4, 'source': 'LFF 2024' },
        10824: { 'name': 'Saint Bartholomew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Bartholomew_the_Apostle', 'prec':7, 'source': 'BCP 1979' },
        10825: { 'name': 'Louis, King, 1270', 'url': 'https://en.wikipedia.org/wiki/Louis_IX_of_France', 'prec':4, 'source': 'LFF 2024' },
        10826: { 'name': 'Simeon Bachos the Ethiopian Eunuch', 'url': 'https://en.wikipedia.org/wiki/Ethiopian_eunuch', 'prec':4, 'source': 'LFF 2024' },
        10827: { 'name': 'Thomas Gallaudet and Henry Winter Syle, Priests, 1902 and 1890', 'url': 'https://en.wikipedia.org/wiki/Thomas_Gallaudet_(priest)', 'prec':4, 'source': 'LFF 2024' },
        10828: { 'name': 'Augustine of Hippo, Bishop and Theologian, 430', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Hippo', 'prec':4, 'source': 'LFF 2024' },
        10829: { 'name': 'The Beheading of Saint John the Baptist', 'url': 'https://en.wikipedia.org/wiki/Beheading_of_John_the_Baptist', 'prec':4, 'source': 'LFF 2024' },
        10830: { 'name': 'Margaret Ward, Margaret Clitherow, and Anne Line, Martyrs, 1588, 1586, and 1601', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Margaret_Clitherow', 'prec':4, 'source': 'LFF 2024' },
        10831: { 'name': 'Aidan of Lindisfarne, Bishop, 651', 'url': 'https://en.wikipedia.org/wiki/Aidan_of_Lindisfarne', 'prec':4, 'source': 'LFF 2024' },

        10901: { 'name': 'David Pendleton Oakerhater, Deacon, 1931', 'url': 'https://en.wikipedia.org/wiki/David_Pendleton_Oakerhater', 'prec':4, 'source': 'LFF 2024' },
        10902: { 'name': 'The Martyrs of New Guinea, 1942', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Papua_New_Guinea', 'prec':4, 'source': 'LFF 2024' },
        10903: { 'name': 'Phoebe, Deacon', 'url': 'https://en.wikipedia.org/wiki/Phoebe_(biblical_figure)', 'prec':4, 'source': 'LFF 2024' },
        10904: { 'name': 'Paul Jones, Bishop, 1941', 'url': 'https://en.wikipedia.org/wiki/Paul_Jones_(bishop)', 'prec':4, 'source': 'LFF 2024' },
        10905: { 'name': 'Katharina Zell, Church Reformer and Writer, 1562', 'url': 'https://en.wikipedia.org/wiki/Katharina_Zell', 'prec':4, 'source': 'LFF 2024' },
        10906: { 'name': 'Hannah More, Religious Writer and Philanthropist, 1833', 'url': 'https://en.wikipedia.org/wiki/Hannah_More', 'prec':4, 'source': 'LFF 2024' },
        10907: (
            { 'name': 'Kassiani, Poet and Hymnographer, 865', 'url': 'https://en.wikipedia.org/wiki/Kassia', 'prec':4, 'source': 'LFF 2024' },
            { 'name': 'Élie Naud', 'prec':3, 'source': 'LFF 2024 (trial use)' },
        ),
        10908: { 'name': 'The Nativity of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_Mary', 'prec':4, 'source': 'LFF 2024' },
        10909: { 'name': 'Constance, Thecla, Ruth, Frances, Charles Parsons, and Louis Schuyler, Martyrs, 1878', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Constance_and_Her_Companions', 'prec':4, 'source': 'LFF 2024' },
        10910: { 'name': 'Alexander Crummell, Priest, 1898', 'url': 'https://en.wikipedia.org/wiki/Alexander_Crummell', 'prec':4, 'source': 'LFF 2024' },
        10912: { 'name': 'John Henry Hobart, Bishop, 1830', 'url': 'https://en.wikipedia.org/wiki/John_Henry_Hobart', 'prec':4, 'source': 'LFF 2024' },
        10913: { 'name': 'Cyprian of Carthage, Bishop and Martyr, 258', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cyprian', 'prec':4, 'source': 'LFF 2024' },
        10914: { 'name': 'Holy Cross Day', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Cross', 'prec':7, 'source': 'BCP 1979' },
        10915: { 'name': 'Catherine of Genoa, Mystic and Nurse, 1510', 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Genoa', 'prec':4, 'source': 'LFF 2024' },
        10916: { 'name': 'Ninian, Bishop, c. 430', 'url': 'https://en.wikipedia.org/wiki/Saint_Ninian', 'prec':4, 'source': 'LFF 2024' },
        10917: { 'name': 'Hildegard of Bingen, Mystic and Scholar, 1179', 'url': 'https://en.wikipedia.org/wiki/Hildegard_of_Bingen', 'prec':4, 'source': 'LFF 2024' },
        10918: { 'name': 'Edward Bouverie Pusey, Priest, 1882', 'url': 'https://en.wikipedia.org/wiki/Edward_Bouverie_Pusey', 'prec':4, 'source': 'LFF 2024' },
        10919: { 'name': 'Theodore of Tarsus, Archbishop of Canterbury, 690', 'url': 'https://en.wikipedia.org/wiki/Theodore_of_Tarsus', 'prec':4, 'source': 'LFF 2024' },
        10920: { 'name': 'John Coleridge Patteson, Bishop, and his Companions, Martyrs, 1871', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/John_Coleridge_Patteson', 'prec':4, 'source': 'LFF 2024' },
        10921: { 'name': 'Saint Matthew, Apostle and Evangelist', 'url': 'https://en.wikipedia.org/wiki/Matthew_the_Apostle', 'prec':7, 'source': 'BCP 1979' },
        10922: { 'name': 'Philander Chase, Bishop, 1852', 'url': 'https://en.wikipedia.org/wiki/Philander_Chase', 'prec':4, 'source': 'LFF 2024' },
        10923: { 'name': 'Thecla of Iconium, Proto-Martyr Among Women, c. 70', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thecla', 'prec':4, 'source': 'LFF 2024' },
        10924: { 'name': 'Anna Ellison Butler Alexander, Deaconess and Teacher, 1947', 'url': 'https://en.wikipedia.org/wiki/Anna_Ellison_Butler_Alexander', 'prec':4, 'source': 'LFF 2024' },
        10925: { 'name': 'Sergius of Radonezh, Monastic, 1392', 'url': 'https://en.wikipedia.org/wiki/Sergius_of_Radonezh', 'prec':4, 'source': 'LFF 2024' },
        10926: { 'name': 'Lancelot Andrewes, Bishop, 1626', 'url': 'https://en.wikipedia.org/wiki/Lancelot_Andrewes', 'prec':4, 'source': 'LFF 2024' },
        10927: { 'name': 'Euphrosyne/Smaragdus of Alexandria, Monastic, fifth century', 'prec':4, 'source': 'LFF 2024' },
        10928: { 'name': 'Paula and Eustochium of Rome, Monastics and Scholars, 404 and c. 419', 'url': 'https://en.wikipedia.org/wiki/Paula_of_Rome', 'prec':4, 'source': 'LFF 2024' },
        10929: { 'name': 'Saint Michael and All Angels', 'url': 'https://en.wikipedia.org/wiki/Michaelmas', 'prec':7, 'source': 'BCP 1979' },
        10930: { 'name': 'Jerome, Priest and Scholar, 420', 'url': 'https://en.wikipedia.org/wiki/Jerome', 'prec':4, 'source': 'LFF 2024' },

        11001: { 'name': 'Thérèse of Lisieux, Monastic, 1897', 'url': 'https://en.wikipedia.org/wiki/Th%C3%A9r%C3%A8se_of_Lisieux', 'prec':4, 'source': 'LFF 2024' },
        11002: { 'name': 'Remigius of Rheims, Bishop, c. 530', 'url': 'https://en.wikipedia.org/wiki/Saint_Remigius', 'prec':4, 'source': 'LFF 2024' },
        11003: { 'name': 'John Raleigh Mott, Ecumenist and Missionary, 1955', 'url': 'https://en.wikipedia.org/wiki/John_R._Mott', 'prec':4, 'source': 'LFF 2024' },
        11004: { 'name': 'Francis of Assisi, Friar and Deacon, 1226', 'url': 'https://en.wikipedia.org/wiki/Francis_of_Assisi', 'prec':4, 'source': 'LFF 2024' },
        11006: { 'name': 'William Tyndale, Priest, 1536', 'url': 'https://en.wikipedia.org/wiki/William_Tyndale', 'prec':4, 'source': 'LFF 2024' },
        11007: { 'name': 'Birgitta of Sweden, Mystic, 1373', 'url': 'https://en.wikipedia.org/wiki/Bridget_of_Sweden', 'prec':4, 'source': 'LFF 2024' },
        11009: { 'name': 'Robert Grosseteste, Bishop, 1253', 'url': 'https://en.wikipedia.org/wiki/Robert_Grosseteste', 'prec':4, 'source': 'LFF 2024' },
        11010: { 'name': 'Vida Dutton Scudder, Educator, 1954', 'url': 'https://en.wikipedia.org/wiki/Vida_Dutton_Scudder', 'prec':4, 'source': 'LFF 2024' },
        11011: { 'name': 'Philip, Deacon and Evangelist', 'url': 'https://en.wikipedia.org/wiki/Philip_the_Evangelist', 'prec':4, 'source': 'LFF 2024' },
        11012: { 'name': 'Edith Cavell, Nurse, 1915', 'url': 'https://en.wikipedia.org/wiki/Edith_Cavell', 'prec':4, 'source': 'LFF 2024' },
        11014: { 'name': 'Samuel Isaac Joseph Schereschewsky, Bishop and Missionary, 1906', 'url': 'https://en.wikipedia.org/wiki/Samuel_I._J._Schereschewsky', 'prec':4, 'source': 'LFF 2024' },
        11015: { 'name': 'Teresa of Avila, Mystic and Monastic Reformer, 1582', 'url': 'https://en.wikipedia.org/wiki/Teresa_of_%C3%81vila', 'prec':4, 'source': 'LFF 2024' },
        11016: { 'name': 'Hugh Latimer and Nicholas Ridley, Bishops and Martyrs, 1555, and Thomas Cranmer, Archbishop of Canterbury, 1556', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Hugh_Latimer', 'prec':4, 'source': 'LFF 2024' },
        11017: { 'name': 'Ignatius of Antioch, Bishop and Martyr, c. 115', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Antioch', 'prec':4, 'source': 'LFF 2024' },
        11018: { 'name': 'Saint Luke the Evangelist', 'url': 'https://en.wikipedia.org/wiki/Luke_the_Evangelist', 'prec':7, 'source': 'BCP 1979' },
        11019: { 'name': 'Henry Martyn, Priest and Missionary, 1812', 'url': 'https://en.wikipedia.org/wiki/Henry_Martyn', 'prec':4, 'source': 'LFF 2024' },
        11020: { 'name': 'Cornelius the Centurion', 'url': 'https://en.wikipedia.org/wiki/Cornelius_the_Centurion', 'prec':4, 'source': 'LFF 2024' },
        11023: { 'name': 'Saint James of Jerusalem, Brother of Our Lord Jesus Christ and Martyr, c. 62', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James,_brother_of_Jesus', 'prec':7, 'source': 'BCP 1979' },
        11025: { 'name': 'Tabitha (Dorcas) of Joppa', 'url': 'https://en.wikipedia.org/wiki/Dorcas', 'prec':4, 'source': 'LFF 2024' },
        11026: { 'name': 'Alfred, King, 899', 'url': 'https://en.wikipedia.org/wiki/Alfred_the_Great', 'prec':4, 'source': 'LFF 2024' },
        11028: { 'name': 'Saint Simon and Saint Jude, Apostles', 'url': 'https://en.wikipedia.org/wiki/Simon_the_Zealot', 'prec':7, 'source': 'BCP 1979' },
        11029: { 'name': 'James Hannington, Bishop, and his Companions, Martyrs, 1885', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James_Hannington', 'prec':4, 'source': 'LFF 2024' },
        11030: { 'name': 'Maryam of Qidun, Monastic, fourth century', 'prec':4, 'source': 'LFF 2024' },

        11101: { 'name': 'All Saints', 'url': 'https://en.wikipedia.org/wiki/All_Saints%27_Day', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        11102: { 'name': 'All Souls / All the Faithful Departed', 'url': 'https://en.wikipedia.org/wiki/All_Souls%27_Day', 'colour':'purple', 'prec':4, 'source': 'LFF 2024' },
        11103: { 'name': 'Richard Hooker, Priest and Theologian, 1600', 'url': 'https://en.wikipedia.org/wiki/Richard_Hooker', 'prec':4, 'source': 'LFF 2024' },
        11104: { 'name': 'Adeline Blanchard Tyler and her Companions', 'prec':3, 'source': 'LFF 2024 (trial use)' },
        11106: { 'name': 'William Temple, Archbishop of Canterbury, 1944', 'url': 'https://en.wikipedia.org/wiki/William_Temple_(bishop)', 'prec':4, 'source': 'LFF 2024' },
        11107: { 'name': 'Willibrord, Bishop and Missionary, 739', 'url': 'https://en.wikipedia.org/wiki/Willibrord', 'prec':4, 'source': 'LFF 2024' },
        11108: { 'name': 'Ammonius, Hermit, c. 403', 'prec':4, 'source': 'LFF 2024' },
        11109: { 'name': 'Richard Rolle, Walter Hilton, and Margery Kempe, Mystics, 1349, 1396, and c. 1440', 'url': 'https://en.wikipedia.org/wiki/Richard_Rolle', 'prec':4, 'source': 'LFF 2024' },
        11110: { 'name': 'Leo of Rome, Bishop, 461', 'url': 'https://en.wikipedia.org/wiki/Pope_Leo_I', 'prec':4, 'source': 'LFF 2024' },
        11111: { 'name': 'Martin of Tours, Bishop, 397', 'url': 'https://en.wikipedia.org/wiki/Martin_of_Tours', 'prec':4, 'source': 'LFF 2024' },
        11112: { 'name': 'Charles Simeon, Priest, 1836', 'url': 'https://en.wikipedia.org/wiki/Charles_Simeon', 'prec':4, 'source': 'LFF 2024' },
        11114: { 'name': 'The Consecration of Samuel Seabury, 1784', 'url': 'https://en.wikipedia.org/wiki/Samuel_Seabury', 'prec':4, 'source': 'LFF 2024' },
        11115: { 'name': 'Herman of Alaska, Missionary, 1837', 'url': 'https://en.wikipedia.org/wiki/Herman_of_Alaska', 'prec':4, 'source': 'LFF 2024' },
        11116: { 'name': 'Margaret of Scotland, Queen, 1093', 'url': 'https://en.wikipedia.org/wiki/Saint_Margaret_of_Scotland', 'prec':4, 'source': 'LFF 2024' },
        11117: { 'name': 'Hugh of Lincoln, Bishop, 1200', 'url': 'https://en.wikipedia.org/wiki/Hugh_of_Lincoln', 'prec':4, 'source': 'LFF 2024' },
        11118: { 'name': 'Hilda of Whitby, Abbess, 680', 'url': 'https://en.wikipedia.org/wiki/Hilda_of_Whitby', 'prec':4, 'source': 'LFF 2024' },
        11119: { 'name': 'Elizabeth of Hungary, Princess, 1231', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_of_Hungary', 'prec':4, 'source': 'LFF 2024' },
        11120: { 'name': 'Edmund, King, 870', 'url': 'https://en.wikipedia.org/wiki/Edmund_the_Martyr', 'prec':4, 'source': 'LFF 2024' },
        11121: { 'name': 'Mechthilde of Hackeborn and Gertrude the Great, Mystics and Theologians, 1298 and 1302', 'url': 'https://en.wikipedia.org/wiki/Mechthild_of_Hackeborn', 'prec':4, 'source': 'LFF 2024' },
        11122: { 'name': 'Clive Staples Lewis, Apologist and Spiritual Writer, 1963', 'url': 'https://en.wikipedia.org/wiki/C._S._Lewis', 'prec':4, 'source': 'LFF 2024' },
        11123: { 'name': 'Clement of Rome, Bishop, c. 100', 'url': 'https://en.wikipedia.org/wiki/Pope_Clement_I', 'prec':4, 'source': 'LFF 2024' },
        11124: { 'name': 'Catherine of Alexandria, Barbara of Nicomedia, and Margaret of Antioch, Martyrs, c. 305', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Alexandria', 'prec':4, 'source': 'LFF 2024' },
        11125: { 'name': 'James Otis Sargent Huntington, Monastic and Priest, 1935', 'url': 'https://en.wikipedia.org/wiki/James_O._S._Huntington', 'prec':4, 'source': 'LFF 2024' },
        11128: { 'name': 'Kamehameha and Emma of Hawai‘i, King and Queen, 1863 and 1885', 'url': 'https://en.wikipedia.org/wiki/Kamehameha_IV', 'prec':4, 'source': 'LFF 2024' },
        11130: { 'name': 'Saint Andrew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Andrew_the_Apostle', 'prec':7, 'source': 'BCP 1979' },

        11201: { 'name': 'Charles de Foucauld, Monastic and Martyr, 1916', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Charles_de_Foucauld', 'prec':4, 'source': 'LFF 2024' },
        11202: { 'name': 'Channing Moore Williams, Bishop and Missionary, 1910', 'url': 'https://en.wikipedia.org/wiki/Channing_Moore_Williams', 'prec':4, 'source': 'LFF 2024' },
        11203: { 'name': 'Francis Xavier, Priest and Missionary, 1552', 'url': 'https://en.wikipedia.org/wiki/Francis_Xavier', 'prec':4, 'source': 'LFF 2024' },
        11204: { 'name': 'John of Damascus, Priest and Theologian, c. 760', 'url': 'https://en.wikipedia.org/wiki/John_of_Damascus', 'prec':4, 'source': 'LFF 2024' },
        11205: { 'name': 'Clement of Alexandria, Priest and Theologian, c. 210', 'url': 'https://en.wikipedia.org/wiki/Clement_of_Alexandria', 'prec':4, 'source': 'LFF 2024' },
        11206: { 'name': 'Nicholas of Myra, Bishop, c. 342', 'url': 'https://en.wikipedia.org/wiki/Saint_Nicholas', 'prec':4, 'source': 'LFF 2024' },
        11207: { 'name': 'Ambrose of Milan, Bishop and Theologian, 397', 'url': 'https://en.wikipedia.org/wiki/Ambrose', 'prec':4, 'source': 'LFF 2024' },
        11208: { 'name': 'Nicholas Ferrar, Deacon, 1637', 'url': 'https://en.wikipedia.org/wiki/Nicholas_Ferrar', 'prec':4, 'source': 'LFF 2024' },
        11211: { 'name': 'Frederick Howden, Jr., Priest and Chaplain of the Armed Forces, 1941', 'url': 'https://en.wikipedia.org/wiki/Frederick_B._Howden_Jr.', 'prec':4, 'source': 'LFF 2024' },
        11212: { 'name': 'Francis de Sales, Bishop, and Jane de Chantal, Vowed Religious, 1622 and 1641', 'url': 'https://en.wikipedia.org/wiki/Francis_de_Sales', 'prec':4, 'source': 'LFF 2024' },
        11213: { 'name': 'Lucy of Syracuse, Martyr, 304', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Lucy', 'prec':4, 'source': 'LFF 2024' },
        11214: { 'name': 'John of the Cross, Mystic and Monastic Reformer, 1591', 'url': 'https://en.wikipedia.org/wiki/John_of_the_Cross', 'prec':4, 'source': 'LFF 2024' },
        11215: { 'name': 'Nino of Georgia, Missionary, c. 332', 'url': 'https://en.wikipedia.org/wiki/Saint_Nino', 'prec':4, 'source': 'LFF 2024' },
        11217: { 'name': 'Dorothy L. Sayers, Apologist and Spiritual Writer, 1957', 'url': 'https://en.wikipedia.org/wiki/Dorothy_L._Sayers', 'prec':4, 'source': 'LFF 2024' },
        11220: { 'name': 'Katharina von Bora, Church Reformer, 1552', 'url': 'https://en.wikipedia.org/wiki/Katharina_von_Bora', 'prec':4, 'source': 'LFF 2024' },
        11221: { 'name': 'Saint Thomas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Thomas_the_Apostle', 'prec':7, 'source': 'BCP 1979' },
        11225: { 'name': 'The Nativity of Our Lord Jesus Christ', 'url': 'https://en.wikipedia.org/wiki/Christmas', 'prec':9, 'type': 'Principal Feast', 'source': 'BCP 1979' },
        11226: { 'name': 'Saint Stephen, Deacon and Martyr', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Stephen', 'prec':7, 'source': 'BCP 1979' },
        11227: { 'name': 'Saint John, Apostle and Evangelist', 'url': 'https://en.wikipedia.org/wiki/John_the_Evangelist', 'prec':7, 'source': 'BCP 1979' },
        11228: { 'name': 'Holy Innocents', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Massacre_of_the_Innocents', 'prec':7, 'source': 'BCP 1979' },
        11229: { 'name': 'Thomas Becket, Archbishop of Canterbury and Martyr, 1170', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_Becket', 'prec':4, 'source': 'LFF 2024' },
        11231: { 'name': 'Frances Joseph Gaudet, Educator and Social Reformer, 1934', 'url': 'https://en.wikipedia.org/wiki/Frances_Joseph-Gaudet', 'prec':4, 'source': 'LFF 2024' },
    }

    # Get the feast(s) from the list above
    entry = feasts.get(datecode)
    if entry is None:
        return None

    # A day may hold several commemorations; normalise to a list of dicts.
    if isinstance(entry, tuple):
        result = list(entry)
    else:
        result = [entry]

    # Append extra common info to each feast. Careful with prec=9 here as some
    # are Principal Feasts, some are Holy Days of Holy Week, and some are
    # Major Fasts; each of these carries an explicit 'type' in the data.
    for feast in result:
        if feast['prec'] == 9 and 'type' in feast:
            if feast['type'] == 'Principal Feast':
                feast['type_url'] = 'https://en.wikipedia.org/wiki/Principal_Feast'
                if 'source' not in feast:
                    feast['source'] = 'BCP 1979'
            elif feast['type'] in ('Major Fast', 'Holy Day'):
                feast['type_url'] = 'https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year'
                if 'source' not in feast:
                    feast['source'] = 'BCP 1979'
        else:
            if feast['prec'] == 3:
                feast['type'] = 'Commemoration'
                feast['type_url'] = 'https://en.wikipedia.org/wiki/Commemoration_(Anglicanism)'
            elif feast['prec'] == 4:
                feast['type'] = 'Lesser Feast'
                feast['type_url'] = 'https://en.wikipedia.org/wiki/Lesser_Feasts_and_Fasts'
            elif feast['prec'] == 7:
                feast['type'] = 'Holy Day'
                feast['type_url'] = 'https://en.wikipedia.org/wiki/The_Calendar_of_the_Church_Year'
                if 'source' not in feast:
                    feast['source'] = 'BCP 1979'

    return result
