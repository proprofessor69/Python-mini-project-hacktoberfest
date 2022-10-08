# Road Incidents

## Background

South Africa's roads have become increasingly bad over the years with numerous potholes, burst water pipes along roads and robots (traffic lights) not working.
Due to various reasons such as management, finances and resources
a good majority of these incidents do not get fixed in a timely manner or at all depending on the incidents location.

---

## Idea Behind the Project

Building an application to crowd source road incidents such as accidents, potholes, burst water pipes, road works and broken robots (traffic lights)
will not only let other drivers know which areas are bad and can then avoid them but can also be intergrated into a municipalities or State Owned Enterprises system
so that they can see exactly where work needs to be done. This may also improve their management systems as incidents will often be reported as fixed on their side
whereas they have in actuality not been fixed.

---

## How it works

Any signed in user can click on the map to add a road incident which will be visually displayed as a point on the map.
A popup will appear on the point prompting the user to select what kind of road incident they have experianced from the available options
(pothole, accident, road works, broken robot (traffic light) and burst pipe).
Once the user has submitted the form the point will be recorded on the map and added to the incidents log.
The incidents log is a record of all points that have ever been recorded and will show the
name of the user that added the point, what kind of incident it was and the date it was added.
Any signed in user can remove a point by clicking on the point itself.
This will remove the point from the map and add the user who removed it, what incident it was and the removed date onto the incident log.

---

## Under the hood

The application uses Django as the back-end and JavaScript as the front-end.
A JavaScript library called Leaflet was used to create the map and handle all of the interactions with the map such as clicking on the map to record a point, clicking on a point to remove it from the map and loading all of the points and incidents in the incident log that have been previsouly recorded.

---

## Running the Application

First navigate into the projects directory \
Install all of the dependencies that the application needs from the requirements.txt file. \
Execute

```bash
python3 manage.py runserver
```

in your terminal and navigate to localhost:8000 in your browser to view the application
