# WHAT THE SCRIPT DOES
The main.py basically takes the .har file the create a book from the images

### BEFORE YOU BEGIN

1. Go to the site
2. Open the Inspect Page (right-click anywhere and select the Inspect option)
3. Go to the Network tab, then minimize
4. Browse the book manually (You can click the next button as fast as you can you dont have to wait)
    - Tip (Zoom in for High quality images)
5. Once on the last page, there is a button to download the `.HAR` file.
    - This is just a json file that has all the request you have made, including the images (stored as Base64)
    - Save the file in `raw` folder rename it to `book.json`

### RUNNING THE MAIN.PY

1. The original `.har`, `book.json` and `deep.pdf` are too large and are stored on the [google drive](https://drive.google.com/drive/folders/1b3CN_dxi0plYUyc0ZpQPtmEgsR8Xz-O0?usp=share_link)
2. All scripts are document
3. Just Run
