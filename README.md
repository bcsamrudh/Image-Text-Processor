# Python Image Text Processor

This Python Tkinter project is designed to open images, extract text from them, open links, correct the extracted text, and translate it to another language. It provides a graphical user interface (GUI) built with Tkinter for easy interaction.

## Features

- Open and display images in various formats.
- Extract text from the opened image using Optical Character Recognition (OCR).
- Open hyperlinks found in the extracted text.
- Correct any errors in the extracted text using an integrated text correction feature.
- Translate the corrected text to another language using a translation service.

## Prerequisites

- Python 3.6 or above
- Tkinter
- googletrans
- pytesseract
- PIL
- textblob
- langdetect

## Installation

1. Clone the repository or download the source code.
1. Install the required libraries by running the following command:

```bash
pip install -r requirements.txt
```

3. Install Tesseract OCR. Refer to the official Tesseract OCR documentation for installation instructions specific to your operating system: [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html).

## Usage

1. Run the `main.py` file to start the application.
1. Click on the "Open Image" button to select an image file.
![Screenshot 2023-08-15 103006](https://github.com/bcsamrudh/Image-Text-Processor/assets/114090255/b5cfdcda-1bb0-425c-b5c2-2548d2a00a43)
1. Once the image is loaded, click on the "Extract Text" button to extract text from the image using OCR.
![Screenshot 2023-08-15 103126](https://github.com/bcsamrudh/Image-Text-Processor/assets/114090255/6906f0b3-e5cb-4907-8f64-7f6b36572510)

1. The extracted text will be displayed in the application's text area.
![Screenshot 2023-08-15 103149](https://github.com/bcsamrudh/Image-Text-Processor/assets/114090255/22564a49-2c9e-4399-96e0-48c0cf99a1b0)

1. To correct any errors in the extracted text, select the text and click on the "Correct Text" button.
1. The corrected text will replace the selected text in the text area.
![Screenshot 2023-08-15 103205](https://github.com/bcsamrudh/Image-Text-Processor/assets/114090255/87457b8e-1487-46a8-bca8-f7d3dfc7776b)

1. To translate the corrected text to another language, select the text and choose the target language from the dropdown menu.
1. Click on the "Translate Text" button to perform the translation. The translated text will be displayed in the text area.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project's GitHub repository: [Link to the repository]([https://github.com/bcsamrudh/Image-Text-Processor]).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
