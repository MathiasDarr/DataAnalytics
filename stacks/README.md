# HBASE notes

### hbase documentation
https://hbase.apache.org/book.html#quickstart



docker exec -it hbase-master bash

### Enter interactive hbase shell
hbase-shell

### Create a table by specifying the table name & the column family name
create 'test', 'cf'

### List information about your table
list 'test'

### Describe the table 'test' for information on column_family dexription
describe 'test'
