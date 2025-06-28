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