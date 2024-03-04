# FastAPI Backend Setup Guide

This guide will walk you through setting up a FastAPI backend, including creating a virtual environment, installing dependencies from a `requirements.txt` file, setting up MongoDB, and testing the APIs.

## Setting Up Virtual Environment

1. **Install Python**: Ensure Python is installed on your system. If not, download and install it from the official Python website.

2. **Install `virtualenv` (if not already installed)**: If you're not using Python 3's built-in `venv` module, install `virtualenv` via pip:

    ```bash
    pip install virtualenv
    ```

3. **Create Virtual Environment**:
   - Navigate to your project directory.
   - Depending on your preference, create a virtual environment using either `venv` or `virtualenv`:
   
   Using `venv` (Python 3):
   ```bash
   python3 -m venv myenv
   ```

   Using `virtualenv`:
   ```bash
   virtualenv myenv
   ```

4. **Activate Virtual Environment**:
   - Activate the virtual environment based on your OS:

   For Linux/macOS:
   ```bash
   source myenv/bin/activate
   ```

   For Windows:
   ```bash
   myenv\Scripts\activate
   ```

5. **Install Dependencies from requirements.txt**:
   - Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## MongoDB Setup

6. **Install MongoDB Community Edition**:
   - Install MongoDB on your platform. You can download it from the official MongoDB website.

## Running the Server

7. **Run the FastAPI server**:
   - Execute the following command to run the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

## Testing the APIs

8. **Access API Documentation**:
   - After running the development server with uvicorn, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
   - This page provides interactive documentation (Swagger UI) for your FastAPI backend, allowing you to explore and test your APIs directly from the browser.

## Loading a New Database

9. **Load MongoDB Database**:
    - Ensure MongoDB is running.
    - Use `mongorestore` to load a dump into a new database:

    ```bash
    mongorestore --db <new_database_name> <dump_directory>/<your_database_name>
    ```

    Replace `<new_database_name>` with the name of the new database and `<dump_directory>/<your_database_name>` with the path to the dump directory containing the dump files for your original database.

10. **Example**:
    Let's say you want to create a dump of a database named `mydatabase` and load it into a new database named `newdatabase`. Here are the commands:

    Creating a Dump:
    ```bash
    mongodump --db mydatabase --out /path/to/dump/directory
    ```

    Loading into a New Database:
    ```bash
    mongorestore --db newdatabase /path/to/dump/directory/mydatabase
    ```

    Replace `/path/to/dump/directory` with the actual path where you want to store your dump files.

That's it! You've successfully set up a FastAPI backend with MongoDB support and tested your APIs using the interactive documentation provided by FastAPI.
