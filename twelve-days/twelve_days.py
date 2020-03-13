def recite(start_verse, end_verse):
    first_line = "On the {count} day of Christmas my true love gave to me: "
    lines = [
            "twelve Drummers Drumming, ",
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, ",
            "{prefix}a Partridge in a Pear Tree.",
            ]
    ordinals = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth",
            ]
    
    verses = []
    for v in range(start_verse-1, end_verse):
        pre = "and " if v > 0 else ""
        verse = "".join([ first_line.format(count = ordinals[v]) ] + [ x.format(prefix = pre) for x in lines[11-v:] ])
        verses.append(verse)

    return verses