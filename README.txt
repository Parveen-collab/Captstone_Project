# Job Market Trend Analysis for IT Roles

## Project Overview
This project analyzes job market trends for various IT roles in India using web scraping and Power BI. It automates the collection of job postings from LinkedIn, extracts and structures the data, and visualizes trends for actionable insights.

---

## 1. Workflow

### a. Data Collection (Python + Playwright) (Piyush Kumar)
- Automated login to LinkedIn
- Search for specific job roles (e.g., Blockchain Developer, Data Scientist, etc.)
- Scrape job postings and save each as an HTML file

### b. Data Extraction & Structuring (Parveen Kumar)
- Parse saved HTML files
- Extract structured data (job title, company, location, etc.)
- Save structured data into CSV files

### c. Data Cleaning & Visualization (Power BI) (Piyush Kumar, Pawan Kumar, Pankaj Kumar)
- Import CSVs into Power BI
- Clean data (remove duplicates, handle missing values)
- Create dashboards to visualize trends (job counts, locations, skills, etc.)

---

## 2. Demo Script

**Introduction:**
“Hello everyone, today I’ll demonstrate our project on analyzing job market trends for IT roles using web scraping and Power BI.”

**Step 1: Data Collection (Python Script)** (Piyush Kumar)
- Show the Python script (`MAIN.PY`)
- Run the script or show a recorded run
- Explain how job details are saved as HTML files

**Step 2: Data Extraction & Structuring** (Parveen Kumar)
- Show a sample CSV file
- Explain the extracted data fields

**Step 3: Data Cleaning & Visualization (Power BI)** (Piyush Kumar, Pawan Kumar, Pankaj Kumar)
- Import CSV into Power BI
- Show cleaning steps and dashboards

**Results & Insights** (Pankaj Kumar)
- Highlight key findings from the dashboard

**Conclusion**
- Summarize the workflow and its value

---

8. Challenges & Solutions


## 5. Future Work
- Automate extraction for more roles and locations
- Enhance data extraction for deeper analytics
- Deploy as a scheduled service for continuous monitoring

---

10. Conclusion & Q/A

---

## 4. Live Demo Checklist

- [ ] Open `MAIN.PY` in the editor
- [ ] Show and explain the code
- [ ] Run the script or show output folder
- [ ] Show a sample CSV file
- [ ] Open Power BI and import CSV
- [ ] Show dashboards and insights
- [ ] Be ready for Q&A

---

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\Backend_Developer-20250701T161924Z-1-001\Backend_Developer'
OUTPUT_CSV = 'extracted_jobs2.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\Blockchain Developer-20250701T174708Z-1-001\Blockchain Developer'
OUTPUT_CSV = 'extracted_jobs3.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\business analst-20250701T175315Z-1-001\business analst'
OUTPUT_CSV = 'extracted_jobs4.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\data analyst html-20250701T175756Z-1-001\data analyst html'
OUTPUT_CSV = 'extracted_jobs5.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\data engineer-20250701T180242Z-1-001\data engineer'
OUTPUT_CSV = 'extracted_jobs6.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\frontend developer-20250701T180738Z-1-001\frontend developer'
OUTPUT_CSV = 'extracted_jobs7.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\Machine Learning Engineer-20250701T181147Z-1-001\Machine Learning Engineer'
OUTPUT_CSV = 'extracted_jobs8.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\Project Manager-20250701T181616Z-1-001\Project Manager'
OUTPUT_CSV = 'extracted_jobs9.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\Technical Recruiter-20250701T182016Z-1-001\Technical Recruiter'
OUTPUT_CSV = 'extracted_jobs10.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\UX Designer-20250701T182440Z-1-001\UX Designer'
OUTPUT_CSV = 'extracted_jobs11.csv'

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\web dev-20250701T182925Z-1-001\web dev'
OUTPUT_CSV = 'extracted_jobs12.csv'

# Job Market Trend Analysis Project

## Project Overview

This project aims to analyze job market trends for Data Scientist roles by extracting structured data from a large collection of job posting HTML files and preparing it for visualization and further analysis.

---

## Workspace Structure

```
Job Market Trend Project/
│
├── script.py                # Python script for data extraction
├── extracted_jobs.csv       # Output: structured job data (CSV)
│
└── Data/
    └── data scientist/
        ├── job_1.html
        ├── job_2.html
        ├── job_3.html
        └── ... (hundreds of HTML files)
```

---

## Data Extraction Process

### 1. **Raw Data**
- Located in `Data/data scientist/`
- Each `.html` file is a job posting, typically scraped from job boards (e.g., LinkedIn).
- Contains information such as job title, company, location, skills, qualifications, etc.

### 2. **Extraction Script**
- File: `script.py`
- **Purpose:** Parses all HTML files and extracts key fields.
- **Libraries Used:** `BeautifulSoup` (HTML parsing), `glob` (file matching), `csv`, `re` (regex).
- **Extracted Fields:**
  - `job_title`
  - `company`
  - `location`
  - `required_skills`
  - `required_qualifications`
  - `experience`
  - `industry_domain`
- **Output:** Writes all extracted data to `extracted_jobs.csv`.

### 3. **How to Run the Script**
1. Ensure Python and dependencies are installed:
   ```sh
   pip install beautifulsoup4
   ```
2. Run the script:
   ```sh
   python script.py
   ```
3. The script will process all HTML files and generate `extracted_jobs.csv`.

---

## Output Data

- **File:** `extracted_jobs.csv`
- **Format:** CSV (comma-separated values)
- **Columns:**  
  - `file`: Source HTML file path  
  - `job_title`: Title of the job  
  - `company`: Company name  
  - `location`: Job location  
  - `required_skills`: Key skills required  
  - `required_qualifications`: Educational or professional qualifications  
  - `experience`: Required experience (years, if available)  
  - `industry_domain`: Industry or domain (if available)

---

## Next Steps for Visualization

1. **Open `extracted_jobs.csv`** in Excel, Google Sheets, or your preferred data analysis tool.
2. **Analyze/Visualize** trends such as:
   - Most in-demand skills
   - Popular job locations
   - Experience requirements
   - Top hiring companies
   - Industry/domain breakdown
3. **Create charts** (bar, pie, line, etc.) to present your findings.

---

## Notes & Tips

- Some fields may be missing for certain jobs due to inconsistent HTML structure.
- If you need more fields or better accuracy, the extraction script can be further refined.
- For any questions about the extraction process or data structure, refer to `script.py` or contact the extraction script author.

---

## Contact

- **Data Extraction:** Parveen Kumar
- **Visualization:** [Your Friend's Name Here]