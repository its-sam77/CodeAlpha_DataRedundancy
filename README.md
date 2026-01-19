# Data Redundancy Removal System

This project is developed as part of the CodeAlpha Cloud Computing Internship.

## Objective
To prevent redundant data from being stored in the cloud database by validating new data entries before insertion.

## Features
- Detects duplicate data
- Allows only unique data entries
- Improves database accuracy and efficiency

## Technologies Used
- Python
- SQLite Database
- AWS EC2 (Cloud Deployment)

## Working
Before inserting any new data, the system checks whether the data already exists in the database.
If duplicate data is detected, insertion is blocked.
Only verified and unique data entries are stored.

## Cloud Deployment
The project is deployed and executed on an AWS EC2 Free Tier instance.

## How to Run
1. Clone the repository
2. Run `python3 app.py`
3. Enter data to test redundancy detection
