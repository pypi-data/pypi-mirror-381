"""
QR Code Generator Module

This module provides a simple and efficient way to generate QR codes from text strings.
It creates PNG image files with timestamp-based naming for easy organization.

Author: Shan Konduru
Created: 2024
License: MIT
"""

import qrcode
import os
from datetime import datetime


class QRCodeGenerator:
    """
    A utility class for generating QR codes from text strings.

    This class creates QR codes with customizable settings and saves them as PNG images
    with timestamped filenames to prevent overwriting.

    Attributes:
        file_prefix (str): Prefix used for generated QR code filenames
        output_folder (str): Directory where QR code images will be saved
        
    Example:
        >>> generator = QRCodeGenerator("my_qr", "output")
        >>> filename = generator.generate_qr_code("https://example.com")
        >>> print(f"QR code saved as: {filename}")
    """
    
    def __init__(self, file_prefix="qr_code", output_folder="output"):
        """
        Initialize the QR Code Generator.
        
        Args:
            file_prefix (str, optional): Prefix for the output filename. 
                                       Defaults to "qr_code".
            output_folder (str, optional): Directory to save QR code images.
                                         Defaults to "output".
                                         
        Example:
            >>> generator = QRCodeGenerator("website_qr", "my_qr_codes")
            >>> # Will create files like: my_qr_codes/website_qr_20241001123456.png
        """
        self.file_prefix = file_prefix
        self.output_folder = output_folder
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def generate_qr_code(self, input_string):
        """
        Generate a QR code from the provided input string and save it as a PNG image.

        This method creates a QR code with predefined settings optimized for readability
        and saves it with a timestamp-based filename to ensure uniqueness.

        Args:
            input_string (str): The text or URL to encode in the QR code.
                              Can be any string content including URLs, text, etc.

        Returns:
            str: The full path of the generated QR code image (includes folder and .png extension).
            
        Raises:
            Exception: If there's an error during QR code generation or file saving.
            
        Example:
            >>> generator = QRCodeGenerator()
            >>> filename = generator.generate_qr_code("https://www.example.com")
            >>> print(f"QR code saved as: {filename}")
            output/qr_code_20241001123456.png        Note:
            - QR code version is set to 1 (21x21 modules)
            - Error correction level is set to L (Low ~7%)
            - Box size is 10 pixels per module
            - Border is 4 modules wide
            - Colors: black foreground on white background
        """
        # Create QR code instance with specific configuration
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is 21x21 modules)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction (~7%)
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size in boxes (minimum is 4)
        )

        # Add data to the QR code
        qr.add_data(input_string)
        qr.make(fit=True)  # Optimize the QR code size

        # Create the actual image
        img = qr.make_image(fill_color="black", back_color="white")

        # Generate timestamp-based filename to avoid conflicts
        # Include microseconds for higher precision to ensure uniqueness
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S%f")
        file_name = f"{self.file_prefix}_{current_datetime}.png"
        
        # Create full path including output folder
        full_path = os.path.join(self.output_folder, file_name)
        
        # Save the image to disk in the output folder
        img.save(full_path)
        
        return full_path