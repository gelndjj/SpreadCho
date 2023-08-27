<a name="readme-top"></a>

[![Contributors][contributors-shield]](https://github.com/gelndjj/SpreadCho/graphs/contributors)
[![Forks][forks-shield]](https://github.com/gelndjj/SpreadCho/forks)
[![Stargazers][stars-shield]](https://github.com/gelndjj/SpreadCho/stargazers)
[![Issues][issues-shield]](https://github.com/gelndjj/SpreadCho/issues)
[![MIT License][license-shield]](https://github.com/gelndjj/SpreadCho/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathanduthil/)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gelndjj/"SpreadCho">
    <img src="https://github.com/gelndjj/SpreadCho/blob/main/resources/image.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SpreadCho</h3>

  <p align="center">
    Generate fake users data. 
    <br />
    <a href="https://github.com/gelndjj/SpreadCho"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/gelndjj/SpreadCho/issues">Report Bug</a>
    ·
    <a href="https://github.com/gelndjj/SpreadCho/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/gelndjj/SpreadCho/blob/main/resources/main_windows.png" alt="Logo" width="874" height="593">
</br>
</br>
This project is a draft of what I originally wanted to do ; the first idea was to generate fake users to after add them into Active Directory.
</br>
</br>
After getting my hands in some Python modules, it took another direction but the main idea remained the same, I can generate fake users data and tinker with them. 
</br>
</br>
</br>

| 	Designation	 |         	Info                    |
|:-------------:|:--------------------------------:|
|  First Name   |           Male/Female            |
|   Last Name   |                -                 |
|      Age      |          From 19 to 65           |
|    Address    |                US                |
|     Email     | firstname.last_name@provider.com |
|     Phone     |                US                |
|   Job Title   |                -                 |
|     City      |                US                |

</br>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

<a href="https://www.python.org">
<img src="https://github.com/gelndjj/SpreadCho/blob/main/resources/py_icon.png" alt="Icon" width="32" height="32">
</a>
&nbsp;
<a href="https://customtkinter.tomschimansky.com">
<img src="https://github.com/gelndjj/SpreadCho/blob/main/resources/ctk_icon.png" alt="Icon" width="32" height="32">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Add Manually Datas<br />
Fill the fields in and click on Add User to add a row to the CSV.<br />

### Generate Multiple Users<br />
Type in a number then click on Generate, the user info will be automatically displayed.<br />

### Delete Row(s) or Replace Information<br />
Select the information you want to delete, write it in the specific field then click on Delete. It will be updated immediately.<br />

### Group By
The Group By function is used to split into groups based on some criteria; The criteria are available in the select boxes. Let say you want to see how many occurences of each first name in the CSV. Select First Name in the first select box then select Size in the second one. It will be displayed  how many times each First Name occurs.<br />

#### If you want for instance, to delete all users who are 30 years old, group by using Age/Size and in the Delete section type 30 and Delete.

### Export
Select the format you wan to export to (CSV or XLS).<br />

### Info
Display info such as Total Rows in the CSV or Number of Duplicates. Infos are updated after every changes.

#### Closing the soft DELETE all *.csv and *.xls located where the script is launched so do not forget to EXPORT to keep the changes.

* Example below grouping by First Name / Mean.<br />It displays the age average of every single user.<br />

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/resources/avg_age.png)

* The same using Age / Size displays the number of users for every single age found in the CSV.<br />

![Screenshot](https://github.com/gelndjj/SpreadCho/blob/main/resources/unique_age.png)

<!-- GETTING STARTED -->
## Standalone APP

Install pyintaller
```
pip install pyinstaller
```
Generate the standalone app
```
pyinstaller --onefile your_script_name.py
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


[LinkedIn](https://github.com/gelndjj/SpreadCho)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
