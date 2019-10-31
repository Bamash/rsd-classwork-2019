from times import *

def test_given_input():
  
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    #print(overlap_time(large, short))
    result = overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] 
    assert result == expected

def test_class_time():
   large = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
   short = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
   result = overlap_time(large, short)
   expected = short
   assert result == expected