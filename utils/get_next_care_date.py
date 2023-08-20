from datetime import datetime, timedelta

def get_next_care_date(last_care_date, care_frequency):

    try:
     # Convert the last_care_date string to a datetime object
        last_care_datetime = datetime.strptime(last_care_date, '%Y-%m-%d %H:%M:%S')
         
    # Calculate the upcoming care date by adding care_frequency days to last_care_datetime
        upcoming_care_datetime = last_care_datetime + timedelta(care_frequency)

    # Convert the upcoming_care_datetime back to a formatted string
        next_care_date = upcoming_care_datetime.strftime('%Y-%m-%d %H:%M:%S')

        return next_care_date
    
    except ValueError :
        print("The provided date format is incorrect. Please use the format 'YYYY-MM-DD HH:MM:SS'")
        return None
    
    except Exception as error:
        print("An unexpected error occurred:", error)
        return None


