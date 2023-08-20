from unittest import TestCase, main
from unittest.mock import patch
from get_next_care_date import get_next_care_date

class TestGetNextCareDateFunction(TestCase):

    def test_valid_date_input(self):
        last_care_date = '2023-08-15 10:00:00'
        care_frequency = 7
        expected = '2023-08-22 10:00:00'
        result = get_next_care_date(last_care_date, care_frequency)
        
        self.assertEqual(expected, result)


    
    def test_invalid_input_format(self):
        invalid_date_format = '08-15-2023 10:00:00'
        care_frequency = 7
        expected_error_message = "The provided date format is incorrect. Please use the format 'YYYY-MM-DD HH:MM:SS'"

        with patch('builtins.print') as mock_print:
            result = get_next_care_date(invalid_date_format, care_frequency)
            mock_print.assert_called_with(expected_error_message)

        self.assertIsNone(result)



    def test_invalid_care_frequency_input(self):
        last_care_date = '2023-05-25 12:30:00'
        care_frequency = "7"
        expected_error_message = "An unexpected error occurred:"

        with patch('builtins.print') as mock_print:
            result = get_next_care_date(last_care_date, care_frequency)
            mock_print.assert_called_once()  
            actual_error_message = mock_print.call_args[0][0] 
            self.assertIn(expected_error_message, actual_error_message)
    
        self.assertIsNone(result)
    
    def test_no_last_care_date_provided(self):
        care_frequency = 4
        expected_error_message = "An unexpected error occurred:"

        with patch('builtins.print') as mock_print:
            result = get_next_care_date(None, care_frequency)
            mock_print.assert_called_once()  
            actual_error_message = mock_print.call_args[0][0]  
            self.assertIn(expected_error_message, actual_error_message)  
        
        self.assertIsNone(result)



if __name__ == '__main__':
    main()