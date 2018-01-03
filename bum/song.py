"""
Get song info.
"""
import shutil
import os
import time
from gi.repository import Playerctl, GLib

from . import util


def init():
    print("initialized")
    player = Playerctl.Player(player_name='spotify')
def get_art(cache_dir, size, client):
    """Get the album art."""
    
    player = Playerctl.Player(player_name='spotify')
    song = {
            'artist' : player.get_artist(),
            'album' : player.get_album(),
    }

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

