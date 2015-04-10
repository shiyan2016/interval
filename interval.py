#!/usr/bin/env python

class Time(object):
    def __init__(self, hour, minute):
        '''Simple time wrapper.

        :param hour: Integer, from 0 to 24.
        :param minute: Integer, from 0 to 59.
        '''
        self.hour = hour
        self.minute = minute
    def __repr__(self):
        return "%02u:%02u"%(self.hour, self.minute)
        
class Interval(object):
    def __init__(self, start, end):
        '''Interval represents a task on schedule. 

        :param start: Time, when the task starts.
        :param end: Time, when the task ends.

        TODO: add support for passing timestap strings.For example,
              Interval('00:00', '02:39').
        TODO: make Interval objects more readable in a python shell.e.g.,

              >>> Interval(Time(0,0), Time(2,30))
              Interval(00:00 -> 02:30)
        '''
        if(isinstance(start,basestring) and isinstance(end,basestring)):
            start_split = start.split(':')
            end_split = end.split(':')
            start = Time(int(start_split[0]),int(start_split[1]))
            end = Time(int(end_split[0]), int(end_split[1]))
      
        self.start = start
        self.end = end
    def __repr__(self):
        '''
        return the readable format in a python shell
        '''
        return "%s -> %s"%(repr(self.start), repr(self.end))

def cmp_time(a, b):
  if(a.hour>b.hour):
    return -1
  elif(a.hour<b.hour):
    return 1
  else:
    if(a.minute>b.minute):
      return -1
    elif(a.minute<b.minute):
      return 1
    else:
      return 0
        
def most_intervals_overlap_count(intervals):
    '''count the maximum overlappes in a schedule.

    tasks on the schedule may overlaps.For example, task A was scheduled
    from 06:00 to 08:00, and task B was scheduled from 07:30 to 09:00, thenjin
    A and B overlap in 07:30-08:00.

    mutiple tasks may overlap on the same time interval, you job is to find
    out the number of tasks when maximum overlap happens.

    :param intervals: list of Interval

    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0))])
    1
    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(7, 30), Time(9,0))])
    2
    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(8, 0), Time(9,0))])
    1
    '''
    # TODO: implement this function
    # Get the time points of all tasks
    all_time_points=[]
    for i in range(len(intervals)):
        all_time_points.append(intervals[i].start)
        all_time_points.append(intervals[i].end)
    #print 'Before sorting: ', all_time_points
    all_time_points.sort(cmp_time, reverse=True)
    #print 'After sorting: ', all_time_points
    
    # count the overlap tasks of each time range
    count = [0]*(len(all_time_points)-1)
    for i in range(len(intervals)):
        index_start = all_time_points.index(intervals[i].start)
        while(cmp_time(intervals[i].end, all_time_points[index_start]) == -1):
            count[index_start] += 1
            index_start += 1           
    #print count
    return max(count)
        

if __name__ == "__main__":
  '''
  Do some unit testing for this module.
  '''
  print Interval(Time(0,0), Time(2,30))
  print Interval('00:00', '02:39')
  
  print "Testing giving cases..."
  print most_intervals_overlap_count([Interval(Time(6,0), Time(8,0))])
  print most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(7, 30), Time(9,0))])
  print most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(8, 0), Time(9,0))])
  
  print "More testing on other cases..."
  # 3
  print most_intervals_overlap_count([Interval(Time(1,20), Time(3,0)), Interval(Time(2, 0), Time(4,30)), Interval(Time(3, 0), Time(5,0)), Interval(Time(3, 30), Time(5,0))])
  # 4
  print most_intervals_overlap_count([Interval(Time(20,20), Time(21,33)), Interval(Time(22, 0), Time(23,30)), Interval(Time(21, 0), Time(22,0)), Interval(Time(21, 01), Time(21,31)), Interval(Time(21, 30), Time(21,53))])