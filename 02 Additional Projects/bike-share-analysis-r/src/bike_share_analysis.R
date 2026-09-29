# Bike Share Analysis in R
# Reconstructed from the rendered project notebook included in the original archive.
# Original analysis: New York City, Chicago, and Washington, D.C.

ny

=

read.csv
(
'new_york_city.csv'
)

wash

=

read.csv
(
'washington.csv'
)

chi

=

read.csv
(
'chicago.csv'
)

# ---- Notebook cell ----

head
(
ny
)

# ---- Notebook cell ----

head
(
wash
)

# ---- Notebook cell ----

head
(
chi
)

# ---- Notebook cell ----

# Function to prepare each city's data

prepare_data

<-

function
(
df
,

city_name
)

{

df
$
Start.Time

<-

as.POSIXct
(

df
$
Start.Time
,

format

=

"%Y-%m-%d %H:%M:%S"

)

df
$
Month

<-

format
(
df
$
Start.Time
,

"%B"
)

df
$
DayOfWeek

<-

format
(
df
$
Start.Time
,

"%A"
)

df
$
Hour

<-

as.numeric
(
format
(
df
$
Start.Time
,

"%H"
))

df
$
City

<-

city_name

return
(
df
)

}

# Prepare all three datasets

chi

<-

prepare_data
(
chi
,

"Chicago"
)

ny

<-

prepare_data
(
ny
,

"New York City"
)

wash

<-

prepare_data
(
wash
,

"Washington"
)

# ---- Notebook cell ----

# Combine the three cities

time_data

<-

rbind
(

chi[
,

c
(
"Month"
,

"DayOfWeek"
,

"Hour"
,

"City"
)
]
,

ny[
,

c
(
"Month"
,

"DayOfWeek"
,

"Hour"
,

"City"
)
]
,

wash[
,

c
(
"Month"
,

"DayOfWeek"
,

"Hour"
,

"City"
)
]

)

# ---- Notebook cell ----

# Find the busiest month for each city

month_counts

<-

aggregate
(

list
(
Rides

=

time_data
$
Month
),

by

=

list
(
City

=

time_data
$
City
,

Month

=

time_data
$
Month
),

FUN

=

length

)

month_counts

<-

month_counts[

order
(
month_counts
$
City
,

-
month_counts
$
Rides
),

]

busiest_months

<-

do.call
(

rbind
,

lapply
(
split
(
month_counts
,

month_counts
$
City
),

head
,

1
)

)

busiest_months

# ---- Notebook cell ----

# Find the busiest day for each city

day_counts

<-

aggregate
(

list
(
Rides

=

time_data
$
DayOfWeek
),

by

=

list
(
City

=

time_data
$
City
,

Day

=

time_data
$
DayOfWeek
),

FUN

=

length

)

day_counts

<-

day_counts[

order
(
day_counts
$
City
,

-
day_counts
$
Rides
),

]

busiest_days

<-

do.call
(

rbind
,

lapply
(
split
(
day_counts
,

day_counts
$
City
),

head
,

1
)

)

busiest_days

# ---- Notebook cell ----

# Find the busiest hour for each city

hour_counts

<-

aggregate
(

list
(
Rides

=

time_data
$
Hour
),

by

=

list
(
City

=

time_data
$
City
,

Hour

=

time_data
$
Hour
),

FUN

=

length

)

hour_counts

<-

hour_counts[

order
(
hour_counts
$
City
,

-
hour_counts
$
Rides
),

]

busiest_hours

<-

do.call
(

rbind
,

lapply
(
split
(
hour_counts
,

hour_counts
$
City
),

head
,

1
)

)

busiest_hours

# ---- Notebook cell ----

library
(
ggplot2
)

ggplot
(
hour_counts
,

aes
(
x

=

Hour
,

y

=

Rides
,

fill

=

City
))

+

geom_col
(
position

=

"dodge"
)

+

labs
(

title

=

"Bike Share Usage by Hour Across Three Cities"
,

x

=

"Hour of Day"
,

y

=

"Number of Rides"
,

fill

=

"City"

)

+

scale_fill_manual
(
values

=

c
(

"Chicago"

=

"#1b9e77"
,

"New York City"

=

"#d95f02"
,

"Washington"

=

"#7570b3"

))

# ---- Notebook cell ----

# Function to find the most common start stations

get_top_stations

<-

function
(
df
,

city_name
,

n

=

10
)

{

station_counts

<-

as.data.frame
(

sort
(
table
(
df
$
Start.Station
),

decreasing

=

TRUE
)

)

names
(
station_counts
)

<-

c
(
"Station"
,

"Rides"
)

station_counts
$
City

<-

city_name

head
(
station_counts
,

n
)

}

# Find the top 10 start stations in each city

top_chicago

<-

get_top_stations
(
chi
,

"Chicago"
)

top_new_york

<-

get_top_stations
(
ny
,

"New York City"
)

top_washington

<-

get_top_stations
(
wash
,

"Washington"
)

top_stations

<-

rbind
(

top_chicago
,

top_new_york
,

top_washington

)

top_stations

# ---- Notebook cell ----

# Find the single busiest start station in each city

busiest_stations

<-

do.call
(

rbind
,

lapply
(
split
(
top_stations
,

top_stations
$
City
),

head
,

1
)

)

busiest_stations

# ---- Notebook cell ----

# Chicago top start stations

ggplot
(

top_chicago
,

aes
(
x

=

reorder
(
Station
,

Rides
),

y

=

Rides
)

)

+

geom_col
(
fill

=

"#1b9e77"
)

+

coord_flip
()

+

labs
(

title

=

"Top 10 Start Stations (Chicago)"
,

x

=

"Start Station"
,

y

=

"Number of Rides"

)

+

theme_minimal
()

# ---- Notebook cell ----

# New York City top start stations

ggplot
(

top_new_york
,

aes
(
x

=

reorder
(
Station
,

Rides
),

y

=

Rides
)

)

+

geom_col
(
fill

=

"#d95f02"
)

+

coord_flip
()

+

labs
(

title

=

"Top 10 Start Stations (New York City)"
,

x

=

"Start Station"
,

y

=

"Number of Rides"

)

+

theme_minimal
()

# ---- Notebook cell ----

# Washington top start stations

ggplot
(

top_washington
,

aes
(
x

=

reorder
(
Station
,

Rides
),

y

=

Rides
)

)

+

geom_col
(
fill

=

"#7570b3"
)

+

coord_flip
()

+

labs
(

title

=

"Top 10 Start Stations (Washington)"
,

x

=

"Start Station"
,

y

=

"Number of Rides"

)

+

theme_minimal
()

# ---- Notebook cell ----

# Count user types for each city

user_types

<-

rbind
(

data.frame
(
City

=

"Chicago"
,

User.Type

=

names
(
table
(
chi
$
User.Type
)),

Count

=

as.numeric
(
table
(
chi
$
User.Type
))),

data.frame
(
City

=

"New York City"
,

User.Type

=

names
(
table
(
ny
$
User.Type
)),

Count

=

as.numeric
(
table
(
ny
$
User.Type
))),

data.frame
(
City

=

"Washington"
,

User.Type

=

names
(
table
(
wash
$
User.Type
)),

Count

=

as.numeric
(
table
(
wash
$
User.Type
)))

)

user_types

# ---- Notebook cell ----

# Display summary counts

aggregate
(

Count

~

City

+

User.Type
,

data

=

user_types
,

sum

)

# ---- Notebook cell ----

library
(
ggplot2
)

ggplot
(
user_types
,

aes
(
x

=

City
,

y

=

Count
,

fill

=

User.Type
))

+

geom_col
(
position

=

"dodge"
)

+

labs
(

title

=

"Bike Share User Types by City"
,

x

=

"City"
,

y

=

"Number of Users"
,

fill

=

"User Type"

)

+

scale_fill_brewer
(
palette

=

"Set2"
)

+

theme_minimal
()

+

theme
(

legend.position

=

"bottom"

)

# ---- Notebook cell ----

system
(
'python -m nbconvert Explore_bikeshare_data.ipynb'
)