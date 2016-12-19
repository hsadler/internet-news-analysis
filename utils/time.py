#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# time utility functions

import time
import pprint

pp = pprint.PrettyPrinter(indent=4)



def get_past_timestamp_by_duration(duration='day'):

    duration_map = {
        'day': 86400,
        'week': 86400 * 7,
        'month': 86400 * 30,
        'year': 86400 * 365
    }

    return int(time.time()) - duration_map[duration]



def get_month_timestamp(timestamp):

    print 'getting beggining of month timestamp from timestamp...'



