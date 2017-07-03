### Log Analysis

- An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
- The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.
- It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### Inspiration

- Project made for Udacity NanoDegree.

### Getting Started
- Clone it by running command:
	git clone https://github.com/yash2code/log-analysis-ud.git

- This project makes use of the Linux-based virtual machine (VM).

- Download the [Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

	You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

- To load the data, use the command `psql -d news -f newsdata.sql`

- Make Views

- Run `python log-analysis.py`

### Version
- Version 0.1

### Views

- author_view
	
	```sql
	create view author_view as
	select authors.name, count(articles.author) as views from articles, log, authors
	where log.path = '/article/' || articles.slug and articles.author = authors.id
	group by authors.name order by views desc;
	```

- error_view

	```sql
	create view error_view as
	select Date,Total,Error, (Error::float*100)/Total::float as Percent from
	(select time::timestamp::date as Date, count(status) as Total,
	sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error from log
	group by time::timestamp::date) as output
	where (Error::float*100)/Total::float > 1.0 order by Percent desc;
	```

### Output or Results:

	- What are the most popular three articles of all time?

		```
 		Candidate is jerk, alleges rival -- 338647
  		Bears love berries, alleges bear -- 253801
  		Bad things gone, say good people -- 170098
   		``` 