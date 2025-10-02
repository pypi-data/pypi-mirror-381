# QR Code Generator in Python

A comprehensive Python application for generating QR codes with both command-line and web interfaces. Features include customizable output directories, multiple content types, comprehensive testing, and a user-friendly Streamlit web UI.

## 🚀 Features

- **Easy to Use**: Simple class-based interface for QR code generation
- **Web Interface**: Modern Streamlit web UI for interactive QR code generation
- **Organized Output**: Automatically saves all QR codes to designated output folders
- **Timestamp Naming**: Automatic file naming with microsecond timestamps to prevent overwrites
- **Customizable Prefix**: Set custom prefixes for generated QR code files
- **Customizable Output Directory**: Choose where to save your QR code files
- **Multiple Content Types**: Support for URLs, text, email, phone, WiFi, vCard, and custom content
- **High Quality**: Optimized settings for clear, scannable QR codes
- **Comprehensive Testing**: 96% test coverage with unit and integration tests
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Professional Setup**: Automated scripts for environment setup and management
```

## 🧪 Testing

Run the built-in example:

```bash
python QRCodeGenerator.py
```

This will create a QR code for the LinkedIn profile URL and save it in the `output` folder.

### 🌐 Streamlit Web Interface

Launch the interactive web interface:

```bash
# Using the provided script (recommended)
streamlit run streamlit_app.py

# Or using batch/shell scripts
scripts\windows\run_streamlit.bat    # Windows
scripts/unix/run_streamlit.sh        # Linux/Mac
```

The web interface provides:
- **Interactive Forms**: Easy-to-use forms for different content types
- **Real-time Preview**: See your QR code generated instantly
- **Download Support**: Direct download of generated QR codes
- **Multiple Content Types**: Support for URLs, text, email, phone, WiFi, vCard
- **Customizable Settings**: Adjust file prefixes and output folders
- **Usage Statistics**: Track QR codes generated in your session

### 🛠️ Quick Setup Scripts

For easy environment management, use the provided scripts:

**Windows (.bat files):**
```bash
scripts\windows\setup_env.bat      # Create virtual environment
scripts\windows\activate.bat       # Activate environment and open interactive shell
scripts\windows\install_deps.bat   # Install all dependencies
scripts\windows\run_main.bat       # Run the main CLI application
scripts\windows\run_tests.bat      # Run unit tests with coverage
scripts\windows\run_coverage.bat   # Generate detailed coverage reports
scripts\windows\run_streamlit.bat  # Launch web interface
```

**Linux/Mac (.sh files):**
```bash
scripts/unix/setup_env.sh      # Create virtual environment
scripts/unix/activate.sh       # Activate environment and open interactive shell
scripts/unix/install_deps.sh   # Install all dependencies
scripts/unix/run_main.sh       # Run the main CLI application
scripts/unix/run_tests.sh      # Run unit tests with coverage
scripts/unix/run_coverage.sh   # Generate detailed coverage reports
scripts/unix/run_streamlit.sh  # Launch web interface
```

### Running Unit Tests

The project includes comprehensive unit tests using pytest:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=QRCodeGenerator --cov-report=term-missing

# Run only unit tests
pytest tests/test_qr_code_generator.py -v

# Run only integration tests
pytest tests/test_main_function.py -v

# Generate HTML coverage report
pytest tests/ --cov=QRCodeGenerator --cov-report=html:htmlcov
```

### Using the Test Runner

You can also use the included test runner script:

```bash
# Run all tests with coverage
python run_tests.py --coverage

# Run tests with HTML coverage report
python run_tests.py --html-cov

# Run only unit tests
python run_tests.py --unit-only --verbose

# Run tests quickly (skip slow tests)
python run_tests.py --fast
```

### Test Coverage

The project maintains high test coverage:

- **Unit Tests**: Test individual components and methods
- **Integration Tests**: Test complete workflows and main function
- **Edge Cases**: Test error conditions and boundary cases
- **Parametrized Tests**: Test multiple scenarios efficiently

Current test coverage: **96%**-based naming to prevent file conflicts.

## 🚀 Features

- **Easy to Use**: Simple class-based interface for QR code generation
- **Organized Output**: Automatically saves all QR codes to a designated output folder
- **Timestamp Naming**: Automatic file naming with timestamps to prevent overwrites
- **Customizable Prefix**: Set custom prefixes for generated QR code files
- **Customizable Output Directory**: Choose where to save your QR code files
- **High Quality**: Optimized settings for clear, scannable QR codes
- **Flexible Input**: Supports any text, URLs, or string data
- **Zero Configuration**: Works out of the box with sensible defaults

## 📋 Requirements

- Python 3.12+
- qrcode library
- Pillow (PIL) for image handling

## 🛠️ Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/ShanKonduru/QRCodeGenPy.git
cd QRCodeGenPy

# Install dependencies using Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/ShanKonduru/QRCodeGenPy.git
cd QRCodeGenPy

# Install dependencies
pip install -r requirements.txt
```

### Manual Installation

Install the required packages:

```bash
pip install qrcode[pil]
```

## 🎯 Quick Start

### Basic Usage

```python
from QRCodeGenerator import QRCodeGenerator

# Create a QR code generator instance (saves to 'output' folder by default)
generator = QRCodeGenerator()

# Generate a QR code for a URL
filename = generator.generate_qr_code("https://www.example.com")
print(f"QR code saved as: {filename}")
# Output: output/qr_code_20241001123456.png
```

### Custom File Prefix and Output Folder

```python
# Use a custom prefix and output folder
generator = QRCodeGenerator("my_website", "my_qr_codes")
filename = generator.generate_qr_code("https://www.mywebsite.com")
# Output: my_qr_codes/my_website_20241001123456.png
```

### Running the Example

```bash
python QRCodeGenerator.py
```

This will generate a QR code for the LinkedIn profile URL and save it in the `output` folder.

## 📖 API Documentation

### Class: `QRCodeGenerator`

#### Constructor

```python
QRCodeGenerator(file_prefix="qr_code", output_folder="output")
```

**Parameters:**

- `file_prefix` (str, optional): Prefix for the output filename. Defaults to "qr_code".
- `output_folder` (str, optional): Directory to save QR code images. Defaults to "output".

#### Methods

##### `generate_qr_code(input_string)`

Generates a QR code from the provided input string and saves it as a PNG image in the specified output folder.

**Parameters:**

- `input_string` (str): The text or URL to encode in the QR code.

**Returns:**

- `str`: The full path of the generated QR code image (includes folder and .png extension).

**Example:**
```python
generator = QRCodeGenerator()
filename = generator.generate_qr_code("Hello, World!")
```

## 🔧 QR Code Settings

The generated QR codes use the following optimized settings:

- **Version**: 1 (21x21 modules)
- **Error Correction**: Low (~7% error correction)
- **Box Size**: 10 pixels per module
- **Border**: 4 modules wide (minimum recommended)
- **Colors**: Black foreground on white background

## 📁 Project Structure

```
QRCodeGenPy/
├── QRCodeGenerator.py          # Main QR code generator class
├── streamlit_app.py           # Streamlit web interface
├── run_security_audit.py      # Security audit script
├── run_tests.py              # Test runner script
├── requirements.txt            # pip dependencies
├── pyproject.toml             # Poetry configuration and PyPI metadata
├── setup.py                  # PyPI setup script
├── poetry.lock               # Poetry lock file
├── pytest.ini               # Pytest configuration
├── README.md                 # This documentation
├── LICENSE                   # MIT license
├── MANIFEST.in              # Package inclusion rules
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── scripts/                  # Automation scripts
│   ├── windows/             # Windows batch files (.bat)
│   │   ├── setup_env.bat
│   │   ├── run_tests.bat
│   │   ├── upload_pypi.bat
│   │   └── ... (other .bat files)
│   ├── unix/                # Unix/Linux/Mac shell scripts (.sh)
│   │   ├── setup_env.sh
│   │   ├── run_tests.sh
│   │   ├── upload_pypi.sh
│   │   └── ... (other .sh files)
│   └── README.md            # Scripts documentation
├── tests/                    # Test directory
│   ├── __init__.py          # Test package init
│   ├── test_qr_code_generator.py  # Unit tests
│   └── test_main_function.py     # Integration tests
├── output/                   # Default QR code output directory
│   └── *.png                # Generated QR code files
├── security_reports/         # Security audit reports
│   ├── bandit_report.json   # Bandit security scan
│   ├── pip_audit_report.json # pip-audit results
│   └── security_summary.md  # Audit summary
└── htmlcov/                  # Coverage report (generated)
    └── index.html           # HTML coverage report
```

## 🎨 Examples

### Generate QR Code for Different Types of Data

```python
from QRCodeGenerator import QRCodeGenerator

# Create generator with custom prefix and output folder
generator = QRCodeGenerator("example", "my_qr_outputs")

# Website URL
website_qr = generator.generate_qr_code("https://www.github.com")
# Output: my_qr_outputs/example_20241001123456.png

# Contact information (vCard format)
contact_info = """BEGIN:VCARD
VERSION:3.0
FN:John Doe
ORG:Example Company
TEL:+1234567890
EMAIL:john@example.com
END:VCARD"""
contact_qr = generator.generate_qr_code(contact_info)

# WiFi connection info
wifi_info = "WIFI:T:WPA;S:MyNetworkName;P:MyPassword;;"
wifi_qr = generator.generate_qr_code(wifi_info)

# Plain text
text_qr = generator.generate_qr_code("Hello, QR Code World!")

# All files are saved in the 'my_qr_outputs' folder
```

## 🧪 Testing

Run the built-in example:

```bash
python QRCodeGenerator.py
```

This will create a QR code for the LinkedIn profile URL and display the filename.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## � PyPI Publishing

### Setup PyPI Credentials

1. Copy the environment template:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your PyPI credentials:
   ```dotenv
   PYPI_USER_NAME=your_pypi_username
   PYPI_PASSWORD=your_pypi_password_or_token
   ```

   **Recommended:** Use an API token instead of your password. Generate one at: https://pypi.org/manage/account/token/

### Upload to PyPI

**Windows:**
```bash
# Upload to PyPI (reads credentials from .env)
scripts\windows\upload_pypi.bat
```

**Linux/Mac:**
```bash
# Make script executable
chmod +x scripts/unix/upload_pypi.sh

# Upload to PyPI (reads credentials from .env)
scripts/unix/upload_pypi.sh
```

The upload script will:
1. Run security audits
2. Run all tests  
3. Build the package
4. Upload to PyPI using credentials from `.env`

### Installation from PyPI

Once published, users can install your package:
```bash
pip install qrcodegenpy-shankonduru
```

## 🔒 Security Auditing

Run comprehensive security audits with:

**Windows:**
```bash
scripts\windows\run_security_audit.bat
```

**Linux/Mac:**
```bash
scripts/unix/run_security_audit.sh
```

Security tools used:
- **safety** - Checks for known vulnerabilities in dependencies
- **bandit** - Scans Python code for security issues
- **pip-audit** - Audits packages for known vulnerabilities

Reports are saved in `security_reports/` folder.

## �📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shan Konduru**
- LinkedIn: [https://www.linkedin.com/in/shankonduru/](https://www.linkedin.com/in/shankonduru/)
- Email: shankonduru@gmail.com

## 🙏 Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) library for QR code generation
- [Pillow](https://python-pillow.org/) for image processing
- Python community for excellent documentation and examples

## 📈 Version History

- **v1.0.0** - Major Release 🎉
  - ✅ Complete project restructure with professional standards
  - ✅ Comprehensive testing suite (26 tests, 96% coverage)
  - ✅ Streamlit web interface for interactive QR generation
  - ✅ Security auditing with safety, bandit, and pip-audit
  - ✅ PyPI publishing automation with .env credential management
  - ✅ Cross-platform automation scripts (.bat and .sh)
  - ✅ HTML test reports and coverage analysis
  - ✅ Professional documentation and project structure
  - ✅ Git workflow integration and CI/CD ready

- **v0.1.0** - Initial Release
  - Basic QR code generation
  - Timestamp-based file naming
  - Customizable file prefixes
  - Basic documentation

---

Made with ❤️ by [Shan Konduru](https://www.linkedin.com/in/shankonduru/)