🏛️ Roman Numeral Converter API
A simple Flask-based REST API that converts between Roman numerals and integers. Built as part of my Kata challenge to deepen understanding of algorithms, parsing, and API development.

🚀 Features
Convert integers to Roman numerals

Convert Roman numerals to integers

Input validation and error handling

Clean api endpoints

Easily extendable for future kata twists

📦 Tech Stack
Backend: Python, Flask

Routing & API: Flask api

Testing: Postman / curl

Run Mode: Local development

🔄 Endpoints

    | Method | Route         | Description                                  |
    | ------ | ------------- | -------------------------------------------- |
    | `POST` | `/to-roman`   | Converts a valid integer to a Roman numeral  |
    | `POST` | `/to-integer` | Converts a valid Roman numeral to an integer |

🧪 Sample Usage
      curl -X POST http://localhost:5000/to-roman \
           -H "Content-Type: application/json" \
           -d '{"number": 9}'
          ➡️ {"roman": "IX"}
      
      curl -X POST http://localhost:5000/to-integer \
       -H "Content-Type: application/json" \
       -d '{"roman": "XLII"}'
       ➡️ {"number": 42}

🛠️ Setup Instructions

1. Clone the repo
2. Create virtual environment
3. Install dependencies with `pip install -r requirements.txt`
4. Run the app with `flask run `

🤓 Dev Notes
This project is part of my 3-day kata challenge to master number-to-roman conversions, 
recursive and greedy approaches,and API design in Flask. Stay tuned for Node.js and FastAPI versions too!






