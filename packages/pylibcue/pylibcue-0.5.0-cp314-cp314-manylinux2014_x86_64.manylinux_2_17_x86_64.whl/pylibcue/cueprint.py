import argparse
from collections.abc import Callable
from os import PathLike

from ._cue import Cd, CDText, Rem

_dump: Callable[[CDText | Rem], list[str]] = lambda x: [
    f"{k.capitalize()}: {v}" for k, v in x._asdict().items() if v
]

_fmtmsf: Callable[[tuple[int, int, int]], str] = lambda x: "%d:%02d.%02d" % x


def cueprint(file: PathLike[str] | str, encoding: str = "utf-8") -> None:
    cd = Cd.from_file(file, encoding)
    print(
        "Disc Information",
        f"Number of Tracks: {len(cd)}",
        *((f"Catalog: {cd.catalog}",) if cd.catalog else ()),
        *_dump(cd.cdtext),
        *_dump(cd.rem),
        "",
        sep="\n",
    )
    for tr in cd:
        print(
            f"Track {tr.track_number} Information",
            f"File: {tr.filename or '*Unknown*'}",
            *((f"Start: {_fmtmsf(tr.start)}",) if tr.start else ()),
            *((f"Length: {_fmtmsf(tr.length)}",) if tr.length else ()),
            *((f"ISRC: {tr.isrc}",) if tr.isrc else ()),
            *_dump(tr.cdtext),
            *_dump(tr.rem),
            "",
            sep="\n",
        )


def cuebreakpoints(file: PathLike[str] | str, encoding: str = "utf-8") -> None:
    print(
        *(
            _fmtmsf(tr.start) for tr in Cd.from_file(file, encoding)
            if tr.start and tr.start != (0, 0, 0)
        ), sep="\n",
    )


def main() -> int:
    from . import __version__
    parser = argparse.ArgumentParser(
        description="Print disc information and tracks breakpoints from a CUE file"
    )
    parser.add_argument("file", help="CUE file path")
    parser.add_argument(
        "--encoding", "-e", default="utf-8", help="file encoding (default: utf-8)"
    )
    parser.add_argument(
        "--version", action="version", version=f"cueprint.py (pylibcue) v{__version__}"
    )
    parser.add_argument(
        "--breakpoints-only", action="store_true",
        help="only print track breakpoints (cuebreakpoints)"
    )
    ns = parser.parse_args()
    if ns.breakpoints_only:
        cuebreakpoints(ns.file, ns.encoding)
    else:
        cueprint(ns.file, ns.encoding)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
