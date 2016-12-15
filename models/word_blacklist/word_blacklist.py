#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# WordBlacklist Model

import json
import pprint

pp = pprint.PrettyPrinter(indent=4)



class WordBlacklist():



    _blacklist = None
    _cache_is_valid = False



    @classmethod
    def get_blacklist(cls):


        # if cached version of blacklist exists and the cache is valid, return cached word_blacklist
        if cls._blacklist is not None and cls._cache_is_valid:
            return cls._blacklist


        try:
            with open('models/word_blacklist/word-blacklist.json') as file:
                blacklist = json.load(file)
        except:
            blacklist = []


        cls._blacklist = blacklist
        cls._cache_is_valid = True

        return blacklist



    @classmethod
    def add_to_blacklist(cls, words):


        if isinstance(words, basestring):
            words = [words]


        with open('models/word_blacklist/word-blacklist.json', 'r+') as file:

            try:
                blacklist = json.load(file)
            except:
                blacklist = [];

            # append word to blacklist json file if it doesn't yet exist
            for word in words:

                if word not in blacklist:
                    blacklist.append(word)


            file.seek(0)
            json.dump(blacklist, file)
            file.truncate()


        cls._blacklist = blacklist;
        cls._cache_is_valid = False



    @staticmethod
    def remove_from_blacklist(word):
        pass
        # set word as inactive in word_blacklist table
        # invalidate cache





