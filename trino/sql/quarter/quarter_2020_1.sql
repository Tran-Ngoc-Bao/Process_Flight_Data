create schema if not exists hive.datasets_quarter;

create table if not exists hive.datasets_quarter.marketing_airline_network_2020_1
with (format = 'parquet')
as select
Year, Quarter, Month,
Marketing_Airline_Network, count(1) cnt
from hive.processed_data.flight_2020
where Quarter = 1
group by Year, Quarter, Month, Marketing_Airline_Network;



create table if not exists hive.datasets_quarter.flights_across_days_of_the_week_2020_1
with (format = 'parquet')
as select
Year, Quarter, Month, DayOfWeek,
count(1) cnt
from hive.processed_data.flight_2020
where Quarter = 1
group by Year, Quarter, Month, DayOfWeek;



create table if not exists hive.datasets_quarter.flight_origins_2020_1
with (format = 'parquet')
as select
Year, Quarter, Month,
Origin, OriginCityName, count(1) cnt
from hive.processed_data.flight_2020
where Quarter = 1
group by Year, Quarter, Month, Origin, OriginCityName;



create table if not exists hive.datasets_quarter.flights_cancellations_by_day_of_the_week_2020_1
with (format = 'parquet')
as select
Year, Quarter, Month, DayOfWeek,
(cast(count_if(Cancelled = 1) as real) / count(1) * 100) percentage
from hive.processed_data.flight_2020
where Quarter = 1
group by Year, Quarter, Month, DayOfWeek;



create table if not exists hive.datasets_quarter.total_cancellations_and_flights_per_carrier_2020_1
with (format = 'parquet')
as select
s.Year, s.Quarter, s.Month,
s.Marketing_Airline_Network,
(cast(count(1) as real) / b.total_flights * 100) percentage_flights, (cast(count_if(Cancelled = 1) as real) / b.total_cancellations * 100) percentage_cancellations
from hive.processed_data.flight_2020 s,
(select Year, Quarter, Month, count(1) total_flights, count_if(Cancelled = 1) total_cancellations from hive.processed_data.flight_2020 where Quarter = 1 group by Year, Quarter, Month) b
where s.Year = b.Year and s.Quarter = b.Quarter and s.Month = b.Month and s.Quarter = 1
group by s.Year, s.Quarter, s.Month, s.Marketing_Airline_Network, b.total_flights, b.total_cancellations;



create table if not exists hive.datasets_quarter.day_of_month_2020_1
with (format = 'parquet')
as select
s.Year, s.Quarter, s.Month, s.DayofMonth,
(cast(count(1) as real) / b.all * 100) percentage_all, (cast(count_if(s.Cancelled = 1) as real) / b.cancelled * 100) percentage_cancelled
from hive.processed_data.flight_2020 s,
(select Year, Quarter, Month, count(1) all, count_if(Cancelled = 1) cancelled from hive.processed_data.flight_2020 where Quarter = 1 group by Year, Quarter, Month) b
where s.Year = b.Year and s.Quarter = b.Quarter and s.Month = b.Month and s.Quarter = 1
group by s.Year, s.Quarter, s.Month, s.DayofMonth, b.all, b.cancelled;



create table if not exists hive.datasets_quarter.mean_delay_by_aircraft_carrier_2020_1
with (format = 'parquet')
as select
Year, Quarter, Month, Marketing_Airline_Network,
avg(CarrierDelay) carrier_delay,
avg(WeatherDelay) weather_delay,
avg(NASDelay) nas_delay,
avg(SecurityDelay) security_delay,
avg(LateAircraftDelay) late_aircraft_delay
from hive.processed_data.flight_2020
where Quarter = 1 
group by Year, Month, Quarter, Marketing_Airline_Network;
