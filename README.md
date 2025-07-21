# 🏦 UBL Bank Career Portal

<div align="center">

![UBL Bank Logo](https://img.shields.io/badge/UBL%20Bank-Career%20Portal-blue?style=for-the-badge&logo=bank&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/sardarahmedmk/bank-career-portal?style=flat&logo=github)](https://github.com/sardarahmedmk/bank-career-portal/stargazers)

**A comprehensive, enterprise-grade career portal for UBL Bank with integrated assessment system and HR management dashboard.**

[🚀 **LIVE DEMO**](https://bank-career-app-w5vuncvfddyeovboppuxrx.streamlit.app/) • [📖 Documentation](#documentation) • [🐛 Report Bug](https://github.com/sardarahmedmk/bank-career-portal/issues) • [✨ Request Feature](https://github.com/sardarahmedmk/bank-career-portal/issues)

</div>

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](images/home-page.png)
*Beautiful landing page with UBL Bank branding and career information*

### 💼 Job Listings
![Job Listings](images/job-listings.png)
*Comprehensive job listings with advanced filtering capabilities*

### 📝 Application Flow
![Application Process](images/application-flow.png)
*4-stage integrated application process with real-time assessment*

### 📊 HR Dashboard
![HR Dashboard](images/hr-dashboard.png)
*Professional HR management dashboard with candidate overview and analytics*

### 📈 Analytics
![Analytics Dashboard](images/analytics.png)
*Detailed analytics and reporting with Excel export functionality*

---

## 🌍 **Mobile Access - Available Worldwide!**

### 📱 **Access from anywhere:**
- **🔗 Live URL**: [https://bank-career-app-w5vuncvfddyeovboppuxrx.streamlit.app/](https://bank-career-app-w5vuncvfddyeovboppuxrx.streamlit.app/)
- **📱 Mobile Ready**: Perfect mobile experience on any device
- **🌎 Global Access**: Works from any country, any network
- **⚡ No Setup Required**: Just click and use!

---

## ✨ Features

### 🎯 For Job Candidates
- **🔍 Smart Job Search** - Advanced filtering by department, level, and location
- **📋 Integrated Application** - Seamless 4-stage application process
- **📝 Role-Specific Assessments** - 12-question assessments tailored to each position
- **⚡ Real-time Results** - Instant feedback and interview selection status
- **📧 Automated Communications** - Email and SMS notifications

### 👩‍💼 For HR Managers
- **📊 Comprehensive Dashboard** - Real-time overview of all applications
- **👥 Candidate Management** - Detailed candidate profiles with assessment scores
- **📈 Advanced Analytics** - Visual charts and performance metrics
- **📥 Excel Export** - Professional reports with multiple export options
- **🔐 Secure Authentication** - Multi-account HR access with role-based permissions

### 🛠️ Technical Features
- **🎨 Modern UI/UX** - Colorful gradient design with perfect text visibility
- **💾 Automatic Data Storage** - Real-time saving to CSV database
- **📱 Responsive Design** - Works seamlessly on all devices
- **🚀 Performance Optimized** - Fast loading and smooth interactions
- **🔒 Data Security** - Secure handling of candidate information

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sardarahmedmk/bank-career-portal.git
   cd bank-career-portal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the portal**
   Open your browser and navigate to `http://localhost:8501`

---

## 🔧 Configuration

### HR Login Credentials
```
Email: hr.manager@ublbank.com
Password: UBL@Hr2024!

Email: admin.hr@ublbank.com
Password: Admin@UBL123

Email: recruitment@ublbank.com
Password: Recruit@2024

Email: hr.director@ublbank.com
Password: Director@UBL2024
```

### Database Structure
The application automatically creates the following directory structure:
```
hr_database/
├── candidates.csv    # Candidate applications and basic info
└── assessments.csv   # Detailed assessment results
```

---

## 📋 Usage Guide

### For Job Candidates

1. **Browse Jobs** 📋
   - Navigate to "Available Jobs" section
   - Use filters to find suitable positions
   - Read detailed job descriptions

2. **Apply for Position** 🎯
   - Click "Apply Now" 
   - Select your desired position
   - Fill out the comprehensive application form
   - Upload your resume/CV

3. **Complete Assessment** 📝
   - Take the role-specific assessment (12 questions)
   - Questions are tailored to your chosen position
   - Receive instant results and feedback

4. **Track Status** 📊
   - Get immediate interview selection status
   - Receive email/SMS notifications
   - View detailed application summary

### For HR Managers

1. **Login to Dashboard** 🔐
   - Select "HR Manager" user type
   - Use provided credentials to login

2. **Review Applications** 👥
   - View real-time candidate overview
   - See assessment scores and status
   - Filter by position, status, or score

3. **Analyze Data** 📈
   - View visual analytics and charts
   - Track recruitment metrics
   - Monitor performance trends

4. **Export Reports** 📥
   - Export candidate data to Excel
   - Generate assessment reports
   - Create combined reports with formatting

---

## 🏗️ Architecture

### Tech Stack
- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with pandas for data processing
- **Database**: CSV files (easily upgradeable to SQL)
- **Visualization**: Plotly for charts and analytics
- **Export**: xlsxwriter for Excel functionality

### Project Structure
```
ubl-career-portal/
├── app.py                 # Main application file
├── job_descriptions.py    # Job data and descriptions
├── requirements.txt       # Python dependencies
├── hr_database/          # Data storage directory
│   ├── candidates.csv    # Candidate applications
│   └── assessments.csv   # Assessment results
├── images/               # Screenshots and assets
└── README.md            # Project documentation
```

---

## 🎨 Customization

### Adding New Job Positions
Edit `job_descriptions.py` to add new positions:
```python
{
    'title': 'Your Job Title',
    'department': 'Department Name',
    'location': 'City, Country',
    'level': 'Entry/Mid/Senior',
    'description': 'Job description...',
    'requirements': ['Requirement 1', 'Requirement 2'],
    'benefits': ['Benefit 1', 'Benefit 2']
}
```

### Customizing Assessment Questions
Modify the `AdvancedAssessmentSystem` class in `app.py` to add new question banks or modify existing ones.

### Styling and Branding
Update the CSS section in `app.py` to match your organization's branding and color scheme.

---

## 📊 Features in Detail

### Assessment System
- **Role-Specific Questions**: Each position has tailored assessment questions
- **Scoring Algorithm**: Point-based scoring with configurable thresholds
- **Automatic Selection**: 80%+ score = Interview, 70-79% = Under Review
- **Detailed Analytics**: Track question performance and candidate insights

### HR Dashboard
- **Real-time Metrics**: Live updates of application statistics
- **Candidate Cards**: Visual overview with status indicators
- **Export Options**: Multiple Excel export formats with professional styling
- **Visual Analytics**: Charts for position distribution and status tracking

### Data Management
- **Automatic Saving**: All applications saved to CSV database
- **Data Validation**: Input validation and error handling
- **Backup Ready**: Easy migration to SQL databases
- **Export Friendly**: Professional Excel reports with formatting

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **UBL Bank** for the inspiration and branding
- **Streamlit** for the amazing framework
- **Open Source Community** for the tools and libraries

---

## 📞 Support

- **Email**: support@ublcareerportal.com
- **Issues**: [GitHub Issues](https://github.com/sardarahmedmk/bank-career-portal/issues)
- **Documentation**: [Wiki](https://github.com/sardarahmedmk/bank-career-portal/wiki)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ for UBL Bank Career Management

[![GitHub followers](https://img.shields.io/github/followers/sardarahmedmk?style=social)](https://github.com/sardarahmedmk)
[![Twitter Follow](https://img.shields.io/twitter/follow/sardarahmedmk?style=social)](https://twitter.com/sardarahmedmk)

</div>
