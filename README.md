# SpreadCho
_SpreadCho is a random users genrator written in Python. It uses the package Faker to generate user informations._

```
   _____                           __________        
  / ___/____  ________  ____ _____/ / ____/ /_  ____ 
  \__ \/ __ \/ ___/ _ \/ __ `/ __  / /   / __ \/ __ \
 ___/ / /_/ / /  /  __/ /_/ / /_/ / /___/ / / / /_/ /
/____/ .___/_/   \___/\__,_/\__,_/\____/_/ /_/\____/ 
    /_/                                               
```
### SUMMARY
SpreadCho generates a CSV file that contains user informations. From that, you can add manually user informations, delete rows that contain specific information, parse the CSV through the group by function and export the results.<br />
##### The generator will create user informations such as :<br />
1. First Name<br />
2. Last Name<br /> 
3. Age<br />
4. Address<br />
5. E-mail<br />
6. Phone<br />
7. Job Title<br />
8. City<br />

### SCREENSHOTS

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/img/main.png)

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/img/main_full.png)

### HOW IT WORKS 

#### Add Manually Datas<br />
######Fill the fields in and click on Add User to add a row to the CSV.<br />

#### Generate Multiple Users<br />
######Type in a number then click on Generate, the user infos will be automatically displayed.<br />

#### Delete Row(s) or Replace Informations<br />
###### Select the information you want to delete, write it in the specific field then click on Delete. It will be updated immediately.<br />

#### Group By
###### The Group By function is used to split into groups based on some criteria; The criteria are available in the select boxes. Let say you want to see how many occurences of each first name in the CSV. Select First Name in the first select box then select Size in the second one. It will be displayed  how many times each First Name occurs.<br />

###### If you want for instance, to delete all users who are 30 years old, group by using Age/Size and in the Delete section type 30 and Delete.

#### Export
###### Select the format you wan to export to (CSV or XLS).<br />

#### Infos
######  Display infos such as Total Rows in the CSV or Number of Duplicates. Infos are updated after every changes.

#### Closing the soft DELETE all *.csv and *.xls located where the script is launched so do not forget to EXPORT to keep the changes.


* Example below grouping by First Name / Mean.<br />It displays the age average of every single user.<br />

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/img/avg_age.png)

* The same using Age / Size displays the number of users for all ages found in the CSV.<br />

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/img/unique_age.png)


### REQUIREMENTS INSTALLATION

> pending