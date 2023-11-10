# API Development assignment: F1 API
I chose to use Formula One as a theme for this assignment because that was the first thing that came to my mind, and I really like watching Formula One. The API consists of 2 main parts, teams and drivers.

## My endpoints
In total, I have 12 endpoints in this API. 2 Of them are POST, 4 of them are DELETE and the remaining 6 of them are GET endpoints.
![Endpoints](img/endpoints.png)

### POST endpoints
I have made 1 POST to create a new team, and 1 POST to create a new driver. You can use them on my front-end as well as on Postman:
![POST team](img/postteam.png)
![POST driver](img/postdriver.png)

### DELETE endpoints
In this API are 4 DELETE endpoints, you can delete all drivers at once or all teams at once. You can also specify a driver number to delete that driver. To delete a specific team you need to use their ID
Drivers:
![DELETE drivers](img/deletedrivers.png)
![DELETE driver](img/deletedriver.png)

Teams:
![DELETE teams](img/deleteteams.png)
![DELETE team](img/deleteteam.png)

### GET endpoints
I have 6 GET endpoints, 3 for teams, and 3 for drivers.
Drivers:
![Get drivers](img/getdrivers.png)
![Get driver by name](img/getdriver_name.png)
![Get driver by number](img/getdriver_number.png)

Teams:
![Get teams](img/getdrivers.png)
![Get team by name](img/getteam_name.png)
![Get team by country](img/getteam_country.png)

## My front-end
Here is an image of my simple front-end I made. With this page you can see a list of every driver and team. You can also add new drivers and teams to the list. And on the bottom of the page you can search driver by name and number, and teams by name and their country.
![Frontend first part](img/frontend1.png)
![Frontend second part](img/frontend2.png)

## Links
-  [Hosted API link](https://f1-api-matscouwenberg.cloud.okteto.net/)
-  [Hosted front-end link](https://matscouwenberg.github.io/API_dev_1/)
-  [GitHub repo link](https://github.com/MatsCouwenberg/API_dev_1)