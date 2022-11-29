# Platform Science code exercise
Code exercise for Platform Science. Application assigns shipment destinations to drivers. One driver, one shipment. Goal is to maximize the suitability score over the set of drivers.


## Dependencies
- Python 3.9
    - If for some reason you don't have Python installed on your machine, you can dowload from:
        - https://www.python.org/downloads/ 
        - or 
        - if you use homebrew, run:
        `brew install python`
        

## Instructions
- Clone the application: `git clone https://github.com/deep-proj/shipment-routing.git`
- Run `pip install -r requirements.txt` to install relevant packages
- Run `python main.py files/mock_address_data.csv files/mock_driver_data.csv`
    - *Note some limitations with passing in files. The application will only run if the address data file is passed in first. Also, note that the csv are  formatted in a specific way. For purposes of the exercise, files must be formatted similarly. At the very least, they must have a `first_name` and `last_name` field for drivers, and a `street_name` field for addresses.
- Sample output:

- ![Screen Shot 2022-11-28 at 1 57 17 PM](https://user-images.githubusercontent.com/119356243/204389511-68a58b94-fe7d-4905-a388-27dd063df8d0.png)

## Approach
This exercise gave me a chance to learn more about the [assignment problem](https://en.wikipedia.org/wiki/Assignment_problem). In researching approaches to solving this sort of problem, I came across [OR-Tools](https://developers.google.com/optimization/introduction/overview). The OR-Tools were built for this sort of problem, so I wanted to make use of them, and not have to reinvent the wheel. Looking through the docs, I found that they had open source libraries for Python. I have minimal experience with Python, but I wanted to make use of the OR-Tools. Learning more about and working with Python was a fun way to complete the problem. Though, I'm sure my code is unlikely to be the best expression of Python. If I had more time, cleaning up the code to be more idiomatic Python, would be a good next step. 

I first put all my code into `main.py` as a proof of concept to get everything working. Once I had working code, I started to move functionality into separate files, to isolate some of the behaviors. My next step was to move the solver functionality out of `main.py`, but time constraints kept me from completing this step. I probably should have done smaller commits along the way. As that would give a better indication of my initial approach, and how the code changed as I refactored.

For purposes of the exercise, I worked under the assumption that the data passed in would be clean, to make it easier to handle. So there's no data validation, or any flexibility in how the files are handled.

## Limitations
- For purposes of the exercise, the files are organized cleanly. So, there no handling of malformed data or files that don't present the data in the correct way.
- The addresses file must have more or equal to the number of rows in the drivers file. This does not currently handle a scenario where there are more addresses than drivers.
- No testing
- Not the most performant code. Will struggle to run efficiently with larger files.
- Likely numerous other scenarios and edge cases

## Next Steps
- Move solver functionality out of `main.py` and into a separate file
- Clean up code to meet Python conventions
- Add testing to have more confidence that the code is behaving correctly.
- Add flexibility for handling additional types of files
- Resolve issue of what to do if there are more addresses than drivers.
- Improve functionality to handle larger file sizes
