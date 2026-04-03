# Introduction

<h3 align="center">Cost Benefit Calculator</h3>

<p align="center">
The "Cost & Benefit Calculators" tool is designed to support farmers and agricultural advisors in assessing the financial impact and potential benefits of adopting various DATSs in crop and livestock farming systems. The tool features dedicated calculator modules for each type of system, tailored to reflect their specific needs.

Users can access two main repositories:

Commercial DATSs, identified through a literature review, which includes cost and benefit data from previous EU projects' knowledge gained and developed repositories, provider materials (e.g. leaflets, brochures), and scientific publications.

Test Case DATSs, which are based on data collected from DATSs implemented and assessed within the QuantiFarm project.
By selecting a DATS and providing basic inputs (e.g., number of units, usage years, area, yield, and costs), users receive key economic outputs such as operational savings (e.g. labour, fuel), potential revenue increases, Return on Investment, and Net Benefit. This aids end-users in gaining a realistic understanding of their potential investment in a DATS.
</p>


## Technologies
<p align="center">
  You will need to have Dokcer installed on your system
  <br>
  Windows : <a href="https://docs.docker.com/desktop/install/windows-install/"><strong>Installation Guide</strong></a>
  <br>
  Ubuntu : <a href="https://docs.docker.com/engine/install/ubuntu/"><strong>Installation Guide</strong></a>
  <br>
  Linux : <a href="https://docs.docker.com/desktop/install/mac-install/"><strong>Installation Guide</strong></a>
</p>

## Installation

- Create a Folder in your System
- Clone / Download the Git Code into the folder
- Execute the following command 
```console
$ docker compose up
```
- Done

<p align="center">
After a successful service initiation the Webservice API documentation is available here:
http://localhost:8687/documentation
</p>

## Initial Configuration of the Web Service
Some initial actions must be taken for the Web Service to become fully installed. Those actions include "**Initializing Database**" and "**Initializing Models**". Those actions can be performed through the following procedure.

- Go to http://localhost:8687/documentation
- Expand the "**/administration/create_db_tables**" (under the "**Administration**" Header) press the "**Try it out**" on the right side and then the "**Execute**" Button. 
- Expand the "**/administration/create_input_models**" (under the "**Administration**" Header) press the "**Try it out**" on the right side and then the "**Execute**" Button. 

## Add User Data in the Webservice
In order to receive the **Calculation Results** , we are going to have to provide User Input Data to the WebService. And those input data will be fed to the Models to produce the desired calculations. This can be achieved by using the "**/generic**" Endpoint , under the "**Add Data**" Header , and fill in each form with the appropriate user data.

<b>Example : </b>

- Go to http://localhost:8687/documentation
- Expand the "**/generic**" (under the "**Add Data**" Header).
- Press the "**Try it out**" on the right side.
- Fill in the JSON Form with the appropriate values.
- Provide a Custom "user_id" so that all data are attached to a specific id.
- Press the "**Execute**" Button.

## Getting the Results 
If all the available User Data have been added in the Web Service we can then proceed in getting the calculation results from the Models either individually running each model and receiving the results or executing them all in paralel and receive a Summary.

### Results from Individual Models
If we want to get the Calculation Results only for a specific model , and for a specific Cultivation Type , for example "**Yield**" for "**Arable**".
Then we will do the following : 

- Go to http://localhost:8687/documentation
- Expand the "**/results/arable/yield**" (under the "**arable_results**" Header).
- Press the "**Try it out**" on the right side.
- Provide the DAT Name you are interested in. 
  - **Important**: If you want to know which DATs are available for the specific Cultivation Type you will have to use the "**/dat_tree**" endpoint under the "**dat_tree**" header. And you will receive a JSON with all the DATs in a Tree Format. Select the name you want and fill it in the form here.
- Provide your custom "**user_id**" that you used to add all the data.
- Press the "**Execute**" Button.

### Results from all Models
If we have filled most of the Models with Data we can also receive some summary calculations : 

- **Total cost Savings**
- **Return on Investment**
- **Net Benefit**

Then we will do the following : 

- Go to http://localhost:8687/documentation
- Expand the "**/totals**" (under the "**totals**" Header).
- Press the "**Try it out**" on the right side.
- Provide your custom "**user_id**" that you used to add all the data.
- Provide the DAT Name you are interested in. 
  - **Important**: If you want to know which DATs are available for the specific Cultivation Type you will have to use the "**/dat_tree**" endpoint under the "**dat_tree**" header. And you will receive a JSON with all the DATs in a Tree Format. Select the name you want and fill it in the form here.
- Provide the Cultivation Type you have provided data for
- Press the "**Execute**" Button.
