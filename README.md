# Weather Company Data API access for IBM Cloud

This project shows how to build a basic data access application that continuously runs in the background, processing a variety of weather data from the Weather Company Data for IBM REST API endpoints, including severe weather alerts, tropical storm forecasts, and the daily weather almanac to find conditions over time.

## Obtain a Weather Company API Key

If you're participating in the [Call for Code](https://developer.ibm.com/callforcode/) Global Challenge, go the the [special Call for Code Weather web site](https://callforcode.weather.com/) and [register](https://callforcode.weather.com/register). A time-limited API key will be sent to you via email. The documentation for the Weather Company APIs for Call for Code can be found the [here](https://callforcode.weather.com/documentation/).

All others, sign up for [IBM Cloud here](https://cloud.ibm.com/login) and provision the [Weather Company Data service](https://cloud.ibm.com/catalog/services/weather-company-data). The Weather Company Data service uses slightly different [API versions](https://twcservice.mybluemix.net/rest-api/). You can reference its documentation [here](https://cloud.ibm.com/docs/services/Weather?topic=weather-insights_weather_overview).

## Getting Started in IBM Cloud

Deploy this application to IBM Cloud.

1. Install and configure the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)

2. Clone this repository

   ```
   $ git clone https://github.com/Call-for-Code/weather-api-python.git
   $ cd weather-api-python
   ```  

3. Deploy the application without starting it

   ```
   $ ibmcloud cf push --no-start
   ```

4. Configure your Weather API key `<YOUR_API_KEY>` and start the application

   ```
   $ ibmcloud cf set-env weather-api-python WEATHER_API_KEY <YOUR_API_KEY>
   $ ibmcloud cf start weather-api-python
   ```

## Getting Started on your local machine

To run this application on your local machine, first install Node.js.

1. Clone this repository

   ```
   $ git clone https://github.com/Call-for-Code/weather-api-python.git
   $ cd weather-api-python
   ```  

2. Install the dependencies

   ```
   $ pip install -r requirements.txt
   ```

3. Set your Weather API key `<YOUR_API_KEY>` when running the application    
   ```
   $ export WEATHER_API_KEY=<YOUR_API_KEY>
   $ python app.py
   ```

## Links

[Call for Code](https://callforcode.org/)  
[Call for Code - IBM Developer](https://developer.ibm.com/callforcode/)  
[Call for Code - The Weather Company](https://callforcode.weather.com/)  
[Call for Code: The Weather Company and you](https://developer.ibm.com/callforcode/blogs/call-for-code-the-weather-company-and-you/)

## License

This code is licensed under Apache 2.0. Full license text is available in [LICENSE](https://github.com/Call-for-Code/weather-api-python/tree/master/LICENSE).
