# Setup Environment
## Using Docker
First build Image 
`docker-compose build`
## Setup environment
Make sure you have python3 3.7+ installed on your system
First create the virtual environment with the following command

`
python3 -m venv ./venv
`

Activate using the following command

`source ./venv/bin/activate`

Note: for windows user, use absolute path.

## Setup Django
`pip install -r requirements.txt
`

# API 
## "room": "http://localhost:8000/api/room/"
### Get
User can get all the rooms in theater 
###Post
Admin can create room with variable in there
## "movie": "http://localhost:8000/api/movie/"
### Get 
User can view all the movies in different show time
### Post 
Admin can create a movie for a given room
## "tickets": "http://localhost:8000/api/tickets/"
### Get 
User can view information on a particular show time for tickets to purchase, can query by room_id and by movie_id
### Post
Admin can create ticket sales for a particular day
## "order": "http://localhost:8000/api/order/"
### Post
User can buy ticket, if there's no available tickets left it will throw error


#Potential improvements
* User management is implemented, including the authentication and authorization mechanism(for both admin and user) but permission level is not included yet. Given more time, it can be included
* Docker-compose is created for a more similar-to-produciton level postgres db, a better way to develop and deploy the current solution.
*  test driven(even know not for all apis due to time constraints)