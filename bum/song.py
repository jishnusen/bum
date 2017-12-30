"""
Get song info.
"""
import shutil
import os
import mpd
import time

from . import util


def init(port=6600):
    """Initialize mpd."""
    client = mpd.MPDClient()

    try:
        client.connect("localhost", port)
        return client

    except ConnectionRefusedError:
        print("error: Connection refused to mpd/mopidy.")
        os._exit(1)  # pylint: disable=W0212


def get_art(cache_dir, size, client):
    """Get the album art."""
    song = client.currentsong()

    if len(song) < 2:
        print("album: Nothing currently playing.")
        return

    file_name = f"{song['artist']}_{song['album']}_{size}.jpg".replace("/", "")
    file_name = cache_dir / file_name

    if file_name.is_file():
        shutil.copy(file_name, cache_dir / "current.jpg")
        print("album: Found cached art.")

    else:
        print("album: Downloading album art...")
        os.system(str('sacad "' + str(song['artist']) + '" "' + str(song['album']) + '" "' + str(250) + '" "' + str(file_name) + '"'))
        shutil.copy(file_name, cache_dir / "current.jpg")

