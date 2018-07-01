import unittest
from court_book import Court_book


class MyTest(unittest.TestCase):

    def test_book(self):
        dic1 = {
            "court_id":"A",
            "start_time":10,
            "end_time":11,
            "booking_date":"2016-06-02",
            "booking_time":"10:00~11:00",
            "seven_days":3
        }
        dic2 = {
            "court_id": "A",
            "start_time": 10,
            "end_time": 11,
            "booking_date": "2016-06-02",
            "booking_time": "10:00~11:00",
            "seven_days": 3
        }

        test = Court_book()
        self.assertEqual(test.parse_book(dic1), True)
        self.assertEqual(test.parse_book(dic2), False)
        # Court_book.parse_book(dic)
        # self.assertEquals(False, False)

if __name__=='__main__':
    unittest.main()
# MyTest.test_book()