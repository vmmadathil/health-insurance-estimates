install.packages('ipumsr')

require("ipumsr")

ddi <- read_ipums_ddi("usa_00012.xml")
data <- read_ipums_micro(ddi)


require(RMySQL)
#connecting to database
con = dbConnect(MySQL(), user='root', password='Economics100!', dbname='health_insurance_modeling', host='127.0.0.1')

#writing to database
dbWriteTable(con, 'ipums_data_raw', data, append = TRUE)
dbDisconnect(con)