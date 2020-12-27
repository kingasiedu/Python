import _sqlite3


def get_cookies():
    #Connects to the path
    path = "cookies.sqlite"
    con = _sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("SELECT * from moz_cookies")
    for data in cur.fetchall():
        print(data[0])


def get_bookmarks(moz_places, moz_bookmarks):
    #Join moz_places and moz_bookmarks
    path2 = "places.sqlite"

    con = _sqlite3.connect(path2)
    cur = con.cursor()
    cur.execute("SELECT id, type, fk, parent, position, title, keyword_id, folder_type, dateAdded, lastModified FROM moz_places, moz_bookmarks WHERE moz_places.url = moz_bookmarks.type")
    results = cur.fetchall()
    for result in results:
        print(result)
    return get_bookmarks


def get_history():
    pass
