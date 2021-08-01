--drop table if exists covid_data;
drop table if exists countries;
/*
create table covid_data (
	loc_code								varchar(10),
	continent								varchar(20),
	location								varchar(50),
	date									date,
	total_cases								numeric,
	new_cases								numeric,
	new_cases_smoothed						numeric,
	total_deaths							numeric,
	new_deaths								numeric,
	new_deaths_smoothed						numeric,
	total_cases_per_million					numeric,
	new_cases_per_million					numeric,
	new_cases_smoothed_per_millon			numeric,
	total_deaths_per_million				numeric,
	new_deaths_per_million					numeric,
	new_deaths_smoothed_per_million			numeric,
	reproduction_rate						numeric,
	icu_patients 							numeric,
	icu_patients_per_million				numeric,
	hosp_patients 							numeric,
	hosp_patients_per_million 				numeric,
	weekly_icu_admissions 					numeric,
	weekly_icu_admissions_per_million		numeric,
	weekly_hosp_admissions 					numeric,
	weekly_hosp_admissions_per_million		numeric,
	new_tests 								numeric,
	total_tests								numeric,
	total_tests_per_thousand				numeric,
	new_tests_per_thousand 					numeric,
	new_tests_smoothed 						numeric,
	new_tests_smoothed_per_thousand			numeric,
	positive_rate							numeric,
	tests_per_case							numeric,
	tests_units§							varchar(20),
	total_vaccinations 						numeric,
	people_vaccinated 						numeric,
	people_fully_vaccinated 				numeric,
	new_vaccinations 						numeric,
	new_vaccinations_smoothed 				numeric,
	total_vaccinations_per_hundred 			numeric,
	people_vaccinated_per_hundred 			numeric,
	people_fully_vaccinated_per_hundred 	numeric,
	new_vaccinations_smoothed_per_million 	numeric,
	stringency_index						numeric,
	population 								numeric,
	population_density						numeric,
	median_age								numeric,
	aged_65_older							numeric,
	aged_70_older							numeric,
	gdp_per_capita							numeric,
	extreme_poverty							numeric,
	cardiovasc_death_rate					numeric,
	diabetes_prevalence						numeric,
	female_smokers							numeric,
	male_smokers 							numeric,
	handwashing_facilities 					numeric,
	hospital_beds_per_thousand 				numeric,
	life_expectancy 						numeric,
	human_development_index					numeric,
	excess_mortality						numeric,
	constraint primary_key primary key(loc_code,date)
);
*/
create table countries (
	CountryCode									char(3) primary key,
	ShortName									varchar(30),
	TableName									varchar(30),
	LongName									varchar(60),
	Alpha2Code									char(2),
	CurrencyUnit								varchar(255),
	SpecialNotes								varchar(511),
	Region										varchar(255),
	IncomeGroup									varchar(255),
	Wb2Code										char(2),
	NationalAccountsBaseYear					varchar(255),
	NationalAccountsReferenceYear				varchar(127),
	SnaPriceValuation							varchar(255),
	LendingCategory								varchar(10),
	OtherGroups									varchar(10),
	SystemOfNationalAccounts					varchar(255),
	AlternativeConversionFactor					varchar(10),
	PppSurveyYear								varchar(127),
	BalanceOfPaymentsManualInUse				varchar(255),
	ExternalDebtReportingStatus					varchar(10),
	SystemOfTrade								varchar(255),
	GovernmentAccountingConcept					varchar(255),
	ImfDataDisseminationStandard				varchar(255),
	LatestPopulationCensus						varchar(255),
	LatestHouseholdSurvey						varchar(255),
	SourceOfMostRecentIncomeAndExpenditureData	varchar(255),
	VitalRegistrationComplete					varchar(10),
	LatestAgriculturalCensus					varchar(255),
	LatestIndustrialData						varchar(127),
	LatestTradeData								varchar(127),
	LatestWaterWithdrawalData					varchar(127)
);
