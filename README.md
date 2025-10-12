# 🧾 PDF Generator Tool

A simple yet powerful Python-based tool that automatically generates structured PDF files from topics listed in a CSV file. Each topic is given a neatly formatted page (or multiple pages) with headers, footers, and horizontal lines — ideal for creating custom notebooks, study guides, or structured notes.

---

## 🧠 Features

- 📄 **Automated PDF generation** from a CSV file of topics and page counts.  
- 🧱 **Custom headers and footers** for every topic.  
- 📏 **Uniform line spacing** (grid-like layout) for clean note-taking.  
- 🔁 **Multi-page topic support** — easily handles any number of pages per topic.  
- ⚙️ **Fully customizable** (fonts, colors, spacing, etc.).

---

## 📂 Project Structure

PDF-Generator-Tool/
│
├── main.py # Main Python script that generates PDFs
├── topics.csv # Input file containing topics and page counts
├── output.pdf # Automatically generated PDF output
└── README.md # Project documentation

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher  
- [fpdf](https://pypi.org/project/fpdf/)  
- [pandas](https://pypi.org/project/pandas/)

---

## ⚙️ Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/PDF-Generator-Tool.git
cd PDF-Generator-Tool
pip install fpdf pandas
