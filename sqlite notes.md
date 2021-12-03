# CLI stuff
## Loading or creating a database (.db) file:
```
sqlite3 [filename]
```
---
## View tables in file
```
.tables
```
- Note: dot commands are sqlite-specific, non-dot commands are just normal SQL.
---
## Create a table
```sql
create table games(name string, year integer);
```
---
## Put stuff into the table

```sql
insert into games values('final fantasy five billion and six', 2069);
insert into games values('GTA VI', 9999);
```
## Look at stuff in table
```sql
SELECT * FROM games;
```
## Count rows in a table
```sql
select count(*) from games;
```
---
## Turn column headers on and off
```
.headers ON
.headers OFF
```
---
## Change display mode
```
.mode [mode]
```
Possible display modes:
- `list`: Default
- `columns`: Everything is nice and aligned
- `html`: HTML table format
- `lines`: Every piece of data is on its own line, with "rows" seperated by blank lines
- `insert`: Every row is represented by the SQL `insert` command that would insert that row


### [SQLite CLI docs](https://sqlite.org/cli.html)
---
<br>

# Python stuff

First, of course:
```python
import sqlite
```

So basically the way the python sqlite lib works is that first you get a connection to the database. Then, from the connection, you get a cursor. You do all your stuff using the cursor. Once you're done, you commit the changes to the database via the connection, then you close the connection.