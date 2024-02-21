# NCSU GIS 714 Spring 2024: Tangible Landscape

_Caitlin Haedrich_

## Assignment Directions

In this assignment, you will create your own Tangible Landscape activity. You can work on your own or in groups.

**You will need to submit:**
* A uniquely-named Python file
* A similarly-named JSON config file

**Your activity needs to:**
* Be submitted to the [2023 Tangible Landscape Activities Repository](https://github.com/ncsu-geoforall-lab/gis714-2024-tangible-landscape/)
* Pass GitHub checks, which means it should:
    - Black and Flake8 formatting compliant
    - Have a unique name and description (i.e. not "test.py")
    - The Python file should have the activity code (i.e. `def run_*:`) and test case with `if __name__==__main__`
    - The JSON file should the activity title, display commands and any other relevant information for the TL GUI
    - Be different from the examples

**Activity Ideas:**
* Where is the probability of flooding highest?
* Model a stream gauge at the outflow of a watershed during a thunderstorm
* How does changing landcover influence overland water flow? 
* How would adding a wetland or pond to the area impact water flow? Or sediment/erosion deposition? Or pollutant transport?
* Or anything related to your own research!

**Tips and Tricks**
* You can develop and test this activity in the [TangibleLandscape.ipynb](./TangibleLandscape.ipynb)  tutorial or by following the directions in the [README](https://github.com/ncsu-geoforall-lab/gis714-2024-tangible-landscape/). You can also test your activity locally by opening GRASS GIS and running your activity from the command line (`$ python -m your_activity.py`).
* The Black command line tool will reformat your python file for you so it will pass the GitHub checks (i.e. run `$ black your_activity.py`). Find directions for installing and using Black [here](https://black.readthedocs.io/en/stable/getting_started.html).
* Once your activity Pull Request is merged, it will appear on [this website](https://ncsu-geoforall-lab.github.io/gis714-2024-tangible-landscape/) automatically! (So cool! Thanks Anna)