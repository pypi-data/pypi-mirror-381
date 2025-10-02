import unittest
from pathlib import Path

import pylibcue

TEST_DATA = Path(__file__).parent / "testdata"


class TestCue(unittest.TestCase):

    def test_minimal(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "minimal.cue")
        self.assertEqual(len(cd), 2)
        self.assertIsNotNone(cd.cdtext)
        self.assertIsNotNone(cd.rem)
        self.assertIsNone(cd.cdtext.title)
        self.assertEqual(cd[1].get_index(1), (4, 10, 59))
        self.assertIsNone(cd[1].get_index(2))
        self.assertEqual(cd[1].start, (4, 10, 59))
        self.assertIsNotNone(cd[1].cdtext)
        self.assertIsNotNone(cd[1].rem)
        self.assertIsNone(cd[1].cdtext.title)

    def test_example_disc(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "example.cue")
        self.assertEqual(cd.catalog, "4549767191621")
        self.assertEqual(cd.cdtext.performer, "サンドリオン")
        self.assertEqual(cd.cdtext.title, "天体図")
        self.assertEqual(cd.cdtext.disc_id, "3503E004")
        self.assertEqual(cd.cdtext.composer, "")
        self.assertEqual(cd.rem.comment, "ExactAudioCopy v1.6")
        self.assertEqual(len(cd.cdtext._asdict()), 11)
        self.assertEqual(len(cd.rem._asdict()), 8)
        self.assertEqual(list(cd.cdtext._asdict().values()).count(None), 11 - 4)

    def test_example_tracks(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "example.cue")
        self.assertEqual(len(cd), 4)
        for i in cd:
            self.assertEqual(i.filename, "COCC-18150.wav")
            self.assertIs(i.mode, pylibcue.TrackMode.AUDIO)
            self.assertEqual(i.cdtext.performer, "サンドリオン")
            self.assertTrue(i in cd)

        self.assertEqual(cd[0].track_number, 1)
        self.assertEqual(cd[0].cdtext.title, "天体図")
        self.assertEqual(cd[0].isrc, "JPCO02329890")
        self.assertIsNone(cd[0].get_index(0))
        self.assertEqual(cd[0].get_index(1), (0, 0, 0))
        self.assertEqual(cd[0].start, (0, 0, 0))
        self.assertEqual(cd[0].length, (4, 8, 50))
        self.assertEqual(cd[0].zero_pre, None)

        self.assertEqual(cd[1].track_number, 2)
        self.assertEqual(cd[1].cdtext.title, "ゆびきりの唄")
        self.assertEqual(cd[1].isrc, "JPCO02329840")
        self.assertEqual(cd[1].get_index(0), (4, 8, 50))
        self.assertEqual(cd[1].get_index(1), (4, 10, 59))
        self.assertEqual(cd[1].start, (4, 10, 59))
        self.assertEqual(cd[1].length, (4, 4, 32))
        self.assertEqual(cd[1].zero_pre, (0, 2, 9))

        self.assertEqual(cd[3].track_number, 4)
        self.assertEqual(cd[3].cdtext.title, "ゆびきりの唄 (off vocal ver.)")
        self.assertEqual(cd[3].isrc, "JPCO02329849")
        self.assertEqual(cd[3].get_index(0), (12, 25, 25))
        self.assertEqual(cd[3].get_index(1), (12, 27, 43))
        self.assertEqual(cd[3].start, (12, 27, 43))
        self.assertIsNone(cd[3].length)
        self.assertEqual(cd[3].zero_pre, (0, 2, 18))

    def test_more(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "more.cue")
        self.assertEqual(cd.cdtext.songwriter, "Songwriter0")
        self.assertEqual(cd.cdtext.composer, "Composer0")
        self.assertEqual(cd.cdtext.arranger, "Arranger0")
        self.assertEqual(cd.cdtext.message, "message0")
        self.assertEqual(cd.cdtext.disc_id, "1234ABCD")
        self.assertEqual(cd.cdtext.upc_isrc, "1234567890")
        self.assertEqual(cd.cdtext.genre, "Genre0")
        self.assertEqual(cd.rem.date, "2023")
        self.assertEqual(cd.rem.disc_number, "1")
        self.assertEqual(cd.rem.total_discs, "2")
        self.assertEqual(cd.cdtextfile, "cdtext0.cdt")
        self.assertEqual(cd[0].zero_pre, (0, 1, 0))
        self.assertEqual(cd[0].zero_post, (0, 1, 0))
        self.assertTrue(cd[0] & pylibcue.TrackFlag.COPY_PERMITTED)
        self.assertTrue(cd[0] & pylibcue.TrackFlag.FOUR_CHANNEL)
        self.assertTrue(cd[0] & pylibcue.TrackFlag.ANY)
        self.assertFalse(cd[0] & pylibcue.TrackFlag.PRE_EMPHASIS)
        self.assertFalse(cd[0] & pylibcue.TrackFlag.NONE)

    def test_multi(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "multi.cue")
        self.assertEqual(len(cd), 4)

        self.assertEqual(cd[0].filename, "COCC-18148.wav")
        self.assertEqual(cd[0].track_number, 1)
        self.assertEqual(cd[0].start, (0, 0, 0))
        self.assertEqual(cd[0].length, (4, 43, 52))
        self.assertEqual(cd[1].filename, "COCC-18148.wav")
        self.assertEqual(cd[1].track_number, 2)
        self.assertEqual(cd[1].start, (4, 45, 53))
        self.assertIsNone(cd[1].length)

        self.assertEqual(cd[2].filename, "COCC-18150.wav")
        self.assertEqual(cd[2].track_number, 3)
        self.assertEqual(cd[2].start, (0, 0, 0))
        self.assertEqual(cd[2].length, (4, 8, 50))
        self.assertEqual(cd[3].filename, "COCC-18150.wav")
        self.assertEqual(cd[3].track_number, 4)
        self.assertEqual(cd[3].start, (4, 10, 59))
        self.assertIsNone(cd[3].length)


class TestParsing(unittest.TestCase):

    def test_from_str(self):
        with open(TEST_DATA / "example.cue", "r", encoding='utf-8') as f:
            cd = pylibcue.Cd.from_str(f.read())
        self.assertEqual(cd.cdtext.title, "天体図")
        self.assertEqual(len(cd), 4)

    def test_encoding(self):
        cd = pylibcue.Cd.from_file(TEST_DATA / "example.jis.cue", encoding='shift-jis')
        self.assertEqual(cd.encoding, 'shift-jis')
        self.assertEqual(cd.cdtext.title, "天体図")
        self.assertEqual(cd[0].cdtext.title, "天体図")

    def test_error_unreadable(self):
        with self.assertRaises(IOError) as e:
            _ = pylibcue.Cd.from_file("not_exist.cue")
        self.assertEqual(str(e.exception), "Failed to read file")

    def test_error_parse(self):
        with self.assertRaises(ValueError) as e:
            _ = pylibcue.Cd.from_str("123456")
        self.assertEqual(str(e.exception), "Failed to parse cue string")


if __name__ == "__main__":
    unittest.main()
