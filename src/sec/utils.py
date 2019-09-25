from __future__ import absolute_import
import requests
import pathlib
import boto3
import datetime
from math import ceil


def get_daily_idx() -> str:

    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    currentYear = yesterday.year
    currentQuarter = int(ceil(yesterday.month/3.))
    yesterdate = yesterday.strftime('%Y%m%d')

    baseURL = f'https://www.sec.gov/Archives/edgar/daily-index/{currentYear}/QTR{currentQuarter}/crawler.{yesterdate}.idx'
    
    return baseURL


def generate_date(startDt, fmt) -> str:
    """
    :param startdt: date string
    :param fmt: format string

    :return:
    """
    startDate = datetime.datetime.strptime(startDt, fmt)
    endDate = datetime.datetime.today()
    delta = endDate - startDate

    for i in range(delta.days):
        dt = startDate + datetime.timedelta(days=i)
        yield datetime.datetime.strftime(dt, '%Y%m%d')


def get_historical_idx(year, quarter):
    """
    :param year: int
    :param quarter: int
    :return:
    """
    url = f'https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{quarter}/crawler.idx'

    response = requests.get(url)

    return response.content.decode(encoding='utf-8')


def parse_idx(idx):
    pass
