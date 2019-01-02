# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


def mapStats(statList):
    """
    List of stats of the character.
    Each chunk of 5 elements relates to a single stat.
    This will split that up and create a dictionary with the required info.
    Args:
        statList (list): list of strings containing details of the character's stats

    Returns (dict): dictionary of the form {'stat':{'value': int,
                                                    'modifier': int}}

    """
    statsChunks = [statList[x:x + 5] for x in range(0, len(statList), 5)]
    stats = {}
    for chunk in statsChunks:
        stat = chunk[0]
        statValue = chunk[2]
        modValue = int(chunk[-2] + chunk[-1])
        stats[stat] = {'value': statValue,
                       'modifier': modValue}

    yield stats

def mapSkills(skillList):
    """
    List of skills of the character.
    Each chunk of 4 elements relates to a single stat.
    This will split that up and create a dictionary with the required info.
    Args:
        skillList (list): list of strings containing details of the character's skills

    Returns (dict): dictionary of the form {'stat':{'attribute': str,
                                                    'modifier': int}}

    """
    skillsChunks = [skillList[x:x + 4] for x in range(0, len(skillList), 4)]
    skills = {}
    for chunk in skillsChunks:
        attribute = chunk[0]
        skill = chunk[1]
        modValue = int(chunk[2] + chunk[3])
        skills[skill] = {'attribute': attribute,
                         'modifier': modValue}

    yield skills


class DndbeyondItem(scrapy.Item):
    name = scrapy.Field(output_processor = TakeFirst())
    stats = scrapy.Field(input_processor = mapStats,
                        output_processor = TakeFirst())
    skills = scrapy.Field(input_processor = mapSkills,
                        output_processor = TakeFirst())