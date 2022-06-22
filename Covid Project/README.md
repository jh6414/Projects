# Full version with loaded charts can be found at:

https://colab.research.google.com/drive/1b7bi2Ict4eMQoFwXOWcgzZPM9sLAK-Lq?usp=sharing

**Main File: GroupProjectSocialNetwork.ipynb**


New York University








Lockdowns Decreased Death Rates in the United States








By: Jack Hartigan, Summer Xia, Ben Kaplan, Emma Sargent, Hansen Guo, Abdur Khan, Matias Bermudez
Social Networks Group 3
Professor B. Mishra
15 December 2020 
Abstract 
	Many studies have been done on lockdowns (because of COVID-19) and their effect on death rate, however, as this is an evolving subject, a lot of questions are still unanswered. We use data collected from all across the US regarding COVID deaths by county, state, and region, nursing home deaths, unemployment rate, homicide rates, suicide rates, drug overdose rates, and US Census data in order to determine changes in death rate pretaining to lockdowns. We can assert that lockdowns decrease death rates, however, none of the data we looked at was significant or correlated enough to determine causation. Our findings were too weak to make any claims, we recommend that in the future, as this is an ongoing event, that more specific components of lockdowns are looked at in order to determine what slows the spread and decreases death caused by the virus. 
Intro-Hypotheses: 
The year 2020 experienced a multitude of world-shifting events and hardships. From major social justice movements, to deadly wildfires, to even murder hornets, this span of twelve months has been deemed the worst year ever by many major news outlets. At the top of the list of the most monumental challenges faced in this past year sits the Covid-19 Pandemic. Covid-19 is a respiratory illness caused by the virus SARS-CoV-2. The first cases of Covid-19 were observed December 30, 2019, with patients in Wuhan, China showing symptoms of pneumonia. However, the causes to how the virus became transmissible to humans are currently under review. The first case of Covid-19 in the United States was diagnosed in January of 2020. As of November 30, 2020, there have been 13,29,605 cases of this disease with 266,051 deaths in the United States alone. In addition to severe health threats, Covid-19 has caused a global economic recession due to mass closing of businesses during the preventative lockdown. As of October 2020, 15.1 million Americans were unemployed due to closed or lost business. Before deep analysis of data detailing each state’s lockdown scores, rankings, death rates, and unemployment rate, a prediction can be suggested that lockdowns will decrease death rates in the United States.

Related Literature 
We want to evaluate the effectiveness and harms of lockdown regulations as a non-pharmaceutical intervention for Covid-19 transmission in the U.S. The COVID-19 pandemic forced the world’s population to alter daily routines, and this unusual situation has physical, psychological, and behavioral consequences to all individuals and has long-term impact on life expectancy. Past research on associations between deaths and lockdowns related to the severe acute respiratory syndrome (SARS) pandemic in 2003 and associations between deaths and recession/large scale unemployment are helpful to form our current analysis for COVID-19. 

Gupta et al. (2004) studied the economic impact of quarantine for SARS in Toronto by comparing the costs of two outbreak scenarios: SARS transmission with and without public health interventions. Costs include healthcare, loss of productivity, and mortality for scenarios without intervention and additional administrative and operating costs for scenarios with intervention. Assuming the transmission rate of infection as 0.08, when the quarantine measure was implemented at the second wave of spread, Toronto would save $274 million, which showed quarantine was cost-saving and life-saving. This study provided an overall understanding of the economics, but the effects only included direct costs associated with illness and quarantine and didn't consider indirect costs for non-SARS patients. 

Strumpf et al. (2017) estimated the impacts of increases in unemployment rates on both all-cause and cause-specific mortality across U.S. metropolitan regions during the 2008 recession. Although mortality rates generally decline during economic recessions in high-income countries, the study specifically found that a 1% increase in the metropolitan area unemployment rate was associated with a decrease in all-cause mortality of 3.95 deaths per 100,000 person years (95%CI -6.80 to -1.10), or 0.5% using fixed effects regression models. Motor vehicle accident mortality declined with unemployment increases and accidental drug poisoning deaths increased with employment increases for both men and women ages 25-64. In our analysis, we would like to consider the associations between mortality and unemployment rates nationwide, not just limited to metropolitan areas. 

We also looked at current studies, and one of them is Atalan’s (2020) analysis of the associations between lockdown days and total cases of COVID-19 by countries. It found that the lockdown days in 49 countries were significantly correlated with COVID-19 cases with the unconstrained correlation value as −0.9126. In our current study, we also used correlation to explore the impact of lockdowns on people’s life expectancy. However, we chose to use Covid-related deaths instead of Covid-19 cases, because it's a more accurate and reliable metric as at the beginning of the outbreak, testing was very limited. 

MVP:
For our methodology, we decided to do correlation analysis on our different parameters to seek out potential correlations to prove our hypothesis. We calculated the correlation with the equation:
 
Where x and y are the two parameters, and n is the number of data points.

	With the correlations, we want to find out whether the correlation is significant and we did not get the correlation just by chance. To do that, we went ahead and found the p-value of the correlation through a hypothesis test with the null hypothesis being “There is no correlation between the two variables.” The p-value is calculated by finding a t-distribution with n – 2 degrees of freedom, which can be found with the following equation:

 
Where r is the correlation, and n is number of data points we have. With the p-value, we can go ahead to reject or fail to reject the null hypothesis.

	Most of our data for the project, including state-by-state death rates, death rate by age groups, suicide rate and drug related death rate came from the Center of Disease Control and Prevention. Other than that, we used the state population data from the U.S. census bureau, lockdown scores from the Wallethub, murder and homicide rates from Macrotrends and nursing home data from Centers for Medicare & Medicaid Services.

Data Analysis:
We Fail to Show Density Causes Higher COVID-19 Deaths: 
For the state data, we made some assumptions that turned out to be inaccurate later in the project. One of these assumptions was that density caused Covid-19 deaths to increase. When we plotted this chart we saw a clear correlation between density and Covid-19 deaths. However, the chart did not appear to have a normal distribution, and several highly dense Northeast states pulled up the curve. We determined that the state by state density charts could not be used because there was not a normal distribution. 
We further investigated by plotting correlation between COVID-19 deaths and densities by county.  This too proved to be an inaccurate method to find a normal symmetric distribution because there were many outliers with a small sample size that had a very high number of COVID-19 deaths per 100,000. To solve this problem we combined all the counties that had a population of less than 100,000 and plotted them on a chart. After this there were 28 very dense cities that were outliers, so we removed those. This gave us a symmetric normal distribution that we could analyze. The results were shocking. 
We plotted 982 counties or combined counties of different densities in the United States and found that the correlation between COVID-19 deaths per 100,000 and county density was -0.01213 (Fig 1). This had a p-value of 0.85 which is greater than 0.05, so we failed to show that there was a relationship between density and COVID-19 deaths.
State Data Fails to Show Lockdowns Work:
We interpreted if the lockdowns work at a state level using three different metrics. The first metric was COVID-19 deaths per 100,000 (Fig 2)  and the second metric was the maximum weekly COVID-19 deaths per 100,000 (Fig 3) which gave us an idea if lockdowns flattened the curve. The third metric we used was excess death rates per 100,000 which is the 2020 death rate minus the 2019 death rate per 100,000 (Fig 4). The third was used to determine if COVID-19 deaths were increasing or decreasing due to the lockdowns. None of these charts had p-value greater than 0.05, so we concluded that the charts failed to show lockdowns were correlated with Non-COVID-19 deaths or COVID-19 deaths. 
County Data Shows Lockdowns Work:
	The country data with the North-East showed there was a weak correlation between lockdowns and deaths per 100,000 (Fig 5)). The P-value was 0.0478 which shows the lockdowns did work to reduce deaths. This is Simpson's paradox because the state data did not show this. However, the p value for the maximum daily death was not significant (Fig 6). We believe that the reason is that the Northeast got hit the hardest. This is shown in the state geographical maps (Fig 7 and Fig 8).
	When we take out the Northeast states it appears probable that lockdowns both reduced both total COVID-19 death rates (Fig 9) and maximum daily COVID-19 death rates (Fig 10). The total COVID-19 death rate had a p-value of 0.00000002 and the maximum daily death rate had a p-value of 0.00003501. If you used the regression line to predict deaths, you would find that lockdowns could reduce deaths by up to a third. However, there is a weak correlation between lockdowns and death rates so that would be a weak predictor.
The North East didn’t do bad because of Nursing Homes:
The North East did bad in nursing homes but that is only because they did bad across the board. The North East did not have more COVID-19 deaths because they had more nursing home deaths. They had more nursing home deaths because they had more COVID-19 deaths (Fig 11). Fig 11 shows that as COVID-19 deaths rise nursing home deaths also rise. 
Don’t Believe New York's Nursing home Data:
If you look at New York’s nursing home data you can see that they are a big outlier. Their data have a 1 in 5,000,000 chance of happening by random variation. This is not due to random variation; it is due to the fact that they only report a nursing home death if the patient died within a nursing home. We can project the deaths and be 95% confident that their actual nursing home death rate is between 10.7% and 15.3% (Fig 12).
Age of Death Data Wasn’t Important:
	We looked at the average COVID-19 age of death and average age of death for each state. We made a correlation matrix (Fig 14) to see if it was correlated to anything. The age of death data wasn’t significantly correlated to anything, so we decided it was not important to investigate. 
Lockdowns are Correlated with Unemployment:
Although lockdowns don’t appear to cause death they are correlated to unemployment (Fig 15). The associated p-value was 0.00009355. 
2008 Recession Data Shows Unemployment doesn’t increase Death:
Given we don’t have categorical death rates for the current pandemic, we looked at the 2008 recession to see if lockdowns increased drug overdose rates, homicide rates, accident deaths, all deaths, or suicide rates. We looked at both the yearly percent increase in these death rates and the total death rates and did not find any of these death rates to be correlated with unemployment rates. (Fig 16-20)
Despite there not being a correlation with these things, the news reported the events differently at the time of the event. In 2008, the news reported that the recession caused countless suicides and increased suicide rates. This was before the data was released. Once the data was released it was too late to convince people that unemployment rates rising is not associated with an increase in suicide rates in the United States. It is possible the same thing is happening here in 2020 where the media is reporting an increase in suicide rates without any data to back it up. Nonetheless, there could be reason to believe they are rising. 
If you look at Japan, you can see that suicide rates are rising since the lockdowns started. However, Japan has a very different culture and their death data cannot be applied to the United States. In conclusion, we don’t know what is happening to these specific death rates in the pandemic. 
Conclusion:
	We can conclude that lockdowns likely decreased the death rates in the United States. However, the data we have collected is not sufficient for us to make a recommendation on whether states should or should not lock down again. The correlation between lockdowns and death rates were weak, which means the level of lockdown is not a good predictor of how many people will die in that state. Moreover, in this paper we show correlations, which does not mean causation, so we will leave the recommendations up to the scientists. Going forward, we would recommend states investigate which individual aspects of lockdowns work on a county by county basis. For example, a study could be done on if mask mandates, restaurant closures, or school closures are effective ways to slow the spread in the United States on a county by county basis. Additionally, we recommend that states release homicide rates, drug overdose rates, and suicide rates, so we can be more sure that lockdowns are not causing those number to increase. Moreover, there should be an investigation into why the northeast did so poorly. We can conclude that it was not due to density or nursing home failures. Data is key to figuring out what methods work for reducing the spread in the pandemic, so we recommend that states release all their data so that data scientists can figure out what works and what doesn’t work for slowing the spread.


 
Appendix: 

Use your NYU email to get access to the following:

To access to all interactive charts and code go to:
https://colab.research.google.com/drive/1YLWn0rhJ_jaHmSY7bD5fWRDfFVClrLvS?usp=sharing

To run the code you must upload the filed found here:
https://drive.google.com/drive/folders/1zenRGyU1tci7yD82Jm1-QN7m58f_5eq7?usp=sharing

Only the most important charts are shown below:

Fig 1:
 
Fig 2:
 
Fig 3:
 
Fig 4:
 
Fig 5:
 
Fig 6: Fig 7:
 
Fig 8:
 
Fig 9:
 
Fig 10:
 



Fig 11:
 
Fig 12:
 
Lower Bound: 433.945+59.966(171.074077)=10692.5731 Nursing Home Deaths per 100,000
Upper Bound: 1747.794+78.994(171.074077)=15261.6196 Nursing Home Deaths per 100,000

Fig 14:
 
Fig 15:
 




Fig 16:
 



Fig 17:
 
Fig 18:
 
Fig 19:
 
Fig 20:
  
Works Cited

(n.d.). Retrieved December 11, 2020, from      https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
Annual Unemployment Rates by State. (n.d.). Retrieved December 11, 2020, from https://www.icip.iastate.edu/tables/employment/unemployment-states
Atalan, A. (2020). Is the lockdown important to prevent the COVID-19 pandemic? Effects on psychology, environment and economy-perspective. In Annals of Medicine and Surgery (Vol. 56, pp. 38-42). doi:https://doi.org/10.1016/j.amsu.2020.06.010
Bureau, U. (2019, December 30). State Population Totals: 2010-2019. Retrieved December 11, 2020, from https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html
Center for Disease Control and Prevention. (2015, December 2). NCHS - Leading Causes of Death: United States. Retrieved December 11, 2020, from https://data.cdc.gov/NCHS/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu
Center for Disease Control and Prevention. (2019). Drug Overdose Deaths in the United     States. Retrieved December 11, 2020, from https://www.cdc.gov/nchs/data/databriefs/db329_tables-508.pdf#page=3
Center for Disease Control and Prevention. (2020, April 21). Weekly Counts of Deaths by State and Select Causes, 2019-2020. Retrieved December 11, 2020, from https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/muzy-jte6
Center for Disease Control and Prevention. (2020, May 1). Provisional COVID-19 Death Counts by Sex, Age, and State. Retrieved December 11, 2020, from https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku
Center for Medicare & Medicaid Services. (2020, May 26). COVID-19 Nursing Home Dataset. Retrieved December 11, 2020, from https://data.cms.gov/Special-Programs-Initiatives-COVID-19-Nursing-Home/COVID-19-Nursing-Home-Dataset/s2uc-8wxp
Devin Michelle Bunten - DATA. (n.d.). Retrieved December 11, 2020, from https://www.devinbunten.com/data
Gupta, A. G., Moyer, C. A., & Stern, D. T. (2005). The economic impact of quarantine: SARS in Toronto as a case study. The Journal of infection, 50(5), 386–393. https://doi.org/10.1016/j.jinf.2004.08.006
List of states and territories of the United States by population density. (2020, December 03). Retrieved December 11, 2020, from https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population_density
McCann, A. (2020, October 06). States with the Fewest Coronavirus Restrictions. Retrieved December 11, 2020, from https://wallethub.com/edu/states-coronavirus-restrictions/73818
Strumpf, E. C., Charters, T. J., Harper, S., & Nandi, A. (2017). Did the Great Recession affect mortality rates in the metropolitan United States? Effects on mortality by age, gender and cause of death. Social science & medicine (1982), 189, 11–16. https://doi.org/10.1016/j.socscimed.2017.07.016
U.S. Murder/Homicide Rate 1990-2020. (n.d.). Retrieved December 11, 2020, from https://www.macrotrends.net/countries/USA/united-states/murder-homicide-rate
Unemployment Rates for States. (2020, November 20). Retrieved December 11, 2020, from https://www.bls.gov/web/laus/laumstrk.htm

























![image](https://user-images.githubusercontent.com/108026776/175179647-3bcdaf82-1f83-4d87-82ca-5e4cd91e1df7.png)
