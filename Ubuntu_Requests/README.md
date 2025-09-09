# 🌍 Ubuntu_Requests - Image Fetcher

**"I am because we are" — Ubuntu Philosophy**

This Python script reflects the Ubuntu spirit of community, sharing, and respect. It connects to the web, fetches an image from a user-provided URL, and stores it locally for later appreciation.

---

## 📌 Features

- 🔗 Prompt user for an image URL
- 📁 Creates a `Fetched_Images` folder if it doesn't exist
- ⬇️ Downloads and saves image in binary mode using `requests`
- 🧠 Extracts or generates a unique filename
- ♻️ Prevents overwriting existing files
- 🧩 Handles HTTP and connection errors gracefully
- 📊 Optional download progress display

---

## 🛠️ Requirements

- Python 3.7+
- `requests` library

Install the required package with:

```bash
pip install requests

🚀 How to Use

1. Clone the repo or download the script:

```bash
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests


2. Run the script:

```bash
python image_fetcher.py


3. Enter a valid image URL (e.g. https://via.placeholder.com/300.png)

📁 Output

Images are saved to the Fetched_Images/ directory with a unique filename.

Example:

Ubuntu_Requests/
├── image_fetcher.py
├── README.md
└── Fetched_Images/
    └── image_8f9d72c9a12b4a32946a.jpg

🧘 Ubuntu Principles in Action

1. Community: Connects with the global internet community.

2. Respect: Handles errors gracefully and avoids crashes.

3. Sharing: Organizes downloads in a shared folder.

4. Practicality: Solves a real-world problem simply and effectively.

🤝 Contributing

Contributions are welcome! Feel free to fork the repo, improve the tool, and submit a pull request.

📄 License

This project is shared under the MIT License.

💬 Acknowledgments

Inspired by the Ubuntu philosophy: "I am because we are."


---

### ✅ To Complete Your Repo

1. Save this content as `README.md` in the same folder as your script.
2. Commit and push:

```bash
git add README.md
git commit -m "Add README with usage and Ubuntu principles"
git push
    