# Travel Cost Calculator -  Testing

[Back to README](README.md)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [PEP8 Testing](#pep8-testing)
* [MANUAL TESTING](#manual-testing)
  * [Manual Python Testing](#manual-python-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)


- - -

## AUTOMATED TESTING

### PEP8 Testing

The code was passed through the [PEP8 linter](https://pep8ci.herokuapp.com/) and there are no problems
<details><summary>Testing Result</summary>
<img src = "docs/pep8_testing.PNG"></details>

- - -

## MANUAL TESTING

### Manual Python Testing

I have manually tested this project by doing the following:
- given invalid inputs: when the user inputs invalid data she/he is notified and asked to try again
- tested in my loval terminal and the Code Institute Heroku terminal


### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? |
| :--- | :--- |
| I want to be able to use the Travel Cost Calculator by inserting data and choosing options | The Travel Cost Calculator lets the user insert data after it asked certain questions and gives options to choose from. |
| I want the Travel Cost Calculator to give me a Travel Cost Index as a result. | The Travel Cost Calculator calculates the Index based on the validated user input. |

`Returning Visitors`

|  Goals | How are they achieved? |
| :--- | :--- |
| I want to check the Travel Cost Index befor every travel that I have in mind. | The user can rerun the programme as many times as she/he wants, repeating it before different travels or to compare the different levels of adventure/comfort |

`Interested Party`

|  Goals | How are they achieved? |
| :--- | :--- |
| I want to understand the data, the underlying logic of the programme and how the data is validated | The interested person can check the data in the google spreadsheet and get the links to the websites where the Indices can be found from the README.md. The code is written according to the [python style guidlines](https://peps.python.org/pep-0008/#introduction) to ensure easy and clear readibility. The validation is done with while loops and try/except statements. |

### Full Testing

`Main Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Entering the programme | The app starts with a few lines stating what it is about and how it works | I ran the app | App starts running | Pass |
| Accepting user input | The app should accept the user input at every stage in the programme where it asks the user for information | I inserted data in every possible input field | The app validates the data and stores it in variables | Pass |
| Input validation and error-checking for each user input | The app should validate the input | I tried out different data input to test the validation | Data is validated appropriately | Pass |
| Guiding the user by reactions to her/his input | The app should give feedback on whether the input meets the input criteria or not. If not, it should ask to insert the data again | I inserted different data types and input to test the reactions | The app gives feedback on whether the criteria are met or not and asks for input again if they are not met | Pass |
| Saving input as variables | The app should save the data input in variables | The whole app was run several times with different data input | The app stores the data inserted in variables and uses them for the final TCI (Travel Cost Index) calculation | Pass |
| Calculating an Index based on the variables | The app should show a calculated Index in the end | The whole app was run several times with different data input | The app calculates the TCI based on the data input | Pass |

- - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | In the setup, my virtual environment didn't let me install any packages | I changed the "include-system-site-packages" boolean value to true in the pyvenv.cfg file. Check: https://stackoverflow.com/questions/57801495/pip-wont-install-packages-in-virtualenv |

- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
| 1 | No known bugs |  |
