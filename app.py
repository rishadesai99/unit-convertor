from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion functions
class UnitConverter:
    # Length conversions (to meters)
    LENGTH_TO_METERS = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    # Temperature conversions
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    # Weight conversions (to grams)
    WEIGHT_TO_GRAMS = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lb': 453.592
    }
    
    # Volume conversions (to liters)
    VOLUME_TO_LITERS = {
        'ml': 0.001,
        'l': 1,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735
    }
    
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        if from_unit not in UnitConverter.LENGTH_TO_METERS or to_unit not in UnitConverter.LENGTH_TO_METERS:
            return None
        meters = value * UnitConverter.LENGTH_TO_METERS[from_unit]
        return meters / UnitConverter.LENGTH_TO_METERS[to_unit]
    
    @staticmethod
    def convert_weight(value, from_unit, to_unit):
        if from_unit not in UnitConverter.WEIGHT_TO_GRAMS or to_unit not in UnitConverter.WEIGHT_TO_GRAMS:
            return None
        grams = value * UnitConverter.WEIGHT_TO_GRAMS[from_unit]
        return grams / UnitConverter.WEIGHT_TO_GRAMS[to_unit]
    
    @staticmethod
    def convert_volume(value, from_unit, to_unit):
        if from_unit not in UnitConverter.VOLUME_TO_LITERS or to_unit not in UnitConverter.VOLUME_TO_LITERS:
            return None
        liters = value * UnitConverter.VOLUME_TO_LITERS[from_unit]
        return liters / UnitConverter.VOLUME_TO_LITERS[to_unit]
    
    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'C' and to_unit == 'F':
            return UnitConverter.celsius_to_fahrenheit(value)
        elif from_unit == 'F' and to_unit == 'C':
            return UnitConverter.fahrenheit_to_celsius(value)
        elif from_unit == 'C' and to_unit == 'K':
            return UnitConverter.celsius_to_kelvin(value)
        elif from_unit == 'K' and to_unit == 'C':
            return UnitConverter.kelvin_to_celsius(value)
        elif from_unit == 'F' and to_unit == 'K':
            return UnitConverter.celsius_to_kelvin(UnitConverter.fahrenheit_to_celsius(value))
        elif from_unit == 'K' and to_unit == 'F':
            return UnitConverter.celsius_to_fahrenheit(UnitConverter.kelvin_to_celsius(value))
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        value = float(data.get('value'))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        category = data.get('category')
        
        converter = UnitConverter()
        result = None
        
        if category == 'length':
            result = converter.convert_length(value, from_unit, to_unit)
        elif category == 'weight':
            result = converter.convert_weight(value, from_unit, to_unit)
        elif category == 'volume':
            result = converter.convert_volume(value, from_unit, to_unit)
        elif category == 'temperature':
            result = converter.convert_temperature(value, from_unit, to_unit)
        
        if result is not None:
            return jsonify({'success': True, 'result': round(result, 10)})
        else:
            return jsonify({'success': False, 'error': 'Invalid units'}), 400
    except (ValueError, TypeError) as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
