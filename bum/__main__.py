"""
'||
 || ...  ... ...  .. .. ..
 ||'  ||  ||  ||   || || ||
 ||    |  ||  ||   || || ||
 '|...'   '|..'|. .|| || ||.

Created by Dylan Araps
"""
import argparse
import pathlib
import time
from gi.repository import Playerctl, GLib

from . import display
from . import song

from .__init__ import __version__


def get_args():
    """Get the script arguments."""
    description = "bum - Download and display album art \
                   for mpd tracks."
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--size", metavar="\"px\"",
                     help="what size to display the album art in.",
                     default=250)

    arg.add_argument("--cache_dir", metavar="\"/path/to/dir\"",
                     help="Where to store the downloaded cover art.",
                     default=pathlib.Path.home() / ".cache/bum")

    arg.add_argument("--version", action="store_true",
                     help="Print \"bum\" version.")

    arg.add_argument("--port",
                     help="Use a custom mpd port.",
                     default=6600)

    return arg.parse_args()


def process_args(args):
    """Process the arguments."""
    if args.version:
        print(f"bum {__version__}")
        exit(0)


def main():
    """Main script function."""
    args = get_args()
    process_args(args)

    disp = display.init(args.size)
    client = Playerctl.Player(player_name='spotify')

    song.get_art(args.cache_dir, args.size, client)
    display.launch(disp, args.cache_dir / "current.jpg")
    
    while True:
        player_status = client.get_album()
        time.sleep(3)
        song.get_art(args.cache_dir, args.size, client)
        display.launch(disp, args.cache_dir / "current.jpg")

if __name__ == "__main__":
    main()
