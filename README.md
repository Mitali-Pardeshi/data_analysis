# Django CSV Upload and Data Analysis

This project is a web application built with Django that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on a web interface.

## Features

1. **File Upload:** Users can upload CSV files through a simple web form.
2. **Data Processing:** The application reads the uploaded CSV file and performs basic data analysis tasks such as:
    - Displaying the first few rows of the data.
    - Calculating summary statistics (mean, median, standard deviation) for numerical columns.
    - Identifying and handling missing values.
3. **Data Visualization:** Generates basic plots using matplotlib and displays them on the web page.
    - Histograms for numerical columns.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/django-csv-analysis.git
    cd django-csv-analysis
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Dependencies:**
    ```bash
    pip install django pandas numpy matplotlib seaborn
    ```

4. **Create and Apply Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/data_analysis/upload/` to upload a CSV file and view the analysis results.

### Project Structure
myproject/</br>
    manage.py</br>
    myproject/</br>
        __init__.py</br>
        settings.py</br>
        urls.py</br>
        wsgi.py</br>
    data_analysis/</br>
        __init__.py</br>
        admin.py</br>
        apps.py</br>
        forms.py</br>
        models.py</br>
        tests.py</br>
        views.py</br>
        templates/</br>
            data_analysis/</br>
                upload.html</br>
                analyze.html</br>
        urls.py</br>


### Explanation of Key Files

- **`data_analysis/models.py`**: Contains the `Upload` model for handling file uploads.
- **`data_analysis/forms.py`**: Defines the `UploadForm` for the file upload form.
- **`data_analysis/views.py`**: Contains the views for handling file uploads and performing data analysis.
- **`data_analysis/urls.py`**: Defines the URL patterns for the data_analysis app.
- **`templates/data_analysis/upload.html`**: Template for the file upload page.
- **`templates/data_analysis/analyze.html`**: Template for displaying the analysis results.

### Additional Notes

- **Media Files**: Uploaded files and generated plots are stored in the `media/` directory. Ensure this directory exists and has the appropriate permissions.
- **Static Files**: For production, you'll need to configure static files handling. This setup is simplified for development purposes.


