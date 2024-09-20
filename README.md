# HR Analytics Dashboard 

## General info
The project contains the analysis of employee attrition data and create an interactive dashboard using Power BI. The data for the project was prepared and cleaning using python.

The aim of the project is analysis of employees attrition data in example company to find out reasons which are most responsible for attrition. The dashboard is designed to help the HR team to interpreting data and analyzing the key factors to reduce the attrition rate. 

### Dataset
The dataset contains the details of the employee attrition (HR Employee Attrition) such as department, age, education field, job role, years at company etc. It comes from Kaggle and can be find [here](https://www.kaggle.com/datasets/itssuru/hr-employee-attrition). 

## Project includes:
- HR dashboard with Power BI - **HR_analytics.pbix**
- view the dashboard - HR_dashboard.jpg, HR_dashboard.pdf.
- python script to clean data - **clean_data.py**

## Visualizations:
The dashboard includes the following visualizations:
1. **Cards:** Displays total employees, count of attrition, average age of employees, average salary and average years at company.
2. **Gender:** Shows attrition rate by gender.
3. **Years at company:**  A line chart shows attrition level by years work at company.
4. **Job Role:**  A bar chart shows which job roles have the highest attrition rates.
5. **Salary:** A bar chart displays employees attrition by salary bracket.
6. **Education field**: A donut chart shows employees attrition by the education field.
7. **Age**: A bar chart displays the attrition of employees by age group.

## Insights generated
- Overview: The total number of employees is 1470 that 237 have left the company. On average the employees were 37 years old,  had worked for 7 years and had 6,5k salary. In employees were 882 male and 588 female.
- The most of employees attrition is in the first years of work.
- The four job roles such as Laboratory Technicians, Sales Executives, Research Scientists and Sales Representatives are with the highest attrition rates.
- A strong influence in employee attrition had salary below 5k. In this group observed the highest employess leaves. 
- Employees with educational backgrounds in life sciences and medical fields have higher index of attrition.
- The highest attrition rate is between the age group of 26-35 years. As the age increases attrition decreases.
- The higher attrition rate have male employees at all age groups.

## Technologies
The project is created with:
- Power BI,
- Python.

**Running the project:**

To use the dashboard:
- clone the repository or download .pbix file;
- open the file in Power BI Desktop;
- use the slicers to filter data by Department or other indicators.

### HR analytics dashboard view:

![Dashboard view](HR_dashboard.jpg)
