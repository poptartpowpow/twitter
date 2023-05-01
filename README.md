<h1>Welcome!</h1>
<h4>For an example of how to utilize this program to create network visualizations in Tableau, check out this <a href="https://public.tableau.com/app/profile/caroline.steel/viz/SampleTwitterNetworkAnalysis/ASGsTwitterNetworks">sample Tableau project</a></h4>

<h1>Twitter_followers.py</h1>
  <p>Twitter_followers hooks into the Twitter API via Tweepy and live-writes a CSV with the followers of any given Twitter user(so that if operation is stopped, the CSV will be rendered up to the last follower loop). It returns a CSV with the following publicly available follower data:</p>
  <ul>
    <li>ID</li>
    <li>Username</li>
    <li>Name</li>
    <li>Location—this is a user's self-reported, uncleaned, location</li>
    <li>City (using tweo)—Tableau compliant</li>
    <li>State (using tweo)—Tableau compliant</li>
    <li>Country (using tweo)—Tableau compliant</li>
    <li>Verified status (whether or not the follower is verified)</li>
    <li>Follower count (the # followers of the follower)</li></ul>
  
  <p>To use the code, include your own config.ini file with a Twitter Developer bearer token. 


<h1>Tweo</h1>
  <p>Tweo is a rather heavy module that takes the follower's self-reported location string (e.g., 'Living the life in Washington, DC') and returns a dictionary with Tableau-compliant city, state(/province), and country data.</p>
  <p>Because users may list multiple locations, the parse_location function iterates through each possible locaiton even after a match has been found. Code is also written to control for multiple places with the same names, so the flow will overwrite erroneous matches.<b> This is by no means a perfect or complete library.</b> It is regularly updated with place names, and they are intentionally input manually to avoid errors. For large datasets, the error rate is within acceptable parameters.</p>
    <p>This module takes considerable time to iterate through user location data. However, due to Twitter API rate limits, will not ultimately slow down any requests, as they are heavily rate limited. 
  <p>Feel free to push with additional place names, or suggest a leaner method of looping!</p>
  
