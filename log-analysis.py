#!/usr/bin/env python3

import psycopg2

# Queries required

#  What are the most popular three articles of all time?

solution_1 = """
select slug as article, count(log.path) as views
  from articles, log
  where log.path = '/article/' || articles.slug
  group by articles.slug
  order by views desc limit 3;"""

# Who are the most popular article authors of all time?

solution_2 = """
select * from authors_view;"""

# On which days did more than 1% of requests lead to errors?

solution_3 = """
select * from error_view;"""

# Database Name

DBNAME = "news"

# function for question 1


def sol1():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(solution_1)
    results = cursor.fetchall()
    conn.close()
    return results

# function for question 2


def sol2():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(solution_2)
    results = cursor.fetchall()
    conn.close()
    return results

# function for question 3


def sol3():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(solution_3)
    results = cursor.fetchall()
    conn.close()
    return results

# Function for executing all queries


def execute():
    sol1()
    sol2()
    sol3()


execute()
