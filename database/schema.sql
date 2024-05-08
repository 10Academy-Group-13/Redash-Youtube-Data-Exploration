-- Create the chart_data database
CREATE DATABASE youtube_data;

-- Switch to the youtube_data database
USE youtube_data;

-- Create the chart_data table for each dataset zip
CREATE TABLE cities_chart_data (
    Date TEXT,
    Cities TEXT,
    CityName TEXT,
    Views INTEGER
);

CREATE TABLE content_type_chart_data (
    Date TEXT,
    Cities TEXT,
    CityName TEXT,
    Views INTEGER
);

CREATE TABLE device_type_chart_data (
    Date TEXT,
    DeviceType TEXT,
    Views INTEGER
);

CREATE TABLE geography_chart_data (
    Date TEXT,
    Geography TEXT,
    Views INTEGER
);


CREATE TABLE New_and_returning_viewers_chart_data (
    Date TEXT,
    NewAndReturningViewers TEXT,
    Views INTEGER
);

CREATE TABLE operating_system_chart_data (
    Date TEXT,
    OperatingSystem TEXT,
    Views INTEGER
);

CREATE TABLE sharing_service_chart_data (
    Date TEXT,
    SharingService TEXT,
    Shares INTEGER
);

CREATE TABLE subscription_source_chart_data (
    Date TEXT,
    SubscriptionSource TEXT,
    Subscribers INTEGER
);

CREATE TABLE subscription_status_chart_data (
    Date TEXT,
    SubscriptionStatus TEXT,
    Views INTEGER
);


CREATE TABLE traffic_source_chart_data (
    Date TEXT,
    TrafficSource TEXT,
    Views INTEGER
);

-- Create the table_data table for each dataset zip
CREATE TABLE cities_table_data (
    Cities TEXT,
    CityName TEXT,
    Geography TEXT,
    Geography1 TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE content_type_table_data (
    ContentType TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE device_type_table_data (
    DeviceType TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE geography_table_data (
    Geography TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE new_and_returning_viewers_table_data (
    NewAndReturningViewers TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE operating_system_table_data (
    OperatingSystem TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE sharing_service_table_data (
    SharingService TEXT,
    Shares INTEGER
);

CREATE TABLE subscription_source_table_data (
    SubscriptionSource TEXT,
    Subscribers INTEGER,
    SubscribersGained INTEGER,
    SubscribersLost INTEGER
);

CREATE TABLE subscription_status_table_data (
    SubscriptionStatus TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE subtitles_and_cc_table_data (
    SubtitlesAndCC TEXT,
    Views INTEGER,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);

CREATE TABLE traffic_source_table_data (
    TrafficSource TEXT,
    Views FLOAT,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT,
    Impressions FLOAT,
    ImpressionsClickThroughRate FLOAT
);

CREATE TABLE viewer_age_table_data (
    ViewerAge TEXT,
    ViewsPercentage FLOAT,
    AverageViewDuration TEXT,
    AveragePercentageViewed FLOAT,
    WatchTimeHoursPercentage FLOAT
);

CREATE TABLE viewer_gender_table_data (
    ViewerGender TEXT,
    ViewsPercentage FLOAT,
    AverageViewDuration TEXT,
    AveragePercentageViewed FLOAT,
    WatchTimeHoursPercentage FLOAT
);

CREATE TABLE viewership_by_age_table_data (
    Date TEXT,
    Views FLOAT,
    WatchTimeHours FLOAT,
    AverageViewDuration TEXT
);