<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the Twitter-Copy-Followers and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** viraatdas, Twitter-Copy-Followers_name, therealviraat, viraat.laldas@gmail.com, project_title, Copy Twitter Followers
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">


  <h3 align="center">Copy Twitter Followers</h3>

  <p align="center">
    ·
    <a href="https://github.com/viraatdas/Twitter-Copy-Followers/issues">Report Bug</a>
    ·
    <a href="https://github.com/viraatdas/Twitter-Copy-Followers/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a way to copy Twitter followers from one account to another. Since there is a usage restriction of how many followers the Twitter API can follow in a day, people who you follow AND that follow you are prioritized when following. More about it it the `Note` section. 

### Built With

* [python-twitter](https://github.com/bear/python-twitter)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* Pipenv
  ```sh
  pip install pipenv
  ```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/viraatdas/Twitter-Copy-Followers.git
   ```
2. Pipenv environment
   ```sh
   pipenv install
   ```
3. Environment file
   ```sh
   mv temp_env.py env.py
   ```
4. Access and API tokens for the old account and new account
    - [Instructions](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

5. Update the values in `env.py` accordingly 


<!-- USAGE EXAMPLES -->
## Usage

Run `python follow.py`

The Twitter API only allows 400 follows every 24 hours [POST friendships/create
](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create). There is not way of getting around this apart from just running this over multiple days if you have more than 400 followers. You can use a [scheduler](https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds) or cronjob to automate this.

For my purposes, I wanted to first follow people that follow me AND that I follow. I used an OrderedSet to add these people to be followed first. Anytime there is  an exception raised (most likely due to the number of people being followed), the list of remaining people that haven't been followed is serialized. When `follow.py` is run again, it resumes using the serialized structure to follow the remaining people. 



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/viraatdas/Twitter-Copy-Followers/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Viraat Das - [@therealviraat](https://twitter.com/therealviraat) - viraat.laldas@gmail.com


README template graciously provided by [othneildrew](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/viraatdas/Twitter-Copy-Followers.svg?style=for-the-badge
[contributors-url]: https://github.com/viraatdas/Twitter-Copy-Followers/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/viraatdas/Twitter-Copy-Followers.svg?style=for-the-badge
[forks-url]: https://github.com/viraatdas/Twitter-Copy-Followers/network/members
[stars-shield]: https://img.shields.io/github/stars/viraatdas/Twitter-Copy-Followers.svg?style=for-the-badge
[stars-url]: https://github.com/viraatdas/Twitter-Copy-Followers/stargazers
[issues-shield]: https://img.shields.io/github/issues/viraatdas/Twitter-Copy-Followers.svg?style=for-the-badge
[issues-url]: https://github.com/viraatdas/Twitter-Copy-Followers/issues
[license-shield]: https://img.shields.io/github/license/viraatdas/Twitter-Copy-Followers.svg?style=for-the-badge
[license-url]: https://github.com/viraatdas/Twitter-Copy-Followers/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/viraatdas
