import unittest
import ParserClass
from ParserClass import EdifactParser
class TestParser(unittest.TestCase):
    def test_file_exists(self):
        true_file   = "./edifact_message.txt"
        false_file  = "./fake_edifact_message.txt"

        exists      = EdifactParser(true_file)
        fake        = EdifactParser(false_file)
        self.assertNotEqual(exists.edifact_message, False)
        self.assertEqual(fake.edifact_message , False)

    def test_errors_in_file(self):
        not_long_enough_file      = "./error_edifact_message.txt"
        not_long_enough  = EdifactParser(not_long_enough_file)
        self.assertEqual(not_long_enough.loc_segments, [])
        # Release Characters present will have one element with escapes. Therefore we should only get 2 elements in the second and third segments
        release_char_present = "./release_char_edifact.txt"
        rel_char_parser  = EdifactParser(release_char_present)
        print("release char present")
        print(rel_char_parser.sec_third_segments)
        self.assertEqual(len(rel_char_parser.sec_third_segments),2)
