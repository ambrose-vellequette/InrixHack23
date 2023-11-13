# InrixHack23

## Inspiration
In recent years, there has been a considerable increase in car break-ins in San Francisco. These incidents disproportionately affect tourists and other people who are unfamiliar with the area they are parking in. We aimed to create a web application to provide a safer, smarter, and faster parking experience.

## What it does
Our project combines publicly available crime data in SF with Inrix's on-street parking API and uses our own algorithm to rank the safest streets to park on. We provide the user with the top three recommended parking locations in the vicinity of any given address or location in San Francisco. 

## How we built it
For Safe Park SF, we built the front end using Google Maps API, Javascript, HTML, and CSS. We created functions to set up the map, access the Google Places search bar, call the backend Flask proxy API, and handle the data returned by the API by displaying parking options as pins on the map. 

For the back end, we used Python and Flask to code the logic. Python’s simple syntax and numerous libraries accelerated our design and prototyping stage, which gave us a better vision for our product throughout the whole process. After the frontend queries our API with the lat and long parameters, we query the INRIX API for the probability of parking spaces, as well as an external government API for the crime data. Then, we implemented a weighted algorithm on the probability and number of crimes in a time period to find the 3 most ideal parking spaces.

## Challenges we ran into
We faced a lot of challenges in this project, many of which stemmed from the fact that this is the first hackathon almost all of our group has ever participated in. Some struggles we faced were choosing a project idea that we were all satisfied with, selecting which languages and frameworks we should use, and setting up the development environment. 

For example, we originally created the frontend using React, which we realized was a little bit inefficient for the goal of our project, and the time constraints we were under. After consulting with our ACM and Inrix mentors, we decided it would be best for us to pivot to a simpler frontend using HTML, CSS, and vanilla Javascript. This allowed us to more easily render information on the map, and significantly simplified our codebase. 

## Accomplishments that we're proud of
We are very proud that we were able to connect our frontend code with our backend code to successfully request and receive information from our proxy API. We are also proud that we were able to develop and deliver a working product in just 24 hours for our first hackathon.

## What we learned
Starting with very limited knowledge we learned how to pick and use frameworks and APIs for a web application. In addition, we learned how to get our frontend and backend  to communicate. We also developed strong interpersonal skills through hours of collaboration, especially under a stressful deadline.

## What's next for Safe Park SF
We have tons of ideas for the future of Safe Park SF. For example, we could allow the user to input their desired radius, weight different types of car crimes in our algorithm, and give the user more detailed information about their parking options. Additionally, we would like to add functionality that calculates the best route to find parking from the location based on the quality of parking along the route.
