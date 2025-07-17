# DrawableFolderToBase64

**DrawableFolderToBase64** is a Python GUI tool (built with Tkinter) that converts all image files in a selected folder into Base64 strings and outputs them as constant Java fields in a `.java` file.

## 📌 Features

- Supports multiple image formats: `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`
- Encodes each image into a Base64 string
- Converts filenames into valid Java constant variable names
- Exports the output into a `.java` file with constants like:

  ```java
  public static final String image_name_png = "BASE64_ENCODED_STRING";
