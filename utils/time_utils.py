#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# time utility functions

import time
import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)



def get_past_timestamp_by_duration(duration):

    duration_map = {
        'day': 86400,
        'week': 86400 * 7,
        'month': 86400 * 30,
        'year': 86400 * 365
    }

    if duration in duration_map:
        return int(time.time()) - duration_map[duration]
    else:
        return 0



def get_month_timestamp_from_timestamp(timestamp):

    dt = datetime.datetime.fromtimestamp(timestamp)
    month_dt = datetime.datetime(year=dt.year, month=dt.month, day=1)
    month_ts = int(time.mktime(month_dt.timetuple()))

    return month_ts



def get_human_readable_from_timestamp(timestamp):

    ts = int(timestamp)
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')






