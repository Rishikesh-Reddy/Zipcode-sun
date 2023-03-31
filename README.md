This is a python project which is used to find the Sunrise and Sunset Times in an area using its zipcode.

This project first fetches the latitude and longitude of the area using the zipcode and then uses the latitude and longitude to find the sunrise and sunset times.

This project uses the following libraries:
- requests - to make HTTP requests
- unittest - For testing

This project uses the following API:
- Sunrise Sunset API - https://sunrise-sunset.org/api
- Zipcode API - https://www.zippopotam.us/

This project has the following classes and Functions:

- Zippopotam
    - get_place_result()
    - store_place_info()
- SunriseSunset
    - get_sun_rise_set()
    - store_place_info()
- Place
    - extract_apis_information()
    - display_output()
- API
    - call_get()
- check_arguments()
- check_date()

# Usage:

To run this Project:

`python main.py <date> <post_code> <country_code>` 

Example:

`python main.py 2022-01-01 90210 us`

output:
`On 2022-01-01, the sunrise and sunset times from Beverly Hills (90210) in California, United States were respectively at 7:30:50 AM and 12:03:28 PM (UTC time)`


To Run tests:

`python -m unittest discover /path/to/project/directory/ -p "test_*.py"`
