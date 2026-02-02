# Unit Converter Web Application

A simple and elegant web application for converting between different units of measurement. Built with Flask and ready to deploy on Render.

## Features

- **Length Conversion**: mm, cm, m, km, in, ft, yd, mi
- **Weight Conversion**: mg, g, kg, oz, lb
- **Volume Conversion**: ml, l, gal, qt, pt, cup, fl oz
- **Temperature Conversion**: Celsius, Fahrenheit, Kelvin
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Conversion**: Quick and accurate conversions
- **Unit Swap**: Easily swap between source and target units

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render
- **Version Control**: Git & GitHub

## Project Structure

```
unit-converter/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
├── .gitignore            # Git ignore file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    └── css/
        └── style.css     # Stylesheet
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/unit-converter.git
   cd unit-converter
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000`

## Deployment on Render

### Prerequisites
- GitHub account with the repository pushed
- Render account (https://render.com)

### Steps to Deploy

1. **Sign up on Render**
   - Visit https://render.com
   - Sign up with your GitHub account

2. **Create a New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository
   - Select the "unit-converter" repository

3. **Configure Deployment**
   - **Name**: unit-converter (or any name you prefer)
   - **Region**: Choose the closest region
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Free tier**: Select for testing (optional)

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy your app
   - Your app will be available at `https://unit-converter-xxxx.onrender.com`

### Environment Variables (if needed)
Currently, the app doesn't require any environment variables. If you add features that need them:
1. Go to your service settings on Render
2. Add environment variables in the "Environment" section

## Usage

1. Select a conversion category (Length, Weight, Volume, or Temperature)
2. Enter a value
3. Choose source and destination units
4. Click "Convert" or press Enter
5. View the result

## API Endpoints

### `/` (GET)
Returns the main converter interface

### `/convert` (POST)
Converts a value between units

**Request body:**
```json
{
  "value": 10,
  "from_unit": "m",
  "to_unit": "ft",
  "category": "length"
}
```

**Response:**
```json
{
  "success": true,
  "result": 32.8084
}
```

## Supported Conversions

### Length
- Millimeter (mm)
- Centimeter (cm)
- Meter (m)
- Kilometer (km)
- Inch (in)
- Foot (ft)
- Yard (yd)
- Mile (mi)

### Weight
- Milligram (mg)
- Gram (g)
- Kilogram (kg)
- Ounce (oz)
- Pound (lb)

### Volume
- Milliliter (ml)
- Liter (l)
- Gallon (gal)
- Quart (qt)
- Pint (pt)
- Cup (cup)
- Fluid Ounce (fl oz)

### Temperature
- Celsius (C)
- Fahrenheit (F)
- Kelvin (K)

## Troubleshooting

### App won't start locally
- Ensure Python is installed: `python --version`
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Render deployment fails
- Check build logs in Render dashboard
- Ensure `requirements.txt` is in root directory
- Verify `Procfile` has correct format
- Check GitHub repository connection

### Conversion not working
- Ensure valid numeric input
- Verify units are from the same category
- Check browser console for errors (F12)

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.

## Author

Created as a demonstration Flask application with deployment capabilities.

## Future Enhancements

- [ ] Add more unit categories (Area, Speed, Pressure, etc.)
- [ ] Add conversion history
- [ ] Dark mode support
- [ ] Multi-language support
- [ ] Database for storing conversions
- [ ] User accounts and preferences

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub or contact the developer.

---

**Happy Converting!** 🔄
