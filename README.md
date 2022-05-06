# VRPTW

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/israelpereira55/MDVRPTW-Solomon">
    <img src="images/M101k10.jpg" alt="Logo" width="541" height="400">
  </a>

  <h3 align="center">Let's solve the VRPTW!</h3>

  <p align="center">
    This is an algorithm that seeks to get the optimum solutions for the VRPTW. 
    <br />
    On this state it just build a constructive solution with Solomon Insertion I1 heuristic (1987).
    I'm currently working on the MDVRPTW, but to solve MDVRPTW I need to solve the VRPTW too! I plan to come back for this algorithm after I finish my research on the MDVRPTW. See ya! =)
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#flags-description">Flags description</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The Vehicle Routing Problem (VRP) is a known combinatorial problem for it's difficult (NP-hard). On this project, we seek to solve the  Vehicle Routing Problem with Time Windows (VRPTW) which is harder!. 





<!-- GETTING STARTED -->
## Getting Started

First you need a MDVRPTW problem instancy, which you can get on VRP Libraries.
We will list some libraries in which you can get them. We have the "instances" folder Solomon VRPTW instances with 25 clients but You can get instances with more clients!

You can also make your own instance, but it needs to follow Solomon standards. 

* [VRP-REP](http://www.vrp-rep.org/variants/item/vrptw.html)
* [NEO LCC](https://neo.lcc.uma.es/vrp/vrp-instances/)

### Prerequisites

Python 3.6 or higher is required.


### Installation

1. Get the dependencies
   ```sh
   python -m pip install -r requirements.txt
   ```
2. Run the project
   ```sh
   python main.py <FLAGS>
   ```



<!-- USAGE EXAMPLES -->
### Flags description

Here we describe the algorithm parameters.

```bash
    main.py:
        (obrigatory)
        --instance: path to the VRPTW instance.

        --N: number of clients

        (optional)
        --[no]toy: run with a toy instance.
        (default: False)
```

* Example of usage:
   ```
   python3 main.py --instance ./instances/solomon_25/C101.txt --N 25

   python main.py --toy
   ```


<!-- CONTACT -->
## Contact

Israel P. - israelpereira55@gmail.com

Project Link: [https://github.com/israelpereira55/MDVRPTW](https://github.com/israelpereira55/MDVRPTW)

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Best README Template](https://github.com/israelpereira55/MDVRPTW)


## References

[1] Solomon, Marius M. "Algorithms for the vehicle routing and scheduling problems with time window constraints." Operations research 35.2 (1987): 254-265.

[2] Cordeau, Jean-François, Gilbert Laporte, and Anne Mercier. "A unified tabu search heuristic for vehicle routing problems with time windows." Journal of the Operational research society 52.8 (2001): 928-936.




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/israel-souza-06737118b/
[product-screenshot]: images/screenshot.png