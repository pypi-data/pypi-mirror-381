"""
Command Line Interface for QR Code Generator

This module provides a command-line interface for generating QR codes.
"""

import argparse
from .qr_generator import QRCodeGenerator


def main():
    """
    Main function - demonstrates basic usage of the QRCodeGenerator class.

    This example creates a QR code for a LinkedIn profile URL and saves it as a PNG file.
    The function will print the filename of the generated QR code upon successful completion.
    """
    # Example data - LinkedIn profile URL
    input_string = "https://www.linkedin.com/in/shankonduru/"

    # Create QR code generator instance with default settings
    qr_generator = QRCodeGenerator()

    # Generate the QR code and get the filename
    file_name = qr_generator.generate_qr_code(input_string)

    # Display success message with filename
    print(f"QR code generated successfully! File saved as: {file_name}")


def cli():
    """Command line interface entry point."""
    parser = argparse.ArgumentParser(description='Generate QR codes from text or URLs')
    parser.add_argument('text', help='Text or URL to encode in QR code')
    parser.add_argument('--prefix', default='qr_code', help='Filename prefix (default: qr_code)')
    parser.add_argument('--output', default='output', help='Output directory (default: output)')
    
    args = parser.parse_args()
    
    generator = QRCodeGenerator(args.prefix, args.output)
    filename = generator.generate_qr_code(args.text)
    print(f"QR code generated successfully! File saved as: {filename}")


if __name__ == "__main__":
    main()