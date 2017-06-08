## Getting Started

The purpose of this repo is to get you started building your own tools and doing
analysis using the BuildingOS API. If you have git installed, and have elementary
Python knowledge, you should be able to get up and running.

To begin:

1. Clone this repo: `git@repos.office.luciddg.com:product/api-examples.git`
2. `cd ./api-examples` and install Python dependencies with `pip install -r requirements.txt`
(using a virtualenv if you are so inclined).
3. Create your own API key at https://buildingos.com/developers. Use the following API settings:
  * Client type: Confidential
  * Auth grant type: Resource owner password-based
  * Redirect uri's: http://localhost:8000 (although this shouldn't matter for our purposes)
4. Add your BuildingOS and API credentials to your `~/.bash_profile` file (assuming you're on a Mac).
```
export BOS_CLIENT_ID=<your api client id>
export BOS_CLIENT_SECRET=<your api client secret>
export BOS_USERNAME=<firstname.lastname@luciddg.com>
export BOS_PASSWORD=<your buildingos password>
```
5. Source your bash profile: `source ~/.bash_profile`


You should now be able to run any of the example scripts: `python <directory>/<name_of_script>.py`
