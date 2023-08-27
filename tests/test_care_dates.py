from unittest import TestCase, main
from unittest.mock import patch
from utils.care_dates import get_next_care_date, is_next_care_date_up_to_date
from datetime import datetime

class TestGetNextCareDateFunction(TestCase):

    def test_valid_date_input(self):
        last_care_date = datetime.strptime('2023-08-15 00:00:00', '%Y-%m-%d %H:%M:%S')
        care_frequency = 7
        expected = '2023-08-22'
        result = get_next_care_date(last_care_date, care_frequency)
        
        self.assertEqual(expected, result)


    def test_invalid_input(self):
        last_care_date = '2023-05-25 12:30:00'
        care_frequency = "7"
        expected_error_message = "Incorrect input, must be daytime object and an int"

        with patch('builtins.print') as mock_print:
            result = get_next_care_date(last_care_date, care_frequency)
            mock_print.assert_called_once()  
            actual_error_message = mock_print.call_args[0][0] 
            self.assertIn(expected_error_message, actual_error_message)
    
        self.assertIsNone(result)
    
    def test_no_last_care_date_provided(self):
        care_frequency = 4
        expected_error_message = "Incorrect input, must be daytime object and an int"

        with patch('builtins.print') as mock_print:
            result = get_next_care_date(None, care_frequency)
            mock_print.assert_called_once()  
            actual_error_message = mock_print.call_args[0][0]  
            self.assertIn(expected_error_message, actual_error_message)  
        
        with self.assertRaises(TypeError):
            get_next_care_date(care_frequency)
        
        self.assertIsNone(result)    


class TestIsNextCareUpToDate(TestCase):

    def test_up_to_date(self):
        upcoming_care = datetime.strptime('2023-09-15 00:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertTrue(is_next_care_date_up_to_date(upcoming_care))

    def test_out_of_date(self):
        upcoming_care = datetime.strptime('2023-07-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertFalse(is_next_care_date_up_to_date(upcoming_care))

    def test_current_date(self):
        upcoming_care = datetime.now()
        self.assertFalse(is_next_care_date_up_to_date(upcoming_care))    
    
    def test_incorrect_input_type(self):
        upcoming_care = "2023-09-03"
        with self.assertRaises(AssertionError):
            is_next_care_date_up_to_date(upcoming_care)

if __name__ == '__main__':
    main()