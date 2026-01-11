# VisionMatch: Intelligent Image Comparison Framework

**VisionMatch** is a robust computer vision framework designed to analyze and compare images for similarity.Unlike traditional pixel-by-pixel comparison tools,
VisionMatch utilizes a **Hybrid Algorithm** combining **Structural Similarity (SSIM)** and **ORB Feature Matching**.This allows it to detect duplicates even when 
images are rotated, scaled, or suffer from lighting variations—simulating human visual perception.
---
## 🚀 Key Features
** Hybrid Comparison Engine:**
*SSIM (Structural Similarity Index):** Detects exact duplicates, compression artifacts, and quality loss.
*ORB (Oriented FAST and Rotated BRIEF):** Identifies matching features (keypoints) to handle rotation, zoom, and perspective shifts.
*Interactive Dashboard:A clean, responsive Web UI built with Flask and Jinja2 for uploading and comparing images instantly.
*clock: History Tracking:Automatically logs all comparison results, timestamps, and similarity scores to a MySQL database.
*User Authentication:Secure login and registration system to maintain private user history.
---
## 🛠️ Tech Stack
* Backend:Python, Flask
* Computer Vision:OpenCV (`cv2`), Scikit-Image
* Database:MySQL
* Frontend:HTML5, CSS3, JavaScript
* Version Control:Git & GitHub
---
## 📂 Project Structure
The project follows a modular Model-View-Controller (MVC) pattern for scalability:
```text
VISIONMATCH/
│
├── app/
│   ├── __init__.py       # App factory & DB initialization
│   ├── routes.py         # Web routes and API logic
│   ├── models/           # Database models (User, History)
│   ├── services/         # The Computer Vision Logic (SSIM + ORB)
│   ├── static/           # CSS, JS, and image assets
│   └── templates/        # HTML Frontend templates
│
├── .env                  # Environment variables (Database creds)
├── config.py             # Configuration settings
├── run.py                # Application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

##🔧 Installation & Setup
Prerequisites
*Python 3.8+
*MySQL Server
1. Clone the Repository
git clone [https://github.com/201183/VISIONMATCH-INTELLIGENT-IMAGE-COMPARISON-FRAMEWORK.git](https://github.com/201183/VISIONMATCH-INTELLIGENT-IMAGE-COMPARISON-FRAMEWORK.git)
cd VISIONMATCH-INTELLIGENT-IMAGE-COMPARISON-FRAMEWORK
2. Install Dependencies
It is recommended to use a virtual environment.
pip install -r requirements.txt
3. Database Configuration
*Create a MySQL database named image_comparison_db.
*Update the .env file (or config.py) with your MySQL credentials:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=image_comparison_db
4. Run the Application
python run.py
The application will start at http://localhost:5000.

##📸 Usage Guide
1.Register/Login: Create an account to access the dashboard.
2.Upload Images: Select "Reference Image" and "Target Image".
3.Compare: Click "Compare". The Hybrid Engine will calculate a similarity percentage based on both texture (SSIM) and features (ORB).
4.View Results: See the match percentage immediately.
5.Check History: Navigate to the "History" tab to see past comparisons.

##👤 Author
K. Radhakrishna
*GitHub: 201183
*Project: Final Year MCA Project

📝 License
*This project is open-source and available for educational purposes.
