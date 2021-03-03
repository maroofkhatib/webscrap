# webscrap

I have scraped the news from NDTV.com and created an API using flask API in python.

1. To run the API first activate the virtual environment in this repository:
   source bin/activate

2. Run command python3 app.py to run the API.

3. Test the API in Postman using the following input format in POST request : 
	{
		"data" : "Your-Keyword"
	} 

4. This should return all the articles which are related to the keyword entered above 

5. This repository also containes the code for web scraping that is used to get the data from ndtv.com/india in the new directory
