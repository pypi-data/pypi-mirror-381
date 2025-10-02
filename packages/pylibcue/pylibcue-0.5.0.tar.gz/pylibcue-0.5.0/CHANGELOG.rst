v0.5.0
------

\+ `Cycloctane/libcue v2.3.0.dev4
<https://github.com/Cycloctane/libcue/tree/v2.3.0.dev4>`_

- Add ``Track.get_index()`` method to directly get the time of a specific INDEX.
- Breaking change: rename previous ``Track.index`` property to ``Track.track_number``.
- Add ``cueprint.py`` cli tool.
- Add support for "REM DISCNUMBER" and "REM TOTALDISCS" fields.
- Fix typing of ``Track.mode``.
- Optimize compilation and reduce binary size.

v0.4.0
------

\+ `Cycloctane/libcue v2.3.0.dev3
<https://github.com/Cycloctane/libcue/tree/v2.3.0.dev3>`_

- Build wheels for Python 3.14.
- Add support for "REM COMMENT" fields.
- Parse "REM DISCID" and "REM COMPOSER" (stored in cdtext as "DISC_ID" and "COMPOSER").

v0.3.0
------

\+ `Cycloctane/libcue v2.3.0.dev2
<https://github.com/Cycloctane/libcue/tree/v2.3.0.dev2>`_

- Add support for CATALOG and INDEX fields.
- Add _asdict() method to CDText and Rem.
- Fix CUE syntax error still showing if installed from sdist.
- Fix album_gain property name typo.

v0.2.1
------

\+ `Cycloctane/libcue v2.3.0.dev1
<https://github.com/Cycloctane/libcue/tree/v2.3.0.dev1>`_

- Fix msvc compatibility issue.
- Disable CUE syntax error output.

v0.2.0
------

\+ `libcue v2.3.0 <https://github.com/lipnitsk/libcue/tree/v2.3.0>`_

- Remove unused ``DiscMode`` and ``TrackSubMode``.
- Refactor ``Cd`` constructors.
- Reduce sdist size.
