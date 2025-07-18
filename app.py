from flask  import Flask, jsonify, request, render_template
from marshmallow import Schema, fields, ValidationError
import  re
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
@app.route('/')  #decorator that routes all requests
class MySchemaNumberValidator(Schema):
    num = fields.Int(required=True)
    
class MySchemaRomanValidator(Schema):
    roman = fields.Str(required=True)
    
    
def index():
    return render_template('index.html')

@app.route('/to_roman/<int:num>')
def to_roman(num):
    result = ""
    num_copy = num
    try:
        MySchemaNumberValidator().load({"num": num})
        if num > 3999:
            return jsonify({ "success": False, "error": "Number too large" })
            
        for symbol, value in roman_numerals.items():
                while(num >= value) :
                    result += symbol
                    num -= value
        with open('conversion_history.txt', 'a') as f:
            f.write(f'Conversion of  number {num_copy} to roman is : {result} \n')
            
        return jsonify({ "success": True, "result": result })

    except ValidationError as err:
        print("Validation error")
        return jsonify({ "success": False, "error": err.messages })
    
@app.route('/to_number/<string:roman>')
def to_number(roman):
    try:
        regex = r"^(?=[MDCLXVI])M{0,3}(CM|CD|D)?(C{0,3}|XC|XL)?(L)?(X{0,3}|IX|IV)?(V)?(I{0,3})$"
        if not re.match(regex, roman.upper()):
            return jsonify({ "success": False, "error": "Invalid Roman numeral" })
        MySchemaRomanValidator().load({'roman': roman})
        result = 0
        prev_value  = 0
        for char in reversed(roman):
            current_value = roman_numerals[char]
            if ( current_value < prev_value) :
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        with open('conversion_history.txt', 'a') as f:
            f.write(f'Conversion of  roman of  {roman} to base 10 number is {result}\n')
            
        return jsonify({ "success": True, "result": result })
    except ValidationError as err:
        return jsonify({ "success": False, "error": err.messages })
        
    
