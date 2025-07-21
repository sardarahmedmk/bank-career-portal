import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import random
from datetime import datetime
import hashlib
import os
from typing import Dict, List

# Try to import from local files, with fallbacks
try:
    from job_descriptions import JOB_DESCRIPTIONS
except ImportError:
    # Fallback job descriptions data
    JOB_DESCRIPTIONS = [
        {
            "title": "Branch Manager",
            "department": "Retail Banking",
            "level": "Senior Management",
            "location": "Karachi",
            "salary_range": "PKR 200K-300K",
            "description": "Lead and manage branch operations, drive business growth, and ensure excellent customer service delivery.",
            "requirements": [
                "Master's degree in Business, Finance, or Banking",
                "8+ years of banking experience with 3+ years in management",
                "Strong leadership and team management skills",
                "Excellent communication and customer relationship skills",
                "Knowledge of banking regulations and compliance"
            ],
            "responsibilities": [
                "Manage daily branch operations and staff performance",
                "Develop and implement business growth strategies",
                "Ensure compliance with banking regulations and policies",
                "Build and maintain relationships with key customers",
                "Drive business growth through effective sales strategies"
            ],
            "skills": ["Leadership", "Sales Management", "Customer Relations", "Risk Management", "Team Building"],
            "benefits": ["Health Insurance", "Provident Fund", "Performance Bonus", "Car Allowance", "Medical Coverage"]
        },
        {
            "title": "Assistant Manager Operations",
            "department": "Operations",
            "level": "Middle Management",
            "location": "Lahore",
            "salary_range": "PKR 180K-250K",
            "description": "Support operational efficiency, process improvement, and quality assurance across various banking operations and services.",
            "requirements": [
                "Bachelor's degree in Business, Finance, or Operations Management",
                "4-6 years of banking or operations experience",
                "Strong analytical and problem-solving skills",
                "Process improvement and project management experience",
                "Proficiency in banking software and MS Office"
            ],
            "responsibilities": [
                "Monitor and improve operational processes and procedures",
                "Ensure compliance with internal controls and regulatory requirements",
                "Manage operational risks and implement mitigation strategies",
                "Coordinate with different departments for seamless operations",
                "Prepare operational reports and performance metrics"
            ],
            "skills": ["Operations Management", "Process Improvement", "Risk Assessment", "Project Management", "Data Analysis"],
            "benefits": ["Health Insurance", "Provident Fund", "Annual Bonus", "Training Programs", "Career Development"]
        },
        {
            "title": "Customer Relationship Officer",
            "department": "Customer Service",
            "level": "Entry Level",
            "location": "Islamabad",
            "salary_range": "PKR 80K-120K",
            "description": "Build and maintain strong relationships with customers, provide excellent service, and identify opportunities for business growth.",
            "requirements": [
                "Bachelor's degree in Business, Marketing, or related field",
                "1-3 years of customer service or sales experience",
                "Excellent communication and interpersonal skills",
                "Customer-focused mindset with problem-solving abilities",
                "Basic knowledge of banking products and services"
            ],
            "responsibilities": [
                "Handle customer inquiries and resolve issues effectively",
                "Promote and sell banking products and services",
                "Maintain accurate customer records and documentation",
                "Follow up with customers to ensure satisfaction",
                "Achieve sales targets and service quality metrics"
            ],
            "skills": ["Customer Service", "Sales", "Communication", "Problem Solving", "Relationship Building"],
            "benefits": ["Health Insurance", "Performance Incentives", "Training Programs", "Career Growth"]
        }
    ]

# Advanced Assessment System
class AdvancedAssessmentSystem:
    def __init__(self):
        self.database_dir = "hr_database"
        self.candidates_file = os.path.join(self.database_dir, "candidates.csv")
        self.assessments_file = os.path.join(self.database_dir, "assessments.csv")
        
        # Create database directory if it doesn't exist
        if not os.path.exists(self.database_dir):
            os.makedirs(self.database_dir)
        
        # Comprehensive question bank for assessments
        self.question_banks = {
            "Branch Manager": [
                {
                    "question": "What is the primary responsibility of a Branch Manager?",
                    "options": ["Only sales targets", "Overall branch operations and team management", "Customer complaints only", "Documentation"],
                    "correct": 1,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "Which financial ratio is most important for branch profitability analysis?",
                    "options": ["Current Ratio", "Return on Assets (ROA)", "Debt-to-Equity", "Inventory Turnover"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you handle a situation where your branch is consistently missing sales targets?",
                    "options": ["Blame the market", "Analyze performance data and implement improvement strategies", "Reduce staff", "Lower targets"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the key to effective team leadership in banking?",
                    "options": ["Strict rules only", "Communication, motivation, and performance monitoring", "Individual work", "Avoiding conflicts"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which compliance regulation is most critical for branch operations?",
                    "options": ["Tax laws only", "Anti-Money Laundering (AML) and KYC", "Employment laws", "Building codes"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you ensure customer satisfaction while maintaining profitability?",
                    "options": ["Focus only on profits", "Balance quality service with efficient operations", "Ignore profitability", "Reduce services"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                },
                {
                    "question": "What is the best approach to handle a major customer complaint?",
                    "options": ["Ignore it", "Listen, investigate, resolve, and follow up", "Transfer to head office", "Offer money immediately"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which metric best indicates branch performance?",
                    "options": ["Number of employees", "Customer satisfaction + financial targets achievement", "Building size", "Number of transactions"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you motivate underperforming team members?",
                    "options": ["Threaten termination", "Provide training, set clear goals, and regular feedback", "Ignore them", "Reduce their responsibilities"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the most effective way to increase branch deposits?",
                    "options": ["Force existing customers", "Develop relationship-based marketing and competitive products", "Reduce interest rates", "Limit services"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                },
                {
                    "question": "How do you ensure regulatory compliance in daily operations?",
                    "options": ["Ignore regulations", "Regular training, monitoring, and audit systems", "One-time training", "External consultants only"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is your approach to risk management in branch operations?",
                    "options": ["Avoid all risks", "Identify, assess, monitor, and mitigate risks systematically", "Accept all risks", "Transfer all risks"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                }
            ],
            "Assistant Manager Operations": [
                {
                    "question": "What is the primary focus of operations management in banking?",
                    "options": ["Sales only", "Process efficiency and quality control", "Marketing", "HR management"],
                    "correct": 1,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "Which tool is most effective for process improvement?",
                    "options": ["Guesswork", "Six Sigma and Lean methodologies", "Random changes", "External consultants"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you identify operational bottlenecks?",
                    "options": ["Ignore delays", "Data analysis and process mapping", "Ask customers only", "Guess the problems"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the key to effective vendor management?",
                    "options": ["Lowest price only", "Performance monitoring and relationship management", "No monitoring", "Multiple vendors for same service"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you ensure operational compliance?",
                    "options": ["Ignore policies", "Regular audits and process documentation", "One-time setup", "External audits only"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which metric best measures operational efficiency?",
                    "options": ["Number of employees", "Process completion time and error rates", "Office size", "Number of meetings"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you handle system downtime in critical operations?",
                    "options": ["Wait for IT", "Activate business continuity plan and backup procedures", "Close operations", "Ignore the issue"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                },
                {
                    "question": "What is the best approach to implement new operational procedures?",
                    "options": ["Force implementation", "Pilot testing, training, and gradual rollout", "Immediate full implementation", "Ignore change management"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you ensure quality control in banking operations?",
                    "options": ["No checks needed", "Regular quality audits and error tracking", "Customer complaints only", "Annual reviews only"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is your approach to cost optimization in operations?",
                    "options": ["Cut all costs", "Analyze cost-benefit and eliminate waste while maintaining quality", "Increase all costs", "Ignore costs"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                },
                {
                    "question": "How do you manage operational risks?",
                    "options": ["Ignore risks", "Risk assessment, mitigation plans, and monitoring", "Accept all risks", "External insurance only"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the key to successful cross-departmental coordination?",
                    "options": ["Work in isolation", "Clear communication and defined processes", "Avoid other departments", "Email only communication"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                }
            ],
            "Customer Relationship Officer": [
                {
                    "question": "What is the most important skill for a Customer Relationship Officer?",
                    "options": ["Technical knowledge only", "Active listening and empathy", "Sales pressure", "Product memorization"],
                    "correct": 1,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "How do you handle a customer who is upset about service charges?",
                    "options": ["Argue with them", "Listen, explain the policy, and find solutions within guidelines", "Ignore their concern", "Immediately waive all charges"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the best way to build long-term customer relationships?",
                    "options": ["One-time sales", "Consistent service, trust-building, and understanding needs", "Aggressive selling", "Minimal contact"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you identify cross-selling opportunities?",
                    "options": ["Random offers", "Analyze customer needs and financial goals", "Sell most expensive products", "Wait for customers to ask"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is your approach to handling customer complaints?",
                    "options": ["Deny responsibility", "Listen, investigate, resolve, and prevent recurrence", "Transfer to manager", "Ignore complaints"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you maintain customer confidentiality?",
                    "options": ["Share information freely", "Strict adherence to privacy policies and need-to-know basis", "Discuss with colleagues", "Post on social media"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the key to effective customer education about products?",
                    "options": ["Complex jargon", "Simple, clear explanations with relevant examples", "Quick information", "Technical details only"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you handle rejection when offering products?",
                    "options": ["Pressure the customer", "Understand reasons and maintain positive relationship", "Get angry", "Never offer again"],
                    "correct": 1,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "What is your strategy for customer retention?",
                    "options": ["Price cuts only", "Exceptional service, regular follow-up, and value addition", "Ignore existing customers", "Focus on new customers only"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you stay updated with banking products and services?",
                    "options": ["Never update", "Regular training, product manuals, and market research", "Ask customers", "Guess the features"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is your approach to managing customer expectations?",
                    "options": ["Overpromise", "Set realistic expectations and deliver consistently", "Underpromise", "Make no commitments"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "How do you measure success in customer relationship management?",
                    "options": ["Number of calls", "Customer satisfaction, retention, and business growth", "Time spent", "Number of products sold"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                }
            ],
            "Banking Fundamentals": [
                {
                    "question": "What is the primary function of a commercial bank?",
                    "options": ["Investment trading", "Accepting deposits and providing loans", "Insurance sales", "Real estate development"],
                    "correct": 1,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "What does KYC stand for in banking?",
                    "options": ["Know Your Customer", "Keep Your Cash", "Key Yield Calculation", "Know Your Credit"],
                    "correct": 0,
                    "points": 6,
                    "difficulty": "Easy"
                },
                {
                    "question": "Which document is NOT typically required for opening a bank account in Pakistan?",
                    "options": ["CNIC", "Utility bill", "Salary certificate", "Marriage certificate"],
                    "correct": 3,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "What is the current policy rate set by State Bank of Pakistan (approximate)?",
                    "options": ["10%", "15%", "22%", "25%"],
                    "correct": 2,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which ratio measures a bank's ability to meet short-term obligations?",
                    "options": ["Capital Adequacy Ratio", "Liquidity Coverage Ratio", "Profit Margin", "Return on Assets"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "What is the minimum Capital Adequacy Ratio required by SBP?",
                    "options": ["8%", "10%", "12%", "15%"],
                    "correct": 1,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which type of account typically offers the highest interest rate?",
                    "options": ["Current Account", "Savings Account", "Term Deposit", "Business Account"],
                    "correct": 2,
                    "points": 7,
                    "difficulty": "Easy"
                },
                {
                    "question": "What is the maximum amount insured by Deposit Protection Corporation (DPC) in Pakistan?",
                    "options": ["PKR 250,000", "PKR 500,000", "PKR 1,000,000", "PKR 2,000,000"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which of the following is a non-performing loan (NPL)?",
                    "options": ["Loan paid on time", "Loan overdue by 60 days", "Loan overdue by 90+ days", "Prepaid loan"],
                    "correct": 2,
                    "points": 8,
                    "difficulty": "Medium"
                },
                {
                    "question": "What does SWIFT stand for in international banking?",
                    "options": ["Secure Wire International Financial Transfer", "Society for Worldwide Interbank Financial Telecommunication", "Standard Wire International Fund Transfer", "Secure Worldwide International Financial Transfer"],
                    "correct": 1,
                    "points": 9,
                    "difficulty": "Medium"
                },
                {
                    "question": "Which is the central bank of Pakistan?",
                    "options": ["National Bank of Pakistan", "State Bank of Pakistan", "United Bank Limited", "Bank Alfalah"],
                    "correct": 1,
                    "points": 6,
                    "difficulty": "Easy"
                },
                {
                    "question": "What is the primary purpose of Anti-Money Laundering (AML) regulations?",
                    "options": ["Increase bank profits", "Prevent illegal money from entering the financial system", "Reduce customer service time", "Eliminate cash transactions"],
                    "correct": 1,
                    "points": 10,
                    "difficulty": "Hard"
                }
            ]
        }
    
    def get_questions(self, assessment_type: str, count: int = 12) -> List[Dict]:
        """Get random questions for assessment"""
        if assessment_type in self.question_banks:
            questions = self.question_banks[assessment_type]
            return random.sample(questions, min(count, len(questions)))
        return []
    
    def calculate_score(self, answers: Dict, questions: List[Dict]) -> float:
        """Calculate assessment score based on points"""
        if not questions:
            return 0
        
        total_points = 0
        earned_points = 0
        
        for i, question in enumerate(questions):
            total_points += question['points']
            if i in answers:
                selected_option = answers[i]
                correct_option = question['options'][question['correct']]
                if selected_option == correct_option:
                    earned_points += question['points']
        
        return (earned_points / total_points) * 100 if total_points > 0 else 0
    
    def save_application_to_database(self, application_data: Dict, assessment_score: float, questions: List[Dict], answers: Dict):
        """Save application and assessment data to HR database"""
        import csv
        import os
        
        # Ensure database directory exists
        os.makedirs(self.database_dir, exist_ok=True)
        
        # Generate unique application ID
        app_id = f"UBL-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
        
        # Determine status based on score
        if assessment_score >= 80:
            status = "Selected for Interview"
        elif assessment_score >= 70:
            status = "Under Review"
        else:
            status = "Not Selected"
        
        # Save to candidates.csv
        candidates_data = {
            'Application_ID': app_id,
            'Name': application_data.get('name', ''),
            'Email': application_data.get('email', ''),
            'Phone': application_data.get('phone', ''),
            'CNIC': application_data.get('cnic', ''),
            'Position': application_data.get('position', ''),
            'Department': application_data.get('department', ''),
            'Education': application_data.get('education', ''),
            'Experience': application_data.get('experience', ''),
            'Assessment_Score': f"{assessment_score:.1f}%",
            'Status': status,
            'Application_Date': application_data.get('submitted_date', ''),
            'Why_UBL': application_data.get('why_ubl', ''),
            'Availability': application_data.get('availability', ''),
            'Salary_Expectation': application_data.get('salary_expectation', '')
        }
        
        # Write to candidates CSV
        file_exists = os.path.isfile(self.candidates_file)
        with open(self.candidates_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=candidates_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(candidates_data)
        
        # Save detailed assessment to assessments.csv
        assessment_data = {
            'Application_ID': app_id,
            'Candidate_Name': application_data.get('name', ''),
            'Position': application_data.get('position', ''),
            'Assessment_Type': self.get_assessment_type(application_data.get('position', '')),
            'Total_Questions': len(questions),
            'Correct_Answers': sum(1 for i, q in enumerate(questions) if i in answers and answers[i] == q['options'][q['correct']]),
            'Score_Percentage': f"{assessment_score:.1f}%",
            'Total_Points_Possible': sum(q['points'] for q in questions),
            'Points_Earned': sum(q['points'] for i, q in enumerate(questions) if i in answers and answers[i] == q['options'][q['correct']]),
            'Duration_Minutes': random.randint(15, 35),  # Simulated duration
            'Completion_Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Status': status,
            'Detailed_Answers': str(answers)  # Store answers as string
        }
        
        # Write to assessments CSV
        file_exists = os.path.isfile(self.assessments_file)
        with open(self.assessments_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=assessment_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(assessment_data)
        
        return app_id
    
    def get_assessment_type(self, job_title: str) -> str:
        """Determine assessment type based on job title"""
        if "Branch Manager" in job_title:
            return "Branch Manager"
        elif "Assistant Manager Operations" in job_title or "Operations" in job_title:
            return "Assistant Manager Operations"
        elif "Customer Relationship Officer" in job_title or "Customer" in job_title:
            return "Customer Relationship Officer"
        else:
            return "Banking Fundamentals"

# HR Credentials for production use
HR_CREDENTIALS = {
    "hr.manager@ublbank.com": "UBL@Hr2024!",
    "admin.hr@ublbank.com": "Admin@UBL123",
    "recruitment@ublbank.com": "Recruit@2024",
    "hr.director@ublbank.com": "Director@UBL2024"
}

def check_hr_authentication():
    """Check if user is authenticated as HR manager"""
    return st.session_state.get('hr_authenticated', False)

def hash_password(password):
    """Simple password hashing for demo"""
    return hashlib.sha256(password.encode()).hexdigest()

# Page config
st.set_page_config(
    page_title="UBL Bank Careers Portal",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS styling with colorful design and perfect text visibility
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #a8edea 0%, #fed6e3 100%) !important;
        backdrop-filter: blur(15px) !important;
    }
    
    [data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #a8edea 0%, #fed6e3 100%) !important;
        backdrop-filter: blur(15px) !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.9) !important;
        color: #2d3748 !important;
        backdrop-filter: blur(15px) !important;
    }
    
    /* Perfect Text Visibility */
    h1, h2, h3, h4, h5, h6 {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8) !important;
    }
    
    p, div, span, label, .stMarkdown {
        color: #2d3748 !important;
        font-weight: 500 !important;
        text-shadow: 1px 1px 1px rgba(255,255,255,0.7) !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {
        color: #1a202c !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8) !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        margin: 1rem 0;
        color: #1a202c !important;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        margin: 1rem 0;
        transition: transform 0.3s ease;
        color: #1a202c !important;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #a8edea 100%);
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        color: #1a202c !important;
    }
    
    .card {
        background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.6);
        transition: transform 0.3s ease;
        color: #1a202c !important;
    }
    
    .card:hover {
        transform: translateY(-5px);
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.7);
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 25px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #f093fb 0%, #764ba2 50%, #667eea 100%);
    }
    
    /* Form Styling with better visibility */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background: rgba(255,255,255,0.95) !important;
        color: #1a202c !important;
        border: 2px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
    }
    
    /* Radio buttons and checkboxes */
    .stRadio > div, .stCheckbox > div {
        color: #1a202c !important;
        font-weight: 600 !important;
        text-shadow: 1px 1px 1px rgba(255,255,255,0.8) !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    }
    
    /* Info boxes with colors */
    .stInfo {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%) !important;
        color: #1a202c !important;
        border-left: 4px solid #667eea !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%) !important;
        color: #1a202c !important;
        border-left: 4px solid #22c55e !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
        color: #1a202c !important;
        border-left: 4px solid #f59e0b !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%) !important;
        color: #1a202c !important;
        border-left: 4px solid #ef4444 !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
        color: #1a202c !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%) !important;
        color: #1a202c !important;
        border-radius: 15px !important;
    }
    
    /* Dataframe styling */
    .dataframe {
        background: rgba(255,255,255,0.95) !important;
        color: #1a202c !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

def show_home():
    """Clean and beautiful home page"""
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 style="font-size: 3.5rem; margin-bottom: 1rem; color: #1a202c;">
            Welcome to UBL Bank Careers 🏦
        </h1>
        <p style="font-size: 1.3rem; margin-bottom: 2rem; color: #2d3748;">
            Your gateway to a successful banking career in Pakistan's leading financial institution
        </p>
        <div style="margin-top: 2rem;">
            <a href="#jobs" class="btn-primary">View Open Positions</a>
            <a href="#apply" class="btn-primary">Apply Now</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown("## 🌟 Why Choose UBL Bank?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1a202c; text-align: center;">🚀 Career Growth</h3>
            <p style="color: #2d3748;">
                Fast-track your career with comprehensive training programs, 
                mentorship opportunities, and clear advancement paths.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1a202c; text-align: center;">💰 Competitive Benefits</h3>
            <p style="color: #2d3748;">
                Enjoy attractive compensation packages, health insurance, 
                performance bonuses, and comprehensive employee benefits.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1a202c; text-align: center;">🌍 Innovation & Technology</h3>
            <p style="color: #2d3748;">
                Work with cutting-edge technology and contribute to digital 
                transformation in Pakistan's banking sector.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("## 📊 UBL Bank at a Glance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h2>1400+</h2>
            <p>Branches Nationwide</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h2>25,000+</h2>
            <p>Dedicated Employees</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h2>75+</h2>
            <p>Years of Excellence</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <h2>#1</h2>
            <p>Private Bank in Pakistan</p>
        </div>
        """, unsafe_allow_html=True)

def show_jobs():
    """Enhanced job listings with filtering and detailed descriptions"""
    st.markdown("## 📋 Available Positions")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        departments = ["All"] + list(set([job['department'] for job in JOB_DESCRIPTIONS]))
        selected_dept = st.selectbox("Filter by Department", departments)
    
    with col2:
        levels = ["All"] + list(set([job['level'] for job in JOB_DESCRIPTIONS]))
        selected_level = st.selectbox("Filter by Level", levels)
    
    with col3:
        locations = ["All"] + list(set([job['location'] for job in JOB_DESCRIPTIONS]))
        selected_location = st.selectbox("Filter by Location", locations)
    
    # Filter jobs
    filtered_jobs = JOB_DESCRIPTIONS
    if selected_dept != "All":
        filtered_jobs = [job for job in filtered_jobs if job['department'] == selected_dept]
    if selected_level != "All":
        filtered_jobs = [job for job in filtered_jobs if job['level'] == selected_level]
    if selected_location != "All":
        filtered_jobs = [job for job in filtered_jobs if job['location'] == selected_location]
    
    st.markdown(f"**Found {len(filtered_jobs)} positions matching your criteria**")
    
    # Display jobs
    for i, job in enumerate(filtered_jobs):
        with st.expander(f"🎯 {job['title']} - {job['department']} ({job['location']})"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**📝 Description:**")
                st.write(job['description'])
                
                st.markdown(f"**💼 Key Requirements:**")
                for req in job['requirements']:
                    st.write(f"• {req}")
                
                st.markdown(f"**🎯 Responsibilities:**")
                for resp in job['responsibilities']:
                    st.write(f"• {resp}")
                
            with col2:
                st.markdown(f"**💰 Salary Range:** {job['salary_range']}")
                st.markdown(f"**📍 Location:** {job['location']}")
                st.markdown(f"**🏢 Department:** {job['department']}")
                st.markdown(f"**📊 Level:** {job['level']}")
                
                st.markdown("**🛠️ Required Skills:**")
                for skill in job['skills']:
                    st.write(f"• {skill}")
                
                st.markdown("**🎁 Benefits:**")
                for benefit in job['benefits']:
                    st.write(f"• {benefit}")
                
                if st.button(f"Apply for this position", key=f"job_apply_{i}"):
                    st.session_state.selected_job = job
                    st.success(f"✅ Selected: {job['title']}. Please go to 'Apply Now' section to complete your application.")

def show_apply():
    """Integrated application and assessment process"""
    
    # Initialize session state
    if 'application_stage' not in st.session_state:
        st.session_state.application_stage = 'job_selection'
    if 'application_data' not in st.session_state:
        st.session_state.application_data = {}
    if 'assessment_system' not in st.session_state:
        st.session_state.assessment_system = AdvancedAssessmentSystem()
    
    # Progress indicator
    stages = ["📋 Job Selection", "👤 Application Form", "📝 Assessment", "✅ Results"]
    current_stage_index = ['job_selection', 'application_form', 'assessment', 'results'].index(st.session_state.application_stage)
    
    st.markdown("## 🚀 Apply for Your Dream Job")
    
    # Progress bar
    cols = st.columns(len(stages))
    for i, stage in enumerate(stages):
        with cols[i]:
            if i < current_stage_index:
                st.markdown(f"✅ {stage}")
            elif i == current_stage_index:
                st.markdown(f"🔄 **{stage}**")
            else:
                st.markdown(f"⏳ {stage}")
    
    st.markdown("---")
    
    # Stage 1: Job Selection
    if st.session_state.application_stage == 'job_selection':
        st.markdown("### 📋 Select Position")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Job cards
            for i, job in enumerate(JOB_DESCRIPTIONS):
                with st.container():
                    st.markdown(f"""
                    <div class="feature-card">
                        <h3 style="color: #1a202c; margin-bottom: 0.5rem;">{job['title']}</h3>
                        <p style="color: #2d3748; margin-bottom: 0.5rem;"><strong>Department:</strong> {job['department']}</p>
                        <p style="color: #2d3748; margin-bottom: 0.5rem;"><strong>Location:</strong> {job['location']}</p>
                        <p style="color: #2d3748; margin-bottom: 0.5rem;"><strong>Level:</strong> {job['level']}</p>
                        <p style="color: #2d3748; margin-bottom: 1rem;"><strong>Salary:</strong> {job['salary_range']}</p>
                        <p style="color: #666;">{job['description'][:100]}...</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"Apply for {job['title']}", key=f"apply_{i}"):
                        st.session_state.selected_job = job
                        st.session_state.application_stage = 'application_form'
                        st.rerun()
        
        with col2:
            st.markdown("### 💡 Application Tips")
            st.info("""
            **Before you apply:**
            • Prepare your updated CV/Resume
            • Have your documents ready
            • Review the job requirements
            • Complete the assessment carefully
            
            **Assessment will include:**
            • Role-specific questions
            • Banking knowledge
            • Situational scenarios
            """)
    
    # Stage 2: Application Form
    elif st.session_state.application_stage == 'application_form':
        selected_job = st.session_state.selected_job
        
        st.markdown(f"### 👤 Application for {selected_job['title']}")
        
        with st.form("application_form", clear_on_submit=False):
            # Personal Information
            st.markdown("#### Personal Information")
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name *", placeholder="Enter your first name")
                email = st.text_input("Email Address *", placeholder="your.email@example.com")
                phone = st.text_input("Phone Number *", placeholder="+92 300 1234567")
                
            with col2:
                last_name = st.text_input("Last Name *", placeholder="Enter your last name")
                cnic = st.text_input("CNIC *", placeholder="12345-1234567-1")
                city = st.selectbox("City *", ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan", "Other"])
            
            # Education & Experience
            st.markdown("#### Education & Experience")
            col1, col2 = st.columns(2)
            with col1:
                education = st.selectbox("Highest Education *", 
                    ["Bachelor's Degree", "Master's Degree", "PhD", "Professional Certification"])
                field_of_study = st.text_input("Field of Study *", placeholder="e.g., Finance, Business Administration")
                
            with col2:
                experience_years = st.selectbox("Years of Experience *", 
                    ["0-1 years", "1-3 years", "3-5 years", "5-10 years", "10+ years"])
                current_position = st.text_input("Current Position", placeholder="Your current job title")
            
            # Documents
            st.markdown("#### Documents")
            resume = st.file_uploader("Upload Resume/CV *", type=['pdf', 'doc', 'docx'])
            
            # Additional Information
            st.markdown("#### Additional Information")
            why_ubl = st.text_area("Why do you want to join UBL Bank? *", 
                                  placeholder="Tell us about your motivation...", height=100)
            
            # Availability
            col1, col2 = st.columns(2)
            with col1:
                availability = st.selectbox("When can you start? *", 
                    ["Immediately", "2 weeks notice", "1 month notice", "2 months notice"])
            with col2:
                salary_expectation = st.text_input("Salary Expectation (PKR)", placeholder="e.g., 150,000")
            
            # Consent
            consent_data = st.checkbox("I consent to the processing of my personal data *")
            consent_communication = st.checkbox("I agree to receive communications *")
            
            submitted = st.form_submit_button("📝 Proceed to Assessment", type="primary")
            
            if submitted:
                if not all([first_name, last_name, email, phone, cnic, education, field_of_study, 
                           why_ubl, consent_data, consent_communication]):
                    st.error("❌ Please fill in all required fields marked with *")
                elif not resume:
                    st.error("❌ Please upload your resume/CV")
                else:
                    # Save application data
                    st.session_state.application_data = {
                        'name': f"{first_name} {last_name}",
                        'email': email,
                        'phone': phone,
                        'cnic': cnic,
                        'position': selected_job['title'],
                        'department': selected_job['department'],
                        'education': education,
                        'experience': experience_years,
                        'why_ubl': why_ubl,
                        'availability': availability,
                        'salary_expectation': salary_expectation,
                        'submitted_date': datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    
                    st.session_state.application_stage = 'assessment'
                    st.session_state.question_index = 0
                    st.session_state.answers = {}
                    st.success("✅ Application submitted! Proceeding to assessment...")
                    st.rerun()
        
        # Back button
        if st.button("⬅️ Back to Job Selection"):
            st.session_state.application_stage = 'job_selection'
            st.rerun()
    
    # Stage 3: Assessment
    elif st.session_state.application_stage == 'assessment':
        selected_job = st.session_state.selected_job
        applicant_name = st.session_state.application_data.get('name', 'Applicant')
        
        st.markdown(f"### 📝 Assessment for {selected_job['title']}")
        st.markdown(f"**Applicant:** {applicant_name}")
        
        # Determine assessment type based on specific job title
        assessment_type = "Banking Fundamentals"  # Default fallback
        
        job_title = selected_job['title']
        if "Branch Manager" in job_title:
            assessment_type = "Branch Manager"
        elif "Assistant Manager Operations" in job_title or "Operations" in job_title:
            assessment_type = "Assistant Manager Operations"
        elif "Customer Relationship Officer" in job_title or "Customer" in job_title:
            assessment_type = "Customer Relationship Officer"
        elif "Risk" in job_title:
            assessment_type = "Banking Fundamentals"  # Can be expanded later
        elif "IT" in job_title:
            assessment_type = "Banking Fundamentals"  # Can be expanded later
        
        st.info(f"📋 **Assessment Type:** {assessment_type}")
        st.info(f"🎯 **Assessment Details:** 12 questions covering role-specific competencies")
        
        # Initialize assessment
        if 'current_questions' not in st.session_state:
            st.session_state.current_questions = st.session_state.assessment_system.get_questions(assessment_type, 12)
        if 'question_index' not in st.session_state:
            st.session_state.question_index = 0
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
        
        questions = st.session_state.current_questions
        total_questions = len(questions)
        current_q = st.session_state.question_index
        
        if total_questions > 0 and current_q < total_questions:
            # Progress
            progress = (current_q + 1) / total_questions
            st.progress(progress)
            st.markdown(f"**Question {current_q + 1} of {total_questions}**")
            
            question = questions[current_q]
            
            st.markdown(f"### {question['question']}")
            
            answer = st.radio(
                "Select your answer:",
                question['options'],
                key=f"q_{current_q}"
            )
            
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if st.button("⬅️ Previous", disabled=(current_q == 0)):
                    st.session_state.question_index -= 1
                    st.rerun()
            
            with col2:
                if current_q < total_questions - 1:
                    if st.button("Next ➡️"):
                        st.session_state.answers[current_q] = answer
                        st.session_state.question_index += 1
                        st.rerun()
                else:
                    if st.button("🏁 Finish Assessment"):
                        st.session_state.answers[current_q] = answer
                        st.session_state.application_stage = 'results'
                        st.rerun()
            
            with col3:
                if st.button("⬅️ Back to Application"):
                    st.session_state.application_stage = 'application_form'
                    st.rerun()
        
        else:
            st.error("No questions available for this assessment.")
    
    # Stage 4: Results
    elif st.session_state.application_stage == 'results':
        selected_job = st.session_state.selected_job
        applicant_data = st.session_state.application_data
        
        # Calculate score
        questions = st.session_state.current_questions
        score = st.session_state.assessment_system.calculate_score(st.session_state.answers, questions)
        
        # Save to HR database
        if 'application_saved' not in st.session_state:
            application_id = st.session_state.assessment_system.save_application_to_database(
                applicant_data, score, questions, st.session_state.answers
            )
            st.session_state.application_id = application_id
            st.session_state.application_saved = True
        
        st.markdown("### 🎉 Application & Assessment Complete!")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown(f"""
            <div class="metric-card" style="text-align: center;">
                <h2 style="color: #1a202c;">Assessment Results</h2>
                <h1 style="color: #1a202c; font-size: 3rem;">{score:.0f}%</h1>
                <p style="color: #2d3748;">Score for {selected_job['title']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Determine result based on score
        if score >= 80:
            st.success("🎉 **Congratulations! You have been SELECTED for Interview!**")
            st.balloons()
            result_status = "Selected for Interview"
            next_step = "HR will contact you within 2-3 business days to schedule your interview."
        elif score >= 70:
            st.info("👍 **Good Performance! Application Under Review**")
            result_status = "Under Review"
            next_step = "Your application will be reviewed by HR team. You may be contacted for further evaluation."
        else:
            st.warning("📚 **Thank you for your interest. We encourage you to apply again in the future.**")
            result_status = "Not Selected"
            next_step = "Consider gaining more experience and applying again after 6 months."
        
        # Display detailed results
        st.markdown("### 📊 Application Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **👤 Applicant Information:**
            - **Name:** {applicant_data['name']}
            - **Email:** {applicant_data['email']}
            - **Position:** {selected_job['title']}
            - **Department:** {selected_job['department']}
            """)
        
        with col2:
            st.markdown(f"""
            **📋 Application Status:**
            - **Score:** {score:.0f}%
            - **Status:** {result_status}
            - **Application ID:** {st.session_state.get('application_id', 'Processing...')}
            - **Date:** {applicant_data['submitted_date']}
            - **Saved to HR Database:** ✅ Yes
            """)
        
        st.info(f"**Next Steps:** {next_step}")
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📧 Email Results"):
                st.success("Results sent to your email!")
        
        with col2:
            if st.button("📱 SMS Notification"):
                st.success("SMS notification sent!")
        
        with col3:
            if st.button("🆕 New Application"):
                # Reset application state
                st.session_state.application_stage = 'job_selection'
                st.session_state.application_data = {}
                if 'current_questions' in st.session_state:
                    del st.session_state.current_questions
                if 'question_index' in st.session_state:
                    del st.session_state.question_index
                if 'answers' in st.session_state:
                    del st.session_state.answers
                if 'application_saved' in st.session_state:
                    del st.session_state.application_saved
                if 'application_id' in st.session_state:
                    del st.session_state.application_id
                st.rerun()

def show_hr_dashboard():
    """Enhanced HR Dashboard with candidate overview and export functionality"""
    st.markdown("## 📊 HR Dashboard")
    
    # Welcome message
    hr_email = st.session_state.get('hr_email', 'HR Manager')
    st.markdown(f"""
    <div class="hero-section">
        <h2 style="color: #1a202c;">Welcome back, {hr_email}! 👋</h2>
        <p style="color: #2d3748;">Here's your recruitment overview for today</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load real data from database
    assessment_system = st.session_state.assessment_system
    candidates_data = []
    assessments_data = []
    
    try:
        import csv
        # Load candidates data
        if os.path.exists(assessment_system.candidates_file):
            with open(assessment_system.candidates_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                candidates_data = list(reader)
        
        # Load assessments data
        if os.path.exists(assessment_system.assessments_file):
            with open(assessment_system.assessments_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                assessments_data = list(reader)
    except Exception as e:
        st.warning(f"Could not load data: {e}")
    
    # Calculate real metrics
    total_applications = len(candidates_data)
    if candidates_data:
        # Count different statuses (handle various column names)
        selected_count = 0
        under_review_count = 0
        assessments_completed = 0
        
        for candidate in candidates_data:
            status = candidate.get('status', candidate.get('Status', 'Unknown')).lower()
            if 'selected' in status or 'interview' in status:
                selected_count += 1
            elif 'review' in status:
                under_review_count += 1
        
        assessments_completed = len(assessments_data)
        
        # Calculate average score
        avg_score = 0
        if assessments_data:
            scores = []
            for assessment in assessments_data:
                score_str = assessment.get('score', assessment.get('overall_score', '0'))
                try:
                    # Handle percentage format
                    if isinstance(score_str, str):
                        score_val = float(score_str.replace('%', ''))
                    else:
                        score_val = float(score_str)
                    scores.append(score_val)
                except:
                    continue
            avg_score = sum(scores) / len(scores) if scores else 0
    else:
        selected_count = 0
        under_review_count = 0
        assessments_completed = 0
        avg_score = 0
    
    # Key Metrics with real data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #1a202c; font-size: 2.5rem;">{total_applications}</h2>
            <p style="color: #2d3748; font-weight: 600;">Total Applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #1a202c; font-size: 2.5rem;">{selected_count}</h2>
            <p style="color: #2d3748; font-weight: 600;">Selected for Interview</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #1a202c; font-size: 2.5rem;">{assessments_completed}</h2>
            <p style="color: #2d3748; font-weight: 600;">Assessments Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <h2 style="color: #1a202c; font-size: 2.5rem;">{avg_score:.1f}%</h2>
            <p style="color: #2d3748; font-weight: 600;">Average Score</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Applications Section
    st.markdown("### 👥 Recent Applications")
    
    if candidates_data:
        # Show recent candidates with assessment status
        recent_candidates = candidates_data[-5:]  # Last 5 applications
        
        for candidate in reversed(recent_candidates):  # Show newest first
            candidate_name = candidate.get('name', candidate.get('Name', 'Unknown'))
            candidate_position = candidate.get('position', candidate.get('Position', 'Unknown'))
            candidate_email = candidate.get('email', candidate.get('Email', 'Unknown'))
            candidate_status = candidate.get('status', candidate.get('Status', 'Unknown'))
            application_date = candidate.get('application_date', candidate.get('Application_Date', 'Unknown'))
            
            # Get assessment score
            assessment_score = "Pending"
            for assessment in assessments_data:
                if (assessment.get('candidate_id') == candidate.get('candidate_id') or 
                    assessment.get('Application_ID') == candidate.get('Application_ID')):
                    assessment_score = assessment.get('score', assessment.get('overall_score', 'N/A'))
                    break
            
            # Status color coding
            if 'selected' in candidate_status.lower() or 'interview' in candidate_status.lower():
                status_color = "#22c55e"
                status_icon = "✅"
            elif 'review' in candidate_status.lower():
                status_color = "#f59e0b"
                status_icon = "⏳"
            elif 'failed' in candidate_status.lower() or 'not selected' in candidate_status.lower():
                status_color = "#ef4444"
                status_icon = "❌"
            else:
                status_color = "#3b82f6"
                status_icon = "📝"
            
            st.markdown(f"""
            <div class="feature-card" style="margin: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="flex: 1;">
                        <strong style="color: #1a202c; font-size: 1.1rem;">{candidate_name}</strong><br>
                        <span style="color: #2d3748;">📧 {candidate_email}</span><br>
                        <span style="color: #2d3748;">💼 {candidate_position}</span>
                    </div>
                    <div style="flex: 1; text-align: center;">
                        <span style="color: #1a202c;"><strong>Assessment Score:</strong></span><br>
                        <span style="color: #2d3748; font-size: 1.2rem; font-weight: bold;">{assessment_score}</span>
                    </div>
                    <div style="flex: 1; text-align: center;">
                        <span style="color: #1a202c;"><strong>Applied:</strong></span><br>
                        <span style="color: #2d3748;">{application_date}</span>
                    </div>
                    <div style="text-align: right;">
                        <div style="
                            background: {status_color};
                            color: white;
                            padding: 0.5rem 1rem;
                            border-radius: 10px;
                            font-weight: bold;
                            display: inline-block;
                        ">
                            {status_icon} {candidate_status}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Export functionality
        st.markdown("### 📊 Data Export")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Export Candidates to Excel"):
                export_candidates_to_excel(candidates_data)
        
        with col2:
            if st.button("📈 Export Assessments to Excel"):
                export_assessments_to_excel(assessments_data)
        
        with col3:
            if st.button("📋 Export Combined Report"):
                export_combined_report(candidates_data, assessments_data)
    
    else:
        st.info("📝 No applications yet. Start by having candidates apply through the 'Apply Now' section.")
    
    # Charts and Analytics (if data available)
    if candidates_data and len(candidates_data) > 0:
        st.markdown("### 📈 Analytics")
        col1, col2 = st.columns(2)
        
        with col1:
            # Position distribution
            positions = [candidate.get('position', candidate.get('Position', 'Unknown')) for candidate in candidates_data]
            position_counts = {}
            for pos in positions:
                position_counts[pos] = position_counts.get(pos, 0) + 1
            
            if position_counts:
                fig = px.pie(
                    values=list(position_counts.values()), 
                    names=list(position_counts.keys()),
                    title="Applications by Position"
                )
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Status distribution
            statuses = [candidate.get('status', candidate.get('Status', 'Unknown')) for candidate in candidates_data]
            status_counts = {}
            for status in statuses:
                status_counts[status] = status_counts.get(status, 0) + 1
            
            if status_counts:
                fig = px.bar(
                    x=list(status_counts.keys()),
                    y=list(status_counts.values()),
                    title="Application Status Distribution"
                )
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True)

def export_candidates_to_excel(candidates_data):
    """Export candidates data to Excel file"""
    try:
        import pandas as pd
        from io import BytesIO
        
        if not candidates_data:
            st.warning("No candidate data to export")
            return
        
        # Create DataFrame
        df = pd.DataFrame(candidates_data)
        
        # Create Excel file in memory
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Candidates', index=False)
            
            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Candidates']
            
            # Add formatting
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#4472C4',
                'font_color': 'white',
                'border': 1
            })
            
            # Write headers with formatting
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)
            
            # Auto-adjust column widths
            for i, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.set_column(i, i, min(max_len, 50))
        
        buffer.seek(0)
        
        # Create download button
        st.download_button(
            label="📥 Download Candidates Excel",
            data=buffer.getvalue(),
            file_name=f"UBL_Candidates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.success("✅ Candidates data ready for download!")
        
    except Exception as e:
        st.error(f"Error creating Excel file: {e}")

def export_assessments_to_excel(assessments_data):
    """Export assessments data to Excel file"""
    try:
        import pandas as pd
        from io import BytesIO
        
        if not assessments_data:
            st.warning("No assessment data to export")
            return
        
        # Create DataFrame
        df = pd.DataFrame(assessments_data)
        
        # Create Excel file in memory
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Assessments', index=False)
            
            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Assessments']
            
            # Add formatting
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#70AD47',
                'font_color': 'white',
                'border': 1
            })
            
            # Write headers with formatting
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)
            
            # Auto-adjust column widths
            for i, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.set_column(i, i, min(max_len, 50))
        
        buffer.seek(0)
        
        # Create download button
        st.download_button(
            label="📊 Download Assessments Excel",
            data=buffer.getvalue(),
            file_name=f"UBL_Assessments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.success("✅ Assessments data ready for download!")
        
    except Exception as e:
        st.error(f"Error creating Excel file: {e}")

def export_combined_report(candidates_data, assessments_data):
    """Export combined report with candidates and assessments"""
    try:
        import pandas as pd
        from io import BytesIO
        
        # Create Excel file in memory
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            
            # Candidates sheet
            if candidates_data:
                candidates_df = pd.DataFrame(candidates_data)
                candidates_df.to_excel(writer, sheet_name='Candidates', index=False)
                
                # Format candidates sheet
                workbook = writer.book
                worksheet = writer.sheets['Candidates']
                header_format = workbook.add_format({
                    'bold': True, 'fg_color': '#4472C4', 'font_color': 'white', 'border': 1
                })
                for col_num, value in enumerate(candidates_df.columns.values):
                    worksheet.write(0, col_num, value, header_format)
            
            # Assessments sheet
            if assessments_data:
                assessments_df = pd.DataFrame(assessments_data)
                assessments_df.to_excel(writer, sheet_name='Assessments', index=False)
                
                # Format assessments sheet
                worksheet2 = writer.sheets['Assessments']
                header_format2 = workbook.add_format({
                    'bold': True, 'fg_color': '#70AD47', 'font_color': 'white', 'border': 1
                })
                for col_num, value in enumerate(assessments_df.columns.values):
                    worksheet2.write(0, col_num, value, header_format2)
            
            # Summary sheet
            summary_data = {
                'Metric': ['Total Applications', 'Assessments Completed', 'Average Score', 'Selected for Interview'],
                'Value': [
                    len(candidates_data),
                    len(assessments_data),
                    f"{sum([float(str(a.get('score', 0)).replace('%', '')) for a in assessments_data]) / len(assessments_data) if assessments_data else 0:.1f}%",
                    len([c for c in candidates_data if 'selected' in str(c.get('status', '')).lower()])
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Format summary sheet
            worksheet3 = writer.sheets['Summary']
            header_format3 = workbook.add_format({
                'bold': True, 'fg_color': '#E74C3C', 'font_color': 'white', 'border': 1
            })
            for col_num, value in enumerate(summary_df.columns.values):
                worksheet3.write(0, col_num, value, header_format3)
        
        buffer.seek(0)
        
        # Create download button
        st.download_button(
            label="📋 Download Combined Report",
            data=buffer.getvalue(),
            file_name=f"UBL_Complete_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.success("✅ Combined report ready for download!")
        
    except Exception as e:
        st.error(f"Error creating combined report: {e}")

def show_hr_candidates():
    """HR Candidates Management with real database data"""
    st.markdown("## 👥 Candidate Management")
    
    # Load real candidate data from CSV
    candidates_data = []
    assessment_system = st.session_state.assessment_system
    
    try:
        import csv
        if os.path.exists(assessment_system.candidates_file):
            with open(assessment_system.candidates_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                candidates_data = list(reader)
    except Exception as e:
        st.warning(f"Could not load candidate data: {e}")
        candidates_data = []
    
    if not candidates_data:
        st.info("📝 No applications submitted yet. Candidates will appear here after completing assessments.")
        
        # Show sample empty state
        st.markdown("### 📊 What you'll see here:")
        st.markdown("""
        - **Real candidate applications** from the Apply Now section
        - **Assessment scores and results** automatically saved
        - **Complete candidate profiles** with contact information
        - **Filtering and search capabilities** by status, position, score
        - **Interview scheduling tools** and communication features
        """)
        return
    
    # Convert to DataFrame for easier handling
    df = pd.DataFrame(candidates_data)
    
    # Ensure required columns exist
    required_columns = ['Status', 'Position', 'Assessment_Score', 'Name', 'Email', 'Phone', 
                       'CNIC', 'Department', 'Education', 'Application_Date', 'Application_ID']
    
    for col in required_columns:
        if col not in df.columns:
            df[col] = 'N/A'
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            status_options = ["All"] + [status for status in df['Status'].unique() if pd.notna(status)]
            status_filter = st.selectbox("Filter by Status", status_options)
        except:
            status_filter = "All"
    
    with col2:
        try:
            position_options = ["All"] + [pos for pos in df['Position'].unique() if pd.notna(pos)]
            position_filter = st.selectbox("Filter by Position", position_options)
        except:
            position_filter = "All"
    
    with col3:
        try:
            # Extract numeric score for filtering
            df['Score_Numeric'] = df['Assessment_Score'].str.replace('%', '').str.replace('N/A', '0').astype(float)
            score_filter = st.slider("Minimum Score", 0, 100, 0)
        except:
            df['Score_Numeric'] = 0
            score_filter = st.slider("Minimum Score", 0, 100, 0)
    
    # Apply filters
    filtered_df = df.copy()
    if status_filter != "All":
        filtered_df = filtered_df[filtered_df['Status'] == status_filter]
    if position_filter != "All":
        filtered_df = filtered_df[filtered_df['Position'] == position_filter]
    filtered_df = filtered_df[filtered_df['Score_Numeric'] >= score_filter]
    
    st.markdown(f"**Found {len(filtered_df)} candidates**")
    
    # Candidate cards
    for idx, candidate in filtered_df.iterrows():
        candidate_name = candidate.get('Name', 'Unknown')
        candidate_position = candidate.get('Position', 'Unknown')
        candidate_score = candidate.get('Assessment_Score', '0%')
        
        with st.expander(f"👤 {candidate_name} - {candidate_position} (Score: {candidate_score})"):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"**📧 Email:** {candidate.get('Email', 'N/A')}")
                st.markdown(f"**📱 Phone:** {candidate.get('Phone', 'N/A')}")
                st.markdown(f"**🆔 CNIC:** {candidate.get('CNIC', 'N/A')}")
                st.markdown(f"**💼 Position:** {candidate.get('Position', 'N/A')}")
                st.markdown(f"**🏢 Department:** {candidate.get('Department', 'N/A')}")
                st.markdown(f"**🎓 Education:** {candidate.get('Education', 'N/A')}")
                st.markdown(f"**📅 Applied:** {candidate.get('Application_Date', 'N/A')}")
                st.markdown(f"**📊 Assessment Score:** {candidate.get('Assessment_Score', 'N/A')}")
                st.markdown(f"**🆔 Application ID:** {candidate.get('Application_ID', 'N/A')}")
                
                # Progress bar for score
                try:
                    score_val = float(candidate.get('Assessment_Score', '0%').replace('%', ''))
                    st.progress(score_val/100)
                except:
                    st.progress(0)
                
            with col2:
                candidate_status = candidate.get('Status', 'Unknown')
                status_color = "#22c55e" if candidate_status == "Selected for Interview" else "#f59e0b" if "Interview" in candidate_status else "#3b82f6"
                st.markdown(f"""
                <div style="
                    background: {status_color};
                    color: white;
                    padding: 0.5rem;
                    border-radius: 10px;
                    text-align: center;
                    font-weight: bold;
                ">
                    {candidate_status}
                </div>
                """, unsafe_allow_html=True)
                
                # Additional info
                st.markdown(f"**Experience:** {candidate.get('Experience', 'N/A')}")
                st.markdown(f"**Availability:** {candidate.get('Availability', 'N/A')}")
                if candidate.get('Salary_Expectation'):
                    st.markdown(f"**Expected Salary:** PKR {candidate.get('Salary_Expectation', 'N/A')}")
                
            with col3:
                if st.button(f"📄 View Assessment", key=f"assessment_{idx}"):
                    # Show assessment details
                    st.info(f"Assessment details for {candidate_name} - {candidate_score}")
                
                if st.button(f"📧 Send Email", key=f"email_{idx}"):
                    st.success(f"Email sent to {candidate_name}")
                
                if st.button(f"🤝 Schedule Interview", key=f"interview_{idx}"):
                    st.success(f"Interview scheduled for {candidate_name}")
                
                if st.button(f"📋 Why UBL", key=f"why_{idx}"):
                    why_ubl = candidate.get('Why_UBL', 'No response provided')
                    st.info(f"**Why UBL Bank:**\n{why_ubl}")
    
    # Summary statistics
    if len(filtered_df) > 0:
        st.markdown("### 📊 Summary Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_apps = len(filtered_df)
            st.metric("Total Applications", total_apps)
        
        with col2:
            selected = len(filtered_df[filtered_df['Status'] == 'Selected for Interview'])
            st.metric("Selected for Interview", selected)
        
        with col3:
            try:
                avg_score = filtered_df['Score_Numeric'].mean()
                st.metric("Average Score", f"{avg_score:.1f}%")
            except:
                st.metric("Average Score", "N/A")
        
        with col4:
            under_review = len(filtered_df[filtered_df['Status'] == 'Under Review'])
            st.metric("Under Review", under_review)

def show_hr_assessments():
    """HR Assessment Management"""
    st.markdown("## 📝 Assessment Management")
    
    tab1, tab2, tab3 = st.tabs(["📊 Assessment Results", "➕ Create Assessment", "⚙️ Question Bank"])
    
    with tab1:
        st.markdown("### 📊 Assessment Results Overview")
        
        # Sample assessment data
        assessment_data = {
            'Candidate': ['Ahmed Khan', 'Sarah Ali', 'Muhammad Hassan', 'Fatima Sheikh', 'Ali Raza'],
            'Position': ['Branch Manager', 'Customer Service Officer', 'Operations Assistant', 'Risk Analyst', 'IT Specialist'],
            'Assessment Type': ['Banking Fundamentals', 'Customer Service', 'Operations', 'Risk Management', 'Technical'],
            'Score': [85, 92, 78, 88, 95],
            'Duration': ['25 min', '20 min', '30 min', '28 min', '35 min'],
            'Completed': ['2024-01-15 10:30', '2024-01-14 14:20', '2024-01-13 09:15', '2024-01-12 16:45', '2024-01-11 11:30']
        }
        
        df = pd.DataFrame(assessment_data)
        
        # Score distribution chart
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(df, x='Score', nbins=10, title="Score Distribution")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(df, y='Score', title="Score Statistics")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
        
        # Detailed results table
        st.dataframe(df, use_container_width=True)
    
    with tab2:
        st.markdown("### ➕ Create New Assessment")
        
        with st.form("create_assessment"):
            col1, col2 = st.columns(2)
            
            with col1:
                assessment_name = st.text_input("Assessment Name")
                assessment_type = st.selectbox("Assessment Type", 
                    ["Banking Fundamentals", "Customer Service", "Operations", "Risk Management", "Technical"])
                difficulty_level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard", "Mixed"])
                
            with col2:
                num_questions = st.number_input("Number of Questions", min_value=5, max_value=50, value=10)
                time_limit = st.number_input("Time Limit (minutes)", min_value=10, max_value=120, value=30)
                passing_score = st.number_input("Passing Score (%)", min_value=50, max_value=100, value=70)
            
            description = st.text_area("Assessment Description")
            
            if st.form_submit_button("Create Assessment"):
                st.success(f"✅ Assessment '{assessment_name}' created successfully!")
    
    with tab3:
        st.markdown("### ⚙️ Question Bank Management")
        
        # Display current question banks
        assessment_system = st.session_state.assessment_system
        
        for category, questions in assessment_system.question_banks.items():
            with st.expander(f"📚 {category} ({len(questions)} questions)"):
                for i, q in enumerate(questions):
                    st.markdown(f"**Q{i+1}:** {q['question']}")
                    st.markdown(f"**Correct Answer:** {q['options'][q['correct']]}")
                    st.markdown(f"**Difficulty:** {q['difficulty']} | **Points:** {q['points']}")
                    st.markdown("---")

def show_hr_jobs():
    """HR Job Management"""
    st.markdown("## 📋 Job Management")
    
    tab1, tab2 = st.tabs(["📋 Current Jobs", "➕ Post New Job"])
    
    with tab1:
        st.markdown("### 📋 Current Job Postings")
        
        for i, job in enumerate(JOB_DESCRIPTIONS):
            with st.expander(f"💼 {job['title']} - {job['department']}"):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.markdown(f"**Description:** {job['description']}")
                    st.markdown(f"**Location:** {job['location']}")
                    st.markdown(f"**Salary Range:** {job['salary_range']}")
                
                with col2:
                    st.markdown(f"**Applications:** {random.randint(5, 25)}")
                    st.markdown(f"**Views:** {random.randint(50, 200)}")
                    st.markdown(f"**Status:** Active")
                
                with col3:
                    if st.button(f"✏️ Edit", key=f"edit_job_{i}"):
                        st.info("Job editing feature")
                    if st.button(f"📊 Analytics", key=f"analytics_{i}"):
                        st.info("Job analytics feature")
                    if st.button(f"⏸️ Pause", key=f"pause_{i}"):
                        st.warning("Job paused")
    
    with tab2:
        st.markdown("### ➕ Post New Job")
        
        with st.form("new_job"):
            col1, col2 = st.columns(2)
            
            with col1:
                job_title = st.text_input("Job Title")
                department = st.selectbox("Department", 
                    ["Retail Banking", "Operations", "Customer Service", "IT", "Risk Management", "HR"])
                location = st.selectbox("Location", 
                    ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan", "Other"])
                level = st.selectbox("Job Level", 
                    ["Entry Level", "Mid Level", "Senior Level", "Management"])
                
            with col2:
                salary_min = st.number_input("Minimum Salary (PKR)", min_value=30000, value=80000)
                salary_max = st.number_input("Maximum Salary (PKR)", min_value=50000, value=150000)
                employment_type = st.selectbox("Employment Type", 
                    ["Full-time", "Part-time", "Contract", "Internship"])
                experience_required = st.selectbox("Experience Required", 
                    ["0-1 years", "1-3 years", "3-5 years", "5+ years"])
            
            job_description = st.text_area("Job Description", height=100)
            requirements = st.text_area("Requirements (one per line)", height=100)
            benefits = st.text_area("Benefits (one per line)", height=100)
            
            if st.form_submit_button("Post Job"):
                st.success(f"✅ Job '{job_title}' posted successfully!")

def show_hr_settings():
    """HR Settings and Configuration"""
    st.markdown("## ⚙️ HR Settings")
    
    tab1, tab2, tab3 = st.tabs(["👤 Profile", "🔧 System Settings", "📊 Reports"])
    
    with tab1:
        st.markdown("### 👤 HR Profile Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Name", value="HR Manager")
            st.text_input("Email", value=st.session_state.get('hr_email', 'hr@ublbank.com'))
            st.text_input("Department", value="Human Resources")
            st.selectbox("Role", ["HR Manager", "Senior HR Manager", "HR Director"])
        
        with col2:
            st.text_input("Phone", value="+92 300 1234567")
            st.text_input("Extension", value="1234")
            st.selectbox("Branch", ["Head Office", "Karachi Main", "Lahore Main", "Islamabad Main"])
            
        if st.button("Update Profile"):
            st.success("✅ Profile updated successfully!")
    
    with tab2:
        st.markdown("### 🔧 System Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Assessment Settings**")
            st.number_input("Default Assessment Time (minutes)", value=30)
            st.number_input("Minimum Passing Score (%)", value=70)
            st.checkbox("Auto-schedule interviews for high scorers", value=True)
            st.checkbox("Send automatic email notifications", value=True)
        
        with col2:
            st.markdown("**Notification Settings**")
            st.checkbox("New application alerts", value=True)
            st.checkbox("Assessment completion alerts", value=True)
            st.checkbox("Interview reminder emails", value=True)
            st.checkbox("Daily summary reports", value=True)
        
        if st.button("Save Settings"):
            st.success("✅ Settings saved successfully!")
    
    with tab3:
        st.markdown("### 📊 Generate Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            report_type = st.selectbox("Report Type", 
                ["Recruitment Summary", "Assessment Analytics", "Department-wise Applications", "Monthly Statistics"])
            date_range = st.date_input("Report Period", value=[datetime.now().date()])
        
        with col2:
            format_type = st.selectbox("Format", ["PDF", "Excel", "CSV"])
            include_charts = st.checkbox("Include Charts", value=True)
        
        if st.button("Generate Report"):
            st.success("✅ Report generated successfully!")
            st.download_button("📥 Download Report", "Sample report data", "report.pdf")

def show_chat():
    """Simple chat interface"""
    st.markdown("""
    <div class="hero-section">
        <h2 style="color: #1a202c;">🤖 Career Assistant</h2>
        <p style="color: #2d3748;">Get instant answers to your career-related questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Hello! 👋 I'm your UBL Bank Career Assistant. How can I help you today?"
        })
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about careers at UBL Bank...", key="career_chat_input"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            if "salary" in prompt.lower():
                response = "💰 UBL Bank offers competitive salary packages based on position and experience. Entry-level positions start from PKR 80K-120K, while senior management roles can go up to PKR 300K+. We also provide performance bonuses, health insurance, and other benefits."
            elif "requirement" in prompt.lower() or "qualification" in prompt.lower():
                response = "🎓 Requirements vary by position. Generally, we look for relevant education (Bachelor's or Master's degree), banking experience, strong communication skills, and customer service orientation. Check specific job descriptions for detailed requirements."
            elif "interview" in prompt.lower():
                response = "🤝 Our interview process includes initial screening, technical assessment, HR interview, and final management interview. We assess both technical knowledge and cultural fit. Prepare by reviewing banking fundamentals and practicing common interview questions."
            elif "benefit" in prompt.lower():
                response = "🎁 UBL Bank offers comprehensive benefits including: Health Insurance, Life Insurance, Provident Fund, Performance Bonuses, Annual Leave, Training & Development Programs, and Career Advancement opportunities."
            elif "apply" in prompt.lower():
                response = "📝 To apply, visit our 'Apply Now' section, select your desired position, fill out the application form, and complete the assessment. Our HR team will contact you if you're shortlisted for interviews."
            else:
                response = "🤖 I'm here to help with UBL Bank career questions! Ask me about salaries, requirements, benefits, application process, or interview tips. You can also visit our other sections for detailed job descriptions and application forms."
            
            st.write(response)
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})

def main():
    """Main application with enhanced features"""
    
    # Initialize session state
    if 'assessment_system' not in st.session_state:
        st.session_state.assessment_system = AdvancedAssessmentSystem()
    if 'user_type' not in st.session_state:
        st.session_state.user_type = 'candidate'
    
    # Navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #1a202c; font-size: 1.8rem; margin-bottom: 0.5rem;">🏦 UBL Bank</h1>
            <p style="color: #2d3748; font-weight: 600;">Career Portal</p>
        </div>
        """, unsafe_allow_html=True)
        
        # User type selection
        user_type = st.radio(
            "Select User Type:",
            ["👨‍💼 Job Candidate", "👩‍💼 HR Manager"],
            horizontal=True,
            key="user_type_radio"
        )
        
        if user_type == "👩‍💼 HR Manager":
            if not check_hr_authentication():
                st.markdown("### 🔐 HR Manager Login")
                
                # Enhanced credentials display with copy functionality
                st.markdown("#### 🔑 **Available HR Accounts:**")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    **📧 Email Addresses:**
                    - `hr.manager@ublbank.com`
                    - `admin.hr@ublbank.com`
                    - `recruitment@ublbank.com`
                    - `hr.director@ublbank.com`
                    """)
                
                with col2:
                    st.markdown("""
                    **🔐 Passwords:**
                    - `UBL@Hr2024!`
                    - `Admin@UBL123`
                    - `Recruit@2024`
                    - `Director@UBL2024`
                    """)
                
                st.warning("💡 **Quick Login:** Use any email above with its corresponding password")
                
                with st.form("hr_login"):
                    # Default to first account for easy testing
                    email = st.text_input("Email", value="hr.manager@ublbank.com", placeholder="Select from above emails")
                    password = st.text_input("Password", value="UBL@Hr2024!", type="password", placeholder="Enter corresponding password")
                    login_btn = st.form_submit_button("🚀 Login to HR Dashboard", type="primary")
                    
                    if login_btn:
                        if email in HR_CREDENTIALS and HR_CREDENTIALS[email] == password:
                            st.session_state.hr_authenticated = True
                            st.session_state.hr_email = email
                            st.success("✅ Login successful! Redirecting to HR Dashboard...")
                            st.rerun()
                        else:
                            st.error("❌ Invalid credentials! Please use the exact email and password from above.")
                            st.info("💡 Make sure to copy the credentials exactly as shown above.")
                return
            
            # HR Navigation
            selected = option_menu(
                menu_title=None,
                options=["📊 Dashboard", "👥 Candidates", "📝 Assessments", "📋 Jobs", "⚙️ Settings"],
                icons=['graph-up', 'people', 'clipboard-check', 'briefcase', 'gear'],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"background-color": "transparent"},
                    "nav-link": {"color": "#1a202c", "font-weight": "700"},
                    "nav-link-selected": {"background-color": "rgba(26,32,44,0.2)", "color": "#1a202c"},
                }
            )
        else:
            # Candidate Navigation
            selected = option_menu(
                menu_title=None,
                options=["🏠 Home", "📋 Job Descriptions", "🚀 Apply Now", "💬 Chat Support"],
                icons=['house', 'journal-text', 'rocket-takeoff', 'chat-dots'],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"background-color": "transparent"},
                    "nav-link": {"color": "#1a202c", "font-weight": "700"},
                    "nav-link-selected": {"background-color": "rgba(26,32,44,0.2)", "color": "#1a202c"},
                }
            )

        # Statistics sidebar
        st.markdown("""
        <div style="
            background: rgba(255,255,255,0.1);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 16px rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            margin-top: 1rem;
        ">
            <h4 style="color: #1a202c; margin-bottom: 1rem; font-weight: 700;">📊 Live Statistics</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div style="
                    background: linear-gradient(135deg, #4facfe, #00f2fe);
                    padding: 1rem;
                    border-radius: 10px;
                    color: white;
                ">
                    <div style="font-size: 1.8rem; font-weight: bold;">24+</div>
                    <small style="font-weight: 600;">Active Jobs</small>
                </div>
                <div style="
                    background: linear-gradient(135deg, #f093fb, #f5576c);
                    padding: 1rem;
                    border-radius: 10px;
                    color: white;
                ">
                    <div style="font-size: 1.8rem; font-weight: bold;">96%</div>
                    <small style="font-weight: 600;">Success Rate</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Content Routing
    if st.session_state.get('user_type_radio') == "👩‍💼 HR Manager" and check_hr_authentication():
        # HR Section Routing
        if selected == "📊 Dashboard":
            show_hr_dashboard()
        elif selected == "👥 Candidates":
            show_hr_candidates()
        elif selected == "📝 Assessments":
            show_hr_assessments()
        elif selected == "📋 Jobs":
            show_hr_jobs()
        elif selected == "⚙️ Settings":
            show_hr_settings()
    else:
        # Candidate Section Routing
        if selected == "🏠 Home":
            show_home()
        elif selected == "📋 Job Descriptions":
            show_jobs()
        elif selected == "🚀 Apply Now":
            show_apply()
        elif selected == "💬 Chat Support":
            show_chat()

if __name__ == "__main__":
    main()
