from flask import Flask, render_template, url_for, request, make_response
import feedparser
import requests
import json
import pickle
import pandas as pd
import random
from time import sleep
import os
import time
import re
import sklearn
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer
import statsmodels.api as sm
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.decomposition import PCA
import numpy as np
import csv
import sys
import lxml
import spicy
from scipy.stats import norm
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from bs4 import BeautifulSoup
import spacy
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib
from spacy.lang.en import English
import seaborn as sns 
os.system("clear")

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
@app.route('/collegeRank', methods = ['GET', 'POST'])
def collegeRank():
	staticSaveFigText = "Add Chart Here"
	textForChart = ""
	matplotlib.use('Agg')
	matplotlib.rcParams.update({'font.size': 6})
	nlp = spacy.load("en_core_web_lg")
	badSpacy = nlp("""Son's death by suicide in college prompts mom's activism.
	 College student accused of. 
	students so stressed they consider suicide. College student charged in boyfrien
	d's suicide. student's suicide prompts concern about mental. Boston College 
	Student Pleads Guilty to Manslaughter. What Student Accused Of Boyfriend 
	Suicide Texts Reveal. College student texted 'go die' to boyfriend 
	Suicide risk is high. Girlfriend Indicted in College Student's Suicide
	College student accused of urging boyfriend in. charged over her suicide
	grapples with string of suicides. Gunfire erupts at vigil for two killed at 
	off-campus college. school board member killed in.  student killed in shooting
	Two dead, more than a dozen injured at. Man killed missing. Man charged in 
	death of. shootings. student killed in apartment complex shooting. 2 killed, 
	4 injured in shooting. Missing student found dead. 1 dead, 10 injured after 
	violent attack at. Arrest made. Violence on College Campuses. There is crime.
	Dating and Domestic Violence on College Campuses. Campus Sexual Violence. 
	evidence of widespread sexual violence. Crimes on campus. College-Crime Reports 
	Are Breaking Records. America's Most Dangerous Universities. Illinois college 
	student charged with hate crime colleges reported several violent crimes
	College student accused of sexual. refused to investigate rape. These colleges 
	have the most reports of rape. 12 arrested in connection with alleged rapes.
	12 men arrested in statutory rape. A dangerous school. Drug overdoses 
	probed in USC student deaths. Possible drug overdoses, tainted. Student 
	Deaths Possibly Linked to Drug Overdoses. 4 of 9 deaths this semester 
	are suspected overdoses. Overdose death of senior hits home
	Man Dies, Woman Hospitalized After Fentanyl Overdose
	There Is a Mental-Health Crisis on Campus. The College Student Mental 
	Health Crisis. A mental health crisis on campus. As Students Struggle With 
	Stress and Depression. The Crisis in College and University Mental Health
	A Mental Health 'Epidemic' Among College Students. Rising suicide rates at 
	college campuses prompt concerns. The Kids are Not Alright: The Mental Health 
	Crisis on College. University student mental health care is at the 
	tipping point. Immediate Mental Health Crisis. Depression Among College 
	Students. Student arrested. police arrest students for. Student arrest matter 
	is troubling. Student charged with threatening, fighting. Police Arrest 
	Suspects in Robbery. student arrested after allegedly threatening. 
	Homelessness among college students is a growing crisis. Homeless college 
	students struggle to continue their education. Hunger And Homelessness Are 
	Widespread. The disturbing trend of homeless community college students
	Asian Americans are rightly angry about racism. Campus Racism.
	There have been at least 5 hate incidents reported on college. 
	Manifesto, racism sparks fear among students on. Colleges are mishandling 
	racial tensions on campus. protests and criticism of racist incidents on 
	college campus. College Admissions Scandal Shows Racism. experiences with 
	everyday forms of racism. Racism on a college campus. Students are bring
	 cripled with debt. Student can barely make enough to survive. College 
	 admissions scandal. college admissions bribery scandal. More Parents 
	 Plead Guilty in College Admissions Scandal. College admissions 
	 cheating scandal: 12th parent sentenced. 10th parent in college 
	 admissions scandal sentenced. Parents cry desperate times in college 
	 admissions scandal. New charges in college admissions scandal affect 
	 11 parents. Father Gets 6 Months In Jail In College Admissions Scandal
	 New College Scandal Jail Sentence Is The Longest So Far. 
	  pleads not guilty to new charges in college. Prosecutors 
	 threaten to add charges in college admissions. parent sentenced to 6 
	 months in prison for college.  College Cheating Scandal. There were real 
	 victims in the admissions scandal. Mom files $500B lawsuit over college 
	 admissions scandal. College bribery scandal: Mom sues. $500 Billion 
	 Lawsuit Filed. 14 more rejected students file class-action suit against.
	 Students and parents file lawsuit in college. Lawyer attempts first-ever 
	 class action lawsuit for college. Students target colleges in 
	 lawsuit over bribery scheme. Lawsuit over student's alcohol-related death.
	 New lawsuit filed against. Discrimination lawsuit against College. 
	 defamation lawsuit verdict to pay. Jeffrey Epstein: The financier charged 	
	 with sex trafficking. College Student Expelled After Racist Rant Goes Viral
	 Student Expelled. She was expelled from college after her racist rants went 
	 viral. Woman sues college after they expelled her. The school recieves 
	 backlash""") 
	goodSpacy = nlp("""college football team ranked number one in the nation. College
	football team wins the championships. A Nobel Prize winner graduated.
	Awarded a nobel prize. Academic scholar. Donates serveral million dollars.
	landmark $20 million donation. receives largest private donation. Receives 
	Largest Donation in School History. $15 Million Donation To  
	College Will Fund. Family makes $6 million donation. colleges offer free 
	tuition. surprises college students with free tuition. Free College Tuition for 
	offers free tuition to Detroit teens who graduate high school. awarded 	
	prestigious Scholarship. student seeks to use scholarship to. receives 
	$3 million for scholarships. University professor receives grant for research.
	awarded additional $2.7 million research. recognized in 
	student-focused research. wins fellowship to study. senior awarded Rhodes 
	Scholarship. receives prestigious national award. receive awards to fund 
	research equipment. awarded Faculty Award. National award honors University's 
	exceptional. honor three with prestigious. Success for University 
	undergraduates at prestigious awards. University student awarded 
	foreign service graduate fellowship. Researchers discover what's behind.
	The schools devision 1 football team. they win another prise. This school
	 has an outstanding global program. The facalty is outstanding. """) 
	badExpression = r"""\d* ([\S]*death[\S]*|[\S]*deaths[\S]*|[\S]*fatality[\S]*|
	[\S]*fatalities[\S]*|[\S]*suicide[\S]*|[\S]*kill[\S]*|[\S]*murder[\S]*|
	[\S]*violence[\S]*|[\S]*gun[\S]*|[\S]*cheating[\S]*|[\S]*cheat[\S]*|
	[\S]*corrupt[\S]*|[\S]*guilty[\S]*|[\S]*fire[\S]*|[\S]*drug[\S]*|
	[\S]*overdose[\S]*|[\S]*depressed[\S]*|[\S]*expensive[\S]*|
	[\S]*shoot[\S]*|[\S]*shooting[\S]*|[\S]*court[\S]*|[\S]*epstein[\S]*|
	[\S]*sue[\S]*|[\S]*lawsuit[\S]*|[\S]*missing[\S]*|[\S]*protest[\S]*|
	[\S]*sexual[\S]*|[\S]*assault[\S]*|[\S]*robbery[\S]*|[\S]*guilty[\S]*|
	[\S]*arrest[\S]*|[\S]*arrested[\S]*|[\S]*fraud[\S]*|[\S]*scandal[\S]*|
	[\S]*scandal[\S]*|[\S]*allegation[\S]*|[\S]*violation[\S]*|
	[\S]*depression[\S]*|[\S]*homeless[\S]*|[\S]*hazard[\S]*|[\S]*suspend[\S]*|
	[\S]*suffer[\S]*|[\S]*attack[\S]*|[\S]*danger[\S]*|[\S]*panic[\S]*|
	[\S]*legal[\S]*|[\S]*hypocrisy[\S]*|[\S]*accused[\S]*|[\S]*plead[\S]*|
	[\S]*expel[\S]*|[\S]*rape[\S]*|[\S]*hate[\S]*|[\S]*debt[\S]*|[\S]*arrest[\S]*|
	|[\S]*crime[\S]*|[\S]*charge[\S]*|[\S]*boycott[\S]*|[\S]*dissapear[\S]*|
	[\S]*racist[\S]*|[\S]*marijuana[\S]*)""" 
	goodExpression = r"""\d* ([\S]*scholarship[\S]*|[\S]*football[\S]*|
	[\S]*fun[\S]*|[\S]*sports[\S]*|[\S]*diverse[\S]*|[\S]*research[\S]*|
	[\S]*reunion[\S]*|[\S]*donation[\S]*|[\S]*change[\S]*|[\S]*global[\S]*|
	[\S]*sustainable[\S]*|[\S]*gift[\S]*|[\S]*contribution[\S]*|
	[\S]*athletic[\S]*|[\S]*academic[\S]*|[\S]*win[\S]*|[\S]*beat[\S]*|
	[\S]*study[\S]*|[\S]*record[\S]*|[\S]*victory[\S]*|[\S]*victories[\S]*|
	[\S]*award[\S]*|[\S]*elite[\S]*|[\S]*division\s1[\S]*|[\S]*upgrade[\S]*|
	[\S]*ivy\sleague[\S]*|[\S]*dream[\S]*|[\S]*free[\S]*|[\S]*scholar[\S]*|
	[\S]*award[\S]*)"""
	# Get Text For Google News Search 
	def fixTextToGoogleLink(myText):
		ogURL = "https://news.google.com/search?q="
		urlCounter = 0
		textList = myText.split()
		for text in textList:
			if urlCounter == 0:
				urlCounter = 1
				ogURL = ogURL + text
			else:
				ogURL = ogURL + "+" + text
		return(ogURL)
		
	# Get Text From URL
	def getTextFrom(url):
		textString = ""
		print(url)
		websiteInt = 0
		r = ""
		while r == "":
			try:
				sleep(1)
				r = requests.get(url, timeout=5)
				break
			except requests.exceptions.RequestException as e:
				print(e)
				print("ERROR GETTING SITE")
				if websiteInt < 3:
					print("Going to start again")
					sleep(1)
					websiteInt = websiteInt + 1
					continue
				else:
					print("failed skipping this site")
					r = "did not run."
		if websiteInt < 3:
			soup = BeautifulSoup(r.text,'html.parser') 
			for title in soup.find_all('title'):
				textString = textString + title.text
			for paragraph in soup.find_all('p'):
				textString = textString + paragraph.text
			print(textString)
			return textString
		else:
			return "C" 
			
	# Get Each Link From Google News
	def getNewsLinkList(url):
		urlList = []
		r = requests.get(url)
		soup = BeautifulSoup(r.text,'html.parser') 
		for unfilteredlink in soup.find_all('a'):
			link = unfilteredlink.get('href')
			if link is not None:
				if len(link) > 12 and link[0:11] == "./articles/":
					titleUrlString = "https://news.google.com" + link[1:]
					thisBool = 1 == 1
					for urlItemLink in urlList:
						if urlItemLink == titleUrlString:
							thisBool = 1 == 2
					if len(urlList) > 0 and thisBool:
						urlList.append(titleUrlString)
					elif len(urlList) == 0:
						urlList.append(titleUrlString)					
		return urlList
	
	# Adds Text To The Same File
	def getSiteText(url):
		myReturnText = ""
		for site in getNewsLinkList(url):
			myReturnText = myReturnText + getTextFrom(site)
		return myReturnText
	
	#Create Dictionary for Text Scraped
	def saveCollegeWordFile(myInput):
		try:  
			myDict = pickle.load(open("dictionaryFile.txt","rb"))
			myDict[myInput] = getSiteText(fixTextToGoogleLink(myInput))
			pickle.dump(myDict, open("dictionaryFile.txt", "wb"))
		except EOFError as e:
			print(e)
			print("Load again. File not found.")
		except FileNotFoundError as e:
			print(e)
			print("Load again. File not found.")
		
	# Rescore Colleges In Dictionary
	def getReScoreCollege(collegeName):
		saveCollegeWordFile(collegeName)
		scoreDict = {}
		myDict = pickle.load(open("dictionaryFile.txt","rb"))
		scoreDict = pickle.load(open("myScoreFile.txt","rb"))
		print(collegeName)
		collegeFullList = myDict[collegeName].lower()
		spacyDoc = nlp(collegeFullList)
		spacyBad = float(spacyDoc.similarity(badSpacy))
		print(spacyBad)
		spacyGood = float(spacyDoc.similarity(goodSpacy))
		print(spacyGood)
		bWords = len(re.findall(badExpression, collegeFullList))
		print("Bad Words: " + str(bWords))
		gWords = len(re.findall(goodExpression, collegeFullList))
		print("Good Words: " + str(gWords))
		collegeScoreS = (float(spacyGood) - float(spacyBad)) / 0.03
		collegeScoreR = float(gWords) / ((float(bWords) * 3.0 ) + 100.0)
		print("collegeScoreS:" + str(collegeScoreS))
		print("collegeScoreR:" + str(collegeScoreR))
		collegeScore = float(collegeScoreS) + float(collegeScoreR) + 2.0
		print("collegeScore:" + str(collegeScore))
		scoreDict[collegeName] = float(collegeScore)
		open("myScoreFile.txt","w")
		pickle.dump(scoreDict, open("myScoreFile.txt", "wb"))
		return weighScoreDict()
		
	# Reload All Colleges In myCollege.txt
	def reloadAllCollegesDangerThisWillTakeDays():
		collegeRunList = pickle.load(open("myCollege.txt","rb"))
		myDump = collegeRunList
		for ent in collegeRunList:
			saveCollegeWordFile(ent)
			print("reloadPROGRESSIS THIS IS:")
			print(ent)
			myDump.remove(ent)
			pickle.dump(myDump, open("myCollege.txt", "wb"))
			newRandInt2 = random.randint(20,60)
			sleep(newRandInt2)

	# Rescore using Dictionary
	def scoreWillTakeHours():
		scoreDict = {}
		myDict = pickle.load(open("dictionaryFile.txt","rb"))
		for collegeName in myDict:
			print(collegeName)
			collegeFullList = myDict[collegeName].lower()
			parseCollegeList = collegeFullList
			pC = 1
			tSB = 0
			tSG = 0
			while len(parseCollegeList) > 999999:
				pC = pC + 1
				tempParse = nlp(parseCollegeList[0:1000000])	
				parseCollegeList = parseCollegeList[1000000:]
				tSB = (float(tempParse.similarity(badSpacy)) + float(tSB))
				tSG = (float(tempParse.similarity(goodSpacy)) + float(tSG))
			spacyDoc = nlp(parseCollegeList)
			spacyBad = (float(spacyDoc.similarity(badSpacy)) + float(tSB)) / float(pC)
			print(spacyBad)
			spacyGood = (float(spacyDoc.similarity(goodSpacy)) + float(tSG)) / float(pC)
			print(spacyGood)
			bWords = len(re.findall(badExpression, collegeFullList))
			print("Bad Words: " + str(bWords))
			gWords = len(re.findall(goodExpression, collegeFullList))
			print("Good Words: " + str(gWords))
			collegeScoreS = (float(spacyGood) - float(spacyBad)) / 0.03
			collegeScoreR = float(gWords) / ((float(bWords) * 3.0 ) + 100.0)
			print("collegeScoreS:" + str(collegeScoreS))
			print("collegeScoreR:" + str(collegeScoreR))
			collegeScore = float(collegeScoreS) + float(collegeScoreR) + 2.0
			print("collegeScore:" + str(collegeScore))
			scoreDict[collegeName] = float(collegeScore)
			open("myScoreFile.txt","w")
			pickle.dump(scoreDict, open("myScoreFile.txt", "wb"))
	
	# Weighs College Score and Rescores
	def weighNewScoreDict():
		maxScore = 0.01
		scoreWillTakeHours()
		unSDict = pickle.load(open("myScoreFile.txt","rb"))
		weightedDict = {}
		for university in unSDict:
			if float(unSDict[university]) > maxScore:
				maxScore = float(unSDict[university])
		for university in unSDict:
			weightedDict[university] = 100 * float(unSDict[university]) / float(maxScore)
		return weightedDict

	# Weighs College Score
	def weighScoreDict():
		maxScore = 0.01
		unSDict = pickle.load(open("myScoreFile.txt","rb"))
		weightedDict = {}
		for university in unSDict:
			if float(unSDict[university]) > maxScore:
				maxScore = float(unSDict[university])
		for university in unSDict:
			weightedDict[university] = 100 * float(unSDict[university]) / float(maxScore)
		return weightedDict

	# Return Survey
	def getsurvey():
		print("TEST")
		return survey()

	# Print Everything in College and Dict
	def printCollegeAndDict():	
		myDictx = pickle.load(open("dictionaryFile.txt","rb"))
		dictSize = 0
		for entX in myDictx:
			print(entX)
			print(dictSize)
			dictSize = dictSize + 1
		print("NOW PRINTING COLLEGE LIST")
		collegeDict = pickle.load(open("myCollege.txt","rb"))
		collSize = 0
		for coll in collegeDict:
			print(coll)
			print(collSize)
			collSize = collSize + 1
	
	# Create Data Frame
	def getDataFrame():
		collegeScoreDict, sRL = getData()
		df = pd.DataFrame(collegeScoreDict, columns=['College','News Score'])
		df = df.sort_values(by=['News Score'], ascending=False)
		df['Rank'] = sRL
		df = df.set_index('Rank')
		return df
		
	# Edit Data In DF
	def getData():
		dataFrameDict = weighScoreDict()
		collegeList = []
		dataScoreList = []
		sideRank = 0
		sideRankList = []
		for dataCollege in dataFrameDict:
			sideRank = sideRank + 1
			collegeList.append(dataCollege)
			dataScoreList.append(dataFrameDict[dataCollege])
			sideRankList.append(sideRank)
		collegeScoreDictionary = { "College" : collegeList, "News Score" : dataScoreList }
		return collegeScoreDictionary, sideRankList
	
	# Create HTML File
	def dfToHTML():
		htmlDF = getDataFrame()
		htmlS = '''
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
				<title>News Ranker</title>
				<link rel="stylesheet" type="text/css" href="{myCSS}"/>
			</head>
			<body>
				<div id="top">
					<ol>
						<li>News Ranker</li>
						<li><a href="./survey/">Survey</a></li>
						<li><a href="./readAPI/">Interactive + Read API</a></li>
						<li><a href="./map/">Map</a></li>
					</ol>
				</div>
				<div id="marginleft">
				</div>
				<p id="first">The top college is {topC}</p>
				{table}
				<p id="notAtHome">Top 10 US News colleges relative to each other</p>
				<p><img src="{topPic}" alt="Not Home"/></p>
				<div>
					<form method="post" action="{mAction}">
						<fieldset>
							<legend>Make College Chart or Add/Remove Colleges</legend>
							<div>
								<br/>
								<label for="loadCollege" class="addCollege">Load New Colleges (Separate by commas)</label>
								<input type="text" name="loadCollege" id="loadCollege"/>
							</div>
							<div>
								<br/>
								<label for="deleteCollege" class="addCollege">Delete Colleges (Separate by commas)</label>
								<input type="text" name="deleteCollege" id="deleteCollege"/>
							</div>
							<div>
								<br/>
								<label for="makeChart" class="addCollege">Make New Chart (Separate by commas)</label>
								<input type="text" name="makeChart" id="makeChart"/>
							</div>
							<div class="buttonarea">
								<input type="submit" value="Run Program"/>
							</div>
						</fieldset>
					</form>
				</div>
				<p><img src="{myChartPic}" alt="Make New Chart" id="makeChart"/></p>
				<br/>
				<p id="notAtHome">Don't do this at home kids.</p>
				<p>I got blocked from US News from web scraping it.</p>
				<p><img src="{htmlPic}" alt="Not Home"/></p>
				<br/>	
			</body>
		</html>
		'''
		with open("templates/index.html", 'w') as writeT:
			writeT.write(htmlS.format(
			myCSS="{{ url_for('static', filename='main.css') }}",
			topC=htmlDF.at[1, 'College'], table=htmlDF.to_html(classes='News Rank'), 
			topPic="{{ url_for('static', filename='top10College.jpg') }}",
			mAction="{{ url_for('collegeRank') }}",
			myChartPic=staticSaveFigText,
			htmlPic="{{ url_for('static', filename='banned.jpg') }}",
			myAction="{{ url_for('collegeRank') }}"))	
	
	# Interactive
	if request.method == 'POST':
		try:
			data = request.form['loadCollege']
			textForChart = "Making a chart for the colleges: " + data
			dataList = data.split(",")
			for newCollegeX in dataList:
				if len(newCollegeX) > 1:
					getReScoreCollege(newCollegeX)
		except IOError as e:
			print(e)
			randomFiller = 4
		try:
			dataDelete = request.form['deleteCollege']
			dataDeleteList = dataDelete.split(",")
			fullDict = pickle.load(open("dictionaryFile.txt","rb")) 
			fullScoreDict = pickle.load(open("myScoreFile.txt","rb"))
			subInt = 0
			for newCollegeXDel in dataDeleteList:
				for i in range(len(fullScoreDict)): 
					if list(fullScoreDict.keys())[i-subInt].strip().lower() == newCollegeXDel.strip().lower():
						if list(fullScoreDict.keys())[i-subInt] in fullDict:
							del fullDict[list(fullScoreDict.keys())[i-subInt]]
						if list(fullScoreDict.keys())[i-subInt] in fullScoreDict:
							del fullScoreDict[list(fullScoreDict.keys())[i-subInt]]
							subInt = subInt + 1
			pickle.dump(fullDict, open("dictionaryFile.txt", "wb"))
			pickle.dump(fullScoreDict, open("myScoreFile.txt", "wb"))
		except IOError as e:
			print(e)
			randomFiller = 4
		try:
			chartScore = pickle.load(open("myScoreFile.txt", "rb"))
			makeChart = request.form['makeChart']
			newDict = {}
			if len(makeChart) > 1: 
				chartInt = 0
				makeChartList = makeChart.split(",")
				for chartCollege in makeChartList:
					for chartENT in chartScore:
						if chartCollege.strip().lower() == chartENT.strip().lower():
							chartInt = chartInt + 1
							newDict[chartENT] = chartScore[chartENT]
							break
				if chartInt > 0:
					figure(figsize=(10, 3))
					plt.bar(range(len(newDict)), list(newDict.values()), align='center')
					plt.xticks(range(len(newDict)), list(newDict.keys()))
					imageChangeInt = pickle.load(open("randomVariableFile.txt", "rb"))
					imageChangeInt = (imageChangeInt + 1)% 2
					pickle.dump(imageChangeInt, open("randomVariableFile.txt", "wb"))
					saveFigText = "static/customChart" + str(imageChangeInt) + ".png"
					saveFigTextStatic = "customChart" + str(imageChangeInt) + ".png"
					staticSaveFigText = "{{ url_for('static', filename='" + saveFigTextStatic + "') }}"
					plt.savefig(saveFigText)
		except IOError as e:
			print(e)
			randomFiller = 4
		dfToHTML()
		return render_template("index.html")
	dfToHTML()	
	return render_template("index.html")
		
@app.route('/survey/', methods = ['GET', 'POST'])
def survey():
	myHTMLEndResult = ""
	satIMGHTML = ""
	data = pd.read_csv(open('data.csv'))
	htmlPrintStr = ""
	try:
   		myPrintData
	except NameError:
		myPrintData = data
	def htmlsurvey():
		htmlsurvey = '''
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
				<title>Survey</title>
				<link rel="stylesheet" type="text/css" href="{myCSS}"/>
			</head>
			<body>
				<div id="top">
					<ol>
						<li><a href="../collegeRank">News Ranker</a></li>
						<li>Survey</li>
						<li><a href="../readAPI/">Interactive + Read API</a></li>
						<li><a href="../map/">Map</a></li>
					</ol>
				</div>
				<div id="marginleft">
				</div>
				<p  id="first">Survey</p>
				<div>
					<form method="post" action="{myAction}">
						<fieldset>
							<legend>College Survey</legend>
							<div>
								<br/>
								<label for="yourName" class="addCollege">What is your name?</label>
								<input type="text" name="yourName" id="yourName"/>
								<br/><br/>
								<label for="gpa" class="addCollege">What was your high school GPA?</label>
								<input type="text" name="gpa" id="gpa"/>
								<br/><br/>
								<label for="satACT" class="addCollege">Did you take the old SAT, new SAT or ACT?</label>
								<br/>
								<input type="radio" name="satACT" value="SAT"> SAT<br/>
								<input type="radio" name="satACT" value="ACT"> ACT<br/>
								<label for="score" class="addCollege">What was your score?</label>
								<input type="text" name="score" id="score"/>
								<br/><br/>
							</div>
							<br/><br/>
							<label for="Region" class="addCollege">Which region would you prefer?</label>
							<select name="Region">
  								<option value="0">No Preference</option>
  								<option value="1">California</option>
  								<option value="2">Northeastern</option>
  								<option value="3">Southern</option>
  								<option value="4">Mid-Western</option>
  								<option value="5">Western</option>
							</select>
							<br/>
								<label for="regionImportant" class="addCollege">On a scale of 1-10. How important is location to you?</label>
								<input type="text" name="regionImportant" id="regionImportant"/>
							<br/><br/>
							<label for="setting" class="addCollege">Which campus setting would you prefer?</label>
							<select name="setting">
  								<option value="0">No Preference</option>
  								<option value="1">Rural</option>
  								<option value="2">Town</option>
  								<option value="3">Suburb</option>
  								<option value="4">City</option>
							</select>
							<br/>
								<label for="settingImportant" class="addCollege">On a scale of 1-10. How important is this to you?</label>
								<input type="text" name="settingImportant" id="settingImportant"/>
							<br/><br/>
								<label for="importantAcademic" class="addCollege">On a scale of 1-100 (Add to 100). How important is academics to you?</label>
								<input type="text" name="importantAcademic" id="importantAcademic"/>
							<br/><br/>
								<label for="importantLife" class="addCollege">On a scale of 1-100 (Add to 100). How important is life and diversity to you?</label>
								<input type="text" name="importantLife" id="importantLife"/>
							<br/><br/>
								<label for="importantIndustry" class="addCollege">On a scale of 1-100 (Add to 100). How important is industry and employment to you?</label>
								<input type="text" name="importantIndustry" id="importantIndustry"/>
							<br/><br/>
							<label for="costTuition" class="addCollege">Which total cost would you prefer?</label>
							<select name="costTuition">
  								<option value="1">below 20,000</option>
  								<option value="2">20,000-40,000</option>
  								<option value="3">40,000-60,000</option>
  								<option value="4">60,000+</option>
							</select>
							<br/><br/>
								<label for="cost1" class="addCollege">On a scale of 1-10. How important is cost to you?</label>
								<input type="text" name="cost1" id="cost1"/>
							<br/><br/>
							<div class="buttonarea">
								<input type="submit" value="Run Program"/>
							<br/>
						</fieldset>
					</form>
				</div>
				{table}	
				<p><img src="{fig1}" alt="No Fig"/></p>
				<p><img src="{fig2}" alt="No Fig"/></p>
				<p><img src="{fig3}" alt="No Fig"/></p>
				<p><img src="{fig4}" alt="No Fig"/></p>
				{manyFig}
				{figX}
				<p><img src="{figY}" alt="No Fig"/></p>
				<p><u>Odds of acceptance:</u></p>
				<p>{htmlEnd}</p><br/><br/>
				<p> </p>
			</body>
		</html>
		'''
		with open("templates/survey.html", 'w') as writeT:
			writeT.write(htmlsurvey.format(
			myCSS="{{ url_for('static', filename='main.css') }}",
			table=myPrintData.to_html(classes='Survey Rank'),
			myAction="{{ url_for('survey') }}",
			fig1="{{ url_for('static', filename='fig1.png') }}",
			fig2="{{ url_for('static', filename='fig2.png') }}",
			fig3="{{ url_for('static', filename='fig3.png') }}",
			fig4="{{ url_for('static', filename='radar_combined.jpg') }}",
			manyFig=htmlPrintStr,
			figX=satIMGHTML,
			figY="{{ url_for('static', filename='CollegesAvgGPAvsYourGPA.jpg') }}",
			htmlEnd=myHTMLEndResult))
	if request.method == 'POST':
		try:
			yName = request.form['yourName']
			typeTest = request.form['satACT']
			thisScore = float(request.form['score'])
			thisGPA = float(request.form['gpa'])
			thisRegion = float(request.form['Region'])
			region_weight = float(request.form['regionImportant'])
			isImportantI = float(request.form['importantIndustry'])/100
			isImportantL = float(request.form['importantLife'])/100
			isImportantA = float(request.form['importantAcademic'])/100
			cost_val = float(request.form['costTuition'])
			campus_val = float(request.form['setting'])
			campus_weight = float(request.form['settingImportant'])
			cost_weight = float(request.form['cost1'])
			total_extra_credit_score = 0
			user_GPA_raw = thisGPA
			if typeTest == 'SAT':
				bool_SAT = True
				bool_ACT = False
				user_score = thisScore
			else:
				bool_SAT = False
				bool_ACT = True
				user_ACT_raw = thisScore
			divideBy = float(1/(isImportantI + isImportantL + isImportantA))
			print("setting equal to 100%")
			isImportantI = float(int(isImportantI * divideBy * 100))/100
			print(str(isImportantI * 100) + "%")
			
			isImportantL = float(int(isImportantL * divideBy  * 100))/100
			print(str(isImportantL * 100) + "%")
			isImportantA = float(int(100 - (100 * (isImportantL + isImportantI))))/100
			print(str(isImportantA * 100) + "%")
			if thisRegion == 0:
  				region_weight == 0.0 #no extra credit points if no preference
  				region_weight = float(region_weight)
			else:
  				total_extra_credit_score = total_extra_credit_score + region_weight
			if campus_val == 0:
  				campus_weight == 0.0 #no extra credit points if no preference
  				campus_weight = float(campus_weight)
			else:
				total_extra_credit_score = campus_weight + total_extra_credit_score
			total_extra_credit_score = total_extra_credit_score + cost_weight
			
			data_filled = data.copy()
			data_filled_selected = data_filled.iloc[:,[3,11,12,14,15,16,30,42,37,17,20,21,22,23,24,25,27,31,32,33,41,35,18,38,39,43,2,3,5,6,7,8,9,10,34,26,36,40]]
			imp = IterativeImputer(RandomForestRegressor(), max_iter=10, random_state=0)
			data_filled_selected = pd.DataFrame(imp.fit_transform(data_filled_selected), columns=data_filled_selected.columns)
			for column_temp in data_filled_selected.columns:
				data_filled[column_temp] = data_filled_selected[column_temp]
			data_filled_aca = data_filled.iloc[:,[3,11,12,14,15,16,30,42,37]]
			data_filled_ind = data_filled.iloc[:,[17,20,21,22,23,24,25,27,31,32,33,41]]
			data_filled_lif = data_filled.iloc[:,[35,18,38,39,43]]
			data_filled_adm = data_filled.iloc[:,[2,3,5,6,7,8,9,10]]
			# conduct standard scaling before PCA
			scaler_aca = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True).fit(data_filled_aca)
			data_filled_aca_scale = pd.DataFrame(scaler_aca.transform(data_filled_aca))                               
			data_filled_aca_scale.columns = data_filled_aca.columns

			# conduct PCA for academics
			pca = PCA(n_components=1)
			data_aca_score = pca.fit_transform(data_filled_aca_scale)
			data_aca_score = (data_aca_score - np.min(data_aca_score)) / (np.max(data_aca_score) - np.min(data_aca_score))*100;
			
			# conduct standard scaling before PCA
			scaler_ind = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True).fit(data_filled_ind)
			data_filled_ind_scale = pd.DataFrame(scaler_ind.transform(data_filled_ind))                               
			data_filled_ind_scale.columns = data_filled_ind.columns

			# conduct PCA for industry
			pca = PCA(n_components=1)
			data_ind_score = pca.fit_transform(data_filled_ind_scale)
			data_ind_score = (data_ind_score - np.min(data_ind_score)) / (np.max(data_ind_score) - np.min(data_ind_score))*100;
			
			# conduct standard scaling before PCA
			scaler_lif = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True).fit(data_filled_lif)
			data_filled_lif_scale = pd.DataFrame(scaler_lif.transform(data_filled_lif))                               
			data_filled_lif_scale.columns = data_filled_lif.columns

			# conduct PCA for life
			pca = PCA(n_components=1)
			data_lif_score = pca.fit_transform(data_filled_lif_scale)
			data_lif_score = (data_lif_score - np.min(data_lif_score)) / (np.max(data_lif_score) - np.min(data_lif_score))*100;
			
			data_filled['Academics'] = data_aca_score
			data_filled['Career'] = data_ind_score
			data_filled['Life'] = data_lif_score
			
			data_filled_plot = data_filled.sort_values(by='US_News_Rank')

			# Creating trace1
			score_trace1 = go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['Academics'],mode = "lines",name = "Academic Score",marker = dict(color = 'rgba(324, 97, 98, 0.8)'),text= data_filled_plot['Name'])
			# Creating trace2
			score_trace2 = go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['Careers'],mode = "lines",name = "Industry Score",marker = dict(color = 'rgba(70, 120, 94, 0.8)'),text= data_filled_plot['Name'])
			# Creating trace3
			score_trace3 = go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['Life'],mode = "lines+markers",name = "Life and Diversity Score",marker = dict(color = 'rgba(50, 172, 230,0.8)'),text= data_filled_plot['Name'])

			score_data = [score_trace1, score_trace2,score_trace3]
			score_layout = dict(title = 'Fundamental Scores',xaxis= dict(title= 'Universities Rank',ticklen= 5,zeroline= False))
			score_fig = dict(data = score_data, layout = score_layout)
			# life_weight = 1/3
			# academic_weight = 1/3
			# industrious_weight = 1/3
			Basic_score = (data_aca_score*isImportantA + data_ind_score*isImportantI + data_lif_score*isImportantL)
			# we do the scoring on the extra credit part
			# campus_val = 4 # 0: no preference, 1: rural, 2: town, 3: suburb, 4: city
			# region_val = 1 # 0: no preference, 1: California, 2: Northeastern, 3: Southern, 4: Midwestern, 5: Western 
			# cost_val = 3  # 1: 20000-, 2: 20000-40000, 3:40000-60000, 4: 60000+
			# campus_weight = 5
			# region_weight = 5
			# cost_weight = 5

			if campus_val == 4:
				campus_matching = (data_filled['LOCALE']>=10) & (data_filled['LOCALE']< 20)
			elif campus_val == 3:
				campus_matching = (data_filled['LOCALE']>=20) & (data_filled['LOCALE']< 30)
			elif campus_val == 2:
				campus_matching = (data_filled['LOCALE']>=30) & (data_filled['LOCALE']< 40)
			elif campus_val == 1:
				campus_matching = (data_filled['LOCALE']>=40)
			elif campus_val == 0:
				campus_matching = (data_filled['LOCALE'] == '')	
			if thisRegion == 1:
				region_matching = (data_filled['Region'] == 'California')
			elif thisRegion == 2:
				region_matching = (data_filled['Region'] == 'Northeastern') 
			elif thisRegion == 3:
				region_matching = (data_filled['Region'] == 'Southern') 
			elif thisRegion == 4:
				region_matching = (data_filled['Region'] == 'Midwestern')
			elif thisRegion == 5:
				region_matching = (data_filled['Region'] == 'Western')
			elif thisRegion == 0:
				region_matching = (data_filled['Region'] == '')

			if cost_val == 1:
				cost_matching = (data_filled['Cost_of_Attendance'] <= 20000) 
			elif cost_val == 2:
				cost_matching = (data_filled['Cost_of_Attendance'] <= 40000) 
			elif cost_val == 3:
				cost_matching = (data_filled['Cost_of_Attendance'] <= 60000) 
			elif cost_val == 4:
				cost_matching = (data_filled['Cost_of_Attendance'] <= 1000000) 
				
			# we combine all sepcial requests with fundamental weights
			Special_score =  (campus_matching*int((campus_weight))) + (region_matching*(int(region_weight))) + (cost_matching* (int(cost_weight)))
			Combined_score = Basic_score.reshape(-1,) + Special_score
			
			# then we calculate the probability of getting in via GPA and SAT/ACT
			# user_GPA_raw = 3.9
			# user_score = 1450
			# test_type = "newSAT" #newSAT, oldSAT,ACT

			SAT_range = data_filled['SAT_75'] -  data_filled['SAT_25']
			SAT_mean = data_filled['SAT_AVG']
			SAT_sd = (SAT_range/(2*0.674)) 
			ACT_range = data_filled['ACTCM75'] -  data_filled['ACTCM25']
			ACT_mean = data_filled['ACTCMMID']
			ACT_sd = (ACT_range/(2*0.674))
			GPA_sd = data_filled['GPA'].std()
			GPA_mean = data_filled['GPA']
			# calculate the possibility of test score
			if (typeTest == "SAT") or (typeTest=="sat"):
				per_score = norm.cdf((float(thisScore)-SAT_mean)/SAT_sd)
			elif (typeTest == "ACT") or (typeTest == "act"):
				per_score = norm.cdf((float(thisScore)-ACT_mean)/ACT_sd)
			# calcualte the probability of GPA
			per_gpa = norm.cdf((float(thisGPA)-GPA_mean)/GPA_sd)
			per_combined = (per_gpa+per_score)/2
			pro_weighted_score = Combined_score * per_combined
			data_filled['pro_weighted_score'] = pro_weighted_score
			index_0_to_72 = np.array(range(72))
			data_filled['original_index'] = index_0_to_72
			data_filled_result = data_filled.sort_values(by='pro_weighted_score',ascending=False).copy()
			data_filled_result.reset_index(drop=True, inplace=True) # print this chart
			myPrintData = data_filled_result
			
			targeted_index = data_filled_result['original_index'][0]
			targeted_rank = data_filled['US_News_Rank'][targeted_index]
						
			# we first examine the school's academic ability via research ranking 	

			research_fig = go.Figure()
			research_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['THEResearch'],mode = "lines",name = "THE research scores",marker = dict(color = 'rgba(194,157,115,0.8)'),text= data_filled_plot['Name']))
			research_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['THECitations'],mode = "lines",name = "THE citation scores",marker = dict(color = 'rgba(150, 200, 0,1)'),text= data_filled_plot['Name']))
			research_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['QS_CITATIONS_PER_FACULTY'],mode = "lines",name = "QS citation scores",marker = dict(color = 'rgba(44, 160, 101,0.8)'),text= data_filled_plot['Name']))
			research_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['QS_ACADEMIC'],mode = "lines+markers",name = "qs academic reputation",marker = dict(color = 'rgba(255, 65, 54,0.5)'),text= data_filled_plot['Name']))


			research_fig.update_xaxes(title_text="Universities Rank")
			research_fig.update_yaxes(title_text="Score")


			research_fig.update_layout(title_text="Academic Reputation",showlegend=True,annotations=[go.layout.Annotation(x=targeted_rank,y=0,xref="x",yref="y",text=data_filled['Name'][targeted_index],showarrow=True,arrowhead=5,ax=0,ay=20)])
			
			research_fig.write_image("static/fig1.png")
			# then we examine the school's teaching quality and workload
			teaching_fig = make_subplots(specs=[[{"secondary_y": True}]])

			# Creating trace1
			teaching_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['Completion_for_150_Expected_Time'],mode = "lines",name = "completion for 150% expected time",marker = dict(color = 'rgba(324, 97, 98, 0.9)'),text= data_filled_plot['Name']),secondary_y = True,)

			teaching_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['Completion_for_200_Expected_Time'],mode = "lines",name = "completion for 200% expected time",marker = dict(color = 'rgba(255, 200, 136, 1)'),text= data_filled_plot['Name']),secondary_y = True,)

			teaching_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['THETeaching'],mode = "lines+markers",name = "THE teaching scores",marker = dict(color = 'rgba(61, 100, 94, 0.8)'),text= data_filled_plot['Name']),secondary_y = False,)

			# Add figure title
			teaching_fig.update_layout(title_text="Teaching and completion rate",annotations=[go.layout.Annotation(x=targeted_rank,y=0,xref="x",yref="y",text=data_filled['Name'][targeted_index],showarrow=True,arrowhead=5,ax=0,ay=20)])

			# Set x-axis title
			teaching_fig.update_xaxes(title_text="Universities Rank")

			# Set y-axes titles
			teaching_fig.update_yaxes(title_text="<b>primary</b> score", secondary_y=False)
			teaching_fig.update_yaxes(title_text="<b>secondary</b> percentage", secondary_y=True)
			teaching_fig.write_image("static/fig2.png")

			
			# we we examine the school's funding  
			funding_fig = go.Figure()

			funding_fig.add_trace(go.Scatter(x = data_filled_plot['US_News_Rank'],y = data_filled_plot['RnD_expenditures_2017'],mode = "lines+markers",name = "school research and development fundings in 2017",marker = dict(color = 'rgba(61, 100, 94, 0.8)'),text= data_filled_plot['Name']))
            

			funding_fig.update_xaxes(title_text="Universities Rank")
			funding_fig.update_yaxes(title_text="Thousands of USD")

			
			funding_fig.update_layout(title_text="Expenditures and Funding for R&D in 2017",showlegend=False,annotations=[go.layout.Annotation(x=targeted_rank,y=5,xref="x",yref="y",text=data_filled['Name'][targeted_index],showarrow=True,arrowhead=5,ax=0,ay=20)])
			funding_fig.write_image("static/fig3.png")
			
			
			best_index = data_filled_result['original_index'][:5]
			radar_data = list(zip(data_aca_score[best_index],data_ind_score[best_index],data_lif_score[best_index]))
			matplotlib.use('Agg')
			school = data_filled_result['Name'][:5]

			N = 3  
			angles=np.linspace(0, 2*np.pi, N, endpoint=False) 
			angles=np.concatenate((angles, [angles[0]]))
			try:
				fig = plt.figure(figsize=(7,7)) 
				ax = fig.add_subplot(111, polar=True) 
				sam = ['r-', 'o-.', 'g--', 'b-.', 'p:'] 
				lab = [] 
				for i in range(len(radar_data)):
					values = radar_data[i]
					feature = np.array([u"Life","Industrious",u"Academics"])
					values=np.concatenate((values,[values[0]]))
					ax.plot(angles, values, sam[i], linewidth=2) 
					ax.fill(angles, values, alpha=0.25) 
					ax.set_thetagrids(angles * 180/np.pi, feature) 
					ax.set_ylim(0, 100) 
					plt.title('colleges') 
					ax.grid(True) 
					lab.append(school[i])
				plt.legend(lab)
				plt.savefig("static/radar_combined.jpg") 
				plt.close(fig) 
			except:
				print("a")
			try:
				school = data_filled_result['Name'][:5]
				#stats=[20, 50, 95, 47, 56, 88]
				labels=np.array([u"Life","Industrious",u"Academics"])
				for i in range(len(radar_data)):
 					stats = radar_data[i]
 					angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
 					stats=np.concatenate((stats,[stats[0]]))
 					angles=np.concatenate((angles,[angles[0]]))
 					# Radar plot with Matplotlib
 					fig = plt.figure()
 					ax = fig.add_subplot(111, polar=True)
 					ax.plot(angles, stats, 'o-', linewidth=2)
 					ax.fill(angles,stats,alpha=0.25)
 					ax.set_thetagrids(angles * 180/np.pi, labels)
 					plt.title(school[i], fontdict=None, loc='center')
 					plt.savefig("static/radar"+str(i)+".jpg")
 					htmlPrintStr = htmlPrintStr + "<p><img src='{{ url_for('static', filename='radar" + str(i) + ".jpg') }}' alt='No Fig'/></p>"
 					plt.close(fig)
			except:
				print("b")
			try:
				if bool_ACT == True:
					satIMGHTML=""
					user_ACT_raw = int(user_score)
					schools_ACT = list(zip(data_filled_result[:5].iloc[:,9],data_filled_result[:5].iloc[:,8],data_filled_result[:5].iloc[:,10]))
					x = [0.25,0.5,0.75]
					y = [user_ACT_raw, user_ACT_raw,user_ACT_raw]
					lab = []
					for i in range(5):
						plt.plot(x,schools_ACT[i],'o-')
						lab.append(school[i])
					lab.append('Your Score')
					plt.plot(x,y,'--')
					plt.legend(lab)
					plt.title('Colleges ACT percentile vs Your score', fontdict=None, loc='center')  
				else:
					user_score = int(user_score)
					schools_SAT = list(zip(data_filled_result[:5].iloc[:,6],data_filled_result[:5].iloc[:,5],data_filled_result[:5].iloc[:,7]))
					x = [0.25,0.5,0.75]
					y = [user_score, user_score,user_score]
					lab = []
					for i in range(5):
						plt.plot(x,schools_SAT[i],'o-')
						lab.append(school[i])
					lab.append('Your Score')
					plt.plot(x,y,'--')
					plt.legend(lab)
					plt.title('Colleges SAT percentile vs Your score', fontdict=None, loc='center') 
					plt.savefig("static/CollegesSATpercentilevsYourscore.jpg")
					satIMGHTML = "<p><img src='{{ url_for('static', filename='CollegesSATpercentilevsYourscore.jpg') }}' alt='No Fig'/></p>"
					plt.close(fig)
			except:
				print("c")
			try:
				user_GPA_raw = float(user_GPA_raw)
				schools_GPA = data_filled_result[:5].iloc[:,3]
				x = [1,2,3,4,5]
				y = [user_GPA_raw for u in range(5)]
				lab1 = []
				plt.plot(x,y,'--')
				lab1.append('Your GPA')
				for j in range(5):
					plt.bar(x[j],schools_GPA[j])
					lab1.append(school[j])


					plt.legend(lab1)
					plt.title('Colleges Avg GPA vs Your GPA', fontdict=None, loc='center') 
					plt.savefig("static/CollegesAvgGPAvsYourGPA.jpg")
					plt.close(fig)
			except:
				print("d")
			result = list(zip(data_filled_result[:5].iloc[:,0],data_filled_result[:5].iloc[:,-2]))
			myHTMLEndResult = str(result)


			

			htmlsurvey()
		except IOError:
			print("PLEASE FILL IN ALL DATA")
			return render_template("survey.html")
		return render_template("survey.html")
        
	htmlsurvey()	
	return render_template("survey.html")	

@app.route('/readAPI/', methods = ['GET', 'POST'])
def readAPI():
	dataC = pd.read_csv(open('rankings.csv'))
	stateCol = ""
	costCol = "" #reading api
	url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'

	# and the rest are given on the website instructions


	#Here's me finding all the prominent schools' sizes. It's stored as a JSON
	parameters = {'school.degrees_awarded.predominant' : '2,3','fields' : 'id,school.name,2013.student.size', 'api_key' : 'rojBZbjMY38eM1icerh5VOSgHdVWWiFqjaYDUBkl'}
	resp = requests.get(url, params=parameters)
	data = resp.json()
	sizes = {}
	for i in range(len(data['results'])):
		size = data['results'][i]['2013.student.size']
		sizes[size] = data['results'][i]['school.name']

	maximum = sorted(sizes)[-1]
	apiStr = 'Read API:<br/>From reading the api (https://api.data.gov/ed/collegescorecard/v1/schools.json), I gathered that the largest college is ' + sizes[maximum] + ' with ' + str(maximum) + ' students'
	def htmlExtraData():
		htmlExtraData = '''
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
				<title>Interactive + Read API</title>
				<link rel="stylesheet" type="text/css" href="{myCSS}"/>
			</head>
			<body>
				<div id="top">
					<ol>
						<li><a href="../collegeRank">News Ranker</a></li>
						<li><a href="../survey/">Survey</a></li>
						<li>Interactive + Read API</li>
						<li><a href="../map/">Map</a></li>
					</ol>
				</div>
				<div id="marginleft">
				</div>
				<p  id="first">Interactive + Read API</p>
				<div>
					<form method="post" action="{myAction}">
						<fieldset>
							<legend>Interactive</legend>
							<br/>
							<label for="stateCollege" class="addCollege">Insert state initials and we'll print out the colleges.</label>
							<input type="text" name="stateCollege" id="stateCollege"/>
							{colList}
							<br/><br/>
							<label for="collegeCost" class="addCollege">Compare College Cost (Separate by commas)</label>
							<input type="text" name="collegeCost" id="collegeCost"/>
							{colCost}
							<br/><br/>
							
							<div class="buttonarea">
								<input type="submit" value="Run Program"/>
							<br/>
						</fieldset>
					</form>
				</div>	
				<p>{apiS}</p>				
			</body>
		</html>
		'''
		with open("templates/readAPI.html", 'w') as writeT:
			writeT.write(htmlExtraData.format(
			myCSS="{{ url_for('static', filename='main.css') }}",
			colList=stateCol,
			colCost=costCol,
			myAction="{{ url_for('readAPI') }}",
			apiS=apiStr)) 	
	if request.method == 'POST':
		try:
			sCollege = request.form['stateCollege'].upper()
			if len(sCollege) > 0:
				stateCol = "<br/><br/>These Colleges are in " + sCollege + ":"
				for i in range(len(dataC)):
					if(sCollege in dataC['Location'][i]):
						stateCol = stateCol +  "<br/>" + dataC['Name'][i]
		except:
			print("please fill out propper state.")
		try:
			cost = request.form['collegeCost']
			if len(cost) > 0:
				costCol = "<br/><br/> These colleges cost:"
				for i in range(len(dataC)):
					costList = cost.split(",")
					for thisCost in costList:
						if(thisCost.strip() in dataC['Name'][i]):
							costCol = costCol + "<br/>" + dataC['Name'][i] + ', ranked ' + str(i + 1) + ', costs on average ' + dataC['Tuition and fees'][i]		
		except:
			print("Please put in colleges to compare Cost.")
		htmlExtraData()
		return render_template("readAPI.html")
	htmlExtraData()
        
	return render_template("readAPI.html")
	
@app.route('/map/')
def map():
	return render_template("map.html")
@app.route('/myJRank/')
def myJRank():
	return render_template("myJRank.html")

@app.after_request
def add_header(response):
    # Clear History
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

app.run(host='0.0.0.0', port=5000, debug=True) #run on http://localhost:5000/collegeRank


