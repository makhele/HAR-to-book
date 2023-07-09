# HAR-to-Book

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

HAR-to-Book is a Python script that converts a HAR (HTTP Archive) file into a book by extracting images from the HAR file and generating a PDF document.

## How it Works

The main.py script takes a `.har` file and creates a book from the images contained within it. The HAR file is a JSON file that stores all the requests made, including the images represented as Base64 strings.

### Prerequisites

Before running the script, follow these steps:

1. Go to the website where you want to create a book.
2. Open the browser's Developer Tools by right-clicking anywhere on the page and selecting the "Inspect" option.
3. Switch to the "Network" tab in the Developer Tools and minimize it.
4. Manually browse through the book, clicking the next button as quickly as possible (you don't have to wait for each image to load).
   - Tip: Zoom in for high-quality images.
5. Once you reach the last page, look for a button to download the `.HAR` file.
   - This file contains all the requests you made, including the images stored as Base64 strings.
   - Save the file in the "raw" folder and rename it to "book.json".

### Usage

1. Download the original `.har`, `book.json`, and `deep.pdf` files from the [Google Drive](https://drive.google.com/drive/folders/1b3CN_dxi0plYUyc0ZpQPtmEgsR8Xz-O0?usp=share_link).
2. Make sure you have the following dependencies installed:
   - Python 3
   - Pillow library: Install it by running the command `python3 -m pip install --upgrade Pillow`.
3. Run the script by executing the following command in your terminal or command prompt:
4. The script will perform the following actions:
- Convert the `book.json` file into a more manageable format and save it as `sample.json`.
- Remove unnecessary data from `sample.json` and save the modified version as `sample2.json`.
- Convert all Base64-encoded images in `sample2.json` into PNG files and save them in the "pageImages" folder.
- Combine all PNG images into a single PDF document named `deep.pdf`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

