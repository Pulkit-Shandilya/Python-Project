"""
Convert HTML to PDF using available Python libraries
"""
import os

# Try method 1: Using matplotlib to save as PDF (simple approach)
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    print("Using reportlab (if available)...")
except ImportError:
    print("reportlab not available")

# Method 2: Using nbconvert with webpdf
try:
    import subprocess
    print("Attempting direct notebook to PDF conversion...")
    result = subprocess.run([
        'python', '-m', 'nbconvert', 
        '--to', 'webpdf',
        'newquestions.ipynb'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✓ PDF created successfully using nbconvert webpdf!")
        print(result.stdout)
    else:
        print("webpdf method failed, trying alternative...")
        print(result.stderr)
        
        # Try PyPDF or other method
        print("\nYou can also:")
        print("1. Open newquestions.html in Chrome/Edge")
        print("2. Press Ctrl+P")
        print("3. Select 'Save as PDF'")
        print("4. Save the file")
        
except Exception as e:
    print(f"Error: {e}")
