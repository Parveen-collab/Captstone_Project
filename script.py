import os
import glob
import csv
import re
from bs4 import BeautifulSoup

HTML_DIR = r'C:\Users\Parveen kumar\Downloads\web dev-20250701T182925Z-1-001\web dev'
OUTPUT_CSV = 'extracted_jobs12.csv'

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
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def extract_from_html(filepath):
    with open(filepath, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

    # job_id: extract from <a data-control-id ... href="/jobs/view/NUMBER/...
    job_id = None
    a_tag = soup.find('a', attrs={'data-control-id': True}, href=re.compile(r'/jobs/view/\d+/'))
    if a_tag:
        m = re.search(r'/jobs/view/(\d+)/', a_tag['href'])
        if m:
            job_id = m.group(1)
    if not job_id:
        # fallback: use filename (without extension)
        job_id = os.path.splitext(os.path.basename(filepath))[0]

    # job_title
    job_title = None
    h1 = soup.find('h1')
    if h1:
        job_title = h1.get_text(strip=True)
    if not job_title:
        h2 = soup.find('h2')
        if h2:
            job_title = h2.get_text(strip=True)

    # company_name
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

    # location
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

    # workplace_type
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

    # employment_type
    employment_type = None
    emp_type_span = soup.find('span', class_='ui-label text-body-small')
    if emp_type_span:
        employment_type = emp_type_span.get_text(strip=True)
    else:
        m = re.search(r'(Full[- ]?time|Internship|Contract|Part[- ]?time)', text, re.I)
        if m:
            employment_type = m.group(1)

    # industry (not always present)
    industry = None
    m = re.search(r'Industry:? ([^\n<]+)', text)
    if m:
        industry = m.group(1).strip()

    # job_description (full HTML, then clean to plain text)
    job_desc_div = soup.find('div', id='job-details')
    job_description = clean_html(str(job_desc_div)) if job_desc_div else None

    # seniority_level
    seniority_level = None
    m = re.search(r'(Entry level|Associate|Manager|Director|Executive)', text, re.I)
    if m:
        seniority_level = m.group(1)

    # experience_required
    experience_required = None
    m = re.search(r'(\d+\+?\s*years? experience)', text, re.I)
    if m:
        experience_required = m.group(1)

    # skills (extract keywords from description)
    skills = []
    skill_keywords = ['Python', 'SQL', 'Excel', 'Tableau', 'Power BI', 'R', 'Machine Learning', 'Data Analysis']
    if job_description:
        for skill in skill_keywords:
            if re.search(r'\b' + re.escape(skill) + r'\b', job_description, re.I):
                skills.append(skill)
    skills_str = ', '.join(skills) if skills else None

    # salary_range
    salary_range = None
    m = re.search(r'Stipend:\s*₹?([\d,]+)\s*-\s*₹?([\d,]+)', text)
    if m:
        salary_range = f"₹{m.group(1)} - ₹{m.group(2)}"
    else:
        m = re.search(r'Salary:\s*₹?([\d,]+)\s*-\s*₹?([\d,]+)', text)
        if m:
            salary_range = f"₹{m.group(1)} - ₹{m.group(2)}"

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
    files = glob.glob(os.path.join(HTML_DIR, '*.html'))
    print(f"Looking for HTML files in: {HTML_DIR}")
    print(f"Found {len(files)} HTML files: {files}")
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(FIELDS)
        for filepath in files:
            row = extract_from_html(filepath)
            writer.writerow(row)
    print(f"Extracted {len(files)} files to {OUTPUT_CSV}")

if __name__ == '__main__':
    main()