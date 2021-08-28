# Surfs Up

## Overview of Analysis
A new venture to open a Surf and Shake shop which would sell surfboards and ice-cream to locals and tourists needs investor backing to be able to get off the ground successfully. The investor is well know for his love of surfing but has some reservations due to a previous bad experience. A previous Surf shop which the investor was engaged with was rained out of business, so this time he wants to understand the weather of the chosen location better before committing to anything. He asks for some Analytics on a dataset of temperatures he has from Oahu.

## Results

|June | December|
|-----|------|
|<img src = 'Resources/JuneTemps'>|<img src = 'Resources/DecTemps'>

### Observations
1. The average temperature in June is 75 while December is 71. There is only a difference of 3 degrees between the summer and winter months.
2. Min temperature in June is 64 while in December this drops to 56. This indicates that not all days in December would be profitable for the Surf shop.
3. Standard Deviation is lower in June, indicating more consistent temperatures. While in December, the Standard Deviation is a bit higher, which indicates there is more fluctuation in the temperature through that month. 

## Summary
Overall the results are positive for year long good weather which would help this shop to be successful. Average temperatures do not vary much throughout the year. The data shows us that while December might be a month where we might see some cooler temperatures, there would still be weather which would allow locals and tourists to surf and for the business to make a profit. There was a significant amount of data points included in these assumptions, so again that gives us robust data set to make confident assumptions on. 

### Recommendations
Two queries which would be useful to gather some further information and gain more insight.
1. This query allows us to see how many temperatures are below first quartile to understand how many cold days were recorded under 69 degrees.
```
session.query(Measurement.tobs).\
filter(extract('month', Measurement.date) ==12).\
filter(Measurement.tobs<=69).count()
```
2. This query allows us to see how many temperatures recorded were over 3rd quartile:
```
session.query(Measurement.tobs).\
filter(extract('month', Measurement.date)==12).\
filter(Measurement.tobs>=74).count()