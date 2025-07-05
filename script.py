# Import required modules
import os           # For file and directory operations (e.g., joining paths, extracting filenames)
import glob         # For finding all HTML files in a directory using wildcard patterns
import csv          # For writing extracted data to a CSV file
import re           # For regular expressions to extract patterns from text
from bs4 import BeautifulSoup  # For parsing and extracting data from HTML files

# Directory containing the LinkedIn job HTML files
HTML_DIR = r'C:\Users\Parveen kumar\Downloads\web dev-20250701T182925Z-1-001\web dev'
# Output CSV file name
OUTPUT_CSV = 'extracted_jobs12.csv'

# List of fields/columns to extract and write to CSV
FIELDS = [
    'job_id',
    'job_title',
    'company_name',
    'location',
    'workplace_type',
    'employment_type',
    'industry',
    'job_description',
    'seniority_level',
    'experience_required',
    'skills',
    'salary_range'
]

def clean_html(raw_html):
    
    # Remove HTML tags and return plain text.
    
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def extract_from_html(filepath):
    
    # Extract job information from a single HTML file.
    # Returns a list of values corresponding to FIELDS.
    
    with open(filepath, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

    # Extract job_id from a specific <a> tag or fallback to filename
    job_id = None
    a_tag = soup.find('a', attrs={'data-control-id': True}, href=re.compile(r'/jobs/view/\d+/'))
    if a_tag:
        m = re.search(r'/jobs/view/(\d+)/', a_tag['href'])
        if m:
            job_id = m.group(1)
    if not job_id:
        # fallback: use filename (without extension)
        job_id = os.path.splitext(os.path.basename(filepath))[0]

    # Extract job title from <h1> or <h2>
    job_title = None
    h1 = soup.find('h1')
    if h1:
        job_title = h1.get_text(strip=True)
    if not job_title:
        h2 = soup.find('h2')
        if h2:
            job_title = h2.get_text(strip=True)

    # Extract company name from a specific <div> or sticky header
    company_name = None
    company_div = soup.find('div', class_='job-details-jobs-unified-top-card__company-name')
    if company_div:
        company_name = company_div.get_text(strip=True)
    if not company_name:
        # fallback: look for company in sticky header
        sticky = soup.find('div', class_='t-14 truncate')
        if sticky:
            parts = sticky.get_text(strip=True).split('·')
            if parts:
                company_name = parts[0].strip()

    # Extract location from sticky header or text
    location = None
    sticky = soup.find('div', class_='t-14 truncate')
    if sticky:
        parts = sticky.get_text(strip=True).split('·')
        if len(parts) > 1:
            location = parts[1].strip()
    if not location:
        m = re.search(r'Location:\s*([^\n<]+)', text)
        if m:
            location = m.group(1).strip()

    # Extract workplace type (Remote, Hybrid, On-site)
    workplace_type = None
    wt_span = soup.find('span', string=re.compile(r'Remote|Hybrid|On-site', re.I))
    if wt_span:
        workplace_type = wt_span.get_text(strip=True)
    else:
        if sticky and 'Remote' in sticky.get_text():
            workplace_type = 'Remote'
        elif sticky and 'Hybrid' in sticky.get_text():
            workplace_type = 'Hybrid'
        elif sticky and 'On-site' in sticky.get_text():
            workplace_type = 'On-site'

    # Extract employment type (Full-time, Internship, etc.)
    employment_type = None
    emp_type_span = soup.find('span', class_='ui-label text-body-small')
    if emp_type_span:
        employment_type = emp_type_span.get_text(strip=True)
    else:
        m = re.search(r'(Full[- ]?time|Internship|Contract|Part[- ]?time)', text, re.I)
        if m:
            employment_type = m.group(1)

    # Extract industry (if present)
    industry = None
    m = re.search(r'Industry:? ([^\n<]+)', text)
    if m:
        industry = m.group(1).strip()

    # Extract job description (cleaned plain text)
    job_desc_div = soup.find('div', id='job-details')
    job_description = clean_html(str(job_desc_div)) if job_desc_div else None

    # Extract seniority level (Entry, Manager, etc.)
    seniority_level = None
    m = re.search(r'(Entry level|Associate|Manager|Director|Executive)', text, re.I)
    if m:
        seniority_level = m.group(1)

    # Extract experience required (e.g., "2+ years experience")
    experience_required = None
    m = re.search(r'(\d+\+?\s*years? experience)', text, re.I)
    if m:
        experience_required = m.group(1)

    # Extract skills by searching for keywords in the job description
    skills = []
    skill_keywords = ['Python', 'SQL', 'Excel', 'Tableau', 'Power BI', 'R', 'Machine Learning', 'Data Analysis']
    if job_description:
        for skill in skill_keywords:
            if re.search(r'\b' + re.escape(skill) + r'\b', job_description, re.I):
                skills.append(skill)
    skills_str = ', '.join(skills) if skills else None

    # Extract salary or stipend range if present
    salary_range = None
    m = re.search(r'Stipend:\s*₹?([\d,]+)\s*-\s*₹?([\d,]+)', text)
    if m:
        salary_range = f"₹{m.group(1)} - ₹{m.group(2)}"
    else:
        m = re.search(r'Salary:\s*₹?([\d,]+)\s*-\s*₹?([\d,]+)', text)
        if m:
            salary_range = f"₹{m.group(1)} - ₹{m.group(2)}"

    # Return all extracted fields as a list
    return [
        job_id,
        job_title,
        company_name,
        location,
        workplace_type,
        employment_type,
        industry,
        job_description,
        seniority_level,
        experience_required,
        skills_str,
        salary_range
    ]

def main():
    """
    Main function to process all HTML files and write extracted data to CSV.
    """
    # Find all HTML files in the specified directory
    files = glob.glob(os.path.join(HTML_DIR, '*.html'))
    print(f"Looking for HTML files in: {HTML_DIR}")
    print(f"Found {len(files)} HTML files: {files}")
    # Open the output CSV file for writing
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(FIELDS)  # Write header row
        # Process each HTML file
        for filepath in files:
            row = extract_from_html(filepath)
            writer.writerow(row)
    print(f"Extracted {len(files)} files to {OUTPUT_CSV}")

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()